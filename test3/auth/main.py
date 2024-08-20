from fastapi import APIRouter, Depends, HTTPException
from fastapi_sso.sso.microsoft import MicrosoftSSO
from starlette.requests import Request
from starlette.responses import RedirectResponse
from config.config import get_settings
from auth.dependencies import get_current_user
from auth.schemas import Token

router = APIRouter()

settings = get_settings()

# Initialize Microsoft SSO
sso = MicrosoftSSO(
    client_id=settings.MICROSOFT_CLIENT_ID,
    client_secret=settings.MICROSOFT_CLIENT_SECRET,
    redirect_uri=settings.MICROSOFT_REDIRECT_URI,
    allow_insecure_http=settings.DEBUG,  # Only for development
)

@router.get("/login")
async def login(request: Request):
    """Redirect user to Microsoft's login page."""
    return await sso.get_login_redirect(request)

@router.get("/callback")
async def callback(request: Request):
    """Callback route that Microsoft will redirect to after login."""
    user = await sso.verify_and_process(request)
    if not user:
        raise HTTPException(status_code=400, detail="Authentication failed")
    
    # Here you can create your own user object and issue a JWT token
    token = Token(access_token="fake-jwt-token", token_type="bearer")
    return token

@router.get("/user", dependencies=[Depends(get_current_user)])
async def get_user(user: dict = Depends(get_current_user)):
    return user
