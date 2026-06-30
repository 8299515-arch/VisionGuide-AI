from sqlalchemy import Column, String, DateTime, Float, Integer, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
import uuid

from app.db.session import Base


class AIRequest(Base):
    __tablename__ = "ai_requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    # Type of AI request (vision, ocr, navigation, assistant)
    request_type = Column(String, nullable=False)

    # Input payload
    input_data = Column(JSONB, nullable=True)

    # AI response payload
    response_data = Column(JSONB, nullable=True)

    # Human-readable summary
    summary = Column(Text, nullable=True)

    # Performance metrics
    processing_time_ms = Column(Integer, nullable=True)
    cost_usd = Column(Float, nullable=True)

    # Status
    status = Column(String, default="success")  # success | error | pending

    error_message = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
