import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict
from src.model.enum import UserRole

class WorkspaceCreate(BaseModel):
    workspace_name : str = Field(...)
    workspace_location : str = Field(...)
    workspace_manager_id : UUID = Field(...)

class WorkspaceResponse(BaseModel):
    workspace_name : Optional[str] = Field(...)
    workspace_location : Optional[str] = Field(...)
    workspace_manager_id : Optional[UUID] = Field(...)