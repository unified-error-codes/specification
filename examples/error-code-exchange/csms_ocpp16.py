"""A minimal mock CSMS backend speaking OCPP 1.6."""

from __future__ import annotations

import logging

import websockets
from ocpp.routing import on
from ocpp.v16 import ChargePoint as ChargePointV16
from ocpp.v16 import call_result

logger = logging.getLogger("csms-ocpp1.6")


class MockCentralSystemV16(ChargePointV16):
    @on("StatusNotification")
    def on_status_notification(self, **kwargs):
        logger.info("received StatusNotification: %s", kwargs)
        print(f"CSMS (OCPP 1.6) received StatusNotification: {kwargs}")
        return call_result.StatusNotification()


async def _handler(websocket) -> None:
    if websocket.subprotocol != "ocpp1.6":
        await websocket.close()
        return
    charge_point_id = websocket.request.path.strip("/").rsplit("/", 1)[-1]
    cp = MockCentralSystemV16(charge_point_id, websocket)
    try:
        await cp.start()
    except websockets.ConnectionClosed:
        pass  # the EVSE disconnects once its single request is answered


def serve(host: str = "localhost", port: int = 9016):
    """Return the `websockets.serve` awaitable for the OCPP 1.6 mock CSMS."""
    return websockets.serve(_handler, host, port, subprotocols=["ocpp1.6"])
