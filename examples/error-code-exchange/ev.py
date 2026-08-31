"""The EV side: raises an ErrorCodeReport towards the EVSE.

The link between EV and EVSE is the Event Notification Protocol (ENP)
specified by ISO 15118-202; this module stands in for it with a direct
in-process call that carries the same OER-encoded bytes (see the note
on the 'coer' codec substitution in common.py's caller, evse.py) that
would cross the wire.
"""

from __future__ import annotations

from typing import Any

from common import build_sample_report, compile_asn1_codec


def raise_error_over_iso15118(codec: Any) -> bytes:
    """The EV builds and encodes an ErrorCodeReport for the EVSE."""
    report = build_sample_report()
    return codec.encode("ErrorCodeReport", report)


if __name__ == "__main__":
    # asn1tools has no 'coer' codec name in the installed release; 'oer' is
    # the closest supported ITU-T X.696-family encoding (see evse.py).
    coer = compile_asn1_codec("oer")
    wire_bytes = raise_error_over_iso15118(coer)
    print(f"EV -> EVSE over ISO 15118-202 ENP ({len(wire_bytes)} bytes):")
    print(wire_bytes.hex())
