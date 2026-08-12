
from fastapi import Depends
from sqlalchemy.orm import Session

from .base import router, router_dev
from api.crud.health_check import check_connection
from api.dependencies import get_session_prod, get_session_dev

HEALTH_CHECK_ROUTE = "health-check"


@router.get(f"/{HEALTH_CHECK_ROUTE}", response_model=dict)
async def check_health(session: Session = Depends(get_session_prod)):
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


@router_dev.get(f"/{HEALTH_CHECK_ROUTE}", response_model=dict)
async def check_health_dev(session: Session = Depends(get_session_dev)):
    """
    Check the health of the development application by verifying the database connection.

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
