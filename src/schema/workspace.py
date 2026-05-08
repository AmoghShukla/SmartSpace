import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict, field_validator
from src.model.enum import UserRole

class WorkspaceCreate(BaseModel):
    workspace_name : str = Field(...)
    workspace_location : str = Field(...)
    workspace_manager_id : UUID = Field(...)
    workspace_floor_capacity : int = Field(...)

    @field_validator("workspace_location")
    @classmethod
    def validate_location(cls, n: str) ->str:
        n = n.strip()
        if not n:
            raise ValueError("Location cannot be empty")
        if not n.replace(" ", "").isalpha():
            raise ValueError("Please Enter City Names only, Location must contain only letters and spaces")
        return n

class WorkspaceResponse(BaseModel):
    workspace_id : Optional[UUID] = Field(...)
    workspace_name : Optional[str] = Field(...)
    workspace_location : Optional[str] = Field(...)
    workspace_manager_id : Optional[UUID] = Field(...)
    workspace_floor_capacity : int = Field(...)