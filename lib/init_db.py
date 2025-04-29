# init_db.py

from models.book import Book
from models.loan import Loan
from models.member import Member

def init_db():
    Book.create_table()
    Member.create_table()
    Loan.create_table()

if __name__ == "__main__":
    init_db()
