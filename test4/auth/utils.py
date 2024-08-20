from typing import Optional
from jose import JWTError, jwt
from auth.config import AuthSettings

auth_settings = AuthSettings()

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, auth_settings.SECRET_KEY, algorithms=[auth_settings.ALGORITHM])
        return payload
    except JWTError:
        return None
