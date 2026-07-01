from fastapi import FastAPI, WebSocket
from pydantic import BaseModel
from typing import List

from ai.vision.pipeline import process_image
from backend.app.ws import websocket_endpoint

app = FastAPI(
    title="VisionGuide AI API",
    description="Core API for VisionGuide AI - accessibility assistant for visually impaired users",
    version="0.1.0"
)

# --------------------
# Models
# --------------------

class ImageRequest(BaseModel):
    image: str

class AnalysisResponse(BaseModel):
    objects: List[str] = []
    text: str = ""
    description: str = ""
    navigation_hint: str = ""

# --------------------
# Routes
# --------------------

@app.get("/")
def root():
    return {
        "service": "VisionGuide AI Backend",
        "status": "running",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze-image", response_model=AnalysisResponse)
def analyze_image(req: ImageRequest):
    result = process_image(req.image)

    return AnalysisResponse(
        objects=result.get("objects", []),
        text=result.get("text", ""),
        description=result.get("description", ""),
        navigation_hint=""
    )

# --------------------
# WebSocket (Sprint 3)
# --------------------

@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await websocket_endpoint(websocket)
