from sqlalchemy import Column, Integer, String, DateTime

from app.drivers.rdb.base import Base, ENGINE

Base.metadata.create_all(bind=ENGINE, checkfirst=False)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_name = Column(String(128), nullable=False)

    password_hash = Column(String(1024), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)

    registered_at = Column(DateTime, nullable=False)
    last_login_at = Column(DateTime, nullable=True)

    updated_at = Column(DateTime, nullable=True)
