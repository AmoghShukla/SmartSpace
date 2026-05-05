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
    def CreateBooking(Payload, db):
        try:
            logger.info(f"Creating Booking with Payload {Payload}")
            res = []
            for resource in Payload.resource_id:
                resource = ResourceRepository.get_resource_by_id(Payload.resource_id, db)
                floor_id = resource.floor_id
                floor = FloorRepository.GetFloorByFloorID(floor_id, db)
                workspace_id = floor.workspace_id
                new_payload = BookingSecondCreate.model_validate(
                    {**Payload.model_dump(), "floor_id" : floor_id, "workspace_id" : workspace_id}
                )
                try:
                    outcome = BookingRepository.CreateBooking(Payload, db)
                    res.append(outcome)
                except CustomException.RepositoryError as e:
                    raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
            return res
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating booking with payload {Payload}") from e
 