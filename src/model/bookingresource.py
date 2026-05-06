
from uuid import UUID, uuid4

from sqlalchemy import Column, ForeignKey, delete
from sqlalchemy.orm import Relationship

from src.database.Base import base


class BookingResource(base):
    __tablename__="BookingResource_Table"

    bookingresource_id = Column(UUID(as_UUID=True), default=uuid4, primary_key=True, nullable=False)
    booking_id = Column(UUID(as_UUID=True), ForeignKey("Booking_Table.booking_id", ondelete="CASCADE"))
    resource_id = Column(UUID(as_UUID=True), ForeignKey("Resource_Class.resource_id", ondelete="CASCADE"))

    resource = Relationship("Booking_Class", back_populates="booking")
    booking = Relationship("Resource_Class", back_populates="booking")