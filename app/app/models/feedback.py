import enum
import datetime

from app.db.base import Base

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    login = Column(String(50), nullable=False,)
    email = Column(String(100))
    phone_number = Column(String(50))
    text = Column(
        String(2000),
        nullable=True
    )
