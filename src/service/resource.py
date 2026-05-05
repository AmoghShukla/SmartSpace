from datetime import UTC, time
from uuid import UUID

from src.schema.resource import ResourceCreateSecond
from src.repository.resource import ResourceRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import ResourceType


class ResourceService:

    @staticmethod
    def CreateResource(payload, db):
        try:
            total_available_capacity = payload.total_resource_capacity
            new_payload = ResourceCreateSecond.model_validate(
                {**payload.model_dump(),"available_resource_capacity": total_available_capacity}
                )
            resource_capacity = ResourceRepository.Capacity_Availability(new_payload.floor_id, payload.resource_type, db)
            if not resource_capacity:
                raise CustomException.ServiceError("Capacity Unavailable")
            return ResourceRepository.CreateResource(new_payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Creating Resource") from e
  
    @staticmethod
    def GetallAvailableResourcesByFloorID(floor_id,  db):
        try:
            return ResourceRepository.GetallAvailableResourcesByFloorID(floor_id, db)
        except CustomException.ServiceError as e:
            raise CustomException.RepositoryError("Error While Getting Resource") from e

    @staticmethod
    def GetallResource(db):
        try:
            return ResourceRepository.GetallResource(db)
        except CustomException.RepositoryError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e
        
    @staticmethod
    def GetResourceByID(resource_id, db):
        try:
            return ResourceRepository.get_resource_by_id(resource_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.RepositoryError(f"Eror while fetching the Resources By id {resource_id}") from e
        
    @staticmethod
    def UpdateResource(resource_id, updated_resource, db):
        try:
            resource = ResourceRepository.get_resource_by_id(resource_id)
            return ResourceRepository.UpdateResource(resource, updated_resource, db)
        except CustomException.RepositoryError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e
        
    @staticmethod
    def soft_delete_resource_by_ID(resource_id, db):
        try:
            current_resource = ResourceRepository.get_resource_by_id(resource_id)
            if not current_resource:
                raise CustomException.ServiceError("No Such Resource Exists")
            
            current_resource.is_deleted = True
            db.commit()
            return {
                "message" : "Resource Deleted Successfully!!!" 
            }
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Such Resource Exists") from e
    
    @staticmethod
    def hard_delete_resource_by_ID(resource_id, db):
        try:
            current_resource = ResourceRepository.get_resource_by_id(resource_id)
            if not current_resource:
                raise CustomException.ServiceError("No Such Resource Exists")
    
            return ResourceRepository.hard_delete_resource_by_ID(current_resource, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("No Such Resource Exists") from e