from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from config.config import Settings

from config.database import engine

from routes import auth, check_authorization, heartbeat_check, inventory_counts, list_action, list_catalog, list_dgn, list_event_type, list_hypervisor, list_machine_source, list_machine_type, list_os, list_status, product, product_source_map, product_target_map, xd_farm

from routes.auth import main
# from routes.check_authorization import main, models
# from routes.heartbeat_check import main, models
from routes.inventory_counts import main, models
from routes.list_action import main, models
from routes.list_catalog import main, models
from routes.list_dgn import main, models
from routes.list_event_type import main, models
from routes.list_hypervisor import main, models
from routes.list_machine_source import main, models
from routes.list_machine_type import main, models
from routes.list_os import main, models
from routes.list_status import main, models
from routes.product import main, models
from routes.product_source_map import main, models
from routes.product_target_map import main, models
from routes.xd_farm import main, models

# check_authorization.models.Base.metadata.create_all(bind=engine)
# heartbeat_check.models.Base.metadata.create_all(bind=engine)
inventory_counts.models.Base.metadata.create_all(bind=engine)
list_action.models.Base.metadata.create_all(bind=engine)
list_catalog.models.Base.metadata.create_all(bind=engine)
list_dgn.models.Base.metadata.create_all(bind=engine)
list_event_type.models.Base.metadata.create_all(bind=engine)
list_hypervisor.models.Base.metadata.create_all(bind=engine)
list_machine_source.models.Base.metadata.create_all(bind=engine)
list_machine_type.models.Base.metadata.create_all(bind=engine)
list_os.models.Base.metadata.create_all(bind=engine)
list_status.models.Base.metadata.create_all(bind=engine)
product.models.Base.metadata.create_all(bind=engine)
product_source_map.models.Base.metadata.create_all(bind=engine)
product_target_map.models.Base.metadata.create_all(bind=engine)
# submit_request.models.Base.metadata.create_all(bind=engine)
xd_farm.models.Base.metadata.create_all(bind=engine)

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
# app.include_router(check_authorization.main.router)
# app.include_router(heartbeat_check.main.router)
app.include_router(inventory_counts.main.router)
app.include_router(list_action.main.router)
app.include_router(list_catalog.main.router)
app.include_router(list_dgn.main.router)
app.include_router(list_event_type.main.router)
app.include_router(list_hypervisor.main.router)
app.include_router(list_machine_source.main.router)
app.include_router(list_machine_type.main.router)
app.include_router(list_os.main.router)
app.include_router(list_status.main.router)
app.include_router(product.main.router)
app.include_router(product_source_map.main.router)
app.include_router(product_target_map.main.router)
app.include_router(xd_farm.main.router)
# ----------------------------------------


# Redirect / -> Swagger-UI documentation
@app.get("/")
def main_function():
    """
    # Redirect
    to documentation (`/docs/`).
    """
    return RedirectResponse(url="/docs/")