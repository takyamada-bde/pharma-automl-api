from sqlalchemy import text
from sqlalchemy.orm import Session


def check_connection(session: Session) -> dict:
    """
    Check the connection to the database.

    Parameters
    ----------
    session : sqlalchemy.orm.Session
        SQLAlchemy session for database connection.

    Returns
    -------
    dict
        Dictionary containing the status and details of the connection.
    """
    try:
        session.execute(text("SELECT 1"))
        return {
            "Status": "Success",
            "Detail": "Connection to database is successful",
            "Host": session.bind.url.host,
            "Database": session.bind.url.database,
            "Query": session.bind.url.query,
        }
    except Exception as e:
        return {
            "Status": "Failed",
            "Detail": str(e),
        }
