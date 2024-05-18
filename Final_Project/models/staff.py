# models/staff.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    library_id = Column(Integer, ForeignKey('libraries.id'))
    library = relationship("Library", back_populates="staff")
