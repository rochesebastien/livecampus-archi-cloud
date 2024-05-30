from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from app.controllers.base import db_instance

class Blog(db_instance.Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    articles = relationship('Article', back_populates='blog')


