## Goal
Add search by author for issue #2 while preserving existing lending behavior. This draft is based only on the user's description, "search by author"; the GitHub issue body could not be retrieved with the available tools. Confirm the issue's acceptance criteria before approving implementation.

## Assumptions
- `library.py` owns search logic; `app.py` only translates HTTP requests and responses.
- Books already have an `author` field, and `GET /books` currently returns all books with their existing fields.
- No issue #2 plan or agent log currently exists.
- Matching rules and the HTTP interface are not assumed; they require reviewer decisions below.

## Steps
1. Update `docs/plans/issue-2-plan.md` after reading the full issue and resolving the open questions. Obtain approval before changing application code or tests.
2. Update `library.py` with an author-search method using the approved matching and input rules. Return matching books without mutating books, loans, or availability.
3. Update `app.py` to expose the approved search interface. If the reviewer approves an optional author filter on `GET /books`, preserve the unfiltered response when that parameter is absent. Keep matching logic in `library.py` and follow the existing JSON error convention for rejected input.
4. Update `tests/test_library.py` with deterministic unit tests for the approved matching rules and preservation of lending state. Do not weaken existing tests.
5. Add `tests/test_app.py` with Flask test-client coverage of the approved HTTP contract, using an isolated library fixture so tests do not change global application state.
6. Update `README.md` to document the approved interface, matching behavior, input handling, and a request example.
7. Create `docs/agent-log/issue-2.md` to record approved decisions, completed steps, and the results of `ruff check .` and `pytest --cov=library --cov-fail-under=80`. Run these checks during implementation, not this planning-only task.

## Tests to add
- Matching authors return the expected books, including multiple books by one author.
- A nonmatching author and an empty catalogue return the approved no-results response.
- Exact versus partial matching, case differences, and whitespace follow the approved rules.
- Missing, empty, whitespace-only, and repeated author parameters follow the approved HTTP contract.
- Search does not modify book availability or loan state; borrowed books follow the approved inclusion rule.
- HTTP results preserve the approved book response fields and ordering.
- If search extends `GET /books`, requests without an author parameter retain the current full-catalogue response.
- Existing borrowing and return tests continue to pass, including the 14-day loan period.

## Risks and rollback
- Unspecified matching or input rules could produce an API that differs from the issue; resolve them before implementation.
- Filtering could unintentionally change unfiltered listing, response shape, or ordering; protect these behaviors with API tests.
- Tests using the module-level library could leak state; isolate and restore it with pytest fixtures.
- Roll back only issue #2 implementation changes in `library.py`, `app.py`, `tests/test_library.py`, `tests/test_app.py`, and `README.md` if regressions occur; retain the decision history in `docs/agent-log/issue-2.md`.

## Out of scope
- Changing the 14-day loan period.
- Fine calculation, fine collection, or the weekly overdue report.
- Search by title or ISBN, pagination, sorting features, or catalogue persistence unless explicitly required by the full issue.
- Changes under `.github/`, dependencies, or workflows.
- Application, test, or workflow changes during this planning task.

## Open questions for the human reviewer
- What is the full issue #2 description and its acceptance criteria?
- Should search use an optional `author` parameter on `GET /books`, a separate endpoint, or only a library method?
- Should author matching be exact, substring, or prefix-based, and should it be case-sensitive?
- Should leading and trailing whitespace be trimmed? Is Unicode-aware case matching required?
- How should empty, whitespace-only, and repeated author parameters be handled?
- Should borrowed books be included, and what ordering and response shape are required?
- The repository instructions say new functions take `today`; should date-independent search functions and HTTP handlers be exempt from that rule?

Status: AWAITING APPROVAL
