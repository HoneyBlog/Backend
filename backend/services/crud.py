from sqlalchemy.orm import Session
from models.models import User
from schemas.schemas import UserCreate
from uuid import uuid4

def create_user(db: Session, user: UserCreate):
    db_user = User(id=uuid4(), username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
