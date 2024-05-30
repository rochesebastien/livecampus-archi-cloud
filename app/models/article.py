from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.controllers.base import db_instance

class Article(db_instance.Base):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    ranking = Column(Integer, nullable=False)
    blog_id = Column(Integer, ForeignKey('blog.id'))
    blog = relationship('Blog', back_populates='articles')

