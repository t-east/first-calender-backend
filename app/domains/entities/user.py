from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    user_name: str = Field(max_length=12)
    password_hash: str
    email: str = Optional[EmailStr]
    birthday: datetime.date

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    pass