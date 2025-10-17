from pydantic import BaseModel
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)
from pathlib import Path

BASE_URL = Path(__file__).parent.parent


class DatabaseConfig(BaseModel):
    engine: str
    name: str
    user:str
    password: str
    host:str
    port: int


class SettingsApp(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(BASE_URL / ".env.template", BASE_URL / ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
    )
    db: DatabaseConfig


settings_app = SettingsApp()