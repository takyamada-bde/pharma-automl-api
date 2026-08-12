from pathlib import Path
from typing import Union

from dotenv import dotenv_values
from sqlalchemy import create_engine, engine, URL
from sqlalchemy.orm import sessionmaker, Session

DB_DIR = Path(__file__).resolve().parent


def get_engine(dotenv_path: Union[Path, str]) -> engine.Engine:
    """
    Create a SQLAlchemy engine for database connection.

    Parameters
    ----------
    dotenv_path : Union[pathlib.Path, str]
        Path to the .env file containing database configuration.
        DB_DIR is the base directory where the .env files are located.

    Returns
    -------
    engine : sqlalchemy.engine.Engine
        SQLAlchemy engine for database connection.
    """
    config = dotenv_values(DB_DIR / dotenv_path)
    url_object = URL.create(
        "postgresql+psycopg",
        username=config["POSTGRES_USER"],
        password=config["POSTGRES_PASSWORD"],  # plain (unescaped) text
        host=config.get("POSTGRES_HOST", "postgres"),
        port=config.get("POSTGRES_PORT", "5432"),
        database=config.get("POSTGRES_DB", "postgres"),
        query={"options": f"-c search_path={config.get('POSTGRES_SCHEMA', 'public')}"},
    )
    engine = create_engine(url_object)
    return engine


def get_sessionmaker(dotenv_path: Union[Path, str]) -> sessionmaker:
    """
    Create a SQLAlchemy sessionmaker for database connection.

    Parameters
    ----------
    dotenv_path : Union[pathlib.Path, str]
        Path to the .env file containing database configuration.

    Returns
    -------
    SessionLocal : sqlalchemy.orm.sessionmaker
        SQLAlchemy sessionmaker for database connection.
    """
    engine = get_engine(dotenv_path)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


def get_session(dotenv_path: Union[Path, str]) -> Session:
    """
    Create a SQLAlchemy session for database connection.

    Parameters
    ----------
    dotenv_path : Union[pathlib.Path, str]
        Path to the .env file containing database configuration.

    Returns
    -------
    session : sqlalchemy.orm.Session
        SQLAlchemy session for database connection.
    """
    SessionLocal = get_sessionmaker(dotenv_path)
    session = SessionLocal()
    return session
