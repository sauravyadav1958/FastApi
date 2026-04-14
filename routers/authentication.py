from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import database
from models.userModel import UserModel
from utils import token
from utils.hash import Hash


router = APIRouter(prefix="/authentication", tags=["authentication"])
get_db = database.get_db  # Assuming get_db is defined elsewhere in your application


@router.post("/", response_model=dict)
def authenticate(
    # OAuth2PasswordRequestForm is a class provided by FastAPI that represents the form data sent by the client during authentication. 
    # Here Depends() is same as Depends(OAuth2PasswordRequestForm).
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
) -> dict:
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if not user:
        return {"error": "Invalid username !!!"}
    if not Hash.verify(user.password, request.password):
        return {"error": "Invalid password !!!"}

    access_token = token.create_access_token(data={"sub": user.username, "id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
