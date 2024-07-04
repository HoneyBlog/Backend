from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.models import User, Post
from schemas.schemas import UserCreate, PostCreate
from uuid import uuid4
import jwt
from datetime import datetime, timedelta

# Replace with your secret key in a real application
SECRET_KEY = "your-secret-key"


# Users CRUD
def create_user(db: Session, user: UserCreate):
    db_user = User(id=str(uuid4()), username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def check_login(db: Session, username: str, password: str) -> str:
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if user is None:
        raise ValueError("Invalid username or password")

    # Generate JWT token
    token = jwt.encode({
        'user_id': str(user.id),
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time
    }, SECRET_KEY, algorithm='HS256')

    return token


# Posts CRUD

def create_post(db: Session, post: PostCreate):
    db_post = Post(id=str(uuid4()), title=post.title, content=post.content, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session):
    return db.query(Post).all()
