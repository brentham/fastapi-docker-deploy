from pydantic import BaseSettings

class AuthSettings(BaseSettings):
    SECRET_KEY: str = "this-is-very-secret"
    MICROSOFT_CLIENT_ID: str
    MICROSOFT_CLIENT_SECRET: str
    MICROSOFT_REDIRECT_URI: str = "http://127.0.0.1:8000/auth/callback"

    class Config:
        env_file = ".env"
