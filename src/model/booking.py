from uuid import uuid4

from sqlalchemy import UUID, Column, DateTime, Enum, ForeignKey, Integer, Enum as SQLAlchemyEnum, Time, Date
from sqlalchemy.orm import Relationship
from datetime import UTC, date, time

from src.database.Base import base
from src.model.enum import BookingStatus

class Booking_Class(base):
    __tablename__="Booking_Table"

    booking_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_id = Column(UUID, ForeignKey('User_Table.user_id'))
    floor_id = Column(UUID, ForeignKey("Floor_Table.floor_id"))
    workspace_id = Column(UUID, ForeignKey('Workspace_Table.workspace_id'))
    start_time = Column(DateTime(timezone=False), nullable=False)
    end_time = Column(DateTime(timezone=False), nullable=False)
    booking_status = Column(SQLAlchemyEnum(BookingStatus), default=BookingStatus.PENDING)

    resource = Relationship("BookingResource_Class", back_populates="booking")
    user = Relationship("User_Class", back_populates="booking")
    floor = Relationship("Floor_Class", back_populates="booking")
    workspace = Relationship("Workspace_Class", back_populates="booking")