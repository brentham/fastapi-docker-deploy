
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    
    DB_URL: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_URL: str
    DB_NAME: str
    DB_TYPE: str

    SECRET_KEY: str

    class Config:
        env_file = ".env"
