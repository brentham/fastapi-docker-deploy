from fastapi import Depends, APIRouter
from fastapi_sso.sso.base import OpenID
from routes.auth.dependencies import get_logged_user

router = APIRouter(
    prefix="/check-authorization",
    tags=["check_authorization"],
    responses={401: {"user": "Not authorized"}}
    )