from typing import Optional, List
import datetime
from pydantic import BaseModel, Field

from app.domains.entities import event


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