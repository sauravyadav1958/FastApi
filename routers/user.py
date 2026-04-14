from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import database
from repository import userRepository
from schemas.userSchema import UserRequest


router = APIRouter(prefix="/user", tags=["users"])

get_db = database.get_db


@router.get("/", response_model=list[UserRequest])
def get_users(db: Session = Depends(get_db)) -> list[UserRequest]:
    return userRepository.get_all(db)


@router.post("/", response_model=UserRequest)
def create_user(request: UserRequest, db: Session = Depends(get_db)) -> UserRequest:
    return userRepository.create_user(request, db)
