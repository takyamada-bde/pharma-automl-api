from pathlib import Path
from typing import Union

from sqlalchemy import create_engine, engine, URL
from sqlalchemy.orm import sessionmaker, Session

from db.config import BaseConfig, DevConfig, ProdConfig


def get_engine(config: BaseConfig) -> engine.Engine:
    """
    Create a SQLAlchemy engine for database connection.

    Parameters
    ----------
    config : BaseConfig
        Database configuration object.

    Returns
    -------
    engine : sqlalchemy.engine.Engine
        SQLAlchemy engine for database connection.
    """
    url_object = URL.create(
        'postgresql+psycopg',
        username=config.database_user,
        password=config.database_password,  # plain (unescaped) text
        host=config.database_host,
        port=config.database_port,
        database=config.database_name,
        query={'options': f'-c search_path={config.database_schema}'},
    )
    engine = create_engine(url_object)
    return engine


def get_sessionmaker(config: BaseConfig) -> sessionmaker:
    """
    Create a SQLAlchemy sessionmaker for database connection.

    Parameters
    ----------
    config : BaseConfig
        Database configuration object.

    Returns
    -------
    SessionLocal : sqlalchemy.orm.sessionmaker
        SQLAlchemy sessionmaker for database connection.
    """
    engine = get_engine(config)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


def get_session(config: BaseConfig) -> Session:
    """
    Create a SQLAlchemy session for database connection.

    Parameters
    ----------
    config : BaseConfig
        Database configuration object.

    Returns
    -------
    session : sqlalchemy.orm.Session
        SQLAlchemy session for database connection.
    """
    SessionLocal = get_sessionmaker(config)
    session = SessionLocal()
    return session
