from fastapi import Depends, APIRouter
from pydantic import BaseModel, Field
from typing import List, Annotated, Union, Optional
from passlib.context import CryptContext
from .models import *
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from exceptions.handler import *
from config.config import Settings

Base.metadata.create_all(bind=engine)

def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()

db_dependency = Annotated[Session, Depends(get_db)]