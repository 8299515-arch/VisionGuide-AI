from fastapi import FastAPI

app = FastAPI(
    title="VisionGuide AI API",
    description="Core API for VisionGuide AI - accessibility assistant for visually impaired users",
    version="0.1.0"
)

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
