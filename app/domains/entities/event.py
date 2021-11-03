from typing import Optional
import datetime
from pydantic import BaseModel, Field


class EventBase(BaseModel):
    user_id: Optional[int]
    title: Optional[str] = Field(max_length=12)
    description: Optional[str] = None
    begin_date: Optional[datetime.date]
    is_all_day: Optional[bool]
    end_date: Optional[datetime.date]
    color: Optional[str]

    class Config:
        orm_mode = True


class EventUpdate(EventBase):
    event_id: int
    event_name: Optional[str]
    description: Optional[str]
    begin_date: Optional[datetime.date]
    is_all_day: Optional[bool]
    end_date: Optional[datetime.date]
    color: Optional[str]
    pass


class EventDelete(EventBase):
    event_id: int
    pass