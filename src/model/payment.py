from datetime import UTC, datetime

from sqlalchemy.orm import Relationship

from src.database.Base import base
from src.model.enum import PaymentStatus

from uuid import uuid4
from sqlalchemy import DateTime, Boolean, Column, ForeignKey, Integer, String, UUID, Enum as SQLAlchemyEnum
from src.model.enum import UserRole


class Payment_Class(base):
    __tablename__ = "Payment_Table"

    payment_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    booking_id = Column(UUID(as_uuid=True), ForeignKey('Booking_Table.booking_id'))
    user_id = Column(UUID, ForeignKey("User_Table.user_id"))
    payment_amount = Column(Integer, nullable=False)
    payment_status = Column(SQLAlchemyEnum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)
    created_at = Column(DateTime, default=datetime.now(UTC), nullable=False)

    user = Relationship("User_Class", back_populates='payment')
    booking = Relationship("Booking_Class", back_populates='payment')