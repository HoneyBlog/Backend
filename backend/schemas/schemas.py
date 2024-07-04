from pydantic import BaseModel, EmailStr, constr
from uuid import UUID

class UserCreate(BaseModel):
        username: str
        email: str
        password: str


class User(BaseModel):
    id: UUID
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
