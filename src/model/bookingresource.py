
from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, delete
from sqlalchemy.orm import Relationship

from src.database.Base import base


class BookingResource_Class(base):
    __tablename__="BookingResource_Table"

    bookingresource_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    booking_id = Column(UUID, ForeignKey("Booking_Table.booking_id", ondelete="CASCADE"))
    resource_id = Column(UUID, ForeignKey("Resource_Table.resource_id", ondelete="CASCADE"))

    resource = Relationship("Booking_Class", back_populates="booking")
    booking = Relationship("Resource_Class", back_populates="booking")