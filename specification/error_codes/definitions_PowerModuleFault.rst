..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _error_powermodulefault:

******************
 PowerModuleFault
******************

Description
===========

A power conversion fault occurs when any power module or converter channel
within the EVSE or EV — such as AC/DC, DC/DC, or DC/AC — fails to deliver the
commanded power. In the EVSE, this usually involves faults in the power modules
that rectify or invert energy for delivery to the vehicle, while in the EV it
includes failures in on-board converters that manage energyflow to or from the
battery.

This error code is applicable to and can be set by either the EV or EVSE,
depending on which side owns the affected power module or converter.

Trigger Conditions
==================

-  A power module or converter reports a fault, whose module-specific error code
   is passed through as the root cause.
-  Internal diagnostics of the power module or converter report a protection
   trip (for example, overvoltage protection) as described by IEC 61851-23,
   sections AA.3.12 and BB.5.6.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_power_module_identifier`
-  :ref:`telemetry_power_module_location`
-  :ref:`telemetry_power_module_specific_error_code`
-  :ref:`telemetry_power_module_vendor`
-  :ref:`telemetry_power_module_model`
-  :ref:`telemetry_power_module_firmware_version`
