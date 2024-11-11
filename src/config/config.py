
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
    
    
    ms_client_id: str
    ms_client_secret: str
    ms_tenant_id: str
    redirect_uri: str
    
    MS_CLIENT_ID: str
    MS_CLIENT_SECRET: str
    MS_TENANT_ID: str
    REDIRECT_URI: str
    
    MS_CLIENT_ID="your-client-id"
    MS_CLIENT_SECRET="your-client-secret"
    MS_TENANT_ID="your-tenant-id"
    REDIRECT_URI="http://127.0.0.1:8000/auth/callback"

    class Config:
        env_file = ".env"
