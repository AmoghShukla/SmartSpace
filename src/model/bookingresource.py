
from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, ForeignKey, delete
from sqlalchemy.orm import Relationship

from src.database.Base import base


class BookingResource_Class(base):
    __tablename__="BookingResource_Table"

    bookingresource_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    booking_id = Column(UUID, ForeignKey("Booking_Table.booking_id", ondelete="CASCADE"))
    resource_id = Column(UUID, ForeignKey("Resource_Table.resource_id", ondelete="CASCADE"))
    floor_id = Column(UUID, ForeignKey("Floor_Table.floor_id"))
    workspace_id = Column(UUID, ForeignKey('Workspace_Table.workspace_id'))
    created_at = Column(DateTime(timezone=False), default=datetime.now(UTC))
    

    resource = Relationship("Resource_Class", back_populates="booking")
    booking = Relationship("Booking_Class", back_populates="resource")
    floor = Relationship("Floor_Class", back_populates="bookingresource")
    workspace = Relationship("Workspace_Class", back_populates="bookingresource")