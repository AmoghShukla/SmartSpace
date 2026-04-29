from fastapi import HTTPException

from src.repository.user import UserRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import UserRole
from src.model import User_Class
from src.core.security import AuthSecurity
from src.repository.user import UserRepository

class AuthService:

    @staticmethod
    def RegisterUser(payload, db):
        try:
            user = UserRepository.GetUserByEmail(payload.user_email, db)

            if user:
                raise CustomException.ServiceError("User Already Exists!!")
            
            if not hasattr(payload, "user_role"):
                role = UserRole.USER.value
            else:
                role = (payload.user_role.value if isinstance(payload.user_role, UserRole) else payload.user_role)
            
            password = AuthSecurity.hash_password(payload.user_password)

            new_user = User_Class(
                user_name = payload.user_name,
                user_email = payload.user_email,
                user_password = password,
                user_contact_no = payload.user_contact_no,
                user_role = role
            )

            return UserRepository.CreateUser(new_user, db)
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError from e
    
    @staticmethod
    def login_user(payload, db):
        try:
            user = UserRepository.GetUserByEmail(payload.username, db)

            if not user:
                raise HTTPException(status_code=404, detail="User does not exist, please signup")
            
            if not AuthSecurity.verify_password(payload.password, user.user_password):
                raise HTTPException(status_code=404, detail="Password Does Not Match!!!")
            
            role = payload.user_role.value if hasattr(user.user_role, 'value') else str(user.user_role)

            access_token = AuthSecurity.create_access_token({
                'sub' : str(user.user_id),
                'user_role' : role,
                'token_type': 'access_token'
            })

            refresh_token = AuthSecurity.create_refresh_token({
                'sub' : str(user.user_id),
                'user_role' : role,
                'token_type': 'refresh_token'

            })

            return {
                'access_token' : access_token,
                'refresh_token' : refresh_token,
                'token_type' : 'Bearer'
            }
        except CustomException.RepositoryError as e:
            raise CustomException.ServiceError from e