from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.security import AuthSecurity
from src.model.booking import Booking_Class 
from src.schema.booking import BookingSecondCreate
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
                    {**Payload.model_dump(),"user_id":current_user_id,"resource_id" : current_resource_id, "floor_id" : floor_id, "workspace_id" : workspace_id}
                )
                try:
                    new_booking = Booking_Class(
                        user_id = new_payload.user_id,
                        workspace_id=new_payload.workspace_id,
                        floor_id=new_payload.floor_id,
                        booking_date=new_payload.booking_date,
                        resource_id=new_payload.resource_id,
                        start_time=new_payload.start_time,
                        end_time=new_payload.end_time,
                    )
                    outcome = BookingRepository.CreateBooking(new_booking, db)
                    res.append(outcome)
                except CustomException.RepositoryError as e:
                    raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
            return res
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
 