import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict

class FloorCreate(BaseModel):
    workspace_id : str = Field(...)
    floor_meeting_room_capacity : str = Field(...)
    floor_auditorium_capacity : str = Field(...)

class FloorResponse(BaseModel):
    floor_id : Optional[UUID] 
    floor_number : int = Field(...)
    floor_capacity : Optional[int] = Field(...)
    workspace_id : Optional[UUID] = Field(...)