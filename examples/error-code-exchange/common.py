"""Shared helpers for the Unified Error Code exchange demo."""

from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any

import asn1tools

ASN1_MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "specification"
    / "protocol"
    / "UnifiedErrorCodeExchange.asn1"
)

VENDOR_ID = "org.charin.unified-error-codes"


def compile_asn1_codec(codec: str) -> Any:
    """Compile the canonical ASN.1 module with the given asn1tools codec."""
    return asn1tools.compile_files(str(ASN1_MODULE_PATH), codec=codec)


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
