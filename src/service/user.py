from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.security import AuthSecurity
from src.model.user import User_Class
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
    def GetUserByRole(page_no, user_role, db: Session):
        try:
            return UserRepository.GetUserByRole(page_no, user_role, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users with the given role!!!") from e

    @staticmethod
    def GetAllUsers(page_no, db: Session):
        try:
            return UserRepository.GetAllUser(page_no, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Fetching Users") from e


    @staticmethod
    def UpdateUser(user, payload, db: Session):
        try:
            return UserRepository.UpdateUser(user, payload, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError("Error While Updating User") from e
