from typing import Optional
import datetime
from pydantic import BaseModel, Field


class ReminderBase(BaseModel):
    user_id: Optional[int]
    event_id: Optional[int]
    remind_time: Optional[datetime.date]

    class Config:
        orm_mode = True


class ReminderUpdate(ReminderBase):
    reminder_id: str
    remind_time: Optional[datetime.date]
    pass


class ReminderDelete(ReminderBase):
    reminder_id: str
    pass