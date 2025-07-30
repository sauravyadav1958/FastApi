
from turtle import back
from sqlalchemy import Column, Integer, String
from database.database import Base
from sqlalchemy.orm import relationship


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    
    blogs = relationship("BlogModel", back_populates="creator")