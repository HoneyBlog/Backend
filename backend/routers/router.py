from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import UserCreate, User, PostCreate, Post, LoginRequest
from services.crud import create_user, create_post, get_users, check_login
from config.database import get_db, test_connection, create_tables

# Ensure these functions are called appropriately and not within the route definitions
test_connection()
create_tables()

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Server is running"}

@router.post("/api/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(db, user)
    user.id = str(user.id)
    return user

@router.post("/api/posts/", response_model=Post)
async def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    post = create_post(db, post)
    post.id = str(post.id)
    post.author_id = str(post.author_id)
    return post

@router.get("/api/users/", response_model=list[User])
async def get_users(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        user.id = str(user.id)
    return users

@router.post("/api/users/login/", response_model=User)
async def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = check_login(db, login_request.username, login_request.password)
        user.id = str(user.id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
