from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    user_email : EmailStr
    user_password : str

class LoginResponse(BaseModel):
    message : str
    access_token : str
    refresh_token : str
    token_type : str