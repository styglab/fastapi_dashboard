# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    '''
    database_hostname: str = os.environ.get("DATABASE_HOSTNAME")
    database_port: int = os.environ.get("DATABASE_PORT")
    database_password: str = os.environ.get("DATABASE_PASSWORD")
    database_name: str = os.environ.get("DATABASE_NAME")
    database_username: str = os.environ.get("DATABASE_USERNAME")
    secret_key: str = os.environ.get("SECRET_KEY")
    algorithm: str = os.environ.get("ALGORITHM")
    debugging: int = os.environ.get("DEBUGGING")
    access_token_expire_minutes: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    '''
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    debugging: int
    access_token_expire_minutes: int

    class Config:
        env_file = "./.env"


settings = Settings()