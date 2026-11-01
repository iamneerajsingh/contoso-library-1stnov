"""Core lending logic for the Contoso Library Lending Service."""
from dataclasses import dataclass
from datetime import date, timedelta
 
LOAN_PERIOD_DAYS = 14
GRACE_PERIOD_DAYS = 2
FINE_PER_LATE_DAY_RUPEES = 10
MAX_FINE_RUPEES = 500
 
 
@dataclass
class Book:
    isbn: str
    title: str
    author: str
    available: bool = True
 
 
@dataclass
class Loan:
    isbn: str
    member_id: str
    borrowed_on: date
    due_on: date
    returned_on: date | None = None
    fine: int = 0
 
 
class Library:
    def __init__(self):
        self.books: dict[str, Book] = {}
        self.loans: list[Loan] = []
 
    def add_book(self, isbn, title, author):
        if isbn in self.books:
            raise ValueError(f"Book {isbn} already exists")
        self.books[isbn] = Book(isbn, title, author)
        return self.books[isbn]
 
    def borrow(self, isbn, member_id, today=None):
        today = today or date.today()
        book = self.books.get(isbn)
        if book is None:
            raise KeyError(f"Unknown book {isbn}")
        if not book.available:
            raise ValueError(f"Book {isbn} is already on loan")
        book.available = False
        loan = Loan(isbn, member_id, today, today + timedelta(days=LOAN_PERIOD_DAYS))
        self.loans.append(loan)
        return loan
 
    def return_book(self, isbn, today=None):
        today = today or date.today()
        for loan in self.loans:
            if loan.isbn == isbn and loan.returned_on is None:
                loan.returned_on = today
                late_days = (today - loan.due_on).days
                chargeable_days = max(0, late_days - GRACE_PERIOD_DAYS)
                loan.fine = min(
                    chargeable_days * FINE_PER_LATE_DAY_RUPEES,
                    MAX_FINE_RUPEES,
                )
                self.books[isbn].available = True
                return loan
        raise ValueError(f"Book {isbn} is not on loan")
