import unittest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.controllers.blog import BlogController
from app.schemas.blog import BlogCreate
from app.models.blog import Blog as BlogModel
from app.models.base import Base

# Configuration de la base de données SQLite fictive
DATABASE_URL = "sqlite:///./mock_database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestBlogController(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)

    def setUp(self):
        self.db = SessionLocal()
        self.blog_controller = BlogController()

    def tearDown(self):
        self.db.close()

    def test_create_blog(self):
        blog_data = BlogCreate(title="Test Blog", topic="Test Topic", date="2024-01-01")
        blog = self.blog_controller.create_blog(blog_data)
        self.assertEqual(blog.title, "Test Blog")
        self.assertEqual(blog.topic, "Test Topic")

    def test_read_blogs(self):
        blogs = self.blog_controller.read_blogs(skip=0)
        self.assertIsInstance(blogs, list)

    def test_read_blog_not_found(self):
        with self.assertRaises(HTTPException) as context:
            self.blog_controller.read_blog(999)
        self.assertEqual(context.exception.status_code, 404)

    def test_update_blog(self):
        blog_data = BlogCreate(title="Initial Title", topic="Initial Topic", date="2024-01-01")
        blog = self.blog_controller.create_blog(blog_data)
        updated_blog_data = BlogCreate(title="Updated Title", topic="Updated Topic", date="2024-01-02")
        updated_blog = self.blog_controller.update_blog(blog.id, updated_blog_data)
        self.assertEqual(updated_blog.title, "Updated Title")
        self.assertEqual(updated_blog.topic, "Updated Topic")

    def test_delete_blog(self):
        blog_data = BlogCreate(title="Test Blog", topic="Test Topic", date="2024-01-01")
        blog = self.blog_controller.create_blog(blog_data)
        deleted_blog = self.blog_controller.delete_blog(blog.id)
        self.assertEqual(deleted_blog.id, blog.id)

if __name__ == '__main__':
    unittest.main()
