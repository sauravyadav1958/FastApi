from pydantic import BaseModel


class UserRequest(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
