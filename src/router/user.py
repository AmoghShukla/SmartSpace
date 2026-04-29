from src.repository.user import UserRepository
from src.schema.user import UserResponse, UserCreate
from src.service.user import UserService
from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException
from src.dependencies.auth import get_current_user, required_role

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
    
@router.get('/get_my_profile', response_model=UserResponse)   
def GetMyProfile(db: Session = Depends(get_db), current_user = Depends(get_current_user), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER', 'GUEST', "USER", 'MEMBER']))):
    try:
        return UserService.GetMyProfile(current_user['user_id'],db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching User Profile!!!") from e

@router.get('/get_user_by_email/{user_email}', response_model=UserResponse)   
def GetUserByEmail(user_email : EmailStr, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        return UserService.GetUserByEmail(user_email, db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching User!!!") from e

@router.get('/get_user_by_role/{user_role}', response_model=UserResponse)  
def GetUserByRole(user_role, db: Session = Depends(get_db), user = Depends(required_role(['ADMIN']))):
    try:
        return UserService.GetUserByRole(user_role.upper(), db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Fetching User!!!") from e

@router.get('/', response_model=list[UserResponse])    
def GetAllUsers(db: Session = Depends(get_db), user = Depends(required_role(['ADMIN', 'RESOURCE_MANAGER']))):
    try:
        return UserService.GetAllUsers(db)
    except CustomException.ServiceError as e:
        raise HTTPException(status_code=401, detail=str(e))