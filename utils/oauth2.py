from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from schemas.userSchema import UserResponse
from utils import token

# tokenUrl is the URL where the client can obtain a token. It should point to the authentication endpoint of your API. 
# OAuth2PasswordBearer = token extractor
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication") 

# token: str = Depends(oauth2_scheme) returns token string.
def get_current_user(token_received: str = Depends(ouath2_scheme)) -> UserResponse:
    return token.verify_access_token(token_received)
