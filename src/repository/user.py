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
                logger.debug("User Already Exists!!")
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
    def GetUserByEmail(user_email, db):
        record = db.execute(select(User_Class).where(User_Class.user_email==user_email)).scalars().first()
        return record
    
    @staticmethod
    def GetUserByRole(user_role, db):
        return db.execute(select(User_Class).where(User_Class.user_role==user_role)).scalars().first()
    
    @staticmethod
    def GetAllUser(db):
        return db.execute(select(User_Class)).scalars().all()