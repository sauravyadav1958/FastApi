from pydantic import BaseModel, Field


class BlogRequest(BaseModel):
    title: str = Field(..., description="Blog title")
    body: str = Field(..., description="Blog body content")
# orm_mode tells Pydantic to read data even if it is not a dict, but an ORM model (like SQLAlchemy model).
    class Config:
        orm_mode = True
