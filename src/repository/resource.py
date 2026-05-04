from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import UUID, func, select

from src.model.resource import Resource_Class
from src.Exceptions.Custom_Exception import CustomException
from src.utils.loggers import get_logger

logger = get_logger(__name__)

class ResourceRepository:

    @staticmethod
    def CreateResource(payload : Resource_Class, db):
        try:            
            db.add(payload)
            db.commit()
            db.refresh(payload)
            return payload
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("Error while Creating Resource : Repository") from e
    
    @staticmethod
    def GetallAvailableResourcesByFloorID(floor_id,  db):
        try:
            return db.execute(select(Resource_Class).where(Resource_Class.floor_id==floor_id and Resource_Class.is_avaialable == True)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Resource Exists") from e
    
    @staticmethod
    def GetallResource(db):
        try:
            return db.execute(select(Resource_Class).where(Resource_Class.is_deleted == False)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e

    @staticmethod
    def Resource_Availability(floor_id, resource_type, db):
        try:
            return db.execute(select(Resource_Class).where(Resource_Class.floor_id == floor_id , Resource_Class.resource_type == resource_type, Resource_Class.is_avaialable == True)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e

    @staticmethod
    def get_resource_by_id(resource_id, db):
        try:
            return db.execute(select(Resource_Class).where(Resource_Class.resource_id == resource_id , Resource_Class.is_deleted == False)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e
        

    @staticmethod
    def get_resource_by_floorID(floor_id, db):
        try:
            return db.execute(select(Resource_Class).where(Resource_Class.floor_id == floor_id , Resource_Class.is_deleted == False)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the Resources") from e
    
    @staticmethod
    def soft_delete_resource_by_ID(resource_id, db):
        try:
            db.commit()
            db.refresh()
            return "Resource Deleted Successfully!!!"
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Error while deleting the Resource with resource_id {resource_id}") from e

    @staticmethod
    def hard_delete_resource_by_ID(resource, db):
        try:
            db.delete(resource)
            db.commit()
            db.refresh()
            return "Resource Deleted Successfully!!!"
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Error while deleting the Resource with resource_id {resource_id}") from e

