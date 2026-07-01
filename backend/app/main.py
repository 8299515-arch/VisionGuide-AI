from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="VisionGuide AI API",
    description="Core API for VisionGuide AI - accessibility assistant for visually impaired users",
    version="0.1.0"
)

# --------------------
# Models
# --------------------

class ImageRequest(BaseModel):
    image: str  # base64 or URL in future

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
    return AnalysisResponse(
        objects=[],
        text="",
        description="VisionGuide AI mock response (Sprint 1)",
        navigation_hint=""
    )
