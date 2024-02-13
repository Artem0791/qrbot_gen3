from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Telegram(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    bot_token: str = Field('BOT_TOKEN')


class Config(BaseSettings):
    tg: Telegram = Telegram()