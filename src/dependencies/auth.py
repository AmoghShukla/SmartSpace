from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import jwt
from src.core.config import settings
from src.database.Session import get_db


OAuth2Scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token : Annotated[str, Depends(OAuth2Scheme)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        if not payload:
            raise jwt.exceptions.InvalidTokenError("Invalid Token!!!")
        
        user_id = payload.get('user_id')
        user_role = payload.get('user_role')

        if not user_id or user_role:
            raise jwt.exceptions.InvalidTokenError("Invalid Token!!!")
        
        return {
            'user_id' : user_id,
            'user_role' : user_role
        }
    
    except SQLAlchemyError as e:
        raise HTTPException("Error While Getting Current User") from e
    

def required_role(roles : list):
    allowed_roles = {str(role).upper() for role in roles}
    def role_checker(user = Depends(get_current_user)):
        if str(user['user_role']) not in allowed_roles:
            raise HTTPException('Not Authorised!!!')
        return user
    return role_checker