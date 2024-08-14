from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi_sso.sso.microsoft import MicrosoftSSO
from fastapi_sso.sso.base import OpenID, SSOBase
from pydantic import BaseModel
import os

# Load environment variables (Client ID and Secret)
from dotenv import load_dotenv

load_dotenv()

# Initialize FastAPI
app = FastAPI()

# SSO Configuration
client_id = os.getenv("AZURE_CLIENT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
redirect_uri = "http://localhost:8000/auth/callback"

# Initialize Microsoft SSO
sso = MicrosoftSSO(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

# Create User model
class User(BaseModel):
    username: str
    email: str

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Microsoft AD Authentication Demo!"}

# SSO Login route
@app.get("/auth/login")
def login():
    return RedirectResponse(sso.get_login_redirect())

# Callback route
@app.get("/auth/callback")
async def callback(code: str):
    user = await sso.verify_and_process(code)
    if user:
        # You can handle user information here (e.g., create a session, store in DB)
        return {"username": user.display_name, "email": user.email}
    else:
        raise HTTPException(status_code=400, detail="Failed to authenticate user")

# Protecting a route with authentication
@app.get("/protected")
async def protected(user: User = Depends(sso.get_current_user)):
    return {"message": f"Hello, {user.username}! This is a protected route."}

# Logout route
@app.get("/auth/logout")
def logout():
    return RedirectResponse(sso.get_logout_redirect(redirect_uri="http://localhost:8000"))
