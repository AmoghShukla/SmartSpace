from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.database.Session import get_db


OAuth2Scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_current_user(user = Depends(OAuth2Scheme), db : Session = Depends(get_db)):
    pass