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

Table: Low Level Communication Error Codes

| Error code                      | Semantics                                                                                   |
| :------------------------------ | :------------------------------------------------------------------------------------------ |
| `ProximityPilotFault`           | Proximity value (voltage/resistance) out of range.                                          |
| `ProximityPilotNotDetected`     | The proximity pilot is not detected, but the EV (CP detected) is connected.                 |
| `ProximityPilotValueChanged`    | The proximity pilot value has been changed while the plug is connected.                     |
| `ControlPilotFault`             | The control pilot parameters are out of range.                                              |
| `ControlPilotStateUnexpected`   | Unexpected Control Pilot state detected.                                                    |
| `ControlPilotStateNotSupported` | Control Pilot state is not supported (e.g. state D (ventilation) is not supported by EVSE). |

### SLAC and PLC

Table: SLAC and PLC Error Codes

| Error code                  | Semantics                                                |
| :-------------------------- | :------------------------------------------------------- |
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

Table: V2G Transport Protocol Error Codes

| Error code                           | Semantics                                       |
| :----------------------------------- | :---------------------------------------------- |
| `V2GTPProtocolVersionInvalid`        | V2GTP header: invalid protocol version.         |
| `V2GTPInverseProtocolVersionInvalid` | V2GTP header: invalid inverse protocol version. |
| `V2GTPPayloadLengthInvalid`          | V2GTP header: invalid payload length.           |
| `V2GTPPayloadTypeInvalid`            | V2GTP header: invalid payload type.             |

### SDP

Table: SDP Error Codes

| Error code                | Semantics                                |
| :------------------------ | :--------------------------------------- |
| `SDPPayloadLengthInvalid` | Invalid request/response payload length. |
| `SDPParameterInvalid`     | Invalid SDP field value.                 |
| `SDPDiscoveryTimeout`     | EVCC was not able to discover SECC.      |

### TCP and TLS

Table: TCP and TLS Error Codes

| Error code             | Semantics                                          |
| :--------------------- | :------------------------------------------------- |
| `TLSHandshakeError`    | TLS handshake failure or warning.                  |
| `TCPError`             | TCP/TLS socket send, receive, listen, etc. error.  |
| `TCPUnexpectedClose`   | Unexpected close of TCP/TLS connection by the EV.  |
| `TCPConnectionTimeout` | Timeout for establishing a connection from the EV. |

### EXI

Table: EXI Error Codes

| Error code         | Semantics           |
| :----------------- | :------------------ |
| `EXIEncodingError` | EXI encoding error. |
| `EXIDecodingError` | EXI decoding error. |

### V2G Application Layer

Table: V2G Application Layer Error Codes

| Error code                          | Semantics                                                                                                |
| :---------------------------------- | :------------------------------------------------------------------------------------------------------- |
| `V2GParameterNotSupported`          | None of the parameter options received by SECC or EVCC are supported.                                    |
| `V2GParameterInvalid`               | Wrong value of V2G message field.                                                                        |
| `V2GParameterNotAllowed`            | Not allowed field present in the message.                                                                |
| `V2GParameterOutOfRange`            | The value of the V2G message field is out of range.                                                      |
| `V2GSequenceError`                  | Wrong sequence of V2G messages.                                                                          |
| `V2GTimeout`                        | V2G timeout exceeded.                                                                                    |
| `V2GPerformanceTime`                | V2G performance exceeded (not reached).                                                                  |
| `V2GNoChargeServiceSelected`        | EVCC did not select charge service - FAILED\_NoChargeServiceSelected.                                    |
| `V2GServiceSelectionInvalid`        | EVCC selected a service that was not offered by SECC - FAILED\_ServiceSelectionInvalid.                  |
| `V2GPaymentSelectionInvalid`        | EVCC selected Payment Option which is not supported (offered) by SECC - FAILED\_PaymentSelectionInvalid. |
| `V2GServiceIdInvalid`               | EVCC requested details of the service that was not offered.                                              |
| `V2GContractCertificateExpired`     | The contract certificate expired.                                                                        |
| `V2GContractCertificateNotYetValid` | The contract certificate is not yet valid.                                                               |

### Certificate

Table: Certificate Error Codes

| Error code                             | Semantics                                                     |
| :------------------------------------- | :------------------------------------------------------------ |
| `CertificateInstallationServerTimeout` | Timeout on server response to the CertificateInstallationReq. |
| `CertificateUpdateServerTimeout`       | Timeout on server response to the CertificateUpdateReq.       |
| `CertificatePrivateAndPublicMismatch`  | The certificate public key and private key are not a pair.    |

