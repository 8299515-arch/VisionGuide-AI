"""
VisionGuide AI - WebSocket Streaming (Sprint 3)
Real-time frame ingestion endpoint for live camera assistant
"""

from fastapi import WebSocket, WebSocketDisconnect
from ai.vision.pipeline import process_image


class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send(self, websocket: WebSocket, message: dict):
        await websocket.send_json(message)


manager = ConnectionManager()


async def process_frame(frame: str, voice: bool = False):
    """Process a single frame through AI pipeline"""
    return process_image(frame, voice=voice)


async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data = await websocket.receive_json()

            frame = data.get("frame")
            voice = data.get("voice", False)

            result = await process_frame(frame, voice)

            await manager.send(websocket, result)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
