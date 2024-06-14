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

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: UUID

class Post(BaseModel):
    id: str
    title: str
    content: str
    author_id: str

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str


