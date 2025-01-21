from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_vm_xd_farm, get_db, Session
from .schemas import VmXDFarm

router = APIRouter(
    prefix="/xd-farm",
    tags=["xd_farm"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("", response_model=list[VmXDFarm])
async def get_vm_xd_farm(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_xd_farm= get_all_vm_xd_farm(db)
    if not vm_xd_farm:
        raise not_found_exception("No OS found")
    return vm_xd_farm