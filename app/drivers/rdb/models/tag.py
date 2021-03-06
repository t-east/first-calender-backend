from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.drivers.rdb.base import Base


class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_id = Column(
        Integer, ForeignKey("events.event_id", ondelete="SET NULL"), nullable=True
    )
    #     user_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"))
    label = Column(String(30), unique=False, index=True, nullable=False)
    color = Column(String(30), nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    event = relationship("Event", back_populates="tags")
