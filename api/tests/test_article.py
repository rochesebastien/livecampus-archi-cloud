import unittest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.article import Article as ArticleModel
from app.schemas.article import ArticleCreate
from app.controllers.base import SqlBase
from app.controllers.article import ArticleController

class TestArticleController(unittest.TestCase):

    def setUp(self):

        self.SQLALCHEMY_DATABASE_URL = f"sqlite:///tests/mock_database.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        ArticleModel.metadata.create_all(bind=self.engine)
        self.db_instance = SqlBase()
        self.db_instance.engine = self.engine
        self.db_instance.SessionLocal = self.SessionLocal
        self.article_controller = ArticleController()
        self.article_controller.db_instance = self.db_instance

    def tearDown(self):
        ArticleModel.metadata.drop_all(bind=self.engine)

    def test_read_articles(self):
        with self.db_instance.get_db() as db:
            db.add(ArticleModel(title="Test Article", content="Test Content", ranking=1, blog_id=1))
            db.commit()
        
        articles = self.article_controller.read_articles(skip=0)
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].title, "Test Article")

    def test_read_article(self):
        with self.db_instance.get_db() as db:
            db.add(ArticleModel(id=1, title="Test Article", content="Test Content", ranking=1, blog_id=1))
            db.commit()
        
        article = self.article_controller.read_article(article_id=1)
        self.assertEqual(article.title, "Test Article")

        with self.assertRaises(HTTPException):
            self.article_controller.read_article(article_id=2)

    def test_create_article(self):
        article_create = ArticleCreate(title="New Article", content="New Content", ranking=2, blog_id=1)
        db_article = self.article_controller.create_article(article=article_create)
        self.assertEqual(db_article.title, "New Article")

    def test_update_article(self):
        with self.db_instance.get_db() as db:
            db.add(ArticleModel(id=1, title="Old Article", content="Old Content", ranking=1, blog_id=1))
            db.commit()

        article_update = ArticleCreate(title="Updated Article", content="Updated Content", ranking=3, blog_id=2)
        db_article = self.article_controller.update_article(article_id=1, article=article_update)
        self.assertEqual(db_article.title, "Updated Article")
        self.assertEqual(db_article.content, "Updated Content")

        with self.assertRaises(HTTPException):
            self.article_controller.update_article(article_id=2, article=article_update)

    def test_delete_article(self):
        with self.db_instance.get_db() as db:
            db.add(ArticleModel(id=1, title="Test Article", content="Test Content", ranking=1, blog_id=1))
            db.commit()

        db_article = self.article_controller.delete_article(article_id=1)
        self.assertEqual(db_article.title, "Test Article")

        with self.assertRaises(HTTPException):
            self.article_controller.delete_article(article_id=2)

if __name__ == "__main__":
    unittest.main()
