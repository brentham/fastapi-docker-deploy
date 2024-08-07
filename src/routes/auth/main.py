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


@router.post("/create/user")
async def create_new_user(create_user: CreateUser, db: Session = Depends(get_db)):
    create_user_model = Users()
    create_user_model.email = create_user.email
    create_user_model.username = create_user.username
    create_user_model.first_name = create_user.first_name
    create_user_model.last_name = create_user.last_name
    hash_password = get_password_hash(create_user.password)
    create_user_model.hashed_password = hash_password
    create_user_model.is_active = True

    db.add(create_user_model)
    db.commit()


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise token_exception()
    token_expires = timedelta(minutes=20)
    token = create_access_token(user.username, user.id, expires_delta=token_expires)

    return {"token": token}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Azure SSO example"}

@app.get("/login")
async def login():
    # Generate the authorization URL
    auth_url = app_msal.get_authorization_request_url(SCOPE, redirect_uri=REDIRECT_URI)
    return RedirectResponse(auth_url)

@app.get("/auth-redirect")
async def auth_redirect(request: Request):
    # Get the authorization code from the query parameters
    code = request.query_params.get("code")
    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not found")

    # Exchange the authorization code for an access token
    result = app_msal.acquire_token_by_authorization_code(code, SCOPE, redirect_uri=REDIRECT_URI)
    if "access_token" not in result:
        raise HTTPException(status_code=400, detail="Failed to acquire access token")

    return {"access_token": result["access_token"], "id_token_claims": result.get("id_token_claims")}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)