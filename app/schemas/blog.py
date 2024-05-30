from datetime import date
from typing import List
from pydantic import BaseModel
from .article import Article

class BlogBase(BaseModel):
    title: str
    topic: str
    date: date

class BlogCreate(BlogBase):
    pass

class Blog(BlogBase):
    id: int
    articles: List[Article] = []

    class Config:
        orm_mode = True
