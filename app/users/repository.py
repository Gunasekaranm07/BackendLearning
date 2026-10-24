from sqlalchemy import select
from sqlalchemy.orm import Session
from app.users.models import User
from app.core.security import hash_password, verify_password

def create_user(db:Session, email: str, password: str) -> (User | None):
    email_exist = True if db.scalar(select(User).where(email == User.email)) else False
    if email_exist:
        return None
    user = User(email=email, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def verify_user(db:Session, email:str, password:str) -> bool | None:
    user = db.scalar(select(User).where(email == User.email))
    email_exist = True if user else False
    if not email_exist:
        return None
    else:
        return verify_password(plain_password=password, hashed_password=user.hashed_password)