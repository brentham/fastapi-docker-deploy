from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import VmStatus

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_vm_list_status(db: db_dependency):
    return db.query(VmStatus).all()
