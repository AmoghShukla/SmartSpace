from datetime import UTC, datetime

from sqlalchemy.orm import Relationship

from src.database.Base import base
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID
from src.model.enum import UserRole


class Floor_Class(base):
    __tablename__ = "Floor_Table"

    floor_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    floor_number = Column(Integer, nullable=False, index=True)
    workspace_id = Column(UUID, ForeignKey('Workspace_Table.workspace_id'))
    is_available = Column(Boolean, default=True)
    floor_meeting_room_capacity = Column(Integer, default=7, server_default="7")
    floor_auditorium_capacity = Column(Integer, default=3, server_default="3")
