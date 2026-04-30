from datetime import UTC, datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from src.model.enum import UserRole
from src.model import workspace
from src.Exceptions.Custom_Exception import CustomException

from src.utils.loggers import get_logger

logger = get_logger(__name__)

class WorkspaceRepository:

    @staticmethod
    def CreateWorkspace(payload, db):
        pass