from fastapi import Depends, APIRouter
from pydantic import BaseModel, Field
from typing import List, Annotated, Union, Optional
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from config.config import Settings
from util.db_dependency import get_db
from .models import Users
from exceptions.handler import *

settings = Settings()

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="token")

db_dependency = Annotated[Session, Depends(get_db)]


auth_model = MSALAuthModel()

def login_service(request: Request):
    session = request.session
    auth_url = auth_model.get_authorization_url(scopes=request.app.config.SCOPE, redirect_uri=request.url_for("auth_response"))
    session["state"] = auth_model.app.get_state()
    return RedirectResponse(url=auth_url)

def auth_response_service(request: Request):
    session = request.session
    if "state" not in session or session["state"] != request.query_params.get("state"):
        raise HTTPException(status_code=400, detail="Invalid state")

    result = auth_model.acquire_token_by_code(
        code=request.query_params.get("code"),
        scopes=request.app.config.SCOPE,
        redirect_uri=request.url_for("auth_response"),
    )

    if "error" in result:
        return {"error": result}

    session["token_cache"] = result
    return RedirectResponse(url="/")

def logout_service(request: Request):
    session = request.session
    logout_url = f'{request.app.config.AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri={request.url_for("index")}'
    session.clear()
    return RedirectResponse(url=logout_url)

def get_user_service(request: Request):
    session = request.session
    return auth_model.get_user()