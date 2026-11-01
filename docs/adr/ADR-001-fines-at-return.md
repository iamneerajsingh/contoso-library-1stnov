# ADR-001: Fines are calculated at return time
 
Status: Accepted
Date: 2026-11-02
Context: Fines could be calculated nightly or when a book is returned.
Decision: Calculate when the book is returned, in Library.return_book.
Consequences: No scheduler is needed. The weekly overdue report (issue #3) must compute fines on the fly.
