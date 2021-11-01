import datetime
#  from typing import Text

#  from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TEXT, Boolean
from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: int
    user_name: str = Field(max_length=12)
    password_hash: str
    email: str = Field(max_length=50)
    profile_image_path: str
    birthday: datetime.date
    resistered_at: datetime.datetime
    last_login_at: datetime.datetime

    class Config:
        orm_mode = True


class Event(BaseModel):
    user_id: int
    event_id: int
    event_name: str = Field(max_length=12)
    description: TEXT
    begin_date: datetime.date
    is_all_day: Boolean
    end_date: datetime.date
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime
    color: str

    class Config:
        orm_mode = True
