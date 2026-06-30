from sqlalchemy import Column, String, Float, Boolean, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.session import Base


class AccessibilitySettings(Base):
    __tablename__ = "accessibility_settings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)

    # Voice settings
    tts_engine = Column(String, default="openai")
    voice = Column(String, nullable=True)
    language = Column(String, default="en")
    speech_rate = Column(Float, default=1.0)
    volume = Column(Float, default=1.0)

    # Vision AI settings
    object_distance_sensitivity = Column(Integer, default=2)
    description_level = Column(String, default="normal")  # minimal | normal | detailed

    # Navigation settings
    safe_route_only = Column(Boolean, default=True)
    avoid_stairs = Column(Boolean, default=False)
    avoid_crowds = Column(Boolean, default=False)
    avoid_construction = Column(Boolean, default=True)

    # Vibration settings
    vibration_enabled = Column(Boolean, default=True)

    # Camera settings
    camera_fps_mode = Column(String, default="balanced")  # low | balanced | high
    continuous_analysis = Column(Boolean, default=True)

    # AI mode
    ai_mode = Column(String, default="hybrid")  # cloud | local | hybrid

    # Offline mode
    offline_mode = Column(Boolean, default=False)
