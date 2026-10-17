from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.dependencies import get_config
from api.routers import base

config = get_config()
app = FastAPI(debug=config.debug)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/media', StaticFiles(directory='media'), name='media')

app.include_router(
    base.router,
    prefix='/api'
)

if config.debug:
    from debug_toolbar.middleware import DebugToolbarMiddleware
    app.add_middleware(
        DebugToolbarMiddleware,
        #panels=['debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel']
    )
