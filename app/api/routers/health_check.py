
from fastapi import Depends
from sqlalchemy.orm import Session

from .base import router
from api.crud.health_check import check_connection
from api.dependencies import get_db_session

HEALTH_CHECK_ROUTE = 'health-check'


@router.get(f'/{HEALTH_CHECK_ROUTE}', response_model=dict)
async def check_health(session: Session = Depends(get_db_session)):
    """
    Check the health of the application by verifying the database connection.

    Parameters
    ----------
    session : sqlalchemy.orm.Session
        SQLAlchemy session for database connection.
    Returns
    -------
    dict
        Dictionary containing the status and details of the connection.
    """
    return check_connection(session)
