from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_catalog, get_db, Session
from .schemas import Catalog


router = APIRouter(
    prefix="/list-catalog",
    tags=["list_catalog"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/catalogs", response_model=list[Catalog])
async def get_catalog(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    catalog = get_all_catalog(db)
    if not catalog:
        raise not_found_exception("No OS found")
    return catalog