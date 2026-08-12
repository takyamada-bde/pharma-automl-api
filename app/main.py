from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routers import base

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(
    base.router_dev,
    prefix="/api-dev",
    tags=["Development"],
)
app.include_router(
    base.router,
    prefix="/api",
    tags=["Production"],
)
