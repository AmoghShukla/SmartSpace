from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.Exceptions.Custom_Exception import CustomException
from src.model.payment import Payment_Class
from src.utils.loggers import get_logger

logger = get_logger(__name__)

class PaymentRepository:

    @staticmethod
    def Create_Payment(payload, db):
        try:
            logger.info(f"Creating Payment")
            db.add(payload)
            db.commit()
            logger.info(f"Payment Created!!!")
            db.refresh(payload)

        except SQLAlchemyError as e:
            db.rollback()
            logger.error('Encountered Error while creating Payment')
            raise CustomException.RepositoryError(" { 'message' : 'Encountered Error while creating Payment' } ")
    
    @staticmethod
    def Complete_Payment(payload , db):
        try:
            logger.info(f'Completing Payment for booking_id : {payload.booking_id}')
            db.commit()
            return {
                "message" : "Thank you for Completing the Payment!!!"
            }
        except SQLAlchemyError as e:
            logger.error('Encountered Error while completing Payment')
            db.rollback()
            raise CustomException.RepositoryError(" { 'message' : 'Encountered Error while completing Payment' } ")
    
    @staticmethod
    def GetPaymentByBookingID(booking_id, db):
        try:
            logger.info(f"Fetching Payment for Booking Id : {booking_id}")
            return db.execute(
                select(Payment_Class)
                .where(Payment_Class.booking_id == booking_id)
                ).scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Error while Intiating Payment forng Id : {booking_id}")
            raise CustomException.RepositoryError("{'message : Error While Fetching Payment by Booking ID'}")
        