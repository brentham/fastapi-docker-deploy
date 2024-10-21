from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from config.config import Settings

from config.database import engine

from routes import auth

from routes.auth import main
from routes.check_authorization import main, models

# check_authorization.models.Base.metadata.create_all(bind=engine)

settings = Settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Set-Cookie"],
    allow_credentials=True,
    
)

# ---------------Routes-------------------
app.include_router(auth.main.router)
# ----------------------------------------


# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")