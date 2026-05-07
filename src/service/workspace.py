from src.repository.workspace import WorkspaceRepository
from src.Exceptions.Custom_Exception import CustomException

class WorkspaceService:

    @staticmethod
    def CreateWorkspace(payload, db):
        try:
            exists = WorkspaceRepository.GetWorkspaceByName(payload.workspace_name, db)
            if exists:
                raise CustomException.ServiceError("Workspace Already Exists")
            return WorkspaceRepository.CreateWorkspace(payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Creating Workspace") from e
        
    
    @staticmethod
    def GetWorkspaceByName(workspace_name, db):
        try:
            return WorkspaceRepository.GetWorkspaceByName(workspace_name, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Workspace") from e

    @staticmethod
    def GetWorkspaceByID(workspace_id, db):
        try:
            return WorkspaceRepository.GetWorkspaceByID(workspace_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Workspace") from e

    @staticmethod
    def GetWorkspaceByLocation(workspace_location, db):
        try:
            return WorkspaceRepository.GetWorkspaceByLocation(workspace_location, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Workspace") from e
    
    @staticmethod
    def GetAllWorkspaces(page_no,db):
        try:
            return WorkspaceRepository.GetallWorkspaces(page_no,db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Workspaces") from e
    
    @staticmethod
    def SoftDeleteWorkspace(workspace_id, db):
        try:
            return WorkspaceRepository.SoftDeleteWorkspace(workspace_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error While Deleteing Workspace with id : {workspace_id}") from e

    @staticmethod
    def HardDeleteWorkspace(workspace_id, db):
        try:
            return WorkspaceRepository.HardDeleteWorkspace(workspace_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error While Deleteing Workspace with id : {workspace_id}") from e
