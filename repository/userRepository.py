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
    # adds the new user to the database session. It does not yet save it to the database.
    db.add(new_user) 
    # commits the current transaction, which means it saves all changes made in the session to the database. This is when the new user is actually saved to the database.
    db.commit() 
    # refreshes the new_user instance with the latest data from the database. 
    # This is useful to get any auto-generated fields (like id) that were created when the user was saved to the database.
    db.refresh(new_user) 
    return new_user
