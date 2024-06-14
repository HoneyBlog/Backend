from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from models.models import User
from schemas.schemas import UserCreate, PostCreate
from uuid import uuid4

def create_user(db: Session, user: UserCreate):
    db_user = User(id=uuid4(), username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_post(db: Session, post: PostCreate):
    db_post = Post(id=uuid4(), title=post.title, content=post.content, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_users(db: Session):
    return db.query(User).all()

def check_login(db: Session, username: str, password: str) -> User:
    user = db.query(User).filter(User.username == username, User.password == password).first()
    if user is None:
        raise ValueError("Invalid username or password")
    return user
