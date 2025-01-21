from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_vm_machine_source, get_db, Session
from .schemas import VmMachineSource

router = APIRouter(
    prefix="/list-machine-source",
    tags=["list_machine_source"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/machine-source", response_model=list[VmMachineSource])
async def get_vm_machine_source(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_machine_source= get_all_vm_machine_source(db)
    if not vm_machine_source:
        raise not_found_exception("No OS found")
    return vm_machine_source