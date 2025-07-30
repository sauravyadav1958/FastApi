from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database import database
from repository import blogRepository
from schemas.blogSchema import BlogRequest
from schemas.userSchema import UserResponse
from utils import oauth2

router = APIRouter(prefix="/blog", tags=["blogs"])
get_db = database.get_db


@router.get("/all")
def get(
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
):
    return blogRepository.get_all(db)


@router.get("/{id}")
def get_By_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
):
    return blogRepository.get_by_id(id, db, current_user)


@router.post("/")
def create_blog(
    request: BlogRequest,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
):
    return blogRepository.create_blog(request, db, current_user)


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
):
    return blogRepository.delete_blog(id, db, current_user)


@router.put("/{id}")
def update(
    id: int,
    request: BlogRequest,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
):
    return blogRepository.update_blog(id, db, request, current_user)
