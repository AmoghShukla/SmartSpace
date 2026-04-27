from fastapi import FastAPI
from sqlalchemy import select
from src.model import UserRole, User_Class
from src.database.Session import session
from src.core.config import settings
from src.utils.loggers import get_logger

app = FastAPI(title="SmartSpace : Workspace ooking & Resource Management API")

logger = get_logger(__name__)

@app.on_event("startup")
def seed_admin():
    db = session()
    try:
        new_admin = db.execute(select(User_Class).where(User_Class.user_role==UserRole.ADMIN)).scalars().first()
        if not new_admin:
            new_admin = User_Class(
                admin_name = settings.ADMIN_NAME,
                admin_email = settings.ADMIN_EMAIL_ID,
                admin_password = settings.ADMIN_PASSWORD,
                admin_role = UserRole.ADMIN
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