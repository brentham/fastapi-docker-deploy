from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_product_target_map, get_db, Session
from .schemas import ProductTargetMap


router = APIRouter(
    prefix="/product-target-map",
    tags=["list_product_target_map"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("", response_model=list[ProductTargetMap])
async def get_product_target_map(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    product_target_map = get_all_product_target_map(db)
    if not product_target_map:
        raise not_found_exception("No OS found")
    return product_target_map