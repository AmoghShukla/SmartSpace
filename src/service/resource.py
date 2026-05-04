from datetime import UTC, time
from uuid import UUID

from src.repository.workspace import WorkspaceRepository
from src.repository.floor import FloorRepository
from src.Exceptions.Custom_Exception import CustomException
from src.model.enum import ResourceType

class ResourceService:

    @staticmethod
    def CreateResource(payload, db):
        if payload.
        