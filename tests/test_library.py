from datetime import date
 
import pytest
 
from library import Library
 
 
@pytest.fixture
def lib():
    library = Library()
    library.add_book("111", "Test Book", "Ada Lovelace")
    return library
 
 
def test_borrow_sets_due_date(lib):
    loan = lib.borrow("111", "M1", today=date(2026, 1, 1))
    assert loan.due_on == date(2026, 1, 15)
 
 
def test_cannot_borrow_twice(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))
    with pytest.raises(ValueError):
        lib.borrow("111", "M2", today=date(2026, 1, 2))
 
 
def test_return_makes_book_available(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))
    lib.return_book("111", today=date(2026, 1, 5))
    assert lib.books["111"].available
 
