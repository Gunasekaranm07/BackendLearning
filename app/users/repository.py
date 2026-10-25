from sqlalchemy import select
from sqlalchemy.orm import Session
from app.users.models import User

def create_user(db:Session, email: str, hashed_password: str) -> User:
    user = User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db:Session, email:str) -> User | None:
    user = db.scalar(select(User).where(email == User.email))
    if user is None:
        return None
    else:
        return user

def get_user_by_id(db:Session, id: int) -> User | None:
    return db.scalar(select(User).where(id == User.id))