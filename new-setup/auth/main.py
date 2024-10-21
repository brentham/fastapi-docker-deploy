import datetime
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from fastapi_sso.sso.microsoft import MicrosoftSSO
from jose import jwt
from config.config import Settings

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
    )

settings = Settings()

sso = MicrosoftSSO(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    tenant=settings.TENANT_ID,
    redirect_uri=settings.REDIRECT_URI,
    allow_insecure_http=settings.DEBUG,  # True Only for development
)
@router.get("/login")
async def login():
    """Redirect the user to the Microsoft login page."""
    return await sso.get_login_redirect()

@router.get("/logout")
async def logout():
    """Forget the user's session."""
    response = RedirectResponse(url="/protected")
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
        # {"pld": openid.dict(), "exp": expiration, "sub": openid.id},
        {"pld": openid.model_dump(), "exp": expiration, "sub": openid.id},
        key=settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

# Cookie Authentication
    response = RedirectResponse(url="/")
    response.set_cookie(
        key="token", value=token, expires=expiration
    )  # This cookie will make the browser send the token in every request
    return response

# Bearer Token Authentication
    # return {"access_token": token, "token_type": "bearer"}


@router.get("/protected")
async def protected_endpoint(user: OpenID = Depends(get_logged_user)):
    """This endpoint will say hello to the logged user.
    If the user is not logged, it will return a 401 error from `get_logged_user`."""
    return {
        "message": f"You are very welcome, {user.email}!",
    }