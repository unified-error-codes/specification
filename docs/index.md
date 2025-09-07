# Unified Error Codes (UEC) Specification

## Abstract

This document specifies the data model, semantics, and behavioral requirements for Unified Error Codes (UEC) used in the e-mobility ecosystem. It provides a common language for reporting diagnostic events and conditions between ecosystem components, primarily the Electric Vehicle Supply Equipment (EVSE) and the Charge Point Management System (CPMS).

## Scope

The scope of this specification is the definition of a unified set of error codes, their associated data models, and the required behavior of systems that implement them. This includes the conditions that trigger an error event and the conditions under which an error state is cleared.

## Normative References

The following referenced documents are indispensable for the application of this document.

* **[DIN99003]** DIN DKE SPEC 99003: A comprehensive list of error codes for the EV charging ecosystem.

## Terms, Definitions

## Abbreviations

* **CPMS:** Charge Point Management System
* **EV:** Electric Vehicle
* **EVSE:** Electric Vehicle Supply Equipment
* **UEC:** Unified Error Code

## Conformance Language

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [RFC2119].

## Architectural Principles

The UEC specification is built upon the following core principles:

* **Transport Agnostic:** The UEC data model is independent of any specific communication protocol like OCPP.
* **Extensibility:** The specification is designed to be extended with new codes and parameters in a structured and backward-compatible manner.
* **Machine-Readability:** The specification prioritizes structured data over free text to enable reliable, automated processing.

## Error Codes

### Low Level Communication

| Error code                      | Semantics                                                                                   |
| ------------------------------- | ------------------------------------------------------------------------------------------- |
| `ProximityPilotFault`           | Proximity value (voltage/resistance) out of range.                                          |
| `ProximityPilotNotDetected`     | The proximity pilot is not detected, but the EV (CP detected) is connected.                 |
| `ProximityPilotValueChanged`    | The proximity pilot value has been changed while the plug is connected.                     |
| `ControlPilotFault`             | The control pilot parameters are out of range.                                              |
| `ControlPilotStateUnexpected`   | Unexpected Control Pilot state detected.                                                    |
| `ControlPilotStateNotSupported` | Control Pilot state is not supported (e.g. state D (ventilation) is not supported by EVSE). |

### SLAC and PLC

| Error code                  | Semantics                                                |
| --------------------------- | -------------------------------------------------------- |
| `PLCNotFound`               | PLC modem not detected.                                  |
| `PLCFault`                  | PLC modem fault.                                         |
| `PLCLinkDetectionTimeout`   | Timeout to detect PLC link.                              |
| `PLCLinkLeaveTimeout`       | Timeout to leave the logical network.                    |
| `PLCLinkLost`               | The PLC link has been lost.                              |
| `SLACTimeout`               | Timeout occurred during SLAC.                            |
| `SLACSequenceError`         | Unexpected SLAC message (not according to the sequence). |
| `SLACParameterInvalid`      | The message field value has an incorrect value.          |
| `SLACParameterNotAllowed`   | The message field value has an incorrect value.          |
| `SLACParameterNotSupported` | The message field value has an incorrect value.          |
| `SLACParameterOutOfRange`   | The value of the SLAC message field is out of range.     |
| `SLACAttenuationHigh`       | SLAC attenuation is too high.                            |

### V2G Transport Protocol

| Error code                           | Semantics                                       |
| ------------------------------------ | ----------------------------------------------- |
| `V2GTPProtocolVersionInvalid`        | V2GTP header: invalid protocol version.         |
| `V2GTPInverseProtocolVersionInvalid` | V2GTP header: invalid inverse protocol version. |
| `V2GTPPayloadLengthInvalid`          | V2GTP header: invalid payload length.           |
| `V2GTPPayloadTypeInvalid`            | V2GTP header: invalid payload type.             |

### SDP

| Error code                | Semantics                                |
| ------------------------- | ---------------------------------------- |
| `SDPPayloadLengthInvalid` | Invalid request/response payload length. |
| `SDPParameterInvalid`     | Invalid SDP field value.                 |
| `SDPDiscoveryTimeout`     | EVCC was not able to discover SECC.      |

