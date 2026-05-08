from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.Exceptions.Custom_Exception import CustomException
from src.model.payment import Payment_Class


class PaymentRepository:

    @staticmethod
    def Create_Payment(payload, db):
        try:
            db.add(payload)
            db.commit()
            db.refresh(payload)

        except:
            db.rollback()

    @staticmethod
    def Complete_Payment(payload , db):
        try:
            db.commit()
            return {
                "message" : "Thank you for Completing the Payment!!!"
            }
        except:
            db.rollback()
    
    @staticmethod
    def GetPaymentByBookingID(booking_id, db):
        try:
            return db.execute(
                select(Payment_Class)
                .where(Payment_Class.booking_id == booking_id)
                ).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("{'message : Error While Fetching Payment by Booking ID'}")