from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.schemas import UserCreate, User, PostCreate, Post
from services.crud import create_user, create_post
from config.database import get_db, test_connection, create_tables

# Ensure these functions are called appropriately and not within the route definitions
test_connection()
create_tables()

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Server is running"}

@router.post("/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user)
    user.id = str(user.id)
    return user

@router.post("/posts/", response_model=Post)
async def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    post = create_post(db, post)
    post.id = str(post.id)
    post.author_id = str(post.author_id)
    return post