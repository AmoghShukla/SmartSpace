from sqlalchemy.orm import Session

from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException

class UserService:

    @staticmethod
    def CreateUser(Payload, db):
        try:
            UserRepository.CreateUser(Payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating user wit payload {Payload}") from e
    
    @staticmethod
    def GetUserByEmail(user_email, db: Session):
        try:
            UserRepository.GetUserByEmail(user_email, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching User!!!") from e

    @staticmethod
    def GetUserByRole(user_role, db: Session):
        try:
            UserRepository.GetUserByRole(user_role, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users with the given role!!!") from e

    @staticmethod
    def GetAllUsers(db: Session):
        try:
            UserRepository.GetAllUser(db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users") from e
