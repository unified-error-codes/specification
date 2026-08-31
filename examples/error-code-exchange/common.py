"""Shared helpers for the Unified Error Code exchange demo."""

from __future__ import annotations

import datetime
import uuid
from pathlib import Path
from typing import Any

import asn1tools

ASN1_MODULE_PATH = (
    Path(__file__).resolve().parents[2]
    / "specification"
    / "protocol"
    / "UnifiedErrorCodeExchange.asn1"
)

# Demonstration scaffolding, not part of the specification — see the file's
# own header for why the demo cannot compile against ISO's own module.
DEMO_EXTENSION_MODULE_PATH = Path(__file__).resolve().parent / "DemoEnpExtension.asn1"

VENDOR_ID = "org.charin.unified-error-codes"

# Proposed (unratified) identifier for registering ErrorCodeReport as an
# ISO 15118-202 ENP extension, per GitHub issue #65. See the "ENP Extension
# Registration" section of definitions_ErrorCodeExchangeMessage.rst.
ERROR_CODE_EXTENSION_ID = uuid.UUID("0F9FA02C-B967-40FF-AF1D-50BF09A1D8DC")


def compile_asn1_codec(codec: str) -> Any:
    """Compile the specification's module plus the demo's extension wrapper."""
    return asn1tools.compile_files(
        [str(ASN1_MODULE_PATH), str(DEMO_EXTENSION_MODULE_PATH)], codec=codec
    )


def build_sample_report() -> dict:
    """A SideB_OverCurrentFailure report as the EV would raise it.

    "Side B" is the vehicle side of the connector, so this is a fault the
    EV itself detects and must tell the EVSE about — the EVSE has no other
    way to learn of it, which is exactly why the EV -> EVSE leg exists.
    """
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
            "source": "ev",
            "codeName": "SideB_OverCurrentFailure",
        },
    }
