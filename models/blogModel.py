from turtle import back
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base
from routers import user


class BlogModel(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    
    creator = relationship("UserModel", back_populates="blogs")
