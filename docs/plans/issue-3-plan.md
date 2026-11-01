## Goal
Add `Library.overdue_loans(today)` to return loans that have not been returned and whose due date is before `today`.

## Assumptions
- A loan due on `today` is not overdue; only `due_on < today` qualifies.
- The method returns a list in the same order as `Library.loans`.
- The request is for the library method described by the success criteria, not a scheduled job or HTTP report endpoint.

## Steps
1. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/library.py` with `Library.overdue_loans(today)`, filtering to unreturned loans whose due date is before the supplied date.
2. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/tests/test_library.py` with fixed-date tests for overdue loans, loans due today or later, returned loans, and an empty result.
3. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/docs/agent-log/issue-3.md` with implementation decisions and validation results.

## Tests to add
- A loan due before `today` and not returned is included.
- A loan due on `today` or after it is excluded.
- A loan returned before `today` is excluded even if its due date has passed.
- No qualifying loans produces an empty list.

## Risks and rollback
- An inclusive due-date comparison could report loans as overdue on their due date; test that boundary explicitly.
- Returned loans must be excluded regardless of their due date.
- Roll back the localized changes to `library.py`, `tests/test_library.py`, and `docs/agent-log/issue-3.md` if they introduce regressions.

## Out of scope
- Scheduling or delivering a weekly report.
- Adding an HTTP endpoint or changing the Flask API.
- Persisting overdue reports or changing loan/return behavior.

## Open questions for the human reviewer
- The issue title says “Weekly overdue report,” but the stated success criteria specify only `Library.overdue_loans(today)`. Is a scheduled or externally delivered report also required, or should implementation remain limited to the library method?

Status: AWAITING APPROVAL
