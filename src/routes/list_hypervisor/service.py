from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import Hypervisor

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_hypervisor(db: db_dependency):
    return db.query(Hypervisor).all()
