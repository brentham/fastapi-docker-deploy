from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import Settings

from config.database import engine
from routes import auth

from routes.auth import main, models
# from routes.todos import main, models
# from routes.listings import main, models

# app = FastAPI()
settings = Settings()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# models.Base.metadata.create_all(bind=engine)
auth.models.Base.metadata.create_all(bind=engine)
# todos.models.Base.metadata.create_all(bind=engine)
# listings.models.Base.metadata.create_all(bind=engine)

# Routes
app.include_router(auth.main.router)
# app.include_router(todos.main.router)
