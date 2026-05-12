from datetime import UTC, time
from uuid import UUID

from src.schema.resource import ResourceCreateSecond, ResourceResponse
from src.repository.resource import ResourceRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import ResourceType
from src.model.resource import Resource_Class


class ResourceService:

    @staticmethod
    def CreateResource(payload, db):
        try:
            total_available_capacity = payload.total_resource_capacity
            new_payload = ResourceCreateSecond.model_validate(
                {**payload.model_dump(),"available_resource_capacity": total_available_capacity}
                )
            floor_capacity = ResourceRepository.Capacity_Availability(new_payload.floor_id, payload.resource_type, db)
            if not floor_capacity:
                raise CustomException.ServiceError("Capacity Unavailable")
            resource_obj = Resource_Class(
                resource_type=new_payload.resource_type,
                total_resource_capacity=new_payload.total_resource_capacity,
                available_resource_capacity=new_payload.available_resource_capacity,
                price_per_booking = new_payload.price_per_booking,
                requires_approval=new_payload.requires_approval,
                open_time=new_payload.open_time,
                close_time=new_payload.close_time,
                floor_id=new_payload.floor_id,
            )
            return ResourceRepository.CreateResource(resource_obj, db)
        except CustomException.RepositoryError as e:
            print(e)
            raise CustomException.ServiceError("Error While Creating Resource : Service") from e
  
    @staticmethod
    def Change_Resource_Costing(resource_id, new_price, db):
        try:
            resource = ResourceRepository.get_resource_by_id(resource_id, db)
            if not resource:
                raise CustomException.ServiceError("Resource not found")

            update_dict = new_price.model_dump()

            for key,value in update_dict.items():
                setattr(resource,key,value) 
            return ResourceRepository.Change_Resource_Costing(resource, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(e) from e

    @staticmethod
    def GetallAvailableResourcesByFloorID(page_no, floor_id,  db):
        try:
            return ResourceRepository.GetallAvailableResourcesByFloorID(page_no, floor_id, db)
        except CustomException.ServiceError as e:
            raise CustomException.RepositoryError("Error While Getting Resource") from e

    @staticmethod
    def GetallAvailableResourcesByWorkspaceID(page_no, workspace_id,  db):
        try:
            return ResourceRepository.GetallAvailableResourcesByWorkspaceID(page_no, workspace_id, db)
        except CustomException.ServiceError as e:
            raise CustomException.RepositoryError(message = "Error While Getting Resources by workspace id")
    
    @staticmethod
    def GetallResource(page_no, db):
        try:
            return ResourceRepository.GetallResource(page_no, db)
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
            resource = ResourceRepository.get_resource_by_id(resource_id, db)
            return ResourceRepository.UpdateResource(resource, updated_resource, db)
        except CustomException.RepositoryError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e
        
    @staticmethod
    def soft_delete_resource_by_ID(resource_id, db):
        try:
            current_resource = ResourceRepository.get_resource_by_id(resource_id, db)
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