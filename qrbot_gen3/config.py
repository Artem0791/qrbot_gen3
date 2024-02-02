from pydantic_settings import BaseSettings
from pydantic import BaseModel, AnyUrl


class Config(BaseSettings):
    bot_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


