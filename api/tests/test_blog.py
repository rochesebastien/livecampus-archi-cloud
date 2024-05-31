import unittest
from unittest.mock import patch, MagicMock
from app.controllers.blog import BlogController
from app.models.blog import Blog as BlogModel
from app.schemas.blog import BlogCreate
from fastapi import HTTPException

class TestBlogController(unittest.TestCase):

    @patch('app.controllers.blog.db_instance')
    def setUp(self, mock_db_instance):
        self.controller = BlogController()
        self.mock_db = MagicMock()
        mock_db_instance.get_db.return_value = iter([self.mock_db])

    def test_read_blogs(self):
        self.controller.read_blogs()
        self.mock_db.query.assert_called_with(BlogModel)
        self.mock_db.query().offset().all.assert_called()

    def test_read_article(self):
        article = ArticleModel(id=1, title="Test Article", content="Test Content")
        self.mock_db.query.return_value.filter.return_value.first.return_value = article
        result = self.controller.read_article(1)

        self.mock_db.query.assert_called_with(ArticleModel)
        self.assertEqual(result, article)

    def test_read_blog_not_found(self):
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.read_blog(1)

    def test_create_blog(self):
        blog = BlogCreate(title="Test", topic="Test topic", date="2022-01-01")
        self.controller.create_blog(blog)
        self.mock_db.add.assert_called()
        self.mock_db.commit.assert_called()
        self.mock_db.refresh.assert_called()

    def test_update_blog(self):
        blog = BlogCreate(title="Test", topic="Test topic", date="2022-01-01")
        self.mock_db.query().filter().first.return_value = BlogModel()
        self.controller.update_blog(1, blog)
        self.mock_db.query.assert_called_with(BlogModel)
        self.mock_db.query().filter.assert_called()
        self.mock_db.commit.assert_called()
        self.mock_db.refresh.assert_called()

    def test_update_blog_not_found(self):
        blog = BlogCreate(title="Test", topic="Test topic", date="2022-01-01")
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.update_blog(1, blog)

    def test_delete_blog(self):
        self.mock_db.query().filter().first.return_value = BlogModel()
        self.controller.delete_blog(1)
        self.mock_db.query.assert_called_with(BlogModel)
        self.mock_db.query().filter.assert_called()
        self.mock_db.delete.assert_called()
        self.mock_db.commit.assert_called()

    def test_delete_blog_not_found(self):
        self.mock_db.query().filter().first.return_value = None
        with self.assertRaises(HTTPException):
            self.controller.delete_blog(1)

if __name__ == '__main__':
    unittest.main()