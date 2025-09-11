# Error Codes Data Model

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

## Requirements

### ProximityPilotFault

*This error code has no specific parameters.*

### ProximityPilotNotDetected

| Parameter Name | Parameter Type    | Semantics                    |
| :------------- | :---------------- | :--------------------------- |
| `actualValue`  | PhysicalValueType | Measured voltage/resistance. |

### ProximityPilotValueChanged

| Parameter Name  | Parameter Type    | Semantics                       |
| :-------------- | :---------------- | :------------------------------ |
| `actualValue`   | PhysicalValueType | Measured voltage/resistance.    |
| `expectedValue` | PhysicalValueType | Expected proximity pilot value. |

### ControlPilotFault

| Parameter Name    | Parameter Type    | Semantics                  |
| :---------------- | :---------------- | :------------------------- |
| `voltagePositive` | PhysicalValueType | Measured positive voltage. |
| `voltageNegative` | PhysicalValueType | Measured negative voltage. |
| `frequency`       | PhysicalValueType | Measured frequency.        |
| `dutyCycle`       | PhysicalValueType | Measured duty cycle.       |

### ControlPilotStateUnexpected

| Parameter Name    | Parameter Type        | Semantics                  |
| :---------------- | :-------------------- | :------------------------- |
| `actualValue`     | ControlPilotStateType | Detected CP state.         |
| `expectedValue`   | ControlPilotStateType | Expected CP state.         |
| `voltagePositive` | PhysicalValueType     | Measured positive voltage. |
| `voltageNegative` | PhysicalValueType     | Measured negative voltage. |
| `frequency`       | PhysicalValueType     | Measured frequency.        |
| `dutyCycle`       | PhysicalValueType     | Measured duty cycle.       |

### ControlPilotStateNotSupported

| Parameter Name | Parameter Type        | Semantics                                            |
| :------------- | :-------------------- | :--------------------------------------------------- |
| `actualValue`  | ControlPilotStateType | Actual controller pilot state - not supported state. |

### PLCNotFound

*This error code has no specific parameters.*

### PLCFault

| Parameter Name | Parameter Type | Semantics                      |
| :------------- | :------------- | :----------------------------- |
| `error`        | string         | PLC modem-specific error code. |

### PLCLinkDetectionTimeout

| Parameter Name | Parameter Type    | Semantics             |
| :------------- | :---------------- | :-------------------- |
| `timeout`      | PhysicalValueType | Actual timeout value. |

### PLCLinkLeaveTimeout

| Parameter Name | Parameter Type    | Semantics             |
| :------------- | :---------------- | :-------------------- |
| `timeout`      | PhysicalValueType | Actual timeout value. |

### PLCLinkLost

*This error code has no specific parameters.*

### SLACTimeout

| Parameter Name | Parameter Type    | Semantics                             |
| :------------- | :---------------- | :------------------------------------ |
| `message`      | SLACMessageType   | SLAC state when the timeout occurred. |
| `timeout`      | PhysicalValueType | Timeout in milliseconds.              |

### SLACSequenceError

| Parameter Name    | Parameter Type  | Semantics         |
| :---------------- | :-------------- | :---------------- |
| `receivedMessage` | SLACMessageType | Received message. |
| `expectedMessage` | SLACMessageType | Expected message. |

### SLACParameterInvalid

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

### SLACParameterNotAllowed

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

### SLACParameterNotSupported

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

### SLACParameterOutOfRange

| Parameter Name | Parameter Type     | Semantics                                 |
| :------------- | :----------------- | :---------------------------------------- |
| `message`      | SLACMessageType    | Affected V2G message.                     |
| `parameter`    | string             | Name of the parameter in the V2G message. |
| `actualValue`  | UniversalValueType | Actual field value.                       |
| `minValue`     | UniversalValueType | Lower bound of allowed range.             |
| `maxValue`     | UniversalValueType | Upper bound of allowed range.             |

