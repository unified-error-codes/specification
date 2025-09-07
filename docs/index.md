# Unified Error Codes (UEC) Specification

## Abstract
This document specifies the data model, semantics, and behavioral requirements for Unified Error Codes (UEC) used in the e-mobility ecosystem. It provides a common language for reporting diagnostic events and conditions between ecosystem components, primarily the Electric Vehicle Supply Equipment (EVSE) and the Charge Point Management System (CPMS).

## Scope

The scope of this specification is the definition of a unified set of error codes, their associated data models, and the required behavior of systems that implement them. This includes the conditions that trigger an error event and the conditions under which an error state is cleared.

## Normative References

The following referenced documents are indispensable for the application of this document.

* **[DIN99003]** DIN DKE SPEC 99003: A comprehensive list of error codes for the EV charging ecosystem.

## Terms, Definitions, and Abbreviations

### Definitions

### Abbreviations

* **CPMS:** Charge Point Management System
* **EV:** Electric Vehicle
* **EVSE:** Electric Vehicle Supply Equipment
* **UEC:** Unified Error Code

### Conformance Language
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [RFC2119].

## Architectural Principles

The UEC specification is built upon the following core principles:

* **Transport Agnostic:** The UEC data model is independent of any specific communication protocol like OCPP.
* **Extensibility:** The specification is designed to be extended with new codes and parameters in a structured and backward-compatible manner.
* **Machine-Readability:** The specification prioritizes structured data over free text to enable reliable, automated processing.
