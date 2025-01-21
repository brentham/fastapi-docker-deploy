from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import DGN

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_dgn(db: db_dependency):
    return db.query(DGN).all()
