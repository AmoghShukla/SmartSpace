from datetime import UTC, datetime

from sqlalchemy.orm import Relationship

from src.database.Base import base
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID
from src.model.enum import UserRole


class Workspace_Class(base):
    __tablename__="Workspace_Table"

    workspace_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    workspace_name = Column(String, nullable=False, unique=True)
    workspace_location = Column(String, nullable=False, index=True)
    workspace_manager_id = Column(UUID, ForeignKey('User_Table.user_id'))
    workspace_floor_capacity = Column(Integer, default=10, server_default="10")
    created_at = Column(String, default=datetime.now(UTC))
    is_deleted = Column(Boolean, default=False)

    user = Relationship('User_Class', back_populates='workspace')
    booking = Relationship('Booking_Class', back_populates='workspace',cascade="all, delete-orphan")
    floor = Relationship('Floor_Class', back_populates="workspace",cascade="all, delete-orphan")
