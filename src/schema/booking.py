import enum
from typing import Optional
import uuid
from uuid import UUID

from pydantic import BaseModel, model_validator
from datetime import date, time, datetime, timedelta
from src.model.enum import BookingStatus

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class BookingCreate(BaseModel):
    start_time : datetime
    end_time : datetime

    @model_validator(mode='after')
    def datetime_checker(self) -> str:
        if self.start_time.date() != self.end_time.date():
            logger.debug("Booking should start and end on same date")
            raise ValueError("Booking should start and end on same date")
        duration = self.end_time - self.start_time
        if duration > timedelta(hours=1):
            logger.debug("Your Booking duration can't be more than 1 hour")
            raise ValueError("Your Booking duration can't be more than 1 hour")
        if duration <= timedelta(minutes=30):
            logger.debug("Your Booking duration can't be less than 30 mins")
            raise ValueError("Your Booking duration can't be less than 30 mins")
        if self.start_time >= self.end_time:
            logger.debug("Your Booking start time can't be greater than or equal to end time")
            raise ValueError("Your Booking start time can't be greater than or equal to end time")
        return self


class MyBookingResponse(BaseModel):
    user_id : UUID
    booking_id : UUID
    start_time : datetime
    end_time : datetime
    booking_status : Optional[BookingStatus]

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