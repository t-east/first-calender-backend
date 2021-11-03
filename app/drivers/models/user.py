from sqlalchemy import Column, Integer, String, DateTime, Date

from app.drivers.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(128), nullable=False)

    password_hash = Column(String(1024), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)

    profile_image_path = Column(String, nullable=True)

    birthday = Column(Date, nullable=True, index=True)

    resistered_at = Column(DateTime, nullable=False)
    last_login_at = Column(DateTime, nullable=True)
