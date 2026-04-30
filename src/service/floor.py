from uuid import UUID

from src.repository.workspace import WorkspaceRepository
from src.repository.floor import FloorRepository
from src.Exceptions.Custom_Exception import CustomException

class FloorService:

    @staticmethod
    def CreateFloor(workspace_id : UUID, db):
        try:
            current_floor = FloorRepository.current_floor(workspace_id, db) + 1        
            return WorkspaceRepository.CreateWorkspace(workspace_id, current_floor, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Creating Workspace") from e
    
    @staticmethod
    def GetAllFloorsByWorkspaceID(workspace_id , db):
        try:
            return FloorRepository.GetallFloorsByWorkspaceID(workspace_id, db)
        except CustomException.RepositoryError() as e:
            raise CustomException.ServiceError(f"Error While Fetching all the Floors of workspace Id : {workspace_id}") from e
    
    @staticmethod
    def GetAllFloors(db):
        try:
            return FloorRepository.GetallFloors(db)
        except CustomException.RepositoryError() as e:
            raise CustomException.ServiceError("Error While Fetching all the Floors") from e
