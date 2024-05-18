# models/review.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="reviews")
