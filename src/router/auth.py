from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.Session import get_db
from src.schema.user import UserResponse, UserCreate
from src.service.auth import AuthService
from src.Exceptions.Custom_Exception import CustomException

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/register', response_model=UserResponse)
def register_user(payload : UserCreate, db : Session = Depends(get_db)):
    return AuthService.RegisterUser(payload, db)
    
@router.post('/login', response_model=UserResponse)
def login_user(payload : UserCreate, db : Session = Depends(get_db)):
    return AuthService.login_user(payload, db)
    