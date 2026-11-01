## Goal
Calculate overdue fines when a book is returned: 10 integer rupees per late day after a two-day grace period, capped at 500 rupees. Returns on or before the due date have no fine. Keep the borrowing API response and persistence model unchanged.

## Assumptions
- Late days are calendar days after the due date; subtract the two grace days before calculating the fine.
- Fine calculation belongs in `Library.return_book`, which already receives an optional `today` date and returns the updated `Loan`.
- The fine should be available on the returned loan as an integer amount in rupees.

## Steps
1. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/library.py` to add a fine amount to `Loan` and calculate it during return using the late-day formula, capped at 500.
2. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/tests/test_library.py` with fixed-date unit tests for an on-time return, a return within the grace period, a chargeable late return, and the 500-rupee cap.
3. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/docs/agent-log/issue-1.md` with the implementation decisions and validation results.

## Tests to add
- A return on the due date has a fine of zero.
- A return two days after the due date has a fine of zero.
- A return three days after the due date has a fine of 10 rupees.
- A sufficiently late return has a fine of exactly 500 integer rupees, verifying the cap.
- Existing return behavior still marks the book available and returns the updated loan.

## Risks and rollback
- Off-by-one errors around the due date and grace-period boundary could overcharge or undercharge members; test both boundaries with fixed dates.
- If adding a field to `Loan` affects construction or callers, keep it defaulted to zero and assign it only when returning a loan.
- Represent all fine amounts as integers; do not use floating-point values for rupees.
- Roll back the localized changes in `library.py`, `tests/test_library.py`, and `docs/agent-log/issue-1.md` if they cause regressions.

## Out of scope
- Database or persistent fine tracking.
- Changes to the borrowing API response.
- Introducing or changing API endpoints for returning books or collecting payment.

## Open questions for the human reviewer
- Should the computed fine be exposed as a field on the returned `Loan`, as assumed here, or should the return operation expose it another way?

Status: AWAITING APPROVAL
