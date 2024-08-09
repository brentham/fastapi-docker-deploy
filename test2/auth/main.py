from fastapi import Depends, APIRouter
from pydantic import BaseModel, Field
from typing import List, Annotated, Union, Optional
from passlib.context import CryptContext
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from exceptions.handler import *
from config.config import Settings

from .models import *
from .controller import *
from .schemas import *


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"user": "Not authorized"}}
    )


@router.get("/login")
async def login(request: Request):
    return login_service(request)

@router.get(request.app.config.REDIRECT_PATH)
async def auth_response(request: Request):
    result = auth_response_service(request)
    if isinstance(result, dict) and "error" in result:
        return templates.TemplateResponse("auth_error.html", {"request": request, "result": result})
    return result

@router.get("/logout")
async def logout(request: Request):
    return logout_service(request)

@router.get("/")
async def index(request: Request):
    user = get_user_service(request)
    if not user:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse('index.html', {"request": request, "user": user, "version": "MSAL"})

@router.get("/call_downstream_api")
async def call_downstream_api(request: Request):
    session = request.session
    token = session.get("token_cache")
    if not token:
        return RedirectResponse(url="/login")

    api_result = requests.get(
        request.app.config.ENDPOINT,
        headers={'Authorization': f"Bearer {token['access_token']}"},
        timeout=30,
    ).json()
    return templates.TemplateResponse('display.html', {"request": request, "result": api_result})