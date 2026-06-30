from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.session import Base


class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    name = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)

    priority = Column(Integer, default=1)  # 1 = highest

    preferred_channel = Column(String, default="phone")  # phone | sms | telegram | whatsapp

    is_active = Column(Boolean, default=True)
