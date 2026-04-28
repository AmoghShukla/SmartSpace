from pydantic import EmailStr
from src.database.Base import base
from uuid import uuid3
from sqlalchemy import Column, String, UUID
from pydantic_extra_types.phone_numbers import PhoneNumber
from model import UserRole


class User_Class(base):
    __tablename__="User_Table"

    user_id = Column(UUID(as_uuid=True), default=uuid3(), primary_key=True)
    user_name = Column(String, nullable=False, index=True)
    user_email = Column(EmailStr, nullable=False)
    user_password = Column(String, nullable=False)
    user_contact_no = Column(PhoneNumber, nullable=False, unique=True)
    user_role = Column(String, default=UserRole.GUEST)

