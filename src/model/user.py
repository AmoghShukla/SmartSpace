from src.database.Base import base
from uuid import uuid4
from sqlalchemy import Column, String, UUID
from src.model.enum import UserRole


class User_Class(base):
    __tablename__="User_Table"

    user_id = Column(UUID(as_uuid=True), default=uuid4, primary_key=True)
    user_name = Column(String, nullable=False, index=True)
    user_email = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    user_contact_no = Column(String, nullable=False, unique=True)
    user_role = Column(String, default=UserRole.USER)

