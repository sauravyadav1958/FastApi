from pydantic import BaseModel


class BlogRequest(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True

        