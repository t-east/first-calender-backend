from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    user_name: str = Field(max_length=12)
    email: Optional[EmailStr]
    birthday: datetime.date


class UserCreate(UserBase):
    password: str


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    password: str
