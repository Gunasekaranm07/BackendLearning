from fastapi import FastAPI, Request
from app.users.router import router as user_router
from app.students.router import router as student_router
from fastapi.responses import JSONResponse
from app.core.exceptions import AppError
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

app = FastAPI()

@app.exception_handler(AppError)
async def app_error_handler(req: Request, exc: AppError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

app.include_router(user_router)
app.include_router(student_router)