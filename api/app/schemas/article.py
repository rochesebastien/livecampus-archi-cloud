from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    content: str
    ranking: int
    blog_id: int

class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id: int

    class Config:
        orm_mode = True
