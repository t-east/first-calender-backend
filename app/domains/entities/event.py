from lib2to3.pgen2.token import OP
from typing import Optional, List
import datetime
from pydantic import BaseModel, Field

from app.drivers.rdb.base import Base


class EventBase(BaseModel):
    title: Optional[str] = Field(max_length=12)
    description: Optional[str] = None
    begin_date: Optional[datetime.date]
    is_all_day: Optional[bool]
    end_date: Optional[datetime.date]
    color: Optional[str]


class EventCreate(EventBase):
    user_id: Optional[int]
    tag_id: Optional[int]


class EventUpdate(EventBase):
    pass

class EventInDBBase(EventBase):
    id: int
    user_id: int
    tag_id: int

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    class Config:
        orm_mode = True


class ListEventsResponse(BaseModel):
    total: int
    events: List[Event]

# class ListEventTags(BaseModel):
