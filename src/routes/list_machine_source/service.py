from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import VmMachineSource

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_vm_machine_source(db: db_dependency):
    return db.query(VmMachineSource).all()
