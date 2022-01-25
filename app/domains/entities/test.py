from pydantic import BaseModel


class TestUserCreate(BaseModel):
    name: str
    email: str


class TestUser(TestUserCreate):
    id: int

    # class Config:
    #     orm_mode = True
