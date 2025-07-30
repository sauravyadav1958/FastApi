
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.blogModel import BlogModel
from schemas.blogSchema import BlogRequest
from schemas.userSchema import UserResponse


def get_all(db: Session):
    blogs = db.query(BlogModel).all()
    return blogs

def get_by_id(id: int, db: Session, current_user: UserResponse):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    return blog

def create_blog(request: BlogRequest, db: Session, current_user: UserResponse):
    new_blog = BlogModel(title=request.title, body=request.body, user_id=current_user.id)
    db.add(new_blog)
    db.commit()

    db.refresh(new_blog)
    return new_blog

def delete_blog(id: int, db: Session, current_user: UserResponse):
    delete_blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not delete_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    delete_blog
    db.commit()
    return {"message": "Blog deleted successfully"}

def update_blog(id: int, db: Session, request: BlogRequest, current_user: UserResponse):
    update_blog = db.query(BlogModel).filter(BlogModel.id == id)
    if not update_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    update_blog.update(request.model_dump(exclude_unset=True))
    db.commit()
    db.refresh(update_blog.first())
    return request