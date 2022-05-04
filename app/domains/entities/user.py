from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    user_name: str = Field(max_length=30)
    email: Optional[EmailStr]


class UserCreate(UserBase):
    password: str


# class UserAuth(UserBase):
#     hashed_password: str
#     disabled: Optional[bool]


class UserUpdate(UserBase):
    password: str


class UserInDBBase(UserBase):
    user_id: int

    class Config:
        orm_mode = True


class User(UserInDBBase):
    class Config:
        orm_mode = True


class UserInDB(UserInDBBase):
    password: str
