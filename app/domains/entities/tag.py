from typing import Optional, List
from pydantic import BaseModel, Field


class TagBase(BaseModel):
    label: Optional[str] = Field(max_length=30)
    color: Optional[str]


class TagCreate(TagBase):
    event_id: Optional[int]


class TagInDBBase(TagBase):
    tag_id: int
    event_id: int

    class Config:
        orm_mode = True


class Tag(TagInDBBase):
    class Config:
        orm_mode = True

class ListTagsResponse(BaseModel):
    total: int
    events: List[Tag]

    class Config:
        orm_mode = True
