import os
import requests
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi_session import FastAPISession
from starlette.middleware.sessions import SessionMiddleware
import msal

import app_config

app = FastAPI()

# Configure sessions
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")  # Replace with your secret key

# Templates setup
templates = Jinja2Templates(directory="templates")

# MSAL Configuration
msal_app = msal.ConfidentialClientApplication(
    app_config.CLIENT_ID,
    authority=app_config.AUTHORITY,
    client_credential=app_config.CLIENT_SECRET,
)

# Session dependency
def get_session(request: Request):
    return request.session

@app.get("/login")
async def login(request: Request):
    session = get_session(request)
    auth_url = msal_app.get_authorization_request_url(
        app_config.SCOPE,
        redirect_uri=request.url_for("auth_response"),
    )
    session["state"] = msal_app.get_state()  # MSAL-generated state value
    return RedirectResponse(url=auth_url)

@app.get(app_config.REDIRECT_PATH)
async def auth_response(request: Request):
    session = get_session(request)
    if "state" not in session or session["state"] != request.query_params.get("state"):
        raise HTTPException(status_code=400, detail="Invalid state")
    
    result = msal_app.acquire_token_by_authorization_code(
        request.query_params.get("code"),
        scopes=app_config.SCOPE,
        redirect_uri=request.url_for("auth_response"),
    )

    if "error" in result:
        return templates.TemplateResponse("auth_error.html", {"request": request, "result": result})
    
    session["token_cache"] = result
    return RedirectResponse(url="/")

@app.get("/logout")
async def logout(request: Request):
    session = get_session(request)
    logout_url = f'{app_config.AUTHORITY}/oauth2/v2.0/logout?post_logout_redirect_uri={request.url_for("index")}'
    session.clear()
    return RedirectResponse(url=logout_url)

@app.get("/")
async def index(request: Request):
    session = get_session(request)
    token = session.get("token_cache")
    if not token:
        return RedirectResponse(url="/login")

    user = msal_app.get_accounts()[0] if msal_app.get_accounts() else None
    if not user:
        return RedirectResponse(url="/login")
    return templates.TemplateResponse('index.html', {"request": request, "user": user, "version": "MSAL"})

@app.get("/call_downstream_api")
async def call_downstream_api(request: Request):
    session = get_session(request)
    token = session.get("token_cache")

    if not token:
        return RedirectResponse(url="/login")

    api_result = requests.get(
        app_config.ENDPOINT,
        headers={'Authorization': f"Bearer {token['access_token']}"},
        timeout=30,
    ).json()
    return templates.TemplateResponse('display.html', {"request": request, "result": api_result})
