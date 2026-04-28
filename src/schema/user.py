from typing import Optional
import uuid

from pydantic import BaseModel, Field, UUID4
from pydantic_extra_types.phone_numbers import PhoneNumber

class UserCreate(BaseModel):
    user_name : str = Field(...)
    user_email : str = Field(...)
    user_password : str = Field(...)
    user_contact_no : PhoneNumber = Field(..., examples=["+91 9999999999"])

class UserResponse(BaseModel):
    user_id : Optional[UUID4]
    user_name : Optional[str]
    user_email : Optional[str]
    user_role : Optional[str]