### SLACAttenuationHigh

| Parameter Name | Parameter Type    | Semantics                    |
| :------------- | :---------------- | :--------------------------- |
| `actualValue`  | PhysicalValueType | Actual attenuation.          |
| `maxValue`     | PhysicalValueType | Maximal allowed attenuation. |

### V2GTPProtocolVersionInvalid

| Parameter Name | Parameter Type | Semantics                 |
| :------------- | :------------- | :------------------------ |
| `actualValue`  | integer        | Invalid protocol version. |

### V2GTPInverseProtocolVersionInvalid

| Parameter Name | Parameter Type | Semantics                         |
| :------------- | :------------- | :-------------------------------- |
| `actualValue`  | integer        | Invalid inverse protocol version. |

### V2GTPPayloadLengthInvalid

| Parameter Name | Parameter Type | Semantics                 |
| :------------- | :------------- | :------------------------ |
| `actualValue`  | integer        | Incorrect payload length. |

### V2GTPPayloadTypeInvalid

| Parameter Name  | Parameter Type | Semantics                    |
| :-------------- | :------------- | :--------------------------- |
| `actualValue`   | integer        | Actual payload type value.   |
| `expectedValue` | integer        | Expected payload type value. |

### SDPPayloadLengthInvalid

| Parameter Name | Parameter Type | Semantics              |
| :------------- | :------------- | :--------------------- |
| `actualValue`  | integer        | Actual payload length. |

### SDPParameterInvalid

| Parameter Name  | Parameter Type     | Semantics                                                                                                 |
| :-------------- | :----------------- | :-------------------------------------------------------------------------------------------------------- |
| `parameter`     | string             | Name of the invalid SDP parameter. E.g. "SECC IP Address", "SECC port", "Security", "Transport Protocol". |
| `actualValue`   | UniversalValueType | Actual field value.                                                                                       |
| `expectedValue` | UniversalValueType | Expected field value.                                                                                     |

### SDPDiscoveryTimeout

| Parameter Name | Parameter Type | Semantics                            |
| :------------- | :------------- | :----------------------------------- |
| `retries`      | integer        | Number of performed SDP Req retries. |

### TLSHandshakeError

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `alert`        | integer        | TLS alert number described in IETF RFC 5246. |

### TCPError

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `error`        | string         | Socket specific error.                       |
| `v2gState`     | V2GStateType   | Communication state when the error occurred. |

### TCPUnexpectedClose

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `v2gState`     | V2GStateType   | Communication state when the error occurred. |

### TCPConnectionTimeout

| Parameter Name | Parameter Type    | Semantics           |
| :------------- | :---------------- | :------------------ |
| `actualValue`  | PhysicalValueType | Timeout in seconds. |

### EXIEncodingError

| Parameter Name | Parameter Type | Semantics                           |
| :------------- | :------------- | :---------------------------------- |
| `exi`          | Base64         | EXI Message data encoded as Base64. |

### EXIDecodingError

| Parameter Name | Parameter Type | Semantics                           |
| :------------- | :------------- | :---------------------------------- |
| `exi`          | Base64         | EXI Message data encoded as Base64. |

### V2GParameterNotSupported

| Parameter Name   | Parameter Type     | Semantics                           |
| :--------------- | :----------------- | :---------------------------------- |
| `message`        | V2GMessageType     | Affected V2G message.               |
| `parameter`      | string             | Name of the V2G parameter.          |
| `receivedValue`  | UniversalValueType | List of received parameter values.  |
| `supportedValue` | UniversalValueType | List of supported parameter values. |

### V2GParameterInvalid

| Parameter Name  | Parameter Type     | Semantics                                 |
| :-------------- | :----------------- | :---------------------------------------- |
| `message`       | V2GMessageType     | Affected V2G message.                     |
| `parameter`     | string             | Name of the parameter in the V2G message. |
| `actualValue`   | UniversalValueType | Actual field value.                       |
| `expectedValue` | UniversalValueType | Expected field value.                     |

