from __future__ import annotations

import asyncio
import json
import socket
from typing import Dict, Any, Callable, Awaitable, Optional, List

try:
    import websockets
    from websockets.server import WebSocketServerProtocol
except ImportError:  # pragma: no cover
    websockets = None
    WebSocketServerProtocol = Any  # type: ignore

from .models import Encounter, Condition, to_dict

DISCOVERY_PORT = 9999
DISCOVERY_MESSAGE = b"AC_DISCOVER"
WEBSOCKET_PORT = 8765


async def discover_servers(timeout: float = 1.0) -> List[Dict[str, Any]]:
    """Broadcast a discovery message and collect server responses."""
    loop = asyncio.get_running_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setblocking(False)
    # Bind to an ephemeral port to receive responses
    sock.bind(("", 0))
    sock.sendto(DISCOVERY_MESSAGE, ("255.255.255.255", DISCOVERY_PORT))

    servers: List[Dict[str, Any]] = []
    start = loop.time()
    while True:
        remaining = timeout - (loop.time() - start)
        if remaining <= 0:
            break
        try:
            data, addr = await asyncio.wait_for(loop.sock_recvfrom(sock, 1024), remaining)
        except asyncio.TimeoutError:
            break
        try:
            info = json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            continue
        info["address"] = addr[0]
        servers.append(info)
    sock.close()
    return servers


class DiscoveryService:
    """Responds to UDP discovery probes from clients."""

    def __init__(self, name: str, port: int = WEBSOCKET_PORT):
        self.name = name
        self.port = port
        self.sock: Optional[socket.socket] = None
        self.task: Optional[asyncio.Task] = None

    async def start(self) -> None:
        loop = asyncio.get_running_loop()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(("", DISCOVERY_PORT))
        self.sock.setblocking(False)
        self.task = asyncio.create_task(self._listen(loop))

    async def _listen(self, loop: asyncio.AbstractEventLoop) -> None:
        assert self.sock is not None
        while True:
            data, addr = await loop.sock_recvfrom(self.sock, 1024)
            if data == DISCOVERY_MESSAGE:
                payload = json.dumps({"name": self.name, "port": self.port}).encode("utf-8")
                self.sock.sendto(payload, addr)

    async def stop(self) -> None:
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
        if self.sock:
            self.sock.close()


class ConnectionManager:
    """Tracks active WebSocket connections."""

    def __init__(self) -> None:
        self.connections: Dict[str, WebSocketServerProtocol] = {}

    async def register(self, player_id: str, websocket: WebSocketServerProtocol) -> None:
        self.connections[player_id] = websocket

    async def unregister(self, player_id: str) -> None:
        ws = self.connections.pop(player_id, None)
        if ws and ws.open:
            await ws.close()

    async def send(self, player_id: str, message: Dict[str, Any]) -> None:
        ws = self.connections.get(player_id)
        if ws and ws.open:
            await ws.send(json.dumps(message))

    async def broadcast(self, message: Dict[str, Any]) -> None:
        data = json.dumps(message)
        await asyncio.gather(
            *(ws.send(data) for ws in self.connections.values() if ws.open),
            return_exceptions=True,
        )

    def get(self, player_id: str) -> Optional[WebSocketServerProtocol]:
        return self.connections.get(player_id)


class MessageDispatcher:
    """Dispatches incoming WebSocket messages to registered handlers."""

    def __init__(self) -> None:
        self.handlers: Dict[str, Callable[[Dict[str, Any], WebSocketServerProtocol], Awaitable[None]]] = {}

    def add_handler(
        self, msg_type: str,
        handler: Callable[[Dict[str, Any], WebSocketServerProtocol], Awaitable[None]],
    ) -> None:
        self.handlers[msg_type] = handler

    async def dispatch(self, message: str, websocket: WebSocketServerProtocol) -> None:
        data = json.loads(message)
        msg_type = data.get("type")
        handler = self.handlers.get(msg_type)
        if handler:
            await handler(data, websocket)


class StateSynchronizer:
    """Sends state updates to clients and handles reconnections."""

    def __init__(self, manager: ConnectionManager) -> None:
        self.manager = manager

    async def send_update(
        self,
        player_id: str,
        entity_id: str,
        hp: int,
        conditions: List[Condition],
    ) -> None:
        payload = {
            "type": "update_state",
            "entity_id": entity_id,
            "hp": hp,
            "conditions": [to_dict(c) for c in conditions],
        }
        await self.manager.send(player_id, payload)

    async def broadcast_encounter(self, encounter: Encounter) -> None:
        payload = {
            "type": "encounter_state",
            "encounter": to_dict(encounter),
        }
        await self.manager.broadcast(payload)

    async def handle_reconnection(
        self, player_id: str, websocket: WebSocketServerProtocol, encounter: Encounter
    ) -> None:
        await self.manager.register(player_id, websocket)
        await self.manager.send(
            player_id,
            {"type": "encounter_state", "encounter": to_dict(encounter)},
        )


async def run_websocket_server(
    manager: ConnectionManager,
    dispatcher: MessageDispatcher,
    host: str = "0.0.0.0",
    port: int = WEBSOCKET_PORT,
) -> websockets.server.Serve:
    """Start a WebSocket server that dispatches messages using the dispatcher."""
    if websockets is None:  # pragma: no cover
        raise RuntimeError("websockets package is required to run the server")

    async def handler(websocket: WebSocketServerProtocol, path: str) -> None:
        async for message in websocket:
            await dispatcher.dispatch(message, websocket)

    return await websockets.serve(handler, host, port)
