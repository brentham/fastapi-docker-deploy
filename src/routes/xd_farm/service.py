from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import VmXDFarm

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_vm_xd_farm(db: db_dependency):
    return db.query(VmXDFarm).all()
