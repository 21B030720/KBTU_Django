# create_tables.py
from database import Base, engine
from models.author import Author
from models.book import Book
from models.genre import Genre
from models.publisher import Publisher
from models.member import Member
from models.loan import Loan
from models.staff import Staff
from models.library import Library
from models.section import Section
from models.review import Review

Base.metadata.create_all(bind=engine)
