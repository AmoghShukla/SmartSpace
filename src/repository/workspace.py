from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.floor import Floor_Class
from src.model.enum import UserRole
from src.model.workspace import Workspace_Class
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class WorkspaceRepository:

    @staticmethod
    def CreateWorkspace(payload, current_floor , db):
        try:
            new_floor = Floor_Class(
                floor_number = current_floor,
                workspace_id = payload.workspace_id,
                floor_meeting_room_capacity = payload.floor_meeting_room_capacity,
                floor_auditorium_capacity = payload.floor_auditorium_capacity
            )
            db.add(new_floor)
            db.commit()
            db.refresh(new_floor)
            return new_floor
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("Error while Creating Floor : Repository") from e

    @staticmethod
    def GetWorkspaceByName(workspace_name, db):
        try:
            return db.execute(select(Workspace_Class).where(Workspace_Class.workspace_name==workspace_name and Workspace_Class.is_deleted == False)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Workspace Exists") from e
    
    @staticmethod
    def GetWorkspaceByID(workspace_id, db):
        try:
            return db.execute(select(Workspace_Class).where(Workspace_Class.workspace_id==workspace_id and Workspace_Class.is_deleted == False)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError("No Such Workspace Exists") from e
    
    @staticmethod
    def GetWorkspaceByLocation(workspace_location, db):
        try:
            return db.execute(select(Workspace_Class).where(Workspace_Class.workspace_location==workspace_location and Workspace_Class.is_deleted == False)).scalars().first()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"No Such Workspace Exists at this location : {workspace_location}") from e
    
    @staticmethod
    def GetallWorkspaces(db):
        try:
            return db.execute(select(Workspace_Class).where(Workspace_Class.is_deleted == False)).scalars().all()
        except SQLAlchemyError as e:
            raise CustomException.RepositoryError(f"Eror while fetching all the workspaces ") from e


    @staticmethod
    def SoftDeleteWorkspace(workspace_id, db):
        try:
            Current_Workspace = db.execute(select(Workspace_Class).where(Workspace_Class.workspace_id==workspace_id and Workspace_Class.is_deleted == False)).scalars().first()
            if not Current_Workspace:
                raise SQLAlchemyError("No Such Workspace Exists")
            
            Current_Workspace.is_deleted = True
            db.commit()
            return {
                "message" : "Workspace Deleted Successfully!!!" 
            }
        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("No Such Workspace Exists") from e
    
    @staticmethod
    def HardDeleteWorkspace(workspace_id, db):
        try:
            Current_Workspace = db.execute(select(Workspace_Class).where(Workspace_Class.workspace_id==workspace_id)).scalars().first()
            if not Current_Workspace:
                raise SQLAlchemyError("No Such Workspace Exists")
            
            db.delete(Current_Workspace)
            db.commit()
            return {
                "message" : "Workspace Deleted Successfully!!!" 
            }
        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("No Such Workspace Exists") from e