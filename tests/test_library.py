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
    loan = lib.borrow("111", "M1", today=date(2026, 1, 1))
    returned_loan = lib.return_book("111", today=date(2026, 1, 5))

    assert lib.books["111"].available
    assert returned_loan is loan
    assert returned_loan.returned_on == date(2026, 1, 5)


def test_return_on_due_date_has_no_fine(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))

    loan = lib.return_book("111", today=date(2026, 1, 15))

    assert loan.fine == 0


def test_return_within_grace_period_has_no_fine(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))

    loan = lib.return_book("111", today=date(2026, 1, 17))

    assert loan.fine == 0


def test_return_three_days_late_has_ten_rupee_fine(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))

    loan = lib.return_book("111", today=date(2026, 1, 18))

    assert loan.fine == 10


def test_late_return_fine_is_capped_at_500_rupees(lib):
    lib.borrow("111", "M1", today=date(2026, 1, 1))

    loan = lib.return_book("111", today=date(2026, 6, 1))

    assert loan.fine == 500
    assert isinstance(loan.fine, int)
 
