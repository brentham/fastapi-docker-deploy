from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_product, get_db, Session
from .schemas import Product


router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("", response_model=list[Product])
async def get_product(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    product = get_all_product(db)
    if not product:
        raise not_found_exception("No OS found")
    return product