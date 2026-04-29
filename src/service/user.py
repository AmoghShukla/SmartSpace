from fastapi import Depends
from sqlalchemy.orm import Session

from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user

class UserService:

    @staticmethod
    def CreateUser(Payload, db):
        try:
            UserRepository.CreateUser(Payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating user wit payload {Payload}") from e
    
    @staticmethod
    def GetMyProfile(user_id, db: Session):
        try:
            return UserRepository.GetMyProfile(user_id, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching User Profile!!!") from e

    @staticmethod
    def GetUserByEmail(user_email, db: Session):
        try:
            return UserRepository.GetUserByEmail(user_email, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching User!!!") from e

    @staticmethod
    def GetUserByRole(user_role, db: Session):
        try:
            return UserRepository.GetUserByRole(user_role, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users with the given role!!!") from e

    @staticmethod
    def GetAllUsers(db: Session):
        try:
            return UserRepository.GetAllUser(db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users") from e
