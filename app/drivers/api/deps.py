from typing import Generator
import app.usecases as usecases
import app.interfaces as interfaces
from fastapi import Depends
from app.drivers.rdb.base import SessionLocal
from sqlalchemy.orm import Session

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_usecase(db: Session = Depends(get_db)) -> usecases.UserUsecase:
    repo: usecases.IUserRepository = interfaces.SQLUserRepository(db)
    return usecases.UserUsecase(repo)

def get_event_usecase(db: Session = Depends(get_db)) -> usecases.EventUsecase:
    repo: usecases.IEventRepository = interfaces.SQLEventRepository(db)
    return usecases.EventUsecase(repo)