# models/book.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
    publisher = relationship("Publisher", back_populates="books")
    reviews = relationship("Review", back_populates="book")
