import datetime
from fastapi import APIRouter, Depends, HTTPException, Security, Request
from fastapi.responses import RedirectResponse
from fastapi.security import APIKeyCookie
from fastapi_sso.sso.microsoft import MicrosoftSSO
from fastapi_sso.sso.base import OpenID
from jose import jwt
from auth.config import AuthSettings
from auth.dependencies import get_logged_user

router = APIRouter()

auth_settings = AuthSettings()

sso = MicrosoftSSO(
    client_id=auth_settings.MICROSOFT_CLIENT_ID,
    client_secret=auth_settings.MICROSOFT_CLIENT_SECRET,
    redirect_uri=auth_settings.MICROSOFT_REDIRECT_URI,
)

@router.get("/login")
async def login():
    """Redirect the user to the Microsoft login page."""
    return await sso.get_login_redirect()

@router.get("/logout")
async def logout():
    """Forget the user's session."""
    response = RedirectResponse(url="/protected")
    response.delete_cookie(key="token")
    return response

@router.get("/callback")
async def login_callback(request: Request):
    """Process login and redirect the user to the protected endpoint."""
    openid = await sso.verify_and_process(request)
    if not openid:
        raise HTTPException(status_code=401, detail="Authentication failed")
    
    # Create a JWT with the user's OpenID
    expiration = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1)
    token = jwt.encode(
        {"pld": openid.dict(), "exp": expiration, "sub": openid.id},
        key=auth_settings.SECRET_KEY,
        algorithm="HS256"
    )
    response = RedirectResponse(url="/protected")
    response.set_cookie(
        key="token", value=token, expires=expiration
    )  # This cookie will make sure /protected knows the user
    return response

@router.get("/protected")
async def protected_endpoint(user: OpenID = Depends(get_logged_user)):
    """This endpoint will say hello to the logged user.
    If the user is not logged, it will return a 401 error from `get_logged_user`."""
    return {
        "message": f"You are very welcome, {user.email}!",
    }
