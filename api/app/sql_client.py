import app

from app.controllers.base import db_instance
from app.models.blog import Blog
from app.models.article import Article
from app.controllers.blog import BlogController
from app.controllers.article import ArticleController

class SqlClient():

    def __init__(self):
        self.sql = db_instance.Base.metadata.create_all(bind=db_instance.engine)
        self.article_controller = ArticleController()
        self.blog_controller = BlogController()
    
    def get_articles(self):
        return self.article_controller.read_articles()
    
    def get_article(self, article_id):
        return self.article_controller.read_article(article_id)

    def create_article(self, article):
        return self.article_controller.create_article(article)
        

    def update_article(self, article_id, article):
        return self.article_controller.update_article(article_id, article)

    def delete_article(self, article_id):
        return self.article_controller.delete_article(article_id)
        

    def get_blogs(self):
        return self.blog_controller.read_blogs()

    def get_blog(self):
        return self.blog_controller.read_blog()

    def create_blog(self):
        return self.blog_controller.create_blog()
    
    def update_blog(self, blog_id, blog):
        return self.blog_controller.update_blog(blog_id, blog) 

    def delete_blog(self, blog_id):
        return self.blog_controller.delete_blog(blog_id)
