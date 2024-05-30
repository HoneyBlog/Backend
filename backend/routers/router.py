from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.schemas import UserCreate, User
from services.crud import create_user
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
    return create_user(db, user)
