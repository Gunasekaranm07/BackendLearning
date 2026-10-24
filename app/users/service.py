from sqlalchemy.orm import Session
from app.users.repository import create_user, verify_user
from app.users.exceptions import EmailAlreadyExist, InvalidCredentials


def register(db:Session, email:str, password: str):
    user = create_user(db, email, password)
    if user is None:
        raise EmailAlreadyExist()
    return user

def verify(db:Session, email:str, password:str):
    verification = verify_user(db, email, password)
    if verification:
        return True
    raise InvalidCredentials()