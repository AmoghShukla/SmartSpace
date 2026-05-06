from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.bookingresource import BookingResource_Class
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
    def PreBooking(payload, db):
        db.add(payload)
        db.flush()
        return payload
  
    @staticmethod
    def GetBookingsByID(user_id, booking_id,  db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.booking_id==booking_id, Booking_Class.user_id==user_id)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Booking Exists") from e
    
    @staticmethod
    def GetBookingsByBookingID(booking_id,  db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.booking_id==booking_id)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Booking Exists") from e

    @staticmethod
    def GetBookingsByUserID(user_id, db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.user_id==user_id)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this user Exists") from e
        
    @staticmethod
    def GetBookingsByResourceID(resource_id, db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.resource_id==resource_id)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this Resource Exists") from e
    
    @staticmethod
    def GetBookingsByWorkspaceID(workspace_id, db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.workspace_id==workspace_id)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this Workspace Exists") from e
        
    @staticmethod
    def GetBookingsByFloorID(floor_id, db):
        try:
            return db.execute(select(Booking_Class).where(Booking_Class.floor_id==floor_id)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this Floor Exists") from e
    
    @staticmethod
    def GetallBookings(db):
        try:
            return db.execute(select(Booking_Class)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Booking for this Exist") from e

    @staticmethod
    def check_booking_overlap(resource_id, requested_start, requested_end, db):
        try:
            return db.execute(select(Booking_Class).join(BookingResource_Class).where(BookingResource_Class.resource_id==resource_id, Booking_Class.booking_status=="APPROVED", Booking_Class.start_time < requested_end, Booking_Class.end_time > requested_start)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError('Error : Repo')
        
    @staticmethod
    def approve_booking(approver_id, booking, db):
        booking.booking_status = BookingStatus.APPROVED
        booking.updated_by = approver_id

        db.commit()
        db.refresh(booking)

        return booking
    
    @staticmethod
    def reject_booking(rejector_id, booking, db):
        booking.booking_status = BookingStatus.REJECTED
        booking.updated_by = rejector_id

        db.commit()
        db.refresh(booking)
        
        return booking
    
    @staticmethod
    def get_booking_resource(booking_id, db):
        try:
            return db.execute(select(BookingResource_Class).where(BookingResource_Class.booking_id==booking_id)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(message = "Error while Fetching the Resources of a booking")
    @staticmethod
    def UpdateBooking(booking, updated_booking, db):
        try:
            update_dict = updated_booking.model_dump(exclude_none = True)

            for key,value in update_dict.items():
                setattr(booking,key,value)
            db.commit()
            db.refresh(booking)
            return booking

        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("Error While Updating Booking") from e
    
    @staticmethod
    def Cancel_Booking(booking, db):
        try:
            db.commit()
            db.refresh()
            return "Booking Cancelled Successfully!!!"
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Error while cancelling the booking ") from e

    @staticmethod
    def Hard_Delete_Booking(booking, db):
        try:
            db.delete(booking)
            db.commit()
            db.refresh()
            return "Booking Deleted Successfully!!!"
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Error while deleting the Booking with booking_id {booking.booking_id}") from e