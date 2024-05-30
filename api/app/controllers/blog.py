from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.blog import Blog as BlogModel
from app.models.article import Article as ArticleModel
from app.schemas.blog import Blog, BlogCreate
from app.schemas.article import Article, ArticleCreate
from app.controllers.base import SqlBase, db_instance

class BlogController(SqlBase):

    def __init__(self):
        super().__init__()

    def read_blogs(self, skip: int = 0):
        db = next(db_instance.get_db())
        blogs = db.query(BlogModel).offset(skip).all()
        return blogs

    def read_blog(self, blog_id: int):
        db = next(db_instance.get_db())
        blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog non trouvé")
        return blog

    def create_blog(self, blog: BlogCreate):
        db = next(db_instance.get_db())
        db_blog = BlogModel(title=blog.title, topic=blog.topic, date=blog.date)
        db.add(db_blog)
        db.commit()
        db.refresh(db_blog)
        return db_blog

    def update_blog(self, blog_id: int, blog: BlogCreate):
        db = next(db_instance.get_db())
        db_blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if db_blog is None:
            raise HTTPException(status_code=404, detail="Blog non trouvé")
        db_blog.title = blog.title
        db_blog.topic = blog.topic
        db_blog.date = blog.date
        db.commit()
        db.refresh(db_blog)
        return db_blog

    def delete_blog(self, blog_id: int):
        db = next(db_instance.get_db())
        db_blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if db_blog is None:
            raise HTTPException(status_code=404, detail="Blog non trouvé")
        db.delete(db_blog)
        db.commit()
        return db_blog

