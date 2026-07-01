from fastapi import FastAPI, WebSocket, HTTPException
from pydantic import BaseModel
from typing import List
from jose import jwt, JWTError

from ai.vision.pipeline import process_image
from backend.app.ws import websocket_endpoint
from backend.app.metrics import metrics
from backend.app.auth import authenticate_user, create_access_token, SECRET_KEY, ALGORITHM

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

class LoginRequest(BaseModel):
    username: str
    password: str

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

@app.post("/login")
def login(req: LoginRequest):
    user = authenticate_user(req.username, req.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/metrics")
def get_metrics():
    return {
        "request_count": metrics.request_count,
        "error_count": metrics.error_count,
        "avg_latency": metrics.avg_latency(),
        "endpoint_hits": dict(metrics.endpoint_hits)
    }

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
# WebSocket (Sprint 5 secured)
# --------------------

@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")

    if not token:
        await websocket.close(code=1008)
        return

    try:
        jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        await websocket.close(code=1008)
        return

    await websocket_endpoint(websocket)
