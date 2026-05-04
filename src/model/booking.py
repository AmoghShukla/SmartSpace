from uuid import uuid4

from sqlalchemy import UUID, Column, Enum, ForeignKey, Integer, Enum as SQLAlchemyEnum, Time, Date
from sqlalchemy.orm import Relationship
from datetime import date, time

from src.database.Base import base
from src.model.enum import BookingStatus

class Booking_Class(base):
    __tablename__="Booking_Table"

    booking_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_id = Column(UUID, ForeignKey('User_Table.user_id'))
    workspace_id = Column(UUID, ForeignKey('Workspace_Table.workspace_id'))
    resource_id = Column(UUID, ForeignKey('Resource_Table.resource_id'))
    booking_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    booking_status = Column(SQLAlchemyEnum(BookingStatus), default=BookingStatus.PENDING)

    resource = Relationship("Resource_Class", back_populates="booking")
    user = Relationship("User_Class", back_populates="booking")