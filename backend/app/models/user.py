from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)

    hashed_password = Column(String, nullable=False)

    role_id = Column(String, nullable=True)

    language = Column(String, default="en")
    timezone = Column(String, default="UTC")

    preferred_voice = Column(String, nullable=True)
    speech_rate = Column(Float, default=1.0)
    tts_engine = Column(String, default="openai")

    navigation_mode = Column(String, default="safe")
    emergency_mode = Column(Boolean, default=True)

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)

    premium_until = Column(DateTime, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    last_login = Column(DateTime(timezone=True), nullable=True)
