import os

from sqlalchemy.orm import Session

from db.config import DevConfig, ProdConfig
from db.session import get_session


def get_config():
    env = os.getenv('APP_ENV', 'dev')

    if env.lower() in ['prod', 'production']:
        return ProdConfig()
    else:
        return DevConfig()


async def get_db_session() -> Session:
    config = get_config()
    try:
        session = get_session(config)
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
