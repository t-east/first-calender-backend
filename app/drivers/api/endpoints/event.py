from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
import app.domains.entities as entities
import app.usecases as usecases
from app.drivers.api.deps import get_event_usecase
import app.domains.entities.tag as tag_entities


router = APIRouter()


@router.post("/", response_model=entities.Event)
async def create_event(
    *,
    event_in: entities.EventCreate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.Event:
    return eu.create(obj_in=event_in)


@router.put("/{user_id}/{event_id}", response_model=entities.Event)
async def update_event(
    *,
    event_id: int,
    user_id: int,
    event_in: entities.EventUpdate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    updated_event: Optional[entities.Event] = eu.update(
        event_id=event_id, user_id=user_id, obj_in=event_in
    )
    if updated_event is None:
        raise HTTPException(status_code=404)
    return updated_event


@router.get("/{user_id}", response_model=entities.ListEventsResponse)
async def get_list_events(
    *, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> entities.ListEventsResponse:
    selected_event: entities.ListEventsResponse = eu.get_list_by_id(user_id=user_id)
    if selected_event is None:
        raise HTTPException(status_code=404)
    return selected_event


@router.get("/{user_id}/{event_id}", response_model=entities.Event)
async def get_by_id(
    event_id: int, user_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[entities.Event]:
    get_event: Optional[entities.Event] = eu.get_by_id(
        event_id=event_id, user_id=user_id
    )
    if get_event is None:
        raise HTTPException(status_code=404)
    return get_event


@router.post("/{event_id}/tag", response_model=tag_entities.Tag)
async def create_event_tag(
    *,
    tag_in: tag_entities.TagCreate,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> tag_entities.Tag:
    return eu.create_tag(obj_in=tag_in)


@router.get("/{event_id}/tag/{tag_id}", response_model=tag_entities.Tag)
async def get_tag_by_id(
    event_id: int, tag_id: int, eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[tag_entities.Tag]:
    get_event: Optional[tag_entities.Tag] = eu.get_tag_by_id(
        event_id=event_id, tag_id=tag_id
    )
    if get_event is None:
        raise HTTPException(status_code=404)
    return get_event


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


@router.delete("/{event_id}/tag/{tag_id}", response_model=tag_entities.Tag)
async def delete_tag(
    *,
    event_id: int,
    tag_id: int,
    eu: usecases.EventUsecase = Depends(get_event_usecase)
) -> Optional[tag_entities.Tag]:
    deleted_tag: Optional[tag_entities.Tag] = eu.delete_tag(
        event_id=event_id, tag_id=tag_id
    )
    if deleted_tag is None:
        raise HTTPException(status_code=404, detail="イベント削除エラー")
    return deleted_tag
