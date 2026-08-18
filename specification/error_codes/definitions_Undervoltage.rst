..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_undervoltage:

**************
 Undervoltage
**************

Description
===========

A condition where the measured voltage at a defined electrical interface falls below the minimum threshold required for safe and effective operation, evaluated relative to the physical location within the EV–EVSE system.
Undervoltage shall be classified based on measurement location (“Site”), independent of energy direction or power type (AC or DC).

Site A - Supply Interface (EVSE Input)
Undervoltage at Site A is a voltage falling below limits at the EVSE terminals connected to the upstream power source (e.g., grid or local generation), such that the system's voltage supply is below its acceptable input range.

Site B  Vehicle Interface (EV-EVSE Connection)
Undervoltage at Site B is a voltage falling below limits at the physical connection between the EVSE and the vehicle (connector or socket outlet), as measured at the interface, such that the system's output voltage is lower than agreed between EV & EVSE.

Trigger Conditions
==================
Threshold Shortfall
   Measured voltage < allowable minimum limit (per applicable standard or manufacturer-defined value)

Measurement Location
   Site A (supply interface), or
   Site B (vehicle interface)

Time Qualification
   Falls below threshold for a defined minimum duration (to filter transients), or
   Instantaneous shortfall where explicitly required (e.g., protection limits)

Criteria
========

Reference criteria from IEC 61851-23, Appendix.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

.. code-block:: json

   {
     "basicMetadata": {
       "eventId": 10234568,
       "timestamp": "2026-08-18T14:32:10Z",
       "identifiers": {
         "evId": "EV_9F3A21",
         "evseId": "EVSE_DC_FAST_4021",
         "sessionId": "SESSION_778900"
       },
       "faultAttribution": {
         "suspectedPrimary": "EVSE",
         "evaluationBasis": "AggregatedEvidence"
       },
       "severity": "FAILED"
     },
     "coreError": {
       "error": {
         "errorCode": "UV_DC_SITEB_DIFF",
         "errorDomain": "Hardware",
         "errorCategory": "Undervoltage",
         "errorSubType": "DC+ to DC-",
         "isFatal": true
       },
       "rootCause": {
         "primary": "EVSE Power Module Regulation Failure",
         "secondary": "Voltage Control Loop Instability",
         "failureMode": "Output voltage fell below commanded setpoint"
       },
       "chargingContext": {
         "phase": "Charging",
         "subPhase": "CurrentRamp",
         "protocolLayer": "ISO15118",
         "message": "CurrentDemand"
       },
       "failureCriteria": {
         "iec61851_23": {
           "requirement": "Appendix",
           "requirementName": "DC Output Voltage Limits",
           "failureCondition": "Measured voltage fell below minimum allowable DC output voltage",
           "evaluationMethod": "Direct measurement at Site B connector"
         },
         "manufacturerSpecific": [
           {
             "manufacturer": "OEM_X",
             "requirementId": "MSP-DC-UV-001",
             "failureCondition": "Voltage < 380 V for > 100 ms"
           }
         ]
       },
       "associatedErrorEvidence": {
         "location": {
           "system": "EVSE",
           "subsystem": "PowerModule",
           "component": "DC Output Stage"
         },
         "expectedVsActual": [
           {
             "parameter": "Voltage_SiteB_DC+_to_DC-",
             "expected": ">= 400 V",
             "actual": "342 V",
             "evaluation": "Below threshold"
           },
           {
             "parameter": "Voltage_SiteB_DC+_to_PE",
             "expected": "<= 250 V",
             "actual": "248 V",
             "evaluation": "Within limit"
           },
           {
             "parameter": "Voltage_SiteA_AC_L-L",
             "expected": "480 V ±10%",
             "actual": "477 V",
             "evaluation": "Within limit"
           }
         ]
       }
     },
     "extensions": {
       "undervoltageContext": {
         "site": "SiteB",
         "measurementReference": {
           "evse": "Connector",
           "ev": "Inlet"
         },
         "powerType": "DC",
         "conductorPair": "DC+ to DC-",
         "thresholdSource": "IEC61851-23",
         "thresholdValue": "400 V",
         "measuredValue": "342 V",
         "durationMs": 120,
         "violationType": "Sustained",
         "dvdt": "-14 V/ms",
         "sampleWindow": {
           "samples": 12,
           "minVoltage": "342 V",
           "avgVoltage": "372 V"
         },
         "connectionState": "Plugged"
       },
       "operationalContext": {
         "shutdownType": "Emergency",
         "triggerCondition": "Voltage fell below threshold for >100 ms during active charging",
         "chargeStateAtFailure": "Active Charging"
       },
       "iso15118": {
         "lastMessage": "CurrentDemand",
         "sessionState": "EnergyTransfer"
       },
       "dtc": {
         "vehicleDTC": "P0C1B",
         "evseDTC": "EVSE_UV_004"
       },
       "errorCodeTuple": {
         "site": "B",
         "system": "EVSE",
         "type": "DC",
         "failureMode": "Undervoltage_Differential"
       }
     }
   }

