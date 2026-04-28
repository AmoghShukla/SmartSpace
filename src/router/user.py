from src.repository.user import UserRepository
from src.schema.user import UserResponse, UserCreate
from src.service.user import UserService
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException

from sqlalchemy.orm import Session
from pydantic import EmailStr

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/User", tags=['User'])

@router.post('/create_user', response_model=UserResponse, include_in_schema=False)
def CreateUser(payload : UserCreate, db : Session = Depends(get_db)):
    try:
        UserService.CreateUser(payload, db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Creating User!!!") from e
    
def GetUserByEmail(user_email : EmailStr, db: Session = Depends(get_db)):
    try:
        UserRepository.GetUserByEmail(user_email, db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching User!!!") from e


def GetUserByRole(user_role, db: Session = Depends(get_db)):
    try:
        UserService.GetUserByRole(user_role, db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching User!!!") from e
    
def GetAllUsers(db: Session = Depends(get_db)):
    try:
        UserService.GetAllUsers(db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching Users!!!") from e