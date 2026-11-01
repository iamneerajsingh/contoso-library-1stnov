## Goal
Support searching books by author through `GET /books?author=...`, while preserving the existing list-books response when no author filter is supplied.

## Assumptions
- The endpoint continues to return a JSON array of the existing book representation (`isbn`, `title`, `author`, and `available`).
- Filtering belongs in `Library`; `app.py` should only read the query parameter, call library logic, and serialize the result.
- A query with no matching books should return an empty JSON array with a successful response.
- Exact versus partial matching, case sensitivity, and handling of an empty `author` value are not specified and need reviewer direction before implementation.

## Steps
1. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/library.py` with a method that returns books matching an author using the matching rules approved by the reviewer.
2. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/app.py` so `GET /books` applies the author filter when supplied and otherwise retains the current unfiltered response.
3. Update `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/tests/test_library.py` with unit tests for matching and no-match behavior.
4. Add `/home/runner/work/contoso-library-1stnov/contoso-library-1stnov/tests/test_app.py` with endpoint tests for author filtering, no matches, and the unfiltered list.

## Tests to add
- Library search returns books for the requested author according to the agreed matching rules.
- Library search returns an empty result when no books match.
- `GET /books?author=...` returns only matching books in the existing JSON shape.
- `GET /books` without an author parameter continues to return all books.
- The endpoint returns an empty JSON array when the requested author has no matches.

## Risks and rollback
- Unspecified matching rules could produce surprising results; confirm exact/partial matching, case sensitivity, and empty-query behavior before implementation.
- Filtering in the HTTP layer rather than `Library` would mix business logic into the route; keep filtering in `library.py`.
- Roll back the localized changes to `library.py`, `app.py`, and the focused tests if existing list behavior regresses.

## Out of scope
- Searching by title or other book fields.
- Pagination, sorting, persistence, or changes to the book response schema.

## Open questions for the human reviewer
- Should author matching be exact or partial?
- Should author matching be case-sensitive?
- Should an empty `author` query value return all books or no matches?

Status: AWAITING APPROVAL
