from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

DB_DIR = Path(__file__).resolve().parent

class BaseConfig(BaseSettings):
    debug: bool
    database_name: str
    database_user: str
    database_password: str
    database_host: str = 'postgres'
    database_port: int = 5432
    database_schema: str = 'public'


class DevConfig(BaseConfig):
    debug: bool = True
    model_config = SettingsConfigDict(
        env_file=DB_DIR / '.env.dev', env_file_encoding='utf-8'
    )


class ProdConfig(BaseConfig):
    debug: bool = False
    model_config = SettingsConfigDict(
        env_file=DB_DIR / '.env', env_file_encoding='utf-8'
    )
