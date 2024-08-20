from fastapi import HTTPException, Security
from fastapi.security import APIKeyCookie
from jose import jwt
from auth.config import AuthSettings
from fastapi_sso.sso.base import OpenID

auth_settings = AuthSettings()

api_key_cookie = APIKeyCookie(name="token")

async def get_logged_user(cookie: str = Security(api_key_cookie)) -> OpenID:
    """Get user's JWT stored in cookie 'token', parse it, and return the user's OpenID."""
    try:
        claims = jwt.decode(cookie, key=auth_settings.SECRET_KEY, algorithms=["HS256"])
        return OpenID(**claims["pld"])
    except Exception as error:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials") from error
