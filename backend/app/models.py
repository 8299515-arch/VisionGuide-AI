"""
VisionGuide AI - Sprint 9 Models
Basic DB models (SQLAlchemy-style placeholder)
"""

from datetime import datetime
from dataclasses import dataclass, field

# ----------------------------
# User Model
# ----------------------------

@dataclass
class User:
    id: int
    username: str
    hashed_password: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_admin: bool = False

# ----------------------------
# Analysis Log Model
# ----------------------------

@dataclass
class AnalysisLog:
    id: int
    user_id: int
    image_hash: str
    description: str
    created_at: datetime = field(default_factory=datetime.utcnow)

# ----------------------------
# Payment Model (Stripe-ready stub)
# ----------------------------

@dataclass
class Payment:
    id: int
    user_id: int
    amount: float
    currency: str = "USD"
    status: str = "pending"
    stripe_session_id: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
