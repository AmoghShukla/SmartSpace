from datetime import UTC, datetime, timedelta
import jwt
from pwdlib import PasswordHash

from src.core.config import settings

PasswordContext = PasswordHash.recommended()


class AuthSecurity:

    @staticmethod
    def hash_password(password : str):
        return PasswordContext.hash(password)
    
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return PasswordContext.verify(plain_password, hashed_password)
    
    @staticmethod
    def create_access_token(data : dict):
        data_to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        data_to_encode.update({'exp' : expire})
        return jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    @staticmethod
    def create_refresh_token(data : dict):
        data_to_encode = data.copy()
        expire = datetime.now(UTC) + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)

        data_to_encode.update({'exp' : expire})
        return jwt.encode(data_to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    

    

