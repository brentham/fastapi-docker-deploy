from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_product_total, get_db, Session
from .schemas import VmProduct, VmInventoryQueue

router = APIRouter(
    prefix="/inventory-counts",
    tags=["inventory_counts"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/product-total", response_model=list[VmProduct])
async def get_vm_product_total(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_product_total= get_product_total(db)
    if not vm_product_total:
        raise not_found_exception("No OS found")
    return vm_product_total