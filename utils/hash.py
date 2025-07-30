from passlib.context import CryptContext

cryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return cryptContext.hash(password)
    
    def verify(hashed_password: str, plain_password: str):
        return cryptContext.verify(plain_password, hashed_password)