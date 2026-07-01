"""
VisionGuide AI - Sprint 9 Admin API
Basic admin dashboard endpoints (MVP)
"""

from fastapi import APIRouter, HTTPException, Depends
from typing import List

from backend.app.auth import verify_token
from backend.app.models import User, AnalysisLog, Payment

router = APIRouter(prefix="/admin", tags=["admin"])

# ------------------------
# Fake in-memory data (MVP)
# ------------------------

fake_users = [
    User(id=1, username="admin", hashed_password="***", is_admin=True),
    User(id=2, username="user1", hashed_password="***"),
]

fake_logs = [
    AnalysisLog(id=1, user_id=2, image_hash="abc123", description="Person detected"),
]

fake_payments = [
    Payment(id=1, user_id=2, amount=9.99, status="completed"),
]

# ------------------------
# Admin guard
# ------------------------

def admin_guard(payload=Depends(verify_token)):
    if payload.get("sub") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return payload

# ------------------------
# Endpoints
# ------------------------

@router.get("/users", dependencies=[Depends(admin_guard)])
def get_users():
    return fake_users

@router.get("/logs", dependencies=[Depends(admin_guard)])
def get_logs():
    return fake_logs

@router.get("/payments", dependencies=[Depends(admin_guard)])
def get_payments():
    return fake_payments
