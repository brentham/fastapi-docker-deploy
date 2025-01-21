from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_dgn, get_db, Session
from .schemas import DGN



router = APIRouter(
    prefix="/list-dgn",
    tags=["list_dgn"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/dgn", response_model=list[DGN])
async def get_dgn(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    dgn = get_all_dgn(db)
    if not dgn:
        raise not_found_exception("No OS found")
    return dgn