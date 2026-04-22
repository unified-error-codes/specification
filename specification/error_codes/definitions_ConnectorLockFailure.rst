..
   SPDX-License-Identifier: CC-BY-4.0
   Copyright CharIN e.V. and Contributors

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
-  The lock position spuriously changes state without a corresponding command.

Related Telemetry
=================

The following telemetry signals are required for analyzing this error:

-  :ref:`telemetry_connector_lock_position`
-  :ref:`telemetry_connector_lock_command`
