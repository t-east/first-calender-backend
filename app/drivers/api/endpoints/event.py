from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Dict, List, Optional

import app.domains.entities as entities
import app.usecases as usecases
import app.interfaces as interfaces

from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_event_usecase(db: Session = Depends(get_db)) -> usecases.EventUsecase:
    repo: usecases.IEventRepository = interfaces.SQLEventRepository(db)
    return usecases.EventUsecase(repo)


@app.post("/", response_model=entities.Event)
async def create_event(
    *,
    event_in: entities.EventCreate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.Event:
    return eu.create(obj_in=event_in)


@app.put("/", response_model=entities.Event)
async def update_event(
    *,
    id: int,
    user_id: int,
    event_in: entities.EventUpdate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    updated_event: Optional[entities.Event] = eu.update(
        id=id, user_id=user_id, obj_in=event_in
    )
    if updated_event is None:
        raise HTTPException(status_code=404)
    return updated_event


@app.get("/{event_id}", response_model=entities.Event)
async def get_event(
    *,
    event_id: int,
    user_id: int,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    selected_event: Optional[entities.Event] = eu.get(id=event_id, user_id=user_id)
    if selected_event is None:
        raise HTTPException(status_code=404)
    return selected_event


@app.get("/", response_model=entities.ListEventsResponse)
async def get_events(
    *, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    return eu.get_list(user_id=user_id)


@app.delete("/", response_model=entities.Event)
async def delete_event(
    *, id: int, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    deleted_event: Optional[entities.Event] = eu.delete(id=id, user_id=user_id)
    if deleted_event is None:
        raise HTTPException(status_code=404)
    return deleted_event
