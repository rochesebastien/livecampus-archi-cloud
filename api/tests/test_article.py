import unittest
from unittest.mock import patch, MagicMock
from app.controllers.article import ArticleController
from app.models.article import Article as ArticleModel
from app.schemas.article import ArticleCreate
from fastapi import HTTPException

class TestArticleController(unittest.TestCase):

    @patch('app.controllers.article.db_instance')
    def setUp(self, mock_db_instance):
        self.controller = ArticleController()
        self.mock_db = MagicMock()
        mock_db_instance.get_db.return_value = iter([self.mock_db])

    def test_read_articles(self):
        self.controller.read_articles()
        self.mock_db.query.assert_called_with(ArticleModel)
        self.mock_db.query().offset().all.assert_called()

    def test_read_article(self):
        self.mock_db.query().filter().first.return_value = ArticleModel()
        self.controller.read_article(1)
        self.mock_db.query.assert_called_with(ArticleModel)
        self.mock_db.query().filter.assert_called()

    def test_read_article_not_found(self):
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.read_article(1)

    def test_create_article(self):
        article = ArticleCreate(title="Test", content="Test content", ranking=1, blog_id=1)
        self.controller.create_article(article)
        self.mock_db.add.assert_called()
        self.mock_db.commit.assert_called()
        self.mock_db.refresh.assert_called()

    def test_update_article(self):
        article = ArticleCreate(title="Test", content="Test content", ranking=1, blog_id=1)
        self.mock_db.query().filter().first.return_value = ArticleModel()
        self.controller.update_article(1, article)
        self.mock_db.query.assert_called_with(ArticleModel)
        self.mock_db.query().filter.assert_called()
        self.mock_db.commit.assert_called()
        self.mock_db.refresh.assert_called()

    def test_update_article_not_found(self):
        article = ArticleCreate(title="Test", content="Test content", ranking=1, blog_id=1)
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.update_article(1, article)

    def test_delete_article(self):
        self.mock_db.query().filter().first.return_value = ArticleModel()
        self.controller.delete_article(1)
        self.mock_db.query.assert_called_with(ArticleModel)
        self.mock_db.query().filter.assert_called()
        self.mock_db.delete.assert_called()
        self.mock_db.commit.assert_called()

    def test_delete_article_not_found(self):
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.delete_article(1)

if __name__ == '__main__':
    unittest.main()