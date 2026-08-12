from pathlib import Path

from sqlalchemy.orm import Session

from db.session import get_session


async def get_session_prod():
    try:
        session = get_session('.env')
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()


async def get_session_dev():
    try:
        session = get_session('.env.dev')
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