### TCP and TLS

| Error code             | Semantics                                          |
| ---------------------- | -------------------------------------------------- |
| `TLSHandshakeError`    | TLS handshake failure or warning.                  |
| `TCPError`             | TCP/TLS socket send, receive, listen, etc. error.  |
| `TCPUnexpectedClose`   | Unexpected close of TCP/TLS connection by the EV.  |
| `TCPConnectionTimeout` | Timeout for establishing a connection from the EV. |

### EXI

| Error code         | Semantics           |
| ------------------ | ------------------- |
| `EXIEncodingError` | EXI encoding error. |
| `EXIDecodingError` | EXI decoding error. |

### V2G Application Layer

| Error code                          | Semantics                                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `V2GParameterNotSupported`          | None of the parameter options received by SECC or EVCC are supported.                                   |
| `V2GParameterInvalid`               | Wrong value of V2G message field.                                                                       |
| `V2GParameterNotAllowed`            | Not allowed field present in the message.                                                               |
| `V2GParameterOutOfRange`            | The value of the V2G message field is out of range.                                                     |
| `V2GSequenceError`                  | Wrong sequence of V2G messages.                                                                         |
| `V2GTimeout`                        | V2G timeout exceeded.                                                                                   |
| `V2GPerformanceTime`                | V2G performance exceeded (not reached).                                                                 |
| `V2GNoChargeServiceSelected`        | EVCC did not select charge service - FAILED_NoChargeServiceSelected.                                    |
| `V2GServiceSelectionInvalid`        | EVCC selected a service that was not offered by SECC - FAILED_ServiceSelectionInvalid.                  |
| `V2GPaymentSelectionInvalid`        | EVCC selected Payment Option which is not supported (offered) by SECC - FAILED_PaymentSelectionInvalid. |
| `V2GServiceIdInvalid`               | EVCC requested details of the service that was not offered.                                             |
| `V2GContractCertificateExpired`     | The contract certificate expired.                                                                       |
| `V2GContractCertificateNotYetValid` | The contract certificate is not yet valid.                                                              |

### Certificate

| Error code                             | Semantics                                                     |
| -------------------------------------- | ------------------------------------------------------------- |
| `CertificateInstallationServerTimeout` | Timeout on server response to the CertificateInstallationReq. |
| `CertificateUpdateServerTimeout`       | Timeout on server response to the CertificateUpdateReq.       |
| `CertificatePrivateAndPublicMismatch`  | The certificate public key and private key are not a pair.    |

### Authorization

| Error code                   | Semantics                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| `AuthorizationTimeoutServer` | No response from the backend system on authorization request (e.g. OCPP server).                        |
| `AuthorizationTimeoutUser`   | The user did not perform authorization action (tap RFID card, use a mobile app (remote start)) on time. |
| `AuthorizationRejected`      | Authorization rejected locally or by the remote server.                                                 |

### General Error Codes

| Error code             | Semantics                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| `InsulationFault`      | Insulation resistance low or below the allowed limit.                                      |
| `PowerModuleFault`     | Power module fault.                                                                        |
| `ContactorFault`       | Contactor fault.                                                                           |
| `HighTemperature`      | The temperature is above a maximum value, or the temperature is above an acceptable level. |
| `LowTemperature`       | The temperature is below a minimum value, or the temperature is below an acceptable level. |
| `PowerLoss`            | The EVSE is unable to supply any power.                                                    |
| `ConnectorLockFailure` | Failure to lock or unlock connector.                                                       |
| `UnderVoltage`         | Voltage has dropped below an acceptable level.                                             |
| `OverVoltage`          | Voltage has risen above an acceptable level.                                               |
| `UnderCurrent`         | Current has dropped below an acceptable level.                                             |
| `OverCurrent`          | Current has risen above an acceptable level.                                               |
| `EVShiftPosition`      | Vehicle shift position, vehicle is not in park.                                            |
| `EVRESSMalfunction`    | Vehicle RESS malfunction. Any non-recoverable fault or error.                              |
