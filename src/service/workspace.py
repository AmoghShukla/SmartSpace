from src.repository.workspace import WorkspaceRepository
from src.Exceptions.Custom_Exception import CustomException

class WorkspaceService:

    @staticmethod
    def CreateWorkspace(payload, db):
        try:
            return WorkspaceRepository.CreateWorkspace(payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Creating Workspace") from e
        