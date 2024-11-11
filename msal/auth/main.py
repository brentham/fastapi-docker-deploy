from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from msal import ConfidentialClientApplication
from jose import jwt
from config.config import settings
from src.auth.schemas import OpenID
import datetime

router = APIRouter()
SECRET_KEY = "your_jwt_secret"  # JWT secret key for encoding tokens
AUTHORITY = f"https://login.microsoftonline.com/{settings.ms_tenant_id}"
SCOPES = ["User.Read"]  # Microsoft Graph API permissions

msal_app = ConfidentialClientApplication(
    client_id=settings.ms_client_id,
    client_credential=settings.ms_client_secret,
    authority=AUTHORITY,
)

async def create_jwt_token(user_info: dict):
    expiration = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    token = jwt.encode({"exp": expiration, "sub": user_info["oid"], "pld": user_info}, SECRET_KEY, algorithm="HS256")
    return token

@router.get("/auth/login")
async def login():
    auth_url = msal_app.get_authorization_request_url(
        scopes=SCOPES,
        redirect_uri=settings.redirect_uri
    )
    return RedirectResponse(auth_url)

@router.get("/auth/callback")
async def auth_callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")

    # Exchange code for token
    result = msal_app.acquire_token_by_authorization_code(
        code,
        scopes=SCOPES,
        redirect_uri=settings.redirect_uri
    )

    if "error" in result:
        raise HTTPException(status_code=400, detail="Token acquisition failed")

    # Parse and create JWT for client session
    user_info = result.get("id_token_claims")
    jwt_token = await create_jwt_token(user_info)

    response = RedirectResponse(url="/protected")
    response.set_cookie(key="token", value=jwt_token)
    return response

@router.get("/protected")
async def protected_route(request: Request):
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        claims = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": f"Welcome, {claims['pld'].get('name', 'user')}!"}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
