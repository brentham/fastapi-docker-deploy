from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_vm_machine_type, get_db, Session
from .schemas import VmMachineType

router = APIRouter(
    prefix="/list-machine-type",
    tags=["list_machine_type"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/machine-type", response_model=list[VmMachineType])
async def get_vm_machine_type(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    vm_machine_type= get_all_vm_machine_type(db)
    if not vm_machine_type:
        raise not_found_exception("No OS found")
    return vm_machine_type