
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from utils import token


ouath2_scheme = OAuth2PasswordBearer(tokenUrl = "/authentication")

def get_current_user(token_received: str = Depends(ouath2_scheme)):
    return token.verify_access_token(token_received)