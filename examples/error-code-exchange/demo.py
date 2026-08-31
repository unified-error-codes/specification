#!/usr/bin/env python3
"""End-to-end demo: EV -> EVSE -> CSMS (OCPP 1.6 and OCPP 2.0.1 in parallel).

See ARCHITECTURE.md for the full design. In short:

1. The EV builds a Unified Error Code ErrorCodeReport and wraps it as an
   ENP extension (the proposed Error Code Extension from GitHub issue
   #65), as it would be sent over the Event Notification Protocol (ENP)
   specified by ISO 15118-202.
2. The EVSE unwraps and decodes it, then relays the same detected error
   to two mock CSMS backends at once: one speaking OCPP 1.6, one
   speaking OCPP 2.0.1.

Requires: pip install -r requirements.txt
Run: python demo.py
"""

from __future__ import annotations

import asyncio
import json

import csms_ocpp16
import csms_ocpp201
from common import compile_asn1_codec
from ev import raise_error_over_iso15118
from evse import decode_from_iso15118, relay_to_both_backends

OCPP16_URI = "ws://localhost:9016/EVSE-DE-ABC-E1234-1"
OCPP201_URI = "ws://localhost:9201/EVSE-DE-ABC-E1234-1"


async def main() -> None:
    # asn1tools has no 'coer' codec name in the installed release ('coer'
    # isn't a recognized asn1tools codec at all as of 0.168); 'oer' is the
    # closest supported ITU-T X.696-family encoding, and this message has
    # no SET types or unconstrained CHOICE alternatives that would make its
    # OER encoding differ from a canonical (COER) one.
    coer = compile_asn1_codec("oer")

    print("=== EV: building ErrorCodeReport, wrapping as an ENP extension ===")
    wire_bytes = raise_error_over_iso15118(coer)
    print(f"EV -> EVSE over ISO 15118-202 ENP (OER, {len(wire_bytes)} bytes):")
    print(wire_bytes.hex())

    print("\n=== EVSE: unwrapping the ENP extension and decoding the report ===")
    report = decode_from_iso15118(coer, wire_bytes)
    print(json.dumps(report, indent=2, default=str))

    print("\n=== Starting mock CSMS backends ===")
    async with csms_ocpp16.serve(), csms_ocpp201.serve():
        print("\n=== EVSE: relaying to both CSMS backends in parallel ===")
        await relay_to_both_backends(report, OCPP16_URI, OCPP201_URI)

    print("\nDone: the same Unified Error Code reached both backends.")


if __name__ == "__main__":
    asyncio.run(main())
