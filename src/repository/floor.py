from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import UUID, func, select

from src.model.floor import Floor_Class
from src.Exceptions.Custom_Exception import CustomException
from src.utils.loggers import get_logger

logger = get_logger(__name__)

class FloorRepository:

    @staticmethod
    def CreateFloor(payload : UUID, db):
        try:            
            db.add(payload)
            db.commit()
            db.refresh(payload)
            return payload
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("Error while Creating Floor : Repository") from e
    
    @staticmethod
    def current_floor(workspace_id, db):
        floors = select(func.count()).where(Floor_Class.workspace_id == workspace_id)
        count = db.execute(floors).scalar()
        return count


    @staticmethod
    def GetallFloorsByWorkspaceID(workspace_id, db):
        try:
            return db.execute(select(Floor_Class).where(Floor_Class.workspace_id==workspace_id, Floor_Class.is_available == True)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Floor Exists") from e
        
    @staticmethod
    def GetFloorByFloorID(floor_id, db):
        try:
            return db.execute(select(Floor_Class).where(Floor_Class.floor_id==floor_id and Floor_Class.is_available == True)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Floor Exists") from e
        
    @staticmethod
    def GetallFloors(db):
        try:
            return db.execute(select(Floor_Class).where(Floor_Class.is_available == True)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the floors") from e

    @staticmethod
    def SoftDeleteWorkspace(floor_id, db):
        try:
            current_floor = db.execute(select(Floor_Class).where(Floor_Class.floor_id==floor_id and Floor_Class.is_available == True)).scalars().first()
            if not current_floor:
                raise SQLAlchemyError("Floor is not Available to use!!!")
            
            Floor_Class.is_available = False
            db.commit()
            return {
                "message" : "Floor Unavailable now!!!" 
            }
        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("Floor Unavailable to use") from e
        
    
    @staticmethod
    def UpdateFloor(floor, updated_floor, db):
        try:
            update_dict = updated_floor.model_dump(exclude_unset = True)

            for key,value in update_dict.items():
                setattr(floor,key,value)
            db.commit()
            db.refresh(floor)
            return floor

        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("Error While Updating Floor") from e
