from fastapi import FastAPI, Request
from app.users.router import router as user_router
from app.students.router import router as student_router
from fastapi.responses import JSONResponse
from app.core.exceptions import AppError
from app.core.logging import setup_log
from fastapi.middleware.cors import CORSMiddleware

setup_log()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"]
)

@app.exception_handler(AppError)
async def app_error_handler(req: Request, exc: AppError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

app.include_router(user_router)
app.include_router(student_router)