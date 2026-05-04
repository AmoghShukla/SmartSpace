from uuid import UUID

from src.repository.workspace import WorkspaceRepository
from src.repository.floor import FloorRepository
from src.Exceptions.Custom_Exception import CustomException
from src.schema.resource import ResourceCreate

class FloorService:

    @staticmethod
    def CreateFloor(payload : ResourceCreate, db):
        try:
            current_floor = FloorRepository.current_floor(payload.workspace_id, db) + 1        
            return FloorRepository.CreateFloor(payload, current_floor, db)
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
    
    @staticmethod
    def GetFloorByFloorID(floor_id, db):
        try:
            return FloorRepository.GetFloorByFloorID(floor_id, db)
        except CustomException.RepositoryError() as e:
            raise CustomException.ServiceError("Error While Fetching all the Floors") from e
    
    @staticmethod
    def MakeFloorUnavailable(floor_id, db):
        try:
            exists = FloorRepository.GetFloorByFloorID(floor_id, db)
            if not exists:
                raise CustomException.ServiceError("No Such Floor Found") from e
            return FloorRepository.SoftDeleteWorkspace(floor_id, db)

        except CustomException.RepositoryError as e:
            raise CustomException.RepositoryError("Floor Unavailable to use : Service Layer") from e