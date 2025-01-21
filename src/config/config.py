from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl

class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    
# Database Vars
    DB_URL: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_URL: str
    DB_NAME: str
    DB_TYPE: str

# Azure SSO Vars
    # BACKEND_CORS_ORIGINS: list[str | AnyHttpUrl] = ['http://localhost:8000']
    TENANT_ID: str
    CLIENT_ID: str
    CLIENT_SECRET: str
    REDIRECT_URI: str
    AUTHORITY: str
    SCOPE: str

# Secret Key
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
   
# Debug 
    # DEBUG: str

    class Config:
        env_file = ".env"