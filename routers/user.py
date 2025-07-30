from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import database
from repository import userRepository
from schemas.userSchema import UserRequest


router = APIRouter(prefix="/user", tags=["users"])

get_db = database.get_db

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return userRepository.get_all(db)

@router.post("/")
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    return userRepository.create_user(request, db)