from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
import app.usecases as usecases
from app.drivers.api.deps import get_tag_usecase
import app.domains.entities as entities


router = APIRouter()

@router.post("/", response_model=entities.Tag)
async def create_event_tag(
    *,
    tag_in: entities.TagCreate,
    eu: usecases.TagUsecase = Depends(get_tag_usecase)
) -> entities.Tag:
    return eu.create_tag(obj_in=tag_in)


@router.get("/{event_id}/{tag_id}", response_model=entities.Tag)
async def get_tag_by_id(
    event_id: int, tag_id: int, eu: usecases.TagUsecase = Depends(get_tag_usecase)
) -> Optional[entities.Tag]:
    get_tag: Optional[entities.Tag] = eu.get_tag_by_id(
        event_id=event_id, tag_id=tag_id
    )
    if get_tag is None:
        raise HTTPException(status_code=404)
    return get_tag


@router.delete("/{event_id}/{tag_id}", response_model=entities.Tag)
async def delete_tag(
    *,
    event_id: int,
    tag_id: int,
    eu: usecases.TagUsecase = Depends(get_tag_usecase)
) -> Optional[entities.Tag]:
    deleted_tag: Optional[entities.Tag] = eu.delete_tag(
        event_id=event_id, tag_id=tag_id
    )
    if deleted_tag is None:
        raise HTTPException(status_code=404, detail="イベント削除エラー")
    return deleted_tag