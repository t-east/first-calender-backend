from typing import Optional, List
import datetime
from pydantic import BaseModel, Field


class EventBase(BaseModel):
    title: Optional[str] = Field(max_length=12)
    description_text: Optional[str] = None
    to_date: datetime.date
    from_date: datetime.date
    is_all_day: Optional[bool]
    # tag: List[Tag]


class EventCreate(EventBase):
    user_id: Optional[int]


class EventUpdate(EventBase):
    pass


class EventInDBBase(EventBase):
    event_id: int
    user_id: int

    class Config:
        orm_mode = True


class Event(EventInDBBase):
    class Config:
        orm_mode = True


class ListEventsResponse(BaseModel):
    total: int
    events: List[Event]

    class Config:
        orm_mode = True
