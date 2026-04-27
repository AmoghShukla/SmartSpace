from pydantic_settings import BaseSettings
from sqlalchemy import String

class Settings(BaseSettings):
    DB_USER : str
    DB_PORT : int
    DB_NAME : str
    DB_PASSWORD : str
    DB_HOST : str

    @property
    def DATABASE_URL(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    class Config:
        env_file = ".env"

settings = Settings()
