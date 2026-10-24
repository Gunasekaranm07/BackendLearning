from fastapi import FastAPI
from app.core.database import Base, engine
from app.students.models import Student
from app.students.router import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router)