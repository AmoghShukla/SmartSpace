from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.enum import BookingStatus
from src.model import Booking_Class
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class BookingRepository:

    @staticmethod
    def CreateBooking(payload, db):
        try:
            pass
        except CustomException.ServiceError as e:
            pass