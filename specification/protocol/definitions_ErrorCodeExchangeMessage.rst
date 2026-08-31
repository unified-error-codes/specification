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
and an EVSE over the **Event Notification Protocol (ENP)**, as
specified by `ISO 15118-202
<https://www.iso.org/standard/89759.html>`_ ("Extensible SECC
Discovery Protocol and Event Notification Protocol", currently at
Draft PAS stage). ENP is designed to run alongside either
ISO 15118-2 or ISO 15118-20.

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

ISO 15118-202 opens a pathway for error/diagnostic data exchange
between the EVSE and the EV, but only defines the *transport* layer,
not the *schema* or *content* of the error codes exchanged over it
(see the `MANIFESTO <../../MANIFESTO.md>`_). This message closes that
gap. Because ENP is designed to also work before or independent of an
active V2G session, most fields here are optional — including
``EVCCID``, an ``EVSEID`` learned by the EV, and a V2G ``sessionID``,
none of which are available before high-level communication begins.

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
      -  ``EVSEID`` (string, at most 37 characters)
      -  Identifier for the charging station / EVSE. The maximum length
         follows ISO 15118-2's ``EVSEIDType``; no minimum is imposed.
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

ENP Extension Registration
============================

ISO 15118-202 carries ENP extensions in a registry whose entries pair a
unique 16-octet identifier with the ASN.1 type that identifier selects.
ISO publishes that registry as a machine-readable ASN.1 module,
`ENPExtensions.asn
<https://standards.iso.org/iso/pas/15118/-202/ed-1/en/ENPExtensions.asn>`_,
separately from the paywalled prose document. Its types are ISO's own
and are neither reproduced nor redistributed here; consult that module
for their normative definitions.

As published, the registry holds six narrowly-scoped extensions (EVSE
grid information, grid code impact level, EV/EVSE stop reason, EV/EVSE
derating reason) — none carries a general-purpose error code.
`GitHub issue #65 <https://github.com/charinev/unified-error-codes/issues/65>`_
proposes registering ``ErrorCodeReport`` (this message's root type) as a
new entry for exactly that purpose. That registration is a proposal, and
the identifier below has not been assigned by the working group:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   -  -  Registration field
      -  Proposed value

   -  -  Identifier (UUID v4)
      -  ``0F9FA02C-B967-40FF-AF1D-50BF09A1D8DC`` — **PROPOSED**,
         pending working-group ratification via issue #65

   -  -  Selected type
      -  ``ErrorCodeReport``

ISO's registry is built on an ASN.1 Information Object Class (ITU-T
X.681). Current open-source ASN.1 compilers cannot yet process that
construct — see the EVerest project's investigation
(`EVerest/EVerest-archived#259 <https://github.com/EVerest/EVerest-archived/issues/259>`_)
— so implementations cannot presently compile against ISO's module
directly. The demonstration code accompanying this specification works
around that with its own simplified stand-in; that stand-in is
demonstration scaffolding and forms no part of this specification.

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

-  **ENP link (EV/EVSE)**: ISO 15118-202 normatively references
   `ISO/IEC 8825-7 <https://www.iso.org/standard/81426.html>`_ (jointly
   published as `ITU-T X.696 <https://www.itu.int/rec/T-REC-X.696>`_),
   which specifies both basic and canonical Octet Encoding Rules. This
   message SHALL use the **canonical** variant (COER), as proposed in
   `GitHub issue #61
   <https://github.com/charinev/unified-error-codes/issues/61>`_, so
   that a given report has exactly one valid encoding.

-  **Charging management system relay (e.g. OCPP)**: an EVSE relaying
   this message to a backend maps its fields onto that backend's
   native protocol rather than tunnelling the ASN.1 encoding through
   it — e.g. ``UnifiedErrorCode.codeName`` into the ``techCode``/
   ``actualValue`` of an OCPP 2.0.1 ``NotifyEventRequest``'s
   ``eventData``, or into the ``vendorErrorCode`` of an OCPP 1.6
   ``StatusNotification``. The schema MAY still be re-encoded directly
   with the **JSON Encoding Rules (JER)**, as defined in `ITU-T X.697
   <https://www.itu.int/rec/T-REC-X.697>`_, where a backend accepts an
   opaque structured payload.

Demonstration Code
====================

A runnable demonstration of the full path — an EV encoding an
``ErrorCodeReport`` and wrapping it as an ENP extension, an EVSE
unwrapping and decoding it, and relaying the same detected error to two
CSMS backends in parallel over OCPP 1.6 and OCPP 2.0.1 — is provided at
`examples/error-code-exchange <../../examples/error-code-exchange>`_
in the repository root.
