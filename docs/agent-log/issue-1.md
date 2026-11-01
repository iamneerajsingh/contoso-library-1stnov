# Agent log: issue #1

## Current status
- All steps complete. Validation: `ruff check .` passed; `pytest --cov=library --cov-fail-under=80` passed (7 tests, 94.12% coverage).
- Last updated by (agent or human): Copilot

## Decisions (append only, never edit old rows)
| Date | Decision | Reason | Decided by |
|------|----------|--------|------------|
| 2026-11-01 | Add a defaulted integer `fine` field to `Loan` and calculate it during return as 10 rupees per day after a two-day grace period, capped at 500 rupees. | Follows the approved plan while preserving loan construction and the API response shape. | Copilot |
| 2026-11-01 | Add fixed-date tests for on-time, grace-period, chargeable, and capped returns, and verify returned-loan and book-availability behavior. | Covers the planned fine boundaries and confirms existing return behavior is preserved. | Copilot |

## Handoffs
| From | To | What was handed over | Link |
|------|----|----------------------|------|

## Open items and blockers
- None.
