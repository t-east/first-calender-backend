from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from sqlalchemy.sql.functions import current_timestamp

from app.drivers.rdb.base import Base


class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    #     user_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    title = Column(String(30), unique=False, index=True, nullable=False)

    description_text = Column(Text(), nullable=True)

    from_date = Column(DateTime, nullable=False, index=True)
    is_all_day = Column(Boolean, nullable=True)
    to_date = Column(DateTime, nullable=False)

    created_at = Column(DateTime, nullable=False, server_default=current_timestamp())
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
