from datetime import date as DateType
from typing import List
from pydantic import BaseModel
from .article import Article

class BlogBase(BaseModel):
    title: str
    topic: str
    date: DateType = DateType.today()

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    articles: List[Article] = []

    class Config:
        from_attributes = True
