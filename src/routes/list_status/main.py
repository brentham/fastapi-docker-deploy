from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_vm_list_status, get_db, Session
from .schemas import VmStatus

router = APIRouter(
    prefix="/list-status",
    tags=["list_status"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/status", response_model=list[VmStatus])
async def get_vm_list_status(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_list_status= get_all_vm_list_status(db)
    if not vm_list_status:
        raise not_found_exception("No OS found")
    return vm_list_status