### V2GParameterNotAllowed

| Parameter Name | Parameter Type | Semantics                                 |
| :------------- | :------------- | :---------------------------------------- |
| `message`      | V2GMessageType | Affected message.                         |
| `parameter`    | string         | Name of the parameter in the V2G message. |

### V2GParameterOutOfRange

| Parameter Name | Parameter Type     | Semantics                                 |
| :------------- | :----------------- | :---------------------------------------- |
| `message`      | V2GMessageType     | Affected V2G message.                     |
| `parameter`    | string             | Name of the parameter in the V2G message. |
| `actualValue`  | UniversalValueType | Actual field value.                       |
| `minValue`     | UniversalValueType | Lower bound of allowed range.             |
| `maxValue`     | UniversalValueType | Upper bound of allowed range.             |

### V2GSequenceError

| Parameter Name    | Parameter Type | Semantics         |
| :---------------- | :------------- | :---------------- |
| `receivedMessage` | V2GMessageType | Received message. |
| `expectedMessage` | V2GMessageType | Expected message. |

### V2GTimeout

| Parameter Name | Parameter Type    | Semantics                       |
| :------------- | :---------------- | :------------------------------ |
| `actualValue`  | PhysicalValueType | Actual timeout in milliseconds. |
| `message`      | V2GMessageType    | Affected V2G message.           |
| `timeoutType`  | V2GTimeoutType    | Timeout type.                   |

### V2GPerformanceTime

| Parameter Name | Parameter Type    | Semantics                                |
| :------------- | :---------------- | :--------------------------------------- |
| `actualValue`  | PhysicalValueType | Actual performance time in milliseconds. |
| `message`      | V2GMessageType    | Affected V2G message.                    |
| `timeoutType`  | V2GTimeoutType    | Timeout type.                            |

### V2GNoChargeServiceSelected

| Parameter Name | Parameter Type | Semantics                         |
| :------------- | :------------- | :-------------------------------- |
| `selected`     | string         | IDs of selected services by EVCC. |

### V2GServiceSelectionInvalid

| Parameter Name | Parameter Type | Semantics                                        |
| :------------- | :------------- | :----------------------------------------------- |
| `selected`     | integer        | ID of the selected service by EVCC               |
| `offered`      | integer[]      | IDs of the offered services to the EVCC by SECC. |

### V2GPaymentSelectionInvalid

| Parameter Name | Parameter Type | Semantics                               |
| :------------- | :------------- | :-------------------------------------- |
| `selected`     | string         | Selected service by EVCC.               |
| `offered`      | string[]       | Offered service(s) to the EVCC by SECC. |

### V2GServiceIdInvalid

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `serviceId`    | integer        | Identifier of the service requested by EVCC. |
| `offered`      | integer[]      | List of offered services by SECC.            |

### V2GContractCertificateExpired

| Parameter Name     | Parameter Type | Semantics                                                        |
| :----------------- | :------------- | :--------------------------------------------------------------- |
| `certificateChain` | string         | Contract certificate and sub-certificates encoded in PEM format. |

### V2GContractCertificateNotYetValid

| Parameter Name     | Parameter Type | Semantics                                                        |
| :----------------- | :------------- | :--------------------------------------------------------------- |
| `certificateChain` | string         | Contract certificate and sub-certificates encoded in PEM format. |

### CertificateInstallationServerTimeout

| Parameter Name | Parameter Type    | Semantics                      |
| :------------- | :---------------- | :----------------------------- |
| `timeout`      | PhysicalValueType | Timeout value in milliseconds. |

### CertificateUpdateServerTimeout

| Parameter Name | Parameter Type    | Semantics                      |
| :------------- | :---------------- | :----------------------------- |
| `timeout`      | PhysicalValueType | Timeout value in milliseconds. |

