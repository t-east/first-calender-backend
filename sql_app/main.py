from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Dict, List

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DB_CREATE
@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.User,
                      db: Session = Depends(get_db)) -> schemas.User:
    return crud.create_user(db=db, user=user)


@app.post("/events", response_model=schemas.Event)
async def create_event(event: schemas.Event,
                       db: Session = Depends(get_db)) -> schemas.Event:
    return crud.create_event(db=db, event=event)


# DB_READ
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100,
                     db: Session = Depends(get_db)) -> List[schemas.User]:
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/events", response_model=List[schemas.Event])
async def read_events(skip: int = 0, limit: int = 100,
                      db: Session = Depends(get_db)) -> List[schemas.Event]:
    events = crud.get_events(db, skip=skip, limit=limit)
    return events


@app.get("/")
def hello() -> Dict[str, str]:
    return {"message": "hello world!"}
