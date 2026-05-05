from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import UUID, func, select

from src.model.floor import Floor_Class
from src.model.resource import Resource_Class
from src.Exceptions.Custom_Exception import CustomException
from src.utils.loggers import get_logger

logger = get_logger(__name__)

class ResourceRepository:

    @staticmethod
    def CreateResource(payload, db):
        try:            
            db.add(payload)
            db.commit()
            db.refresh(payload)
            return payload
        except SQLAlchemyError as e:
            print(e)
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
    def Capacity_Availability(floor_id, resource_type, db):
        try:
            floor = db.execute(select(Floor_Class).where(Floor_Class.floor_id == floor_id)).scalar_one_or_none()

            if not floor:
                raise SQLAlchemyError("Floor not Found!!")

            if resource_type.value == "MEETING_ROOM":
                if floor.available_floor_meeting_room_capacity > 0:
                    floor.available_floor_meeting_room_capacity -= 1
                    db.commit()
                    return floor
            elif resource_type.value == "AUDITORIUM":
                if floor.avaialable_floor_auditorium_capacity > 0:
                    floor.avaialable_floor_auditorium_capacity -= 1
                    db.commit()
                    return floor
            
            return None
        except SQLAlchemyError as e:
            db.rollback() 
            raise CustomException.RepositoryError("Error while updating capacity") from e
    
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
    def UpdateResource(resource, updated_resource, db):
        try:
            update_dict = updated_resource.model_dump(exclude_unset = True)

            for key,value in update_dict.items():
                setattr(resource,key,value)
            db.commit()
            db.refresh(resource)
            return resource

        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("Error While Updating Floor") from e

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
            raise CustomException.RepositoryError(f"Error while deleting the Resource with resource_id {resource.resource_id}") from e

