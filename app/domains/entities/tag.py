from typing import Optional
from pydantic import BaseModel, Field


class TagBase(BaseModel):
    label: str = Field(max_length=32)


class TagInDBBase(TagBase):
    id: int

    class Config:
        orm_mode = True
