import enum
from typing import Optional
import uuid

from pydantic import BaseModel, Field, UUID4
from src.model.enum import UserRole

class UserCreate(BaseModel):
    user_name : str = Field(...)
    user_email : str = Field(...)
    user_password : str = Field(...)
    user_contact_no : str = Field(..., min_length=10, max_length=10)
    user_role : UserRole

class UserResponse(BaseModel):
    user_id : Optional[UUID4]
    user_name : Optional[str]
    user_email : Optional[str]
    user_role : Optional[str]