### Authorization

Table: Authorization Error Codes

| Error code                   | Semantics                                                                                               |
| :--------------------------- | :------------------------------------------------------------------------------------------------------ |
| `AuthorizationTimeoutServer` | No response from the backend system on authorization request (e.g. OCPP server).                        |
| `AuthorizationTimeoutUser`   | The user did not perform authorization action (tap RFID card, use a mobile app (remote start)) on time. |
| `AuthorizationRejected`      | Authorization rejected locally or by the remote server.                                                 |

### General Error Codes

Table: General Error Codes

| Error code             | Semantics                                                                                  |
| :--------------------- | :----------------------------------------------------------------------------------------- |
| `InsulationFault`      | insulation resistance low or below the allowed limit.                                      |
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

{{ table_caption('prox_pilot_not_detected_parameters', 'Semantics and type definition for ProximityPilotNotDetected error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                    |
| :------------- | :---------------- | :--------------------------- |
| `actualValue`  | PhysicalValueType | Measured voltage/resistance. |

{{ requirement() }} The `ProximityPilotNotDetected` error code parameters shall be used as defined in {{ table_ref('prox_pilot_not_detected_parameters') }}.

### ProximityPilotValueChanged

{{ table_caption('prox_pilot_value_changed_parameters', 'Semantics and type definition for ProximityPilotValueChanged error code parameters') }}

| Parameter Name  | Parameter Type    | Semantics                       |
| :-------------- | :---------------- | :------------------------------ |
| `actualValue`   | PhysicalValueType | Measured voltage/resistance.    |
| `expectedValue` | PhysicalValueType | Expected proximity pilot value. |

{{ requirement() }} The `ProximityPilotValueChanged` error code parameters shall be used as defined in {{ table_ref('prox_pilot_value_changed_parameters') }}.

### ControlPilotFault

{{ table_caption('ctrl_pilot_fault_parameters', 'Semantics and type definition for ControlPilotFault error code parameters') }}

| Parameter Name    | Parameter Type    | Semantics                  |
| :---------------- | :---------------- | :------------------------- |
| `voltagePositive` | PhysicalValueType | Measured positive voltage. |
| `voltageNegative` | PhysicalValueType | Measured negative voltage. |
| `frequency`       | PhysicalValueType | Measured frequency.        |
| `dutyCycle`       | PhysicalValueType | Measured duty cycle.       |

{{ requirement() }} The `ControlPilotFault` error code parameters shall be used as defined in {{ table_ref('ctrl_pilot_fault_parameters') }}.

### ControlPilotStateUnexpected

{{ table_caption('ctrl_pilot_state_unexpected_parameters', 'Semantics and type definition for ControlPilotStateUnexpected error code parameters') }}

| Parameter Name    | Parameter Type        | Semantics                  |
| :---------------- | :-------------------- | :------------------------- |
| `actualValue`     | ControlPilotStateType | Detected CP state.         |
| `expectedValue`   | ControlPilotStateType | Expected CP state.         |
| `voltagePositive` | PhysicalValueType     | Measured positive voltage. |
| `voltageNegative` | PhysicalValueType     | Measured negative voltage. |
| `frequency`       | PhysicalValueType     | Measured frequency.        |
| `dutyCycle`       | PhysicalValueType     | Measured duty cycle.       |

{{ requirement() }} The `ControlPilotStateUnexpected` error code parameters shall be used as defined in {{ table_ref('ctrl_pilot_state_unexpected_parameters') }}.

### ControlPilotStateNotSupported

{{ table_caption('ctrl_pilot_state_not_supported_parameters', 'Semantics and type definition for ControlPilotStateNotSupported error code parameters') }}

| Parameter Name | Parameter Type        | Semantics                                            |
| :------------- | :-------------------- | :--------------------------------------------------- |
| `actualValue`  | ControlPilotStateType | Actual controller pilot state - not supported state. |

{{ requirement() }} The `ControlPilotStateNotSupported` error code parameters shall be used as defined in {{ table_ref('ctrl_pilot_state_not_supported_parameters') }}.

### PLCNotFound

*This error code has no specific parameters.*

### PLCFault

{{ table_caption('plc_fault_parameters', 'Semantics and type definition for PLCFault error code parameters') }}

| Parameter Name | Parameter Type | Semantics                      |
| :------------- | :------------- | :----------------------------- |
| `error`        | string         | PLC modem-specific error code. |

{{ requirement() }} The `PLCFault` error code parameters shall be used as defined in {{ table_ref('plc_fault_parameters') }}.

### PLCLinkDetectionTimeout

{{ table_caption('plc_link_detect_timeout_parameters', 'Semantics and type definition for PLCLinkDetectionTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics             |
| :------------- | :---------------- | :-------------------- |
| `timeout`      | PhysicalValueType | Actual timeout value. |

{{ requirement() }} The `PLCLinkDetectionTimeout` error code parameters shall be used as defined in {{ table_ref('plc_link_detect_timeout_parameters') }}.

### PLCLinkLeaveTimeout

{{ table_caption('plc_link_leave_timeout_parameters', 'Semantics and type definition for PLCLinkLeaveTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics             |
| :------------- | :---------------- | :-------------------- |
| `timeout`      | PhysicalValueType | Actual timeout value. |

{{ requirement() }} The `PLCLinkLeaveTimeout` error code parameters shall be used as defined in {{ table_ref('plc_link_leave_timeout_parameters') }}.

### PLCLinkLost

*This error code has no specific parameters.*

### SLACTimeout

{{ table_caption('slac_timeout_parameters', 'Semantics and type definition for SLACTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                             |
| :------------- | :---------------- | :------------------------------------ |
| `message`      | SLACMessageType   | SLAC state when the timeout occurred. |
| `timeout`      | PhysicalValueType | Timeout in milliseconds.              |

{{ requirement() }} The `SLACTimeout` error code parameters shall be used as defined in {{ table_ref('slac_timeout_parameters') }}.

### SLACSequenceError

{{ table_caption('slac_seq_error_parameters', 'Semantics and type definition for SLACSequenceError error code parameters') }}

| Parameter Name    | Parameter Type  | Semantics         |
| :---------------- | :-------------- | :---------------- |
| `receivedMessage` | SLACMessageType | Received message. |
| `expectedMessage` | SLACMessageType | Expected message. |

{{ requirement() }} The `SLACSequenceError` error code parameters shall be used as defined in {{ table_ref('slac_seq_error_parameters') }}.

### SLACParameterInvalid

{{ table_caption('slac_param_invalid_parameters', 'Semantics and type definition for SLACParameterInvalid error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

{{ requirement() }} The `SLACParameterInvalid` error code parameters shall be used as defined in {{ table_ref('slac_param_invalid_parameters') }}.

### SLACParameterNotAllowed

{{ table_caption('slac_param_not_allowed_parameters', 'Semantics and type definition for SLACParameterNotAllowed error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

{{ requirement() }} The `SLACParameterNotAllowed` error code parameters shall be used as defined in {{ table_ref('slac_param_not_allowed_parameters') }}.

### SLACParameterNotSupported

{{ table_caption('slac_param_not_supported_parameters', 'Semantics and type definition for SLACParameterNotSupported error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                         |
| :-------------- | :----------------- | :-------------------------------- |
| `message`       | SLACMessageType    | Affected message.                 |
| `parameter`     | string             | Name of the field in the message. |
| `actualValue`   | UniversalValueType | Actual field value.               |
| `expectedValue` | UniversalValueType | Expected field value.             |

{{ requirement() }} The `SLACParameterNotSupported` error code parameters shall be used as defined in {{ table_ref('slac_param_not_supported_parameters') }}.

### SLACParameterOutOfRange

{{ table_caption('slac_param_out_of_range_parameters', 'Semantics and type definition for SLACParameterOutOfRange error code parameters') }}

| Parameter Name | Parameter Type     | Semantics                                 |
| :------------- | :----------------- | :---------------------------------------- |
| `message`      | SLACMessageType    | Affected V2G message.                     |
| `parameter`    | string             | Name of the parameter in the V2G message. |
| `actualValue`  | UniversalValueType | Actual field value.                       |
| `minValue`     | UniversalValueType | Lower bound of allowed range.             |
| `maxValue`     | UniversalValueType | Upper bound of allowed range.             |

{{ requirement() }} The `SLACParameterOutOfRange` error code parameters shall be used as defined in {{ table_ref('slac_param_out_of_range_parameters') }}.

### SLACAttenuationHigh

{{ table_caption('slac_attenuation_high_parameters', 'Semantics and type definition for SLACAttenuationHigh error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                    |
| :------------- | :---------------- | :--------------------------- |
| `actualValue`  | PhysicalValueType | Actual attenuation.          |
| `maxValue`     | PhysicalValueType | Maximal allowed attenuation. |

{{ requirement() }} The `SLACAttenuationHigh` error code parameters shall be used as defined in {{ table_ref('slac_attenuation_high_parameters') }}.

### V2GTPProtocolVersionInvalid

{{ table_caption('v2gtp_proto_ver_invalid_parameters', 'Semantics and type definition for V2GTPProtocolVersionInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                 |
| :------------- | :------------- | :------------------------ |
| `actualValue`  | integer        | Invalid protocol version. |

{{ requirement() }} The `V2GTPProtocolVersionInvalid` error code parameters shall be used as defined in {{ table_ref('v2gtp_proto_ver_invalid_parameters') }}.

### V2GTPInverseProtocolVersionInvalid

{{ table_caption('v2gtp_inv_proto_ver_invalid_parameters', 'Semantics and type definition for V2GTPInverseProtocolVersionInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                         |
| :------------- | :------------- | :-------------------------------- |
| `actualValue`  | integer        | Invalid inverse protocol version. |

{{ requirement() }} The `V2GTPInverseProtocolVersionInvalid` error code parameters shall be used as defined in {{ table_ref('v2gtp_inv_proto_ver_invalid_parameters') }}.

### V2GTPPayloadLengthInvalid

{{ table_caption('v2gtp_payload_len_invalid_parameters', 'Semantics and type definition for V2GTPPayloadLengthInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                 |
| :------------- | :------------- | :------------------------ |
| `actualValue`  | integer        | Incorrect payload length. |

{{ requirement() }} The `V2GTPPayloadLengthInvalid` error code parameters shall be used as defined in {{ table_ref('v2gtp_payload_len_invalid_parameters') }}.

### V2GTPPayloadTypeInvalid

{{ table_caption('v2gtp_payload_type_invalid_parameters', 'Semantics and type definition for V2GTPPayloadTypeInvalid error code parameters') }}

| Parameter Name  | Parameter Type | Semantics                    |
| :-------------- | :------------- | :--------------------------- |
| `actualValue`   | integer        | Actual payload type value.   |
| `expectedValue` | integer        | Expected payload type value. |

{{ requirement() }} The `V2GTPPayloadTypeInvalid` error code parameters shall be used as defined in {{ table_ref('v2gtp_payload_type_invalid_parameters') }}.

### SDPPayloadLengthInvalid

{{ table_caption('sdp_payload_len_invalid_parameters', 'Semantics and type definition for SDPPayloadLengthInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics              |
| :------------- | :------------- | :--------------------- |
| `actualValue`  | integer        | Actual payload length. |

{{ requirement() }} The `SDPPayloadLengthInvalid` error code parameters shall be used as defined in {{ table_ref('sdp_payload_len_invalid_parameters') }}.

### SDPParameterInvalid

{{ table_caption('sdp_param_invalid_parameters', 'Semantics and type definition for SDPParameterInvalid error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                                                                                                 |
| :-------------- | :----------------- | :-------------------------------------------------------------------------------------------------------- |
| `parameter`     | string             | Name of the invalid SDP parameter. E.g. "SECC IP Address", "SECC port", "Security", "Transport Protocol". |
| `actualValue`   | UniversalValueType | Actual field value.                                                                                       |
| `expectedValue` | UniversalValueType | Expected field value.                                                                                     |

{{ requirement() }} The `SDPParameterInvalid` error code parameters shall be used as defined in {{ table_ref('sdp_param_invalid_parameters') }}.

### SDPDiscoveryTimeout

{{ table_caption('sdp_discovery_timeout_parameters', 'Semantics and type definition for SDPDiscoveryTimeout error code parameters') }}

| Parameter Name | Parameter Type | Semantics                            |
| :------------- | :------------- | :----------------------------------- |
| `retries`      | integer        | Number of performed SDP Req retries. |

{{ requirement() }} The `SDPDiscoveryTimeout` error code parameters shall be used as defined in {{ table_ref('sdp_discovery_timeout_parameters') }}.

### TLSHandshakeError

{{ table_caption('tls_handshake_error_parameters', 'Semantics and type definition for TLSHandshakeError error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `alert`        | integer        | TLS alert number described in IETF RFC 5246. |

{{ requirement() }} The `TLSHandshakeError` error code parameters shall be used as defined in {{ table_ref('tls_handshake_error_parameters') }}.

### TCPError

{{ table_caption('tcp_error_parameters', 'Semantics and type definition for TCPError error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `error`        | string         | Socket specific error.                       |
| `v2gState`     | V2GStateType   | Communication state when the error occurred. |

{{ requirement() }} The `TCPError` error code parameters shall be used as defined in {{ table_ref('tcp_error_parameters') }}.

### TCPUnexpectedClose

{{ table_caption('tcp_unexpected_close_parameters', 'Semantics and type definition for TCPUnexpectedClose error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `v2gState`     | V2GStateType   | Communication state when the error occurred. |

{{ requirement() }} The `TCPUnexpectedClose` error code parameters shall be used as defined in {{ table_ref('tcp_unexpected_close_parameters') }}.

### TCPConnectionTimeout

{{ table_caption('tcp_conn_timeout_parameters', 'Semantics and type definition for TCPConnectionTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics           |
| :------------- | :---------------- | :------------------ |
| `actualValue`  | PhysicalValueType | Timeout in seconds. |

{{ requirement() }} The `TCPConnectionTimeout` error code parameters shall be used as defined in {{ table_ref('tcp_conn_timeout_parameters') }}.

### EXIEncodingError

{{ table_caption('exi_encoding_error_parameters', 'Semantics and type definition for EXIEncodingError error code parameters') }}

| Parameter Name | Parameter Type | Semantics                           |
| :------------- | :------------- | :---------------------------------- |
| `exi`          | Base64         | EXI Message data encoded as Base64. |

{{ requirement() }} The `EXIEncodingError` error code parameters shall be used as defined in {{ table_ref('exi_encoding_error_parameters') }}.

### EXIDecodingError

{{ table_caption('exi_decoding_error_parameters', 'Semantics and type definition for EXIDecodingError error code parameters') }}

| Parameter Name | Parameter Type | Semantics                           |
| :------------- | :------------- | :---------------------------------- |
| `exi`          | Base64         | EXI Message data encoded as Base64. |

{{ requirement() }} The `EXIDecodingError` error code parameters shall be used as defined in {{ table_ref('exi_decoding_error_parameters') }}.

### V2GParameterNotSupported

{{ table_caption('v2g_param_not_supported_parameters', 'Semantics and type definition for V2GParameterNotSupported error code parameters') }}

| Parameter Name   | Parameter Type     | Semantics                           |
| :--------------- | :----------------- | :---------------------------------- |
| `message`        | V2GMessageType     | Affected V2G message.               |
| `parameter`      | string             | Name of the V2G parameter.          |
| `receivedValue`  | UniversalValueType | List of received parameter values.  |
| `supportedValue` | UniversalValueType | List of supported parameter values. |

{{ requirement() }} The `V2GParameterNotSupported` error code parameters shall be used as defined in {{ table_ref('v2g_param_not_supported_parameters') }}.

### V2GParameterInvalid

{{ table_caption('v2g_param_invalid_parameters', 'Semantics and type definition for V2GParameterInvalid error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                                 |
| :-------------- | :----------------- | :---------------------------------------- |
| `message`       | V2GMessageType     | Affected V2G message.                     |
| `parameter`     | string             | Name of the parameter in the V2G message. |
| `actualValue`   | UniversalValueType | Actual field value.                       |
| `expectedValue` | UniversalValueType | Expected field value.                     |

{{ requirement() }} The `V2GParameterInvalid` error code parameters shall be used as defined in {{ table_ref('v2g_param_invalid_parameters') }}.

### V2GParameterNotAllowed

{{ table_caption('v2g_param_not_allowed_parameters', 'Semantics and type definition for V2GParameterNotAllowed error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                 |
| :------------- | :------------- | :---------------------------------------- |
| `message`      | V2GMessageType | Affected message.                         |
| `parameter`    | string         | Name of the parameter in the V2G message. |

{{ requirement() }} The `V2GParameterNotAllowed` error code parameters shall be used as defined in {{ table_ref('v2g_param_not_allowed_parameters') }}.

### V2GParameterOutOfRange

{{ table_caption('v2g_param_out_of_range_parameters', 'Semantics and type definition for V2GParameterOutOfRange error code parameters') }}

| Parameter Name | Parameter Type     | Semantics                                 |
| :------------- | :----------------- | :---------------------------------------- |
| `message`      | V2GMessageType     | Affected V2G message.                     |
| `parameter`    | string             | Name of the parameter in the V2G message. |
| `actualValue`  | UniversalValueType | Actual field value.                       |
| `minValue`     | UniversalValueType | Lower bound of allowed range.             |
| `maxValue`     | UniversalValueType | Upper bound of allowed range.             |

{{ requirement() }} The `V2GParameterOutOfRange` error code parameters shall be used as defined in {{ table_ref('v2g_param_out_of_range_parameters') }}.

### V2GSequenceError

{{ table_caption('v2g_seq_error_parameters', 'Semantics and type definition for V2GSequenceError error code parameters') }}

| Parameter Name    | Parameter Type | Semantics         |
| :---------------- | :------------- | :---------------- |
| `receivedMessage` | V2GMessageType | Received message. |
| `expectedMessage` | V2GMessageType | Expected message. |

{{ requirement() }} The `V2GSequenceError` error code parameters shall be used as defined in {{ table_ref('v2g_seq_error_parameters') }}.

### V2GTimeout

{{ table_caption('v2g_timeout_parameters', 'Semantics and type definition for V2GTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                       |
| :------------- | :---------------- | :------------------------------ |
| `actualValue`  | PhysicalValueType | Actual timeout in milliseconds. |
| `message`      | V2GMessageType    | Affected V2G message.           |
| `timeoutType`  | V2GTimeoutType    | Timeout type.                   |

{{ requirement() }} The `V2GTimeout` error code parameters shall be used as defined in {{ table_ref('v2g_timeout_parameters') }}.

### V2GPerformanceTime

{{ table_caption('v2g_perf_time_parameters', 'Semantics and type definition for V2GPerformanceTime error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                                |
| :------------- | :---------------- | :--------------------------------------- |
| `actualValue`  | PhysicalValueType | Actual performance time in milliseconds. |
| `message`      | V2GMessageType    | Affected V2G message.                    |
| `timeoutType`  | V2GTimeoutType    | Timeout type.                            |

{{ requirement() }} The `V2GPerformanceTime` error code parameters shall be used as defined in {{ table_ref('v2g_perf_time_parameters') }}.

### V2GNoChargeServiceSelected

{{ table_caption('v2g_no_charge_svc_selected_parameters', 'Semantics and type definition for V2GNoChargeServiceSelected error code parameters') }}

| Parameter Name | Parameter Type | Semantics                         |
| :------------- | :------------- | :-------------------------------- |
| `selected`     | string         | IDs of selected services by EVCC. |

{{ requirement() }} The `V2GNoChargeServiceSelected` error code parameters shall be used as defined in {{ table_ref('v2g_no_charge_svc_selected_parameters') }}.

### V2GServiceSelectionInvalid

{{ table_caption('v2g_svc_selection_invalid_parameters', 'Semantics and type definition for V2GServiceSelectionInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                        |
| :------------- | :------------- | :----------------------------------------------- |
| `selected`     | integer        | ID of the selected service by EVCC.              |
| `offered`      | integer[]      | IDs of the offered services to the EVCC by SECC. |

{{ requirement() }} The `V2GServiceSelectionInvalid` error code parameters shall be used as defined in {{ table_ref('v2g_svc_selection_invalid_parameters') }}.

### V2GPaymentSelectionInvalid

{{ table_caption('v2g_payment_selection_invalid_parameters', 'Semantics and type definition for V2GPaymentSelectionInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                               |
| :------------- | :------------- | :-------------------------------------- |
| `selected`     | string         | Selected service by EVCC.               |
| `offered`      | string[]       | Offered service(s) to the EVCC by SECC. |

{{ requirement() }} The `V2GPaymentSelectionInvalid` error code parameters shall be used as defined in {{ table_ref('v2g_payment_selection_invalid_parameters') }}.

### V2GServiceIdInvalid

{{ table_caption('v2g_svc_id_invalid_parameters', 'Semantics and type definition for V2GServiceIdInvalid error code parameters') }}

| Parameter Name | Parameter Type | Semantics                                    |
| :------------- | :------------- | :------------------------------------------- |
| `serviceId`    | integer        | Identifier of the service requested by EVCC. |
| `offered`      | integer[]      | List of offered services by SECC.            |

{{ requirement() }} The `V2GServiceIdInvalid` error code parameters shall be used as defined in {{ table_ref('v2g_svc_id_invalid_parameters') }}.

### V2GContractCertificateExpired

{{ table_caption('v2g_contract_cert_expired_parameters', 'Semantics and type definition for V2GContractCertificateExpired error code parameters') }}

| Parameter Name     | Parameter Type | Semantics                                                        |
| :----------------- | :------------- | :--------------------------------------------------------------- |
| `certificateChain` | string         | Contract certificate and sub-certificates encoded in PEM format. |

{{ requirement() }} The `V2GContractCertificateExpired` error code parameters shall be used as defined in {{ table_ref('v2g_contract_cert_expired_parameters') }}.

### V2GContractCertificateNotYetValid

{{ table_caption('v2g_contract_cert_not_yet_valid_parameters', 'Semantics and type definition for V2GContractCertificateNotYetValid error code parameters') }}

| Parameter Name     | Parameter Type | Semantics                                                        |
| :----------------- | :------------- | :--------------------------------------------------------------- |
| `certificateChain` | string         | Contract certificate and sub-certificates encoded in PEM format. |

{{ requirement() }} The `V2GContractCertificateNotYetValid` error code parameters shall be used as defined in {{ table_ref('v2g_contract_cert_not_yet_valid_parameters') }}.

### CertificateInstallationServerTimeout

{{ table_caption('cert_install_server_timeout_parameters', 'Semantics and type definition for CertificateInstallationServerTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                      |
| :------------- | :---------------- | :----------------------------- |
| `timeout`      | PhysicalValueType | Timeout value in milliseconds. |

{{ requirement() }} The `CertificateInstallationServerTimeout` error code parameters shall be used as defined in {{ table_ref('cert_install_server_timeout_parameters') }}.

### CertificateUpdateServerTimeout

{{ table_caption('cert_update_server_timeout_parameters', 'Semantics and type definition for CertificateUpdateServerTimeout error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                      |
| :------------- | :---------------- | :----------------------------- |
| `timeout`      | PhysicalValueType | Timeout value in milliseconds. |

{{ requirement() }} The `CertificateUpdateServerTimeout` error code parameters shall be used as defined in {{ table_ref('cert_update_server_timeout_parameters') }}.

### CertificatePrivateAndPublicMismatch

{{ table_caption('cert_priv_pub_mismatch_parameters', 'Semantics and type definition for CertificatePrivateAndPublicMismatch error code parameters') }}

| Parameter Name     | Parameter Type | Semantics                                |
| :----------------- | :------------- | :--------------------------------------- |
| `message`          | V2GMessageType | V2G message with certificates.           |
| `certificateChain` | string         | Certificate chain encoded in PEM format. |

{{ requirement() }} The `CertificatePrivateAndPublicMismatch` error code parameters shall be used as defined in {{ table_ref('cert_priv_pub_mismatch_parameters') }}.

### AuthorizationTimeoutServer

{{ table_caption('auth_timeout_server_parameters', 'Semantics and type definition for AuthorizationTimeoutServer error code parameters') }}

| Parameter Name | Parameter Type    | Semantics                                            |
| :------------- | :---------------- | :--------------------------------------------------- |
| `timeout`      | PhysicalValueType | Server response timeout in milliseconds.             |
| `requestId`    | string            | Id of the authorization message sent to the backend. |

{{ requirement() }} The `AuthorizationTimeoutServer` error code parameters shall be used as defined in {{ table_ref('auth_timeout_server_parameters') }}.

### AuthorizationTimeoutUser

{{ table_caption('auth_timeout_user_parameters', 'Semantics and type definition for AuthorizationTimeoutUser error code parameters') }}

| Parameter Name        | Parameter Type          | Semantics                                                 |
| :-------------------- | :---------------------- | :-------------------------------------------------------- |
| `timeout`             | PhysicalValueType       | User interaction timeout in milliseconds.                 |
| `authorizationMethod` | AuthorizationMethodType | Method of authorization that the user is expected to use. |

{{ requirement() }} The `AuthorizationTimeoutUser` error code parameters shall be used as defined in {{ table_ref('auth_timeout_user_parameters') }}.

### AuthorizationRejected

{{ table_caption('auth_rejected_parameters', 'Semantics and type definition for AuthorizationRejected error code parameters') }}

| Parameter Name        | Parameter Type          | Semantics                                                 |
| :-------------------- | :---------------------- | :-------------------------------------------------------- |
| `authorizationMethod` | AuthorizationMethodType | Method of authorization that the user is expected to use. |

{{ requirement() }} The `AuthorizationRejected` error code parameters shall be used as defined in {{ table_ref('auth_rejected_parameters') }}.

### InsulationFault

{{ table_caption('insulation_fault_parameters', 'Semantics and type definition for InsulationFault error code parameters') }}

| Parameter Name | Parameter Type         | Semantics                                     |
| :------------- | :--------------------- | :-------------------------------------------- |
| `v2gState`     | CommunicationStateType | Communication state where the error occurred. |
| `resistance`   | PhysicalValueType      | Cable line resistance.                        |
| `capacity`     | PhysicalValueType      | Cable capacity.                               |

{{ requirement() }} The `InsulationFault` error code parameters shall be used as defined in {{ table_ref('insulation_fault_parameters') }}.

### PowerModuleFault

{{ table_caption('power_module_fault_parameters', 'Semantics and type definition for PowerModuleFault error code parameters') }}

| Parameter Name | Parameter Type | Semantics                    |
| :------------- | :------------- | :--------------------------- |
| `error`        | string         | Power module-specific error. |
| `id`           | string         | Power module identifier.     |

{{ requirement() }} The `PowerModuleFault` error code parameters shall be used as defined in {{ table_ref('power_module_fault_parameters') }}.

### ContactorFault

{{ table_caption('contactor_fault_parameters', 'Semantics and type definition for ContactorFault error code parameters') }}

| Parameter Name  | Parameter Type     | Semantics                 |
| :-------------- | :----------------- | :------------------------ |
| `id`            | string             | Contactor identifier.     |
| `actualValue`   | ContactorStateType | Actual contactor state.   |
| `expectedValue` | ContactorStateType | Expected contactor state. |
| `type`          | ContactorType      | Type of the contactor.    |

{{ requirement() }} The `ContactorFault` error code parameters shall be used as defined in {{ table_ref('contactor_fault_parameters') }}.

### HighTemperature

{{ table_caption('high_temp_parameters', 'Semantics and type definition for HighTemperature error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                                 |
| :------------- | :---------------------- | :---------------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual temperature.                       |
| `threshold`    | PhysicalValueType       | Warning or error threshold.               |
| `location`     | TemperatureLocationType | Location of the temperature measurements. |

{{ requirement() }} The `HighTemperature` error code parameters shall be used as defined in {{ table_ref('high_temp_parameters') }}.

### LowTemperature

{{ table_caption('low_temp_parameters', 'Semantics and type definition for LowTemperature error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                                 |
| :------------- | :---------------------- | :---------------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual temperature.                       |
| `threshold`    | PhysicalValueType       | Warning or error threshold.               |
| `location`     | TemperatureLocationType | Location of the temperature measurements. |

{{ requirement() }} The `LowTemperature` error code parameters shall be used as defined in {{ table_ref('low_temp_parameters') }}.

### PowerLoss

*This error code has no specific parameters.*

{{ requirement() }} The `PowerLoss` error code must be reported if the EVSE is unable to supply any power.

### ConnectorLockFailure

{{ table_caption('conn_lock_fail_parameters', 'Semantics and type definition for ConnectorLockFailure error code parameters') }}

| Parameter Name  | Parameter Type         | Semantics            |
| :-------------- | :--------------------- | :------------------- |
| `actualValue`   | ConnectorLockStateType | Actual lock state.   |
| `expectedValue` | ConnectorLockStateType | Expected lock state. |

{{ requirement() }} The `ConnectorLockFailure` error code parameters shall be used as defined in {{ table_ref('conn_lock_fail_parameters') }}.

### UnderVoltage

{{ table_caption('under_voltage_parameters', 'Semantics and type definition for UnderVoltage error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual voltage.                      |
| `minValue`     | PhysicalValueType       | Lower bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the voltage measurement. |

{{ requirement() }} The `UnderVoltage` error code parameters shall be used as defined in {{ table_ref('under_voltage_parameters') }}.

### OverVoltage

{{ table_caption('over_voltage_parameters', 'Semantics and type definition for OverVoltage error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual voltage.                      |
| `maxValue`     | PhysicalValueType       | Upper bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the voltage measurement. |

{{ requirement() }} The `OverVoltage` error code parameters shall be used as defined in {{ table_ref('over_voltage_parameters') }}.

### UnderCurrent

{{ table_caption('under_current_parameters', 'Semantics and type definition for UnderCurrent error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual current.                      |
| `minValue`     | PhysicalValueType       | Lower bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the current measurement. |

{{ requirement() }} The `UnderCurrent` error code parameters shall be used as defined in {{ table_ref('under_current_parameters') }}.

### OverCurrent

{{ table_caption('over_current_parameters', 'Semantics and type definition for OverCurrent error code parameters') }}

| Parameter Name | Parameter Type          | Semantics                            |
| :------------- | :---------------------- | :----------------------------------- |
| `actualValue`  | PhysicalValueType       | Actual current.                      |
| `maxValue`     | PhysicalValueType       | Upper bound of allowed range.        |
| `location`     | MeasurementLocationType | Location of the current measurement. |

{{ requirement() }} The `OverCurrent` error code parameters shall be used as defined in {{ table_ref('over_current_parameters') }}.

### EVShiftPosition

*This error code has no specific parameters.*

### EVRESSMalfunction

*This error code has no specific parameters.*
