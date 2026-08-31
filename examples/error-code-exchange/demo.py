#!/usr/bin/env python3
"""Demonstrates the CharIN Unified Error Codes exchange message.

Simulates an EVSE detecting a fault, encoding an ErrorCodeReport with the
Canonical Octet Encoding Rules (COER, ITU-T X.696) for transmission over
ISO 15118-2, and an EV decoding the same bytes. It then re-encodes the
identical report with the JSON Encoding Rules (JER, ITU-T X.697), as would
be relayed to a charging management system, e.g. inside an OCPP 2.0.1
NotifyEventRequest `eventData` field.

Requires: pip install -r requirements.txt
Run: python demo.py
"""

from __future__ import annotations

import datetime
import json
from pathlib import Path

import asn1tools

ASN1_MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "specification"
    / "protocol"
    / "UnifiedErrorCodeExchange.asn1"
)


def build_sample_report() -> dict:
    """A SideB_OverCurrentFailure report as the EVSE would raise it."""
    return {
        "metadata": {
            "evseID": "DE*ABC*E1234*1",
            "communicationProtocol": {
                "protocolNamespace": "urn:iso:std:iso:15118:-2:2013:MsgDef",
                "versionMajor": 2,
                "versionMinor": 0,
                "schemaID": 1,
                "priority": 1,
            },
            "sessionContext": {
                "sessionID": bytes.fromhex("0102030405060708"),
                "messageName": "CurrentDemandReq",
                "timestamp": datetime.datetime.now(
                    tz=datetime.timezone.utc
                ).replace(microsecond=0),
            },
        },
        "errorCode": {
            "source": "evse",
            "codeName": "SideB_OverCurrentFailure",
        },
    }


def evse_encode_report(codec, report: dict) -> bytes:
    """The EVSE serializes the report for transmission over ISO 15118-2."""
    return codec.encode("ErrorCodeReport", report)


def ev_decode_report(codec, wire_bytes: bytes) -> dict:
    """The EV deserializes the bytes it received from the EVSE."""
    return codec.decode("ErrorCodeReport", wire_bytes)


def relay_to_ocpp_json(jer_codec, report: dict) -> str:
    """A charging management system relays the same report as JSON."""
    return jer_codec.encode("ErrorCodeReport", report).decode("utf-8")


def main() -> None:
    # The installed asn1tools (>=0.166) does not expose a 'coer' codec name
    # (its compile_files() only accepts 'ber', 'der', 'gser', 'jer', 'oer',
    # 'per', 'uper', 'xer' -- see asn1tools.compiler.compile_dict). COER
    # (ITU-T X.696) is the *canonical* variant of OER: same base encoding,
    # just with the extra canonicalization rules (e.g. shortest-form
    # lengths, fixed bit ordering) that make it byte-for-byte deterministic.
    # 'oer' is therefore the closest supported ITU-T X.696-family codec, and
    # for this message (no SET types, no unconstrained CHOICE alternatives
    # affecting encoding order) plain OER already produces the same bytes a
    # canonical encoder would. We use 'oer' here and note the substitution.
    coer = asn1tools.compile_files(str(ASN1_MODULE_PATH), codec="oer")
    jer = asn1tools.compile_files(str(ASN1_MODULE_PATH), codec="jer")

    report = build_sample_report()
    print("EVSE builds ErrorCodeReport:")
    print(json.dumps(report, indent=2, default=str))

    wire_bytes = evse_encode_report(coer, report)
    print(f"\nEVSE -> EV over ISO 15118-2 (OER, standing in for COER since this")
    print(f"asn1tools release has no 'coer' codec name, {len(wire_bytes)} bytes):")
    print(wire_bytes.hex())

    decoded = ev_decode_report(coer, wire_bytes)
    print("\nEV decodes the received bytes:")
    print(json.dumps(decoded, indent=2, default=str))
    assert decoded["errorCode"]["codeName"] == report["errorCode"]["codeName"]

    ocpp_payload = relay_to_ocpp_json(jer, report)
    print("\nCharging management system relays the same report as JER/JSON")
    print("(e.g. OCPP 2.0.1 NotifyEventRequest.eventData):")
    print(ocpp_payload)


if __name__ == "__main__":
    main()
