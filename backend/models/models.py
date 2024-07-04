from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from config.database import Base 

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(length=20), unique=True, index=True)
    email = Column(String(length=50), unique=True, index=True)
    password = Column(String(length=25)),

class Post(Base):
    __tablename__ = "posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    content = Column(String(length=300)),
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))