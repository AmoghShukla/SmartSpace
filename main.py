from fastapi import FastAPI
from sqlalchemy import select

from src.core.security import AuthSecurity
from src.model import User_Class
from src.model.enum import UserRole
from src.database.Session import session
from src.core.config import settings
from src.utils.loggers import get_logger
from src.router.auth import router as AuthRouter
from src.router.user import router as UserRouter
from src.router.promotions import router as PromtionsRouter

app = FastAPI(title="SmartSpace : Workspace Booking & Resource Management API", version="1.0")

logger = get_logger(__name__)

app.include_router(AuthRouter)
app.include_router(UserRouter)
app.include_router(PromtionsRouter)


@app.on_event("startup")
def seed_admin():
    db = session()
    try:
        new_admin = db.query(User_Class).filter(User_Class.user_role =="ADMIN").first()
        if not new_admin:
            password = AuthSecurity.hash_password(settings.ADMIN_PASSWORD)
            new_admin = User_Class(
                user_name = settings.ADMIN_NAME,
                user_email = settings.ADMIN_EMAIL_ID,
                user_password = password,
                user_contact_no = settings.ADMIN_CONTACT_NO,
                user_role = UserRole.ADMIN.name
            )

            db.add(new_admin)
            db.commit()
            logger.info("DB Seeded Successfully!!!")
        else:
            logger.info("Admin Already Exists!!!")
    except Exception as e:
        db.rollback()
        print("Error creating admin:", str(e))

    finally:
        db.close()
    

@app.get('/')
def home():
    return {
        'message' : 'SmartSpace Application is up and running!!!'
    }