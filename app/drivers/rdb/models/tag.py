from sqlalchemy import Column
from app.domains.entities import tag
from app.drivers.rdb.base import Base
from sqlalchemy import Column, Integer, String

class Tag(Base):
    __tablename__ = "tags"
    tag_id = Column(Integer, primary_key=True, index=True)
    label = Column(String(32), unique=False, index=True, nullable=False)
    user_id = Column(Integer, primary_key=True, index=True)