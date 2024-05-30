from pydantic import BaseModel
from uuid import UUID


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(BaseModel):
    id: str
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True
