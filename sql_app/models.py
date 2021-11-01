from sqlalchemy import (Column, ForeignKey, Integer,
                        String, DateTime, Date, Boolean, Text)
from .database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    password_hash = Column(String, nullable=False)
    email = Column(String, nullable=True, index=True)
    profile_image_path = Column(String, nullable=True)
    birthday = Column(Date, nullable=True, index=True)
    resistered_at = Column(DateTime, nullable=False)
    last_login_at = Column(DateTime, nullable=True)


class Event(Base):
    __tablename__ = 'events'
    user_id = Column(Integer,
                     ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    event_id = Column(Integer, primary_key=True, index=True, nullable=False)
    event_name = Column(String, unique=False, index=True, nullable=False)
    description = Column(Text, nullable=True)
    begin_date = Column(DateTime, nullable=False, index=True)
    is_all_day = Column(Boolean, nullable=True)
    end_date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime, nullable=False)
    color = Column(String, nullable=False, index=True)
    