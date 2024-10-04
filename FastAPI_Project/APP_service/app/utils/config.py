"""
Config file provides the settings/configuration needed for that specific launched instance
"""
from typing import List

from pydantic import BaseSettings, Field


class BaseConf(BaseSettings):
    """
    Default params for all env
    """
    PROJECT_NAME: str = "APP-SERVICE"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    ALLOWED_HOSTS: List[str] = Field(
        default=[],
        description="To restrict requests coming from only few hosts or to allow all by passing '*'"
    )


settings = BaseConf()
