import re
from urllib import response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from database import database
from repository import blogRepository
from schemas.blogSchema import BlogRequest
from schemas.userSchema import UserResponse
from utils import oauth2

router = APIRouter(prefix="/blog", tags=["blogs"]) # prefix is added to all routes in this router, tags are used for grouping routes in documentation.
get_db = database.get_db


@router.get("/all", response_model=list[BlogRequest])
def get(
    # Depends(get_db) is a dependency that provides a database session to the route handler. 
    # It ensures that a new session is created for each request and properly closed after the request is processed. A DB session is not thread-safe
    # If you reuse one session across requests → data corruption / race conditions.
    db: Session = Depends(get_db), 
    current_user: UserResponse = Depends(oauth2.get_current_user),
) -> list[BlogRequest]:
    return blogRepository.get_all(db)


@router.get("/{id}", response_model=BlogRequest)
def get_By_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
) -> BlogRequest:
    return blogRepository.get_by_id(id, db, current_user)


@router.post("/", response_model=BlogRequest)
def create_blog(
    request: BlogRequest,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
) -> BlogRequest:
    return blogRepository.create_blog(request, db, current_user)


@router.delete("/{id}", response_model=dict)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
) -> dict:
    return blogRepository.delete_blog(id, db, current_user)


@router.put("/{id}", response_model=BlogRequest)
def update(
    id: int,
    request: BlogRequest,
    db: Session = Depends(get_db),
    current_user: UserResponse = Depends(oauth2.get_current_user),
) -> BlogRequest:
    return blogRepository.update_blog(id, db, request, current_user)
