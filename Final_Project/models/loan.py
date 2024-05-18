# models/loan.py
from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    member_id = Column(Integer, ForeignKey('members.id'))
    loan_date = Column(Date)
    return_date = Column(Date)
    book = relationship("Book")
    member = relationship("Member", back_populates="loans")
