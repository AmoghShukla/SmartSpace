from src.schema.user import UserResponse, UserCreate
from src.service.user import UserService

from src.database.Session import get_db
from src.Exceptions.Custom_Exception import CustomException

from sqlalchemy.orm import Session

from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(prefix="/User", tags=['User'])

@router.post('/create_user', response_model=UserResponse)
def CreateUser(payload : UserCreate, db : Session = Depends(get_db)):
    try:
        UserService.CreateUser(payload, db)
    except CustomException.ServiceError as e:
        raise HTTPException("Error While Creating User!!!") from e