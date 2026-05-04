import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field, UUID4, ConfigDict
from datetime import DateTime
from sqlalchemy import DateTime

class BookingCreate(BaseModel):
    user_id : UUID
    workspace_id : UUID
    resource_id : list[UUID]
    start_time : DateTime
    end_time : DateTime