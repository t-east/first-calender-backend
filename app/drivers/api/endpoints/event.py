from fastapi import APIRouter, Depends, HTTPException
from typing import Optional

import app.domains.entities as entities
import app.usecases as usecases
import app.interfaces as interfaces
from app.drivers.rdb.base import Session

router = APIRouter()


def get_db() -> Session:
    db = Session()
    try:
        yield db
    finally:
        db.close()


def get_event_usecase(db: Session = Depends(get_db)) -> usecases.EventUsecase:
    repo: usecases.IEventRepository = interfaces.SQLEventRepository(db)
    return usecases.EventUsecase(repo)


@router.post("/", response_model=entities.Event)
async def create_event(
    *,
    event_in: entities.EventCreate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.Event:
    return eu.create(obj_in=event_in)


@router.put("/", response_model=entities.Event)
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


@router.get("/{event_id}", response_model=entities.Event)
async def get_event(
    *,
    event_id: int,
    user_id: int,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    selected_event: Optional[entities.Event] = eu.read(id=event_id, user_id=user_id)
    if selected_event is None:
        raise HTTPException(status_code=404)
    return selected_event


@router.get("/", response_model=entities.ListEventsResponse)
async def get_events(
    *,
    user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    return eu.get_list(user_id=user_id)


@router.delete("/", response_model=entities.Event)
async def delete_event(
    *, id: int, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    deleted_event: Optional[entities.Event] = eu.delete(id=id, user_id=user_id)
    if deleted_event is None:
        raise HTTPException(status_code=404)
    return deleted_event


@router.get("/{event_id}/tag/{tag_id}", response_model=entities.ListEventsResponse)
async def get_event_tags(
    *,
    user_id: int,
    event_id: int,
    tag_id: int,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    return eu.get_event_tag(user_id=user_id)


@router.post("/{event_id}/tag", response_model=entities.ListEventsResponse)
async def get_events(
    *, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    return eu.get_list(user_id=user_id)