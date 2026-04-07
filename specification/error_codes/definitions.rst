..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

#############
 Error Codes
#############

This section defines the error codes.

.. _error_powerloss:

***********
 PowerLoss
***********

Description
===========

This error is raised when the charging station experiences a partial or
complete loss of its main power supply.

Trigger Conditions
==================

-  The main power supply voltage drops below a threshold that prevents the charging station from operating.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_communication_state`
-  :ref:`telemetry_supply_voltage_l1`
-  :ref:`telemetry_supply_voltage_l2`
-  :ref:`telemetry_supply_voltage_l3`

.. _error_connectorlockfailure:

**********************
 ConnectorLockFailure
**********************

Description
===========

This error is raised when the connector lock mechanism fails to reach
the expected locked or unlocked position.

Trigger Conditions
==================

-  The lock position feedback does not reach the locked threshold within the
   expected time after a lock command is issued.
-  The lock position feedback does not reach the unlocked threshold within the
   expected time after an unlock command is issued.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_connector_lock_position`
-  :ref:`telemetry_connector_lock_command`

.. _error_insulationfault:

*****************
 InsulationFault
*****************

Description
===========

This error is raised when the insulation resistance between any
high-voltage line (DC+, DC-) and protective earth (PE) or chassis drops
below a safety threshold defined by IEC 61851-23.

Before energy transfer begins, both the EV and the EVSE perform an
insulation resistance check. This includes a functional test of the
EVSE's Insulation Monitoring Device (IMD). Charging is inhibited if the
measured resistance does not meet the required threshold.

During DC charging, the EVSE continuously monitors insulation resistance.
If the resistance degrades below the fault threshold, or if the IMD
itself fails, charging is immediately terminated.

Two severity levels are defined:

-  **Warning** — The measured insulation resistance falls below the
   warning threshold specified in IEC 61851-23, but charging is still
   permitted.
-  **Fault** — The measured insulation resistance drops below the fault
   threshold defined in IEC 61851-23. Charging is no longer permitted
   and shall be terminated immediately.

Trigger Conditions
==================

-  The insulation resistance measured by the IMD drops below the warning
   threshold specified in IEC 61851-23 (warning level).
-  The insulation resistance measured by the IMD drops below the fault
   threshold specified in IEC 61851-23 (fault level).
-  The IMD functional self-test fails before or during charging.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_insulation_resistance`
-  :ref:`telemetry_imd_status`
-  :ref:`telemetry_communication_state`
