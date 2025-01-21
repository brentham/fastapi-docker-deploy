from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID

from routes.auth.dependencies import get_logged_user
from exceptions.handler import not_found_exception

from .service import get_all_vm_os, get_db, Session
from .schemas import ListOS

router = APIRouter(
    prefix="/list-os",
    tags=["list-os"],
    responses={401: {"user": "Could not validate credentials"}}
    )

@router.get("/os", response_model=list[ListOS])
async def get_os(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    list_os = get_all_vm_os(db)
    if not list_os:
        raise not_found_exception("No OS found")
    return list_os