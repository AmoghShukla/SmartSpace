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
    workspace_id = Column(UUID, ForeignKey('Workspace_Table.workspace_id', ondelete="CASCADE"))
    is_available = Column(Boolean, default=True)
    total_floor_meeting_room_capacity = Column(Integer, default=7, server_default="7")
    available_floor_meeting_room_capacity = Column(Integer, default=7, server_default="7")
    total_floor_auditorium_capacity = Column(Integer, default=7, server_default="7")
    avaialable_floor_auditorium_capacity = Column(Integer, default=3, server_default="3")

    resource = Relationship("Resource_Class", back_populates="floor",cascade="all, delete-orphan")
    booking = Relationship("Booking_Class", back_populates="floor")
    workspace = Relationship('Workspace_Class', back_populates="floor")
    
