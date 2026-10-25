from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from app.core.security import decode_access_token
from app.core.database import get_db
from app.users.models import User
from app.users.repository import get_user_by_id

bearer = HTTPBearer()

def get_current_user(
    creds: HTTPAuthorizationCredentials = Depends(bearer),
    db: Session = Depends(get_db)
) -> User:
    id = decode_access_token(creds.credentials)
    user = get_user_by_id(db, int(id)) if id else None
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token or Expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return user