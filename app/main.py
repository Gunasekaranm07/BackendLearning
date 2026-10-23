from fastapi import FastAPI
from app.core.database import engine, SessionLocal, Base
from app.students.models import Student   
from app.students.schemas import StudentReq, StudentRes
from app.students.repository import *
from app.students.router import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router)