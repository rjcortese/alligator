from functools import lru_cache
from pydantic import (
    BaseSettings,
    PositiveInt,
    SecretStr,
)


class Settings(BaseSettings):
    db_host: str
    db_port: PositiveInt
    db_username: str
    db_password: SecretStr


@lru_cache
def get_settings():
    return Settings()
