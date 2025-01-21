from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user
from exceptions.handler import not_found_exception

from .service import get_all_vm_action, get_db, Session
from .schemas import VmAction

router = APIRouter(
    prefix="/list-action",
    tags=["list_action"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/vm-actions", response_model=list[VmAction])
async def get_os(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_action= get_all_vm_action(db)
    if not vm_action:
        raise not_found_exception("No OS found")
    return vm_action