### CertificatePrivateAndPublicMismatch

| Parameter Name     | Parameter Type | Semantics                                |
| :----------------- | :------------- | :--------------------------------------- |
| `message`          | V2GMessageType | V2G message with certificates.           |
| `certificateChain` | string         | Certificate chain encoded in PEM format. |

### AuthorizationTimeoutServer

| Parameter Name | Parameter Type    | Semantics                                            |
| :------------- | :---------------- | :--------------------------------------------------- |
| `timeout`      | PhysicalValueType | Server response timeout in milliseconds.             |
| `requestId`    | string            | Id of the authorization message sent to the backend. |

### AuthorizationTimeoutUser

| Parameter Name        | Parameter Type          | Semantics                                                 |
| :-------------------- | :---------------------- | :-------------------------------------------------------- |
| `timeout`             | PhysicalValueType       | User interaction timeout in milliseconds.                 |
| `authorizationMethod` | AuthorizationMethodType | Method of authorization that the user is expected to use. |

### AuthorizationRejected

| Parameter Name        | Parameter Type          | Semantics                                                 |
| :-------------------- | :---------------------- | :-------------------------------------------------------- |
| `authorizationMethod` | AuthorizationMethodType | Method of authorization that the user is expected to use. |

### InsulationFault

| Parameter Name | Parameter Type         | Semantics                                     |
| :------------- | :--------------------- | :-------------------------------------------- |
| `v2gState`     | CommunicationStateType | Communication state where the error occurred. |
| `resistance`   | PhysicalValueType      | Cable line resistance.                        |
| `capacity`     | PhysicalValueType      | Cable capacity.                               |

### PowerModuleFault

| Parameter Name | Parameter Type | Semantics                    |
| :------------- | :------------- | :--------------------------- |
| `error`        | string         | Power module-specific error. |
| `id`           | string         | Power module identifier.     |


### ContactorFault

| Parameter Name  | Parameter Type     | Semantics                 |
| :-------------- | :----------------- | :------------------------ |
| `id`            | string             | Contactor identifier.     |
| `actualValue`   | ContactorStateType | Actual contactor state.   |
| `expectedValue` | ContactorStateType | Expected contactor state. |
| `type`          | ContactorType      | Type of the contactor.    |

### HighTemperature

| Parameter Name | Parameter Type          | Semantics                                 |
| :------------- | :---------------------- | :---------------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual temperature.                       |
| `threshold`    | PhysicalValueType       | Warning or error threshold.               |
| `location`     | TemperatureLocationType | Location of the temperature measurements. |

### LowTemperature

| Parameter Name | Parameter Type          | Semantics                                 |
| :------------- | :---------------------- | :---------------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual temperature.                       |
| `threshold`    | PhysicalValueType       | Warning or error threshold.               |
| `location`     | TemperatureLocationType | Location of the temperature measurements. |

### PowerLoss

*This error code has no specific parameters.*

### ConnectorLockFailure

| Parameter Name  | Parameter Type         | Semantics            |
| :-------------- | :--------------------- | :------------------- |
| `actualValue`   | ConnectorLockStateType | Actual lock state.   |
| `expectedValue` | ConnectorLockStateType | Expected lock state. |

### UnderVoltage

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual voltage.                      |
| `minValue`     | PhysicalValueType       | Lower bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the voltage measurement. |

### OverVoltage

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual voltage.                      |
| `maxValue`     | PhysicalValueType       | Upper bound of allowed range         |
| `location`     | MeasurementLocationType | Location of the voltage measurement. |

### UnderCurrent

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual current.                      |
| `minValue`     | PhysicalValueType       | Lower bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the current measurement. |

### OverCurrent

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual current.                      |
| `maxValue`     | PhysicalValueType       | Upper bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the current measurement. |

### EVShiftPosition

*This error code has no specific parameters.*

### EVRESSMalfunction

*This error code has no specific parameters.*
