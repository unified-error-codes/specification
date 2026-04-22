..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

.. _telemetry_connector_lock_position:

************************
 Connector Lock Position
************************

-  **Description**: The current position of the connector lock mechanism. The state is
   determined by evaluating the lock actuator's feedback signal against defined
   thresholds.
-  **Values**: locked, unlocked, unknown
-  **Unit**: N/A
-  **Resolution**: N/A

.. _telemetry_connector_lock_command:

***********************
 Connector Lock Command
***********************

-  **Description**: Used to correlate the commanded state with the reported position
   feedback for failure analysis.
-  **Values**: lock, unlock, none
-  **Unit**: N/A
-  **Resolution**: N/A
