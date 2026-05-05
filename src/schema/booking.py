import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel
from datetime import date, time

class BookingCreate(BaseModel):
    resource_id : list[UUID]
    booking_date : date
    start_time : time
    end_time : time

class BookingSecondCreate(BaseModel):
    workspace_id : UUID
    floor_id : UUID
    booking_date : date
    resource_id : list[UUID]
    start_time : time
    end_time : time

class BookingCreateResponse(BaseModel):
    booking_id : UUID
    workspace_id : UUID
    floor_id : UUID
    booking_date : date
    resource_id : list[UUID]
    start_time : time
    end_time : time
    booking_status : Optional[bool]

class BookingUpdateResponse(BaseModel):
    booking_date : date
    resource_id : list[UUID]
    start_time : time
    end_time : time