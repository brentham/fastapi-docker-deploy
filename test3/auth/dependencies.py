from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from auth.config import AuthSettings
from fastapi_sso.sso.base import OpenID

auth_settings = AuthSettings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

async def get_logged_user(token: str = Depends(oauth2_scheme)) -> OpenID:
    """Get user's JWT stored in the Authorization header, parse it, and return the user's OpenID."""
    try:
        claims = jwt.decode(token, key=auth_settings.SECRET_KEY, algorithms=["HS256"])
        return OpenID(**claims["pld"])
    except Exception as error:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials") from error
