from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class Article(BaseModel):
    title: str
    url: HttpUrl
    source: str
    published_at: datetime | None = None
    summary: str | None = None
    topics: list[str] = Field(default_factory=list)
    is_paywalled: bool | None = None
