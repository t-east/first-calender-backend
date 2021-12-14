from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey

from app.drivers.base import Base


class Event(Base):
    __tablename__ = "events"

    user_id = Column(
        Integer, ForeignKey("users.user_id", ondelete="SET NULL"), nullable=False
    )
    event_id = Column(Integer, primary_key=True, index=True, nullable=False)
    event_name = Column(String(128), unique=False, index=True, nullable=False)

    description = Column(Text(1000), nullable=True)

    begin_date = Column(DateTime, nullable=False, index=True)
    is_all_day = Column(Boolean, nullable=True)
    end_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    color = Column(String(32), nullable=False, index=True)
