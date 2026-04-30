from uuid import UUID

from src.repository.workspace import WorkspaceRepository
from src.repository.floor import FloorRepository
from src.Exceptions.Custom_Exception import CustomException

class WorkspaceService:

    @staticmethod
    def CreateFloor(workspace_id : UUID, db):
        try:
            current_floor = FloorRepository.current_floor(workspace_id, db) + 1        
            return WorkspaceRepository.CreateWorkspace(workspace_id, current_floor, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Creating Workspace") from e
        
    