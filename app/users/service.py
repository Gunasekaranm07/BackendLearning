from sqlalchemy.orm import Session
from app.users.repository import create_user, get_user_by_email
from app.users.exceptions import EmailAlreadyExist, InvalidCredentials
from app.core.security import hash_password, verify_password
import logging

logger = logging.getLogger(__name__)

def register_user(db:Session, email:str, password: str):
    hashed_password = hash_password(password)
    if get_user_by_email(db, email) is not None:
        logger.error("Email already exist")
        raise EmailAlreadyExist()
    user = create_user(db, email.strip().lower(), hashed_password)
    return user

def authenticate(db:Session, email:str, password:str):
    user = get_user_by_email(db, email.strip().lower())
    if user is None:
        logger.error("Email not registered")
        raise InvalidCredentials()
    elif not verify_password(password, user.hashed_password):
        logger.error("Wrong Password")
        raise InvalidCredentials()
    else:
        return user