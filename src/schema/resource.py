from datetime import time
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field
from src.model.enum import ResourceType

class ResourceCreateRegister(BaseModel):
    resource_type : ResourceType = Field(...)
    total_resource_capacity : int = Field(...)
    requires_approval : bool = Field(...)
    open_time : time
    close_time : time
    floor_id : UUID

class UpdateResource(BaseModel):
    resource_type : Optional[ResourceType] = None
    total_resource_capacity : Optional[int] = None 
    requires_approval : Optional[bool] = None 
    open_time : Optional[time] = None
    close_time : Optional[time] = None


class ResourceCreateSecond(BaseModel):
    resource_type : ResourceType = Field(...)
    total_resource_capacity : int = Field(...)
    requires_approval : bool = Field(...)
    open_time : time
    close_time : time
    floor_id : UUID
    available_resource_capacity : int = Field(...)

    class Config:
        from_attribute = True


class ResourceResponse(BaseModel):
    resource_id : UUID
    resource_type : ResourceType
    total_resource_capacity : int
    open_time : time
    close_time : time
    floor_id : UUID