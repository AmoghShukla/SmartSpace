from datetime import UTC, time
from uuid import UUID

from src.repository.resource import ResourceRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import ResourceType


class ResourceService:

    @staticmethod
    def CreateResource(payload, db):
        try:
            resource_capacity = ResourceRepository.Resource_Availability(payload.floor_id, payload.resource_type, db)
            if resource_capacity:
                return ResourceRepository.CreateResource(payload, db)
        except CustomException.ServiceError as e:
            raise CustomException.RepositoryError("Error While Creating Resource") from e

        