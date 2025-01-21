from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_hypervisor, get_db, Session
from .schemas import Hypervisor

router = APIRouter(
    prefix="/list-hypervisor",
    tags=["list_hypervisor"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/hypervisor", response_model=list[Hypervisor])
async def get_hypervisor(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    hypervisor = get_all_hypervisor(db)
    if not hypervisor:
        raise not_found_exception("No OS found")
    return hypervisor