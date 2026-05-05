import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel
from datetime import date, time
from src.model.enum import BookingStatus

class BookingCreate(BaseModel):
    booking_date : date
    start_time : time
    end_time : time

class BookingSecondCreate(BaseModel):
    workspace_id : UUID
    floor_id : UUID
    booking_date : date
    resource_id : UUID
    start_time : time
    end_time : time

class BookingCreateResponse(BaseModel):
    booking_id : UUID
    workspace_id : UUID
    floor_id : UUID
    booking_date : date
    resource_id : UUID
    start_time : time
    end_time : time
    booking_status : Optional[BookingStatus]

class BookingUpdateResponse(BaseModel):
    booking_date : date
    resource_id : list[UUID]
    start_time : time
    end_time : time