import unittest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.controllers.article import ArticleController
from app.schemas.article import ArticleCreate
from app.models.article import Article as ArticleModel
from app.models.base import Base

# mock database
DATABASE_URL = "sqlite:///./mock_database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestArticleController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)

    def setUp(self):
        self.db = SessionLocal()
        self.article_controller = ArticleController()

    def tearDown(self):
        self.db.close()

    def test_create_article(self):
        article_data = ArticleCreate(title="Test Title", content="Test Content", ranking=1, blog_id=1)
        article = self.article_controller.create_article(article_data)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")

    def test_read_articles(self):
        articles = self.article_controller.read_articles(skip=0)
        self.assertIsInstance(articles, list)

    def test_read_article_not_found(self):
        with self.assertRaises(HTTPException) as context:
            self.article_controller.read_article(999)
        self.assertEqual(context.exception.status_code, 404)

    def test_update_article(self):
        article_data = ArticleCreate(title="Updated Title", content="Updated Content", ranking=1, blog_id=1)
        article = self.article_controller.create_article(article_data)
        updated_article_data = ArticleCreate(title="New Title", content="New Content", ranking=2, blog_id=2)
        updated_article = self.article_controller.update_article(article.id, updated_article_data)
        self.assertEqual(updated_article.title, "New Title")
        self.assertEqual(updated_article.content, "New Content")

    def test_delete_article(self):
        article_data = ArticleCreate(title="Test Title", content="Test Content", ranking=1, blog_id=1)
        article = self.article_controller.create_article(article_data)
        deleted_article = self.article_controller.delete_article(article.id)
        self.assertEqual(deleted_article.id, article.id)

if __name__ == '__main__':
    unittest.main()
