..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _protocol_error_code_exchange_message:

****************************
 Error Code Exchange Message
****************************

Description
===========

This message carries a single Unified Error Code report between an EV
and an EVSE over **ISO 15118-2**, via the Event Notification Protocol
extensions referenced by the ISO 15118-2 working draft.

The message intentionally carries the *minimum* data required to
answer three questions on receipt:

#. Who raised the error — the EV or the EVSE (``UnifiedErrorCode.source``)?
#. Which error occurred (``UnifiedErrorCode.codeName``, matching a code
   name from the :doc:`../error_codes/definitions` section)?
#. In what protocol/session context did it occur (``BasicMetadata``)?

It deliberately excludes telemetry, diagnostic payloads, and severity
classification. Those remain the responsibility of the corresponding
:doc:`../telemetry/definitions` signals and of the receiving system,
which resolves ``codeName`` against the Unified Error Codes catalog.

Scope
======

ISO 15118-2 opens a pathway for error/diagnostic data exchange between
the EVSE and the EV, but only defines the *transport* layer, not the
*schema* or *content* of the error codes exchanged over it (see the
`MANIFESTO <../../MANIFESTO.md>`_). This message closes that gap,
including exchanges that occur via the Event Signalling/Notification
Protocol (ESDP/ENP) extensions referenced by the ISO 15118-2 working
draft, before high-level communication (and therefore before an
``EVCCID``, an ``EVSEID`` learned by the EV, or a V2G ``sessionID``)
is available.

Message Structure
==================

``ErrorCodeReport``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 45 15

   -  -  Field
      -  Type
      -  Description
      -  Presence

   -  -  ``metadata``
      -  ``BasicMetadata``
      -  Identifies the participants, negotiated protocol, and session
         the error occurred in.
      -  Required

   -  -  ``errorCode``
      -  ``UnifiedErrorCode``
      -  The Unified Error Code being reported and the side that
         detected it.
      -  Required

``BasicMetadata``
------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 45 15

   -  -  Field
      -  Type
      -  Description
      -  Presence

   -  -  ``evseID``
      -  ``EVSEID`` (string)
      -  Identifier for the charging station / EVSE, per ISO 15118-2
         Annex A.1 (``EVSEIDType``).
      -  Optional — not yet known to the EV in an EV-side (``source``
         = ``ev``) pre-session error report; the EVSEID is first
         returned to the EV in ``SessionSetupRes``, at the earliest.

   -  -  ``evccID``
      -  ``EVCCID`` (6-to-8-byte address)
      -  Identifier for the EV communication controller, per
         ISO 15118-2 Annex A.1 (``EVCCIDType``): a 6-byte EUI-48 MAC
         address, or an 8-byte EUI-64 address.
      -  Optional — not yet known before SLAC/SDP completes.

   -  -  ``communicationProtocol``
      -  ``CommunicationProtocol``
      -  The negotiated application protocol, mirroring
         ``AppProtocolType`` from ``SupportedAppProtocolReq``/``Res``.
      -  Optional — an ESDP/ENP error can occur before protocol
         negotiation.

   -  -  ``sessionContext``
      -  ``SessionContext``
      -  Where, in time and in the message flow, the error occurred.
      -  Required

``CommunicationProtocol``
--------------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 45 15

   -  -  Field
      -  Type
      -  Description
      -  Presence

   -  -  ``protocolNamespace``
      -  string
      -  Full protocol namespace used during protocol negotiation
         (e.g. ``urn:iso:std:iso:15118:-2:2013:MsgDef``).
      -  Optional

   -  -  ``versionMajor``
      -  integer
      -  Major version number of the selected protocol.
      -  Optional

   -  -  ``versionMinor``
      -  integer
      -  Minor version number of the selected protocol.
      -  Optional

   -  -  ``schemaID``
      -  integer
      -  Schema identifier selected during protocol negotiation.
      -  Optional

   -  -  ``priority``
      -  integer
      -  Priority used during ``SupportedAppProtocol`` negotiation.
      -  Optional

