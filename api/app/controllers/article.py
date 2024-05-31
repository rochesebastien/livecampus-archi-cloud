from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.article import Article as ArticleModel
from app.schemas.article import ArticleCreate, Article
from app.controllers.base import SqlBase, db_instance

class ArticleController(SqlBase):

    def __init__(self):
        super().__init__()

    def read_articles(self, skip: int = 0):
        db = next(db_instance.get_db())
        articles = db.query(ArticleModel).offset(skip).all()
        return articles

    def read_article(self, article_id: int):
        db = next(db_instance.get_db())
        article = db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
        if article is None:
            raise HTTPException(status_code=404, detail="Article non trouvé")
        return article

    def create_article(self, article: ArticleCreate):
        db = next(db_instance.get_db())
        db_article = ArticleModel(
            title=article.title, content=article.content, ranking=article.ranking, blog_id=article.blog_id)
        db.add(db_article)
        db.commit()
        db.refresh(db_article)
        return db_article

    def update_article(self, article_id: int, article: ArticleCreate):
        db = next(db_instance.get_db())
        db_article = db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
        if db_article is None:
            raise HTTPException(status_code=404, detail="Article non trouvé")
        db_article.title = article.title
        db_article.content = article.content
        db_article.ranking = article.ranking
        db_article.blog_id = article.blog_id
        db.commit()
        db.refresh(db_article)
        return db_article

    def delete_article(self, article_id: int):
        db = next(db_instance.get_db())
        db_article = db.query(ArticleModel).filter(ArticleModel.id == article_id).first()
        if db_article is None:
            raise HTTPException(status_code=404, detail="Article non trouvé")
        db.delete(db_article)
        db.commit()
        return db_article

