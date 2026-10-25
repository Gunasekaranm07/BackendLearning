from pydantic import EmailStr, BaseModel, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)

class TokenRes(BaseModel):
    access_token: str
    token_type: str = "bearer"

    model_config = {'from_attributes': True}

class UserRes(BaseModel):
    model_config = {'from_attributes': True}
    
    id: int
    email: str