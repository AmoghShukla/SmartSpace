import uuid

from pydantic import BaseModel, Field, UUID3

class UserCreate(BaseModel):
    user_name : str = Field(...)
    user_email : str = Field(...)
    user_password : str = Field(...)
    user_contact_no : str = Field(...)

class UserResponse(BaseModel):
    user_id : UUID3
    user_name : str = Field(...)
    user_email : str = Field(...)
    user_role : str

