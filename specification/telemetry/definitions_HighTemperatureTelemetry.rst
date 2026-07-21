..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_hightemperature_actual:

***********************
 Actual Temperature
***********************

-  **Description**: The measured temperature of the EVSE or EV component
   reported as the source of the overtemperature condition.
-  **Unit**: Degrees Celsius (°C)
-  **Resolution**: `1 °C`

.. _telemetry_hightemperature_threshold:

*******************************
 Calibration Threshold
*******************************

-  **Description**: The calibrated safety or performance temperature threshold
   for the reporting component, above which the overtemperature fault is
   raised, as defined by the applicable standard or the manufacturer.
-  **Unit**: Degrees Celsius (°C)
-  **Resolution**: `1 °C`

.. _telemetry_hightemperature_location:

**********************
 Temperature Location
**********************

-  **Description**: The subsystem or device component against which the
   temperature is reported.
-  **Values**:

   -  ``Cable`` — Charging cable.
   -  ``CablePositive`` — Charging cable positive line.
   -  ``CableNegative`` — Charging cable negative line.
   -  ``CableHousingPositive`` — Cable housing positive line.
   -  ``CableHousingNegative`` — Cable housing negative line.
   -  ``ConnectorPositive`` — Connector/Plug positive pin.
   -  ``ConnectorNegative`` — Connector/Plug negative pin.
   -  ``PowerModulesSideA`` — Power modules Side A.
   -  ``PowerModulesSideB`` — Power modules Side B.
   -  ``Electronics`` — Electronic/control components.
   -  ``Socket`` — Charging socket.
   -  ``SocketPositive`` — Charging socket positive pin.
   -  ``SocketNegative`` — Charging socket negative pin.
   -  ``Battery`` — EV Battery.
   -  ``Body`` — EVSE/EV body.
