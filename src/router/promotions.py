from src.repository.user import UserRepository
from src.schema.user import UserResponse, UserCreate
from src.service.promotions import PromotionsService
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role
from src.utils.loggers import get_logger

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/promotions", tags=['Promotions'])
logger = get_logger(__name__)

   
@router.post('/make_Admin', response_model=UserResponse)
def MakeAdmin(user_email : EmailStr, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        logger.info(f"Promoting user with user_email : {user_email} to Admin")
        return PromotionsService.MakeAdmin(user_email, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Promoting user with user_email : {user_email} to Member")
        raise HTTPException("Error While Promoting user with user_email : {user_email} to Member") from e
    
@router.post('/make_member', response_model=UserResponse)
def MakeMember(user_email : EmailStr, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Promoting user with user_email : {user_email} to Member")
        return PromotionsService.MakeMember(user_email, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Promoting user with user_email : {user_email} to Member")
        raise HTTPException("Error While Promoting user with user_email : {user_email} to Member") from e
    
@router.post('/make_user', response_model=UserResponse)
def MakeUser(user_email : EmailStr, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        logger.info(f"Making user with user_email : {user_email} to User")
        return PromotionsService.MakeUser(user_email, db)
    except CustomException.ServiceError as e:
        logger.error(f"Error while Making user with user_email : {user_email} to User")
        raise HTTPException(f"Error While Making user with user_email : {user_email} to User") from e
 