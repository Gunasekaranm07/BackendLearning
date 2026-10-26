from app.core.exceptions import AppError
class EmailAlreadyExist(AppError):
    status_code = 409
    detail = "Email already registered"

class InvalidCredentials(AppError):
    status_code = 401
    detail = "Invalid Credentials"