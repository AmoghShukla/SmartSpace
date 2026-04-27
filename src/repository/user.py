from src.model import User_Class

from sqlalchemy import select


class UserRepository:

    def CreateUser(payload, db):
        user = UserRepository.GetUserByEmail(payload.user_email, db)

    def GetUserByEmail(user_email, db):
        return db.execute(select(User_Class).where(User_Class.user_email==user_email)).scalars().first()
    