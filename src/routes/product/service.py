from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from config.config import Settings
from util.db_dependency import get_db
from .models import Product

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_all_product(db: db_dependency):
    return db.query(Product).all()
