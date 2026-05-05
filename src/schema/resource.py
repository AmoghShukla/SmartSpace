from datetime import time
import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict
from src.model.enum import ResourceType

class ResourceCreateRegister(BaseModel):
    resource_type : ResourceType = Field(...)
    total_resource_capacity : int = Field(...)
    requires_approval : bool = Field(...)
    open_time : time
    close_time : time
    floor_id : UUID

class UpdateResource(BaseModel):
    resource_type : Optional[ResourceType] 
    total_resource_capacity : Optional[int] 
    requires_approval : Optional[bool] 
    open_time : Optional[time]
    close_time : Optional[time]


class ResourceCreateSecond(BaseModel):
    resource_type : ResourceType = Field(...)
    total_resource_capacity : int = Field(...)
    available_resource_capacity : int = Field(...)
    requires_approval : bool = Field(...)
    open_time : time
    close_time : time
    floor_id : UUID


class ResourceResponse(BaseModel):
    resource_id : UUID
    resource_type : ResourceType
    resource_capacity : int
    is_avaialable : bool
    requires_approval : bool
    open_time : time
    close_time : time
    floor_id : UUID