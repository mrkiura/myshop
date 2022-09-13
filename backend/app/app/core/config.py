import pathlib

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator, Field
from typing import List, Optional, Union


ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    BACKEND_CORS_ORIGIN_REGEX: Optional[
        str
    ] = "https.*\.(netlify.app|herokuapp.com)"  # noqa: W605

    SQLALCHEMY_DATABASE_URI: str = Field(..., env="DATABASE_URL")
    FIRST_SUPERUSER: EmailStr = "admin@shopapi.com"
    FIRST_SUPERUSER_PW: str = "CHANGEME"

    class Config:
        case_sensitive = True


settings = Settings()

db_uri = settings.SQLALCHEMY_DATABASE_URI

if db_uri.startswith("postgres://"):
    settings.SQLALCHEMY_DATABASE_URI = db_uri.replace("postgres://", "postgresql://", 1)