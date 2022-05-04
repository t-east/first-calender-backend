from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    user_name: str = Field(max_length=30)
    email: Optional[EmailStr]


class UserAuth(UserBase):
    hashed_password: str
    disabled: Optional[bool]


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
