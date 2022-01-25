from sqlalchemy import Column, Integer, String
from .base import Base


class TestUserTable(Base):
    __tablename__ = "test_user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(128), nullable=False)
