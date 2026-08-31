"""The EVSE side: receives an ErrorCodeReport from the EV and relays it,
unchanged in meaning, to two CSMS backends at once — one speaking
OCPP 1.6, one speaking OCPP 2.0.1.

The EVSE does not tunnel the ASN.1 message through OCPP; it translates
the Unified Error Code into each protocol's native error representation.
"""

from __future__ import annotations

import asyncio
import datetime

import websockets
from ocpp.v16 import ChargePoint as ChargePointV16
from ocpp.v16 import call as call16
from ocpp.v16 import enums as enums16
from ocpp.v201 import ChargePoint as ChargePointV201
from ocpp.v201 import call as call201
from ocpp.v201 import datatypes as datatypes201
from ocpp.v201 import enums as enums201

from common import VENDOR_ID, compile_asn1_codec

CHARGE_POINT_ID = "EVSE-DE-ABC-E1234-1"


def decode_from_iso15118(codec, wire_bytes: bytes) -> dict:
    """The EVSE decodes the bytes it received from the EV."""
    return codec.decode("ErrorCodeReport", wire_bytes)


def map_code_name_to_ocpp16_error(code_name: str) -> enums16.ChargePointErrorCode:
    """Best-effort match onto OCPP 1.6's small, fixed error vocabulary.

    OCPP 1.6 cannot carry an arbitrary Unified Error Code name in its
    `errorCode` field, so this only picks the closest standard value for
    interoperability with 1.6-only monitoring; the exact Unified Error
    Code always also travels in `vendorErrorCode`, unabridged.
    """
    lowered = code_name.lower()
    for candidate in enums16.ChargePointErrorCode:
        if candidate.value.lower() in lowered:
            return candidate
    return enums16.ChargePointErrorCode.other_error


async def relay_over_ocpp16(report: dict, uri: str) -> None:
    """Report the error to a CSMS speaking OCPP 1.6, via StatusNotification."""
    error_code = report["errorCode"]
    async with websockets.connect(uri, subprotocols=["ocpp1.6"]) as ws:
        cp = ChargePointV16(CHARGE_POINT_ID, ws)
        listener = asyncio.ensure_future(cp.start())
        try:
            response = await cp.call(
                call16.StatusNotification(
                    connector_id=1,
                    error_code=map_code_name_to_ocpp16_error(error_code["codeName"]),
                    status=enums16.ChargePointStatus.faulted,
                    timestamp=report["metadata"]["sessionContext"][
                        "timestamp"
                    ].isoformat(),
                    vendor_id=VENDOR_ID,
                    vendor_error_code=error_code["codeName"],
                )
            )
        finally:
            listener.cancel()
    print(f"EVSE -> CSMS (OCPP 1.6) StatusNotification: accepted={response is not None}")


async def relay_over_ocpp201(report: dict, uri: str) -> None:
    """Report the error to a CSMS speaking OCPP 2.0.1, via NotifyEventRequest."""
    error_code = report["errorCode"]
    async with websockets.connect(uri, subprotocols=["ocpp2.0.1"]) as ws:
        cp = ChargePointV201(CHARGE_POINT_ID, ws)
        listener = asyncio.ensure_future(cp.start())
        try:
            response = await cp.call(
                call201.NotifyEvent(
                    generated_at=datetime.datetime.now(
                        tz=datetime.timezone.utc
                    ).isoformat(),
                    seq_no=0,
                    event_data=[
                        datatypes201.EventDataType(
                            event_id=1,
                            timestamp=report["metadata"]["sessionContext"][
                                "timestamp"
                            ].isoformat(),
                            trigger=enums201.EventTriggerEnumType.alerting,
                            actual_value=error_code["codeName"],
                            event_notification_type=(
                                enums201.EventNotificationEnumType.hard_wired_notification
                            ),
                            component=datatypes201.ComponentType(name="EVSE"),
                            variable=datatypes201.VariableType(name="ErrorCode"),
                            tech_code=error_code["codeName"],
                            tech_info=f"source={error_code['source']}",
                        )
                    ],
                )
            )
        finally:
            listener.cancel()
    print(f"EVSE -> CSMS (OCPP 2.0.1) NotifyEventRequest: accepted={response is not None}")


async def relay_to_both_backends(report: dict, uri_ocpp16: str, uri_ocpp201: str) -> None:
    """Relay the same error to both CSMS backends concurrently."""
    await asyncio.gather(
        relay_over_ocpp16(report, uri_ocpp16),
        relay_over_ocpp201(report, uri_ocpp201),
    )


if __name__ == "__main__":
    import sys

    from ev import raise_error_over_iso15118

    coer = compile_asn1_codec("oer")
    wire_bytes = raise_error_over_iso15118(coer)
    report = decode_from_iso15118(coer, wire_bytes)
    print("EVSE decoded report:", report)

    uri16 = sys.argv[1] if len(sys.argv) > 1 else "ws://localhost:9016/EVSE"
    uri201 = sys.argv[2] if len(sys.argv) > 2 else "ws://localhost:9201/EVSE"
    asyncio.run(relay_to_both_backends(report, uri16, uri201))
