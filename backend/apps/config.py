from functools import lru_cache
from pydantic_settings import BaseSettings
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):

    # Application settings
    APP_NAME: str = "campus-security"
    APP_VERSION: str = "0.1.0"

    class Config:
        env_file = os.getenv('ENV_FILE', 'local.env')
        extra = 'allow'


@lru_cache()
def get_settings():
    print(Settings().model_dump())
    return Settings()
