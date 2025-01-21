from fastapi import Depends
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import func
from config.config import Settings
from util.db_dependency import get_db
from .models import VmInventoryQueue, VmProduct

settings = Settings()

db_dependency = Annotated[Session, Depends(get_db)]

def get_product_total(db: db_dependency):
    return ( 
        db.query(
        VmInventoryQueue.Product_ID,
        VmProduct.Product_Description,
        func.count(VmInventoryQueue.Product_ID).label('Product_Total')
        )
        .join(VmProduct, VmInventoryQueue.Product_ID == VmProduct.Product_ID)
        .group_by(VmInventoryQueue.Product_ID, VmProduct.Product_Description)
        .order_by(VmInventoryQueue.Product_ID)
        .all()
    )