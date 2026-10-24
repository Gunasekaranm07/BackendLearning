from pydantic import EmailStr, BaseModel

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRes(BaseModel):
    model_config = {'from_attributes': True}
    
    id: int
    email: str