.. note::

   An earlier draft of this schema (see `GitHub issue #61
   <https://github.com/charinev/unified-error-codes/issues/61>`_) also
   carried a ``protocolName`` field. It was dropped because
   ``protocolNamespace`` already identifies the protocol unambiguously.

``SessionContext``
--------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 45 15

   -  -  Field
      -  Type
      -  Description
      -  Presence

   -  -  ``sessionID``
      -  1-to-8-byte octet string
      -  The V2G session identifier assigned in ``SessionSetupRes``
         (8 octets), or the reserved single-byte ``0x00`` "no active
         session" encoding used elsewhere in ISO 15118-2.
      -  Optional — not yet known before ``SessionSetupRes``.

   -  -  ``messageName``
      -  string
      -  Name of the V2G/SLAC message most closely associated with the
         error (ISO 15118-2 Table 8 ``V2GMessageType``, or Table 4
         ``SLACMessageType``).
      -  Optional

   -  -  ``timestamp``
      -  ``GeneralizedTime``
      -  UTC time the error was detected.
      -  Required

.. note::

   ``timestamp`` uses the ASN.1 ``GeneralizedTime`` type rather than a
   free-form string, per GitHub issue #61 feedback requesting a
   stricter type. This is equivalent in value to RFC 3339 / ISO 8601
   but is encoded and validated as a native ASN.1 date-time, not as an
   unconstrained string.

   An earlier draft also carried a ``couplingSessionID`` identifying
   the physical coupling session. It was dropped as out of scope for
   this message per review feedback.

   ``sessionID``'s 1-to-8-octet size range matches ISO 15118-2's
   ``sessionIDType`` (``hexBinary``, ``maxLength`` 8, no minimum), so
   that both an assigned 8-octet session identifier and the reserved
   single-byte ``0x00`` sentinel are representable.

``UnifiedErrorCode``
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 20 45 15

   -  -  Field
      -  Type
      -  Description
      -  Presence

   -  -  ``source``
      -  ``ErrorSource`` (``ev`` | ``evse``)
      -  Which side of the charging session detected/raised the error.
      -  Required

   -  -  ``codeName``
      -  string
      -  Name of the reported error code, matching a code defined in
         :doc:`../error_codes/definitions` (e.g. ``GridPowerLoss``,
         ``SideB_OverCurrentFailure``).
      -  Required

ASN.1 Module
=============

The canonical, machine-readable definition of this message is the
ASN.1 module below. It is the single source of truth; the tables above
are a human-readable summary of it.

.. literalinclude:: UnifiedErrorCodeExchange.asn1
   :language: text
   :caption: specification/protocol/UnifiedErrorCodeExchange.asn1

Encoding Rules
===============

-  **ISO 15118-2 link (EV/EVSE)**: this message SHALL be encoded
   using the **Canonical Octet Encoding Rules (COER)**, as defined in
   `ITU-T X.696 <https://www.itu.int/rec/T-REC-X.696>`_. COER matches
   the byte-, string-, and integer-encoding conventions already used
   by ISO 15118-2's Event Notification Protocol extensions.

-  **Charging management system relay (e.g. OCPP)**: the same schema
   MAY be re-encoded using the **JSON Encoding Rules (JER)**, as
   defined in `ITU-T X.697 <https://www.itu.int/rec/T-REC-X.697>`_.
   This produces a JSON document suitable for use as, for example, the
   ``eventData`` payload of an OCPP 2.0.1 ``NotifyEventRequest``.

Using one ASN.1 schema with two encoding rules keeps the EV/EVSE wire
format and the backend/OCPP representation of an error report
structurally identical, differing only in bytes-on-the-wire vs. JSON.

Demonstration Code
====================

A runnable demonstration of an EVSE encoding an ``ErrorCodeReport``
with COER, an EV decoding it, and the same report being re-encoded
with JER for an OCPP relay, is provided at
`examples/error-code-exchange <../../examples/error-code-exchange>`_
in the repository root.
