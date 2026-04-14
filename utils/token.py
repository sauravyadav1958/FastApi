from datetime import datetime, timedelta
from fastapi import HTTPException, status
from jose import JWTError, jwt
from sqlalchemy import Integer

from schemas.userSchema import UserResponse

SECRET_KEY = "12345"
ALGORITHM = "HS256"
EXPIRE_MINUTES = 30


def create_access_token(data: dict) -> str:

    toencode = data.copy() # toencode is data to be encoded in the JWT token.
    exp_time = datetime.now() + timedelta(minutes=EXPIRE_MINUTES) # timedelta helps to add a specific duration to a datetime object.
    access_token = jwt.encode(toencode, SECRET_KEY, algorithm=ALGORITHM)
    return access_token


def verify_access_token(token: str) -> UserResponse:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Token",
                headers={"WWW-Authenticate": "Bearer"},
            )
        id: int = payload.get("id")
        return UserResponse(id=id, username=username)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token",
            headers={"WWW-Authenticate": "Bearer"},
        )
