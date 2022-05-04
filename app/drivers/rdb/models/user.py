from sqlalchemy import TEXT, Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import EmailType
from app.drivers.rdb.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(30), nullable=False)

    password_hash = Column(TEXT(), nullable=False)
    email = Column(EmailType, unique=True, index=True, nullable=False)

    registered_at = Column(DateTime, nullable=False)
    last_login_at = Column(DateTime, nullable=True)

    updated_at = Column(DateTime, nullable=True)
    disabled =     disabled = Column(Boolean, nullable=False)