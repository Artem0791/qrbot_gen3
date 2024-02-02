from pydantic import BaseModel, AnyUrl


class UserMessage(BaseModel):
    url: str = AnyUrl
