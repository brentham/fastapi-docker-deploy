from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

from exceptions.handler import not_found_exception

from .service import get_all_event_type, get_db, Session
from .schemas import EventType


router = APIRouter(
    prefix="/list-event-type",
    tags=["list_event_type"],
    responses={401: {"user": "Not authorized"}}
    )

@router.get("/event-type", response_model=list[EventType])
async def get_event_type(db: Session = Depends(get_db), user: OpenID = Depends(get_logged_user)):
    event_type = get_all_event_type(db)
    if not event_type:
        raise not_found_exception("No OS found")
    return event_type