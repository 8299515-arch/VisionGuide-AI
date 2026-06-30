from sqlalchemy import Column, String

from app.db.session import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    description = Column(String, nullable=True)
