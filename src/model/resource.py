from datetime import UTC, date, time

from sqlalchemy.orm import Relationship

from src.database.Base import base
from uuid import uuid4
from sqlalchemy import CheckConstraint, Boolean, Column, ForeignKey, Integer, String, Time, UUID, Enum as SQLAlchemyEnum
from src.model.enum import ResourceType


class Resource_Class(base):
    __tablename__ = "Resource_Table"

    resource_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    resource_type = Column(SQLAlchemyEnum(ResourceType))
    total_resource_capacity = Column(Integer, nullable=False)
    available_resource_capacity = Column(Integer, nullable=False)
    requires_approval = Column(Boolean, default=True)
    open_time = Column(Time, nullable=False, default=time(6, 30), server_default="06:30:00")
    close_time = Column(Time, nullable=False, default=time(22, 30), server_default="22:30:00")
    is_deleted = Column(Boolean, default=False)
    floor_id = Column(UUID, ForeignKey('Floor_Table.floor_id'))

    booking = Relationship('BookingResource_Class', back_populates="resource")
    floor = Relationship('Floor_Class', back_populates='resource')

    __table_args__ = (CheckConstraint("total_resource_capacity > 0", name = "check_capacity_positive"),)
    
    