from sqlalchemy.orm import Session
from src.repository.promotions import PromotionsRepository
from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException

class PromotionsService:

    @staticmethod
    def MakeMember(user_email, db):
        try:
            user = UserRepository.GetUserByEmail(user_email, db)

            if user.user_role == "USER":
                user.user_role = "MEMBER"
            
            return PromotionsRepository.promote(user, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating user wit payload {user}") from e
        
    @staticmethod
    def MakeAdmin(user_email, db):
        try:
            user = UserRepository.GetUserByEmail(user_email, db)

            if not user:
                raise CustomException.ServiceError("User Does Not Exists")

            if user.user_role != "ADMIN":
                user.user_role = "ADMIN"
            else:
                raise CustomException.ServiceError("User is Already an Admin!!")
            
            return PromotionsRepository.promote(user, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while creating user wit payload {user}") from e
        
    @staticmethod
    def MakeUser(user_email, db):
        try:
            user = UserRepository.GetUserByEmail(user_email, db)

            if not user:
                raise CustomException.ServiceError("User Does Not Exists")

            if not user.user_role == "USER":
                user.user_role = "USER"
            else:
                raise CustomException.ServiceError("Already an USER!!")
            
            return PromotionsRepository.promote(user, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError(f"Error Encountered while making user :  {user}") from e
        