"""
VisionGuide AI - v7 FINAL PRODUCT ENTRYPOINT
Unified SaaS + AI orchestration layer
"""

from fastapi import FastAPI, Request

from backend.app.api_gateway import gateway
from backend.app.services.v5_super_ai import super_ai
from backend.app.services.v4_multimodal_brain import brain_v4
from backend.app.services.vision_reasoning import engine as brain_v2

from backend.app.payments import router as payments_router
from backend.app.admin import router as admin_router

app = FastAPI(
    title="VisionGuide AI",
    version="7.0.0"
)

# ----------------------------
# Routers
# ----------------------------

app.include_router(payments_router)
app.include_router(admin_router)

# ----------------------------
# Health
# ----------------------------

@app.get("/")
def root():
    return {"status": "VisionGuide AI v7 running 🚀"}

# ----------------------------
# Core AI Gateway Endpoint
# ----------------------------

@app.post("/ai")
async def ai_endpoint(request: Request):
    payload = await request.json()

    gw = await gateway.handle_request(request, payload)
    route = gw["route"]

    if route == "vision_pipeline":
        return brain_v2.reason(payload.get("vision", {}))

    if route == "voice_pipeline":
        return brain_v4.run(
            payload.get("vision", {}),
            audio=payload.get("audio"),
            prompt=payload.get("prompt", "")
        )

    if route == "stripe_pipeline":
        return {"hint": "Use /payments/create-checkout-session"}

    return super_ai.process(
        user_input=payload.get("text", ""),
        vision=payload.get("vision")
    )
