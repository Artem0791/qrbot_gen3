from pydantic_settings import BaseSettings
from pydantic import BaseModel, AnyUrl


class Config(BaseSettings):
    bot_token: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


class QRCodeConfig(BaseModel):
    version: int = 1  # QR Code version: 1-40
    box_size: int = 20  # Size of each box in pixels
    border: int = 4  # Border thickness in boxes


class UserMessage(BaseModel):
    url: str = AnyUrl
