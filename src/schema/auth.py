from pydantic import BaseModel, EmailStr, Field

class LoginRequest(BaseModel):
    user_email : EmailStr
    user_password : str

class LoginResponse(BaseModel):
    access_token : str
    refresh_token : str
    token_type : str = Field(default='Bearer')