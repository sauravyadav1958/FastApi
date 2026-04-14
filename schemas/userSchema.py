from pydantic import BaseModel, Field


class UserRequest(BaseModel):
    username: str = Field(..., description="Username for the user")
    password: str = Field(..., description="Password for the user")

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="Username for the user")

    class Config:
        orm_mode = True
