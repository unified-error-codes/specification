..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_power_module_identifier:

************************
 Power Module Identifier
************************

-  **Description**: The identifier of the power module or converter channel that raised
   the fault. Distinguishes the affected module when multiple modules are
   present in the EVSE or EV.

.. _telemetry_power_module_location:

**********************
 Power Module Location
**********************

-  **Description**: The physical location of the power module or converter channel within
   the EVSE or EV. Used together with the identifier to locate the affected
   module for diagnostics and service.

.. _telemetry_power_module_specific_error_code:

*********************************
 Power Module Specific Error Code
*********************************

-  **Description**: The error code reported by the power module itself, forwarded up
   through the specification to convey the root cause. On the EVSE this is the
   vendor-specific error code; on the EV this is typically the inverter error
   code or Diagnostic Trouble Code (DTC) that was set. Decoding may require the
   module vendor, model, and
   firmware version.

.. _telemetry_power_module_vendor:

********************
 Power Module Vendor
********************

-  **Description**: The vendor of the power module or converter channel. Aids decoding of
   the vendor-specific error code.

.. _telemetry_power_module_model:

*******************
 Power Module Model
*******************

-  **Description**: The model of the power module or converter channel.

.. _telemetry_power_module_firmware_version:

******************************
 Power Module Firmware Version
******************************

-  **Description**: The firmware version of the power module or converter channel. Aids
   decoding of the vendor-specific error code and correlating known
   firmware-related faults.
