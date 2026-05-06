from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.enum import UserRole
from src.model import User_Class
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class UserRepository:

    @staticmethod
    def CreateUser(payload, db):
        try:
            user = UserRepository.GetUserByEmail(payload.user_email, db)
            if user:
                logger.info("User Already Exists!!")
                raise SQLAlchemyError("User Already Exists!!")
            
            if isinstance(payload, User_Class):
                new_user = payload
                if new_user.user_role is None:
                    new_user.user_role = UserRole.USER
            else:
                role = payload.user_role if hasattr(payload, "user_role") and payload.user_role is not None else UserRole.USER
                new_user = User_Class(
                    user_name = payload.user_name,
                    user_email = payload.user_email,
                    user_password = payload.user_password,
                    user_contact_no = payload.user_contact_no,
                    user_role = role
                )
            logger.info(f"Creating User with payload : {payload}")
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            logger.info(f"User Created with payload : {payload}")
            return payload
        except SQLAlchemyError as e:
            db.rollback()
            logger.error("Error while creating User!!")
            raise CustomException.RepositoryError("Error Creating User : Repo") from e

    @staticmethod
    def GetMyProfile(user_id, db):
        try:
            logger.info(f"Fetching User Profile : {user_id}")
            return db.execute(select(User_Class).where(User_Class.user_id==user_id)).scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Error while Fetching User Profile : {user_id}")
            raise CustomException.RepositoryError("Error While Fetching user profile") from e
    

    @staticmethod
    def GetUserByEmail(user_email, db):
        try:
            logger.info(f"Fetching User with email : {user_email}")
            return db.execute(select(User_Class).where(User_Class.user_email==user_email)).scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Error while Fetching User Email : {user_email} {e}")
            raise CustomException.RepositoryError("Error While Fetching user using the Given Email") from e
    
    @staticmethod
    def GetCurrentUserByEmail(user_email, db):
        try:
            logger.info(f"Fetching User with email : {user_email}")
            return db.execute(select(User_Class).where(User_Class.user_email==user_email)).scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Error while Fetching User Email : {user_email} {e}")
            raise CustomException.RepositoryError("Error While Fetching user using the Given Email") from e
    
    @staticmethod
    def GetUserByRole(user_role, db):
        try:
            logger.info(f"Fetching User By Role : {user_role}")
            return db.execute(select(User_Class).where(User_Class.user_role==user_role)).scalars().first()
        except SQLAlchemyError as e:
            logger.error(f"Error while Fetching User By Role : {user_role}")
            raise CustomException.RepositoryError("Error While Fetching user using the Given Role") from e

    @staticmethod
    def GetAllUser(db):
        try:
            logger.error(f"Fetching all Users")
            return db.execute(select(User_Class)).scalars().all()
        except SQLAlchemyError as e:
            logger.error(f"Error while Fetching all Users")
            raise CustomException.RepositoryError("Error While Fetching All Users") from e
        
    @staticmethod
    def UpdateUser(user, updated_user, db):
        try:
            update_dict = updated_user.model_dump(exclude_none = True)

            for key,value in update_dict.items():
                setattr(user,key,value)
            user.updated_at = datetime.now(UTC)
            db.commit()
            db.refresh(user)
            return user

        except SQLAlchemyError as e:
            db.rollback()
            raise CustomException.RepositoryError("Error While Updating User") from e