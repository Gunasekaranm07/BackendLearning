from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.schemas import UserCreate, UserRes, UserLogin
from app.users.service import register_user, authenticate
from app.core.database import get_db
from app.users.exceptions import EmailAlreadyExist, InvalidCredentials

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.post("/register", status_code=201, response_model=UserRes)
def register(req: UserCreate, db:Session=Depends(get_db)):
    try:
        return register_user(db, req.email, req.password)
    except EmailAlreadyExist:
        raise HTTPException(status_code=409, detail="Email already registered")
    
@router.post("/login", response_model=UserRes)
def login(req: UserLogin, db:Session = Depends(get_db)):
    try:
        return authenticate(db, req.email, req.password)
    except InvalidCredentials:
        raise HTTPException(status_code=401, detail="Invalid Credentials")