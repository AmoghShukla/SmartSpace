from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from src.model.bookingresource import BookingResource_Class
from src.model.enum import BookingStatus
from src.core.security import AuthSecurity
from src.model.booking import Booking_Class 
from src.schema.booking import BookingCreateResponse, BookingSecondCreate
from src.repository.floor import FloorRepository
from src.repository.booking import BookingRepository 
from src.repository.resource import ResourceRepository
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class BookingService:

    @staticmethod
    def CreateBooking(user, resource_ids, Payload, db):
        try:
            current_user_id = user["user_id"]
            logger.info(f"Creating Booking with Payload {Payload}")
            res = []
            for current_resource_id in resource_ids:
                resource = ResourceRepository.get_resource_by_id(current_resource_id, db)
                floor_id = resource.floor_id
                floor = FloorRepository.GetFloorByFloorID(floor_id, db)
                workspace_id = floor.workspace_id
                new_payload = BookingSecondCreate.model_validate(
                    {**Payload.model_dump(),"user_id":current_user_id, "floor_id" : floor_id, "workspace_id" : workspace_id}
                )
                try:
                    new_booking = Booking_Class(
                        user_id = new_payload.user_id,
                        workspace_id=new_payload.workspace_id,
                        floor_id=new_payload.floor_id,
                        start_time=new_payload.start_time,
                        end_time=new_payload.end_time

                    )
                    outcome = BookingRepository.PreBooking(new_booking, db)
                    res.append(outcome)
                    booking_resource = BookingResource_Class(
                        booking_id = outcome.booking_id,
                        resource_id = current_resource_id
                    )
                    BookingRepository.CreateBooking(booking_resource, db)
                except CustomException.RepositoryError as e:
                    raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
            response = BookingCreateResponse(
                user_id = new_booking.user_id,
                booking_id = outcome.booking_id,
                workspace_id = new_booking.workspace_id,
                floor_id = new_booking.floor_id,
                resource_ids=resource_ids,
                start_time=new_booking.start_time,
                end_time=new_booking.end_time,
                booking_status=BookingStatus.PENDING                
            )
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
    
    @staticmethod
    def GetBookingsByID(user_id, booking_id,  db):
        try:
            return BookingRepository.GetBookingsByID(user_id, booking_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Such Booking Exists : Service") from e
    
    @staticmethod
    def GetBookingsByUserID(user_id, db):
        try:
            return BookingRepository.GetBookingsByUserID(user_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Booking for this user Exists: Service") from e
        
    @staticmethod
    def GetBookingsByResourceID(resource_id, db):
        try:
            return BookingRepository.GetBookingsByUserID(resource_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Booking for this Resource Exists: Service") from e
    
    @staticmethod
    def GetBookingsByWorkspaceID(workspace_id, db):
        try:
            return BookingRepository.GetBookingsByUserID(workspace_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Booking for this Workspace Exists: Service") from e
        
    @staticmethod
    def GetBookingsByFloorID(floor_id, db):
        try:
            return BookingRepository.GetBookingsByFloorID(floor_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Booking for this Floor Exists : Service") from e
    
    @staticmethod
    def GetallBookings(db):
        try:
            return BookingRepository.GetallBookings(db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Booking Exist") from e
        
    @staticmethod
    def approve_booking(booking_id : UUID, updated_by : UUID, db : Session):
        booking = BookingRepository.GetBookingsByID(booking_id, db)
        if not booking:
            raise CustomException.NotFoundError(message = "Booking not found")
        
        if booking.booking_status != BookingStatus.PENDING:
            raise CustomException.BadRequestException( message = "Booking Already Updated")
        
        booking_resources = BookingRepository.get_booking_resource(booking_id, db)
        if not booking_resources:
            raise CustomException.BadRequestException(message = "No Resources Attched to the Following Booking")
        
        for resource in booking_resources:
            overlap = BookingRepository.check_booking_overlap(db, resource_id=resource.resource_id, requested_start=booking.start_time, requested_end=booking.end_time)
            if overlap:
                BookingRepository.reject_booking(rejector_id=updated_by, booking=booking, db=db)
                raise CustomException.BadRequestException(message=f"Resource {booking.resource_id} is already Booked")
            approved_booking = BookingRepository.approve_booking(updated_by, booking, db)
        return {
            'message' : "Booking Approved"
        }



    @staticmethod
    def UpdateBooking(booking_id, updated_booking, db):
        try:
            booking = BookingRepository.GetBookingsByID(booking_id, db)
            return ResourceRepository.UpdateResource(booking, updated_booking, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Updating Booking") from e
    
    @staticmethod
    def Cancel_Booking(booking_id, db):
        try:
            booking = BookingRepository.GetBookingsByID(booking_id, db)
            if not booking:
                raise CustomException.ServiceError("No Such Booking Exists")
            booking.booking_status = "CANCELLED"
            BookingRepository.Cancel_Booking(booking, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error while cancelling the booking ") from e

    @staticmethod
    def Hard_Delete_Booking(booking_id, db):
        try:
            booking = BookingRepository.GetBookingsByID(booking_id, db)
            if not booking:
                raise CustomException.ServiceError("No Such Booking Exists")
            return BookingRepository.Hard_Delete_Booking(booking, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error while deleting the Booking with booking_id {booking.booking_id}") from e