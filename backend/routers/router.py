from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.schemas import UserCreate, User, PostCreate, Post, LoginRequest
from services.crud import create_user, create_post, get_users, check_login, get_posts, get_user_by_id
from config.database import get_db, test_connection, create_tables
import re


# Ensure these functions are called appropriately and not within the route definitions
test_connection()
create_tables()

router = APIRouter()

# User Regex
USERNAME_REGEX = r'^[a-zA-Z0-9._-]{5,20}$'
PASSWORD_REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,25}$'

# User validation
validation_err = "Invalid username or password"

def user_validaton(user):
    if not re.match(USERNAME_REGEX, user.username):
        raise HTTPException(status_code=400, detail=validation_err)
    if not re.match(PASSWORD_REGEX, user.password):
        raise HTTPException(status_code=400, detail=validation_err)

@router.get("/")
async def root():
    return {"message": "Server is running"}

# Users APIs
@router.get("/api/users/", response_model=list[User])
async def get_users_endpoint(db: Session = Depends(get_db)):
    users = get_users(db)
    for user in users:
        user.id = str(user.id)
    return users

@router.get("/api/users/{user_id}", response_model=User)
async def get_user_by_id_endpoint(user_id: str, db: Session = Depends(get_db)):
        try:
            user = get_user_by_id(db, user_id)
            user.id = str(user.id)
            return user
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
        
@router.post("/api/users/", response_model=User)
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    user_validaton(user)
    user = create_user(db, user)
    user.id = str(user.id)
    return user

@router.post("/api/users/login/", response_model=User)
async def login(login_request: LoginRequest, db: Session = Depends(get_db)):
    try:
        user_validaton(login_request)
        user = check_login(db, login_request.username, login_request.password)
        user.id = str(user.id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

# Posts APIs
@router.post("/api/posts/", response_model=Post)
async def create_post_endpoint(post: PostCreate, db: Session = Depends(get_db)):
    post = create_post(db, post)
    post.id = str(post.id)
    post.author_id = str(post.author_id)
    return post


@router.get("/api/posts/", response_model=list[User])
async def get_posts(db: Session = Depends(get_db)):
    posts = get_posts(db)
    for post in posts:
        post.id = str(post.id)
        post.author_id = str(post.author_id)
    return posts