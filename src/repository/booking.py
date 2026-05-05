from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.enum import BookingStatus
from src.model.booking import Booking_Class
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class BookingRepository:

    @staticmethod
    def CreateBooking(payload, db):
        try:
            db.add(payload)
            db.commit()
            db.refresh(payload)
            return payload
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Error while Creating Booking with Payload : {payload}") from e
        
    
    @staticmethod
    def GetBookingsByID(user_id, booking_id,  db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.booking_id==booking_id, Booking_Class.user_id==user_id)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Booking Exists") from e
    
    @staticmethod
    def GetBookingsByUserID(user_id, db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.user_id==user_id)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this user Exists") from e