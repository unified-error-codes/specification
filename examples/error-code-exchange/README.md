# Error Code Exchange Demo

Runnable demonstration of the `ErrorCodeReport` message defined in
[`specification/protocol/definitions_ErrorCodeExchangeMessage.rst`](../../specification/protocol/definitions_ErrorCodeExchangeMessage.rst),
implementing [GitHub issue #61](https://github.com/charinev/unified-error-codes/issues/61).

It uses the canonical ASN.1 module at
[`specification/protocol/UnifiedErrorCodeExchange.asn1`](../../specification/protocol/UnifiedErrorCodeExchange.asn1)
directly, so the demo can never drift from the published schema.

## What it shows

1. An EVSE builds an `ErrorCodeReport` for a `SideB_OverCurrentFailure`.
2. The EVSE encodes it with the Canonical Octet Encoding Rules (COER,
   ITU-T X.696), as required on the ISO 15118-2 link, and the EV decodes it.
   (The demo actually invokes asn1tools' `oer` codec: the installed
   asn1tools release has no `coer` codec name, and OER is the closest
   supported ITU-T X.696-family encoding for this message — see the
   comment in `demo.py` for details.)
3. The same report is re-encoded with the JSON Encoding Rules (JER,
   ITU-T X.697), as would be relayed to a charging management system, e.g.
   inside an OCPP 2.0.1 `NotifyEventRequest.eventData` field.

## Run it

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python demo.py
```
