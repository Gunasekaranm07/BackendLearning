from fastapi import FastAPI
from app.users.router import router as user_router
from app.students.router import router as student_router

app = FastAPI()

app.include_router(user_router)
app.include_router(student_router)