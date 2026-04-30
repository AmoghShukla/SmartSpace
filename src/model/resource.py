from datetime import UTC, datetime

from sqlalchemy.orm import Relationship

from src.database.Base import base
from uuid import uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, Enum as SQLAlchemyEnum
from src.model.enum import ResourceType


class Resource_Class(base):
    __tablename__ = "Resource_Table"

    resource_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    resource_type = Column(SQLAlchemyEnum(ResourceType))
    resource_capacity = Column(Integer, nullable=False)
    is_avaialable = Column(Boolean, default=True)
    floor_id = Column(UUID, ForeignKey('Floor_Table.floor_id'))

    user = Relationship('User_Class', back_populates='resource')
    
    