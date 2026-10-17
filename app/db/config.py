from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    debug: bool = False
    database_name: str
    database_user: str
    database_password: str
    database_host: str = 'postgres'
    database_port: int = 5432
    database_schema: str = 'public'


class DevConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_file='.env.dev', env_file_encoding='utf-8'
    )


class ProdConfig(BaseConfig):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
