from pydantic import BaseModel

class TestUser(BaseModel):
    id: int
    name: str
    email: str