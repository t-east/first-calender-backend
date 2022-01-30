from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
import app.domains.entities as entities
import app.usecases as usecases
from app.drivers.api.deps import get_event_usecase

router = APIRouter()


@router.post("/", response_model=entities.Event)
async def create_event(
    *,
    event_in: entities.EventCreate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.Event:
    return eu.create(obj_in=event_in)


@router.put("/{user_id}", response_model=entities.Event)
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


@router.get("/{user_id}", response_model=entities.ListEventsResponse)
async def get_event(
    *, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    selected_event: entities.ListEventsResponse = eu.get_list_by_id(user_id=user_id)
    if selected_event is None:
        raise HTTPException(status_code=404)
    return selected_event

# todo: 不要
@router.get("/", response_model=entities.ListEventsResponse)
async def get_events(
    *, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    return eu.get_list()


@router.delete("/{user_id}/{event_id}", response_model=entities.Event)
async def delete_event(
    *,
    event_id: int,
    user_id: int,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    deleted_event: Optional[entities.Event] = eu.delete(
        event_id=event_id, user_id=user_id
    )
    if deleted_event is None:
        raise HTTPException(status_code=404, detail="イベント削除エラー")
    return deleted_event
