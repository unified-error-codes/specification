"""The EVSE side: receives an ENP-extension-wrapped ErrorCodeReport from
the EV and relays it, unchanged in meaning, to two CSMS backends at
once — one speaking OCPP 1.6, one speaking OCPP 2.0.1.

The EVSE does not tunnel the ASN.1 message through OCPP; it translates
the Unified Error Code into each protocol's native error representation.
"""

from __future__ import annotations

import asyncio
import datetime
from typing import Any

import csms_ocpp16
import csms_ocpp201
import demolog
import websockets
from ocpp.v16 import ChargePoint as ChargePointV16
from ocpp.v16 import call as call16
from ocpp.v16 import enums as enums16
from ocpp.v201 import ChargePoint as ChargePointV201
from ocpp.v201 import call as call201
from ocpp.v201 import datatypes as datatypes201
from ocpp.v201 import enums as enums201

from common import ERROR_CODE_EXTENSION_ID, VENDOR_ID, compile_asn1_codec

CHARGE_POINT_ID = "EVSE-DE-ABC-E1234-1"


def decode_from_iso15118(codec: Any, wire_bytes: bytes) -> dict:
    """The EVSE unwraps the ENP extension it received from the EV and
    decodes the ErrorCodeReport carried in its extensionValue.
    """
    extension = codec.decode("ErrorCodeExtension", wire_bytes)
    extension_id = extension["extensionID"]
    if extension_id != ERROR_CODE_EXTENSION_ID.bytes:
        raise ValueError(
            f"unrecognized ENP extensionID: {extension_id.hex()} "
            f"(expected the Error Code Extension, {ERROR_CODE_EXTENSION_ID})"
        )
    return codec.decode("ErrorCodeReport", extension["extensionValue"])


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


async def relay_over_ocpp16(report: dict, uri: str) -> list[str]:
    """Report the error to a CSMS speaking OCPP 1.6, via StatusNotification.

    Returns the log lines for this relay so the caller can emit them as one
    block; see demolog.block for why.
    """
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
    return [
        demolog.format_line("EVSE", f"--> CSMS (OCPP 1.6) at {uri}"),
        demolog.format_line("", "StatusNotification.req"),
        demolog.as_json(csms_ocpp16.last_received),
        demolog.format_line("CSMS (OCPP 1.6)", "--> EVSE  StatusNotification.conf"),
        demolog.format_line("", f"accepted={response is not None}"),
    ]


async def relay_over_ocpp201(report: dict, uri: str) -> list[str]:
    """Report the error to a CSMS speaking OCPP 2.0.1, via NotifyEventRequest.

    Returns the log lines for this relay so the caller can emit them as one
    block; see demolog.block for why.
    """
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
    return [
        demolog.format_line("EVSE", f"--> CSMS (OCPP 2.0.1) at {uri}"),
        demolog.format_line("", "NotifyEventRequest"),
        demolog.as_json(csms_ocpp201.last_received),
        demolog.format_line("CSMS (OCPP 2.0.1)", "--> EVSE  NotifyEventResponse"),
        demolog.format_line("", f"accepted={response is not None}"),
    ]


async def relay_to_both_backends(report: dict, uri_ocpp16: str, uri_ocpp201: str) -> None:
    """Relay the same error to both CSMS backends concurrently.

    Both requests are genuinely in flight at once; their log blocks are
    emitted afterwards in a fixed order so the transcript stays readable.
    """
    blocks = await asyncio.gather(
        relay_over_ocpp16(report, uri_ocpp16),
        relay_over_ocpp201(report, uri_ocpp201),
    )
    for lines in blocks:
        demolog.block(lines)


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
