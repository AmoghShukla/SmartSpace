from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.enum import UserRole
from src.model import User_Class
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class PromotionsRepository:

    @staticmethod
    def promote(payload, db):
        try:
            logger.info("Repo : Promoting User")
            db.add(payload)
            db.commit()
            db.refresh(payload)
            logger.info("Repo : User Promoted")
            return payload
        except SQLAlchemyError as e:
            logger.error("Error While Promoting user")
            db.rollback()
            raise CustomException.RepositoryError("Error While Promoting User!!") from e
        