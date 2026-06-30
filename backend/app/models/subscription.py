from sqlalchemy import Column, String, DateTime, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.db.session import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True)

    plan = Column(String, default="free")  # free | premium | family | business | enterprise

    is_active = Column(Boolean, default=True)

    started_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)

    auto_renew = Column(Boolean, default=False)

    payment_provider = Column(String, nullable=True)

    payment_status = Column(String, default="inactive")