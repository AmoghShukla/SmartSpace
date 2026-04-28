from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import UserRole
from src.model import User_Class

class AuthService:

    @staticmethod
    def RegisterUser(payload, db):
        user = UserRepository.GetUserByEmail(payload.user_email, db)

        if user:
            raise CustomException.ServiceError("User Already Exists!!")
        
        role = UserRole.USER if payload.user_role is None else payload.user_role
        
        # password

        new_user = User_Class(
            user_name = payload.user_name,
            # user
        )