from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import base64

from app.ai.vision import analyze_image

router = APIRouter()

@router.websocket("/ws/vision")
async def vision_stream(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()

            # Expect base64 image frame
            try:
                image_bytes = base64.b64decode(data)
            except Exception:
                await websocket.send_json({
                    "error": "Invalid image format"
                })
                continue

            result = await analyze_image(image_bytes)

            await websocket.send_json({
                "description": result.description,
                "objects": result.objects,
                "danger_level": result.danger_level,
            })

    except WebSocketDisconnect:
        print("Vision stream disconnected")