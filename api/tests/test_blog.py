import unittest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.blog import Blog as BlogModel
from app.schemas.blog import BlogCreate
from app.controllers.base import SqlBase
from app.controllers.blog import BlogController

class TestBlogController(unittest.TestCase):

    def setUp(self):
        self.SQLALCHEMY_DATABASE_URL = f"sqlite:///tests/mock_database.db"
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        BlogModel.metadata.create_all(bind=self.engine)

        self.db_instance = SqlBase()
        self.db_instance.engine = self.engine
        self.db_instance.SessionLocal = self.SessionLocal

        self.blog_controller = BlogController()
        self.blog_controller.db_instance = self.db_instance
    
    def tearDown(self):
        BlogModel.metadata.drop_all(bind=self.engine)

    def test_read_blogs(self):
        with self.db_instance.get_db() as db:
            db.add(BlogModel(title="Test Blog", description="Test Description", topic="Test Topic"))
            db.commit()
        
        blogs = self.blog_controller.read_blogs(skip=0)
        self.assertEqual(len(blogs), 1)
        self.assertEqual(blogs[0].title, "Test Blog")

    def test_read_blog(self):
        with self.db_instance.get_db() as db:
            db.add(BlogModel(id=1, title="Test Blog", description="Test Description", topic="Test Topic"))
            db.commit()
        
        blog = self.blog_controller.read_blog(blog_id=1)
        self.assertEqual(blog.title, "Test Blog")

        with self.assertRaises(HTTPException):
            self.blog_controller.read_blog(blog_id=2)

    def test_create_blog(self):
        blog_create = BlogCreate(title="New Blog", description="New Description", topic="Test Topic")
        db_blog = self.blog_controller.create_blog(blog=blog_create)
        self.assertEqual(db_blog.title, "New Blog")

    def test_update_blog(self):
        with self.db_instance.get_db() as db:
            db.add(BlogModel(id=1, title="Old Blog", description="Old Description", topic="Old Topic"))
            db.commit()

        blog_update = BlogCreate(title="Updated Blog", description="Updated Description", topic="Test Topic")
        db_blog = self.blog_controller.update_blog(blog_id=1, blog=blog_update)
        self.assertEqual(db_blog.title, "Updated Blog")
        self.assertEqual(db_blog.description, "Updated Description")

        with self.assertRaises(HTTPException):
            self.blog_controller.update_blog(blog_id=2, blog=blog_update)

    def test_delete_blog(self):
        with self.db_instance.get_db() as db:
            db.add(BlogModel(id=1, title="Test Blog", description="Test Description",topic="Test Topic"))
            db.commit()

        db_blog = self.blog_controller.delete_blog(blog_id=1)
        self.assertEqual(db_blog.title, "Test Blog")

        with self.assertRaises(HTTPException):
            self.blog_controller.delete_blog(blog_id=2)

if __name__ == "__main__":
    unittest.main()
