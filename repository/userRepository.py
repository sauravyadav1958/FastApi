from sqlalchemy.orm import Session

from models.userModel import UserModel
from schemas.userSchema import UserRequest
from utils.hash import Hash


def get_all(db: Session) -> list[UserModel]:
    users = db.query(UserModel).all()
    return users


def create_user(request: UserRequest, db: Session) -> UserModel:
    new_user = UserModel(
        username=request.username, password=Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()

    db.refresh(new_user)
    return new_user
