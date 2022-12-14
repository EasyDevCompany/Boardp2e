import enum
import datetime

from uuid import uuid4

from sqlalchemy import Column, Integer, Enum, ForeignKey, DateTime, String, BigInteger, Float, LargeBinary
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base
from app.utils.bytes_field import HexByteString


class User(Base):
    __tablename__ = 'user'

    class UserStatus(str, enum.Enum):
        user = {"ru": "пользователь", "eng": "user"}
        moderator = {"ru": "модератор", "eng": "moderator"}
        admin = {"ru": "админ", "eng": "admin"}

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid4
    )
    token = Column(String)
    login = Column(
        String(15),
        nullable=False,
        unique=True
    )
    status = Column(Enum(UserStatus), default=UserStatus.user)
    email = Column(String)
    balance = Column(BigInteger, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    # TODO Сделать хэш паролей
    password = Column(String)
    secret_key = Column(String)
    raiting = Column(Float(precision=1), default=0)
    review_amount = Column(Integer, default=0)

