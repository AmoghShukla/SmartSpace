from datetime import time
import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict
from src.model.enum import UserRole

class ResourceCreate(BaseModel):
    resource_type : str = Field(...)
    resource_capacity : int = Field(...)
    requires_approval : bool = Field(...)
    open_time : time
    close_time : time
    floor_id : UUID


class ResourceResponse(BaseModel):
    resource_id : UUID
    resource_type : str
    resource_capacity : int
    is_avaialable : bool
    requires_approval : bool
    open_time : time
    close_time : time
    floor_id : UUID