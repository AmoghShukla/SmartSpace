from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError

import re
from src.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


def get_current_user(token: str =  Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        if not payload:
            raise jwt.exceptions.InvalidTokenError("Invalid Token!!!")

        user_id = payload.get('sub')
        user_role = payload.get('user_role')

        if not user_id or not user_role:
            raise jwt.exceptions.InvalidTokenError("Invalid Token!!!")

        return {
            'user_id': user_id,
            'user_role': user_role
        }
    
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400 ,detail="Error While Getting Current User") from e



def required_role(roles: list):
    allowed_roles = {str(role).upper() for role in roles}
    def role_checker(user=Depends(get_current_user)):
        if str(user['user_role']).upper() not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not Authorised!!",
            )
        return user

    return role_checker


def normalize_search(text : str) -> str:
    text = text.lower().strip()

    text = re.sub(r"\s+", " ", text)
    return text