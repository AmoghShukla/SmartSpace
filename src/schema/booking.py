import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel
from datetime import date, time, datetime
from src.model.enum import BookingStatus

class BookingCreate(BaseModel):
    start_time : datetime
    end_time : datetime

class BookingSecondCreate(BaseModel):
    user_id : UUID
    start_time : datetime
    end_time : datetime

class BookingThirdCreate(BaseModel):
    booking_id : UUID
    resource_id : UUID
    workspace_id : UUID
    floor_id : UUID

class BookingCreateResponse(BaseModel):
    user_id : UUID
    booking_id : UUID
    resource_ids : list[UUID]
    start_time : datetime
    end_time : datetime
    booking_status : Optional[BookingStatus]

class BookingUpdateResponse(BaseModel):
    resource_id : list[UUID]
    start_time : datetime
    end_time : datetime