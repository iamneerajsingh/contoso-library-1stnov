# Contoso Library Lending Service: instructions for Copilot
 
## Project layout
- Python 3.12. Flask API in app.py. Business logic in library.py. Tests in tests/.
 
## How to build and test
- Install: pip install -r requirements.txt
- Lint: ruff check .
- Test: pytest --cov=library --cov-fail-under=80
 
## Rules
- Keep business logic in library.py; app.py only translates HTTP to library calls.
- Every new behaviour needs a unit test. Never delete or weaken existing tests.
- New functions take `today` as a parameter; never call date.today() inside new logic.
- Money is an integer number of rupees. Never use floats for money.
- Do not modify anything under .github/ unless the issue explicitly asks for it.
- Before finishing, run lint and tests and paste the results into the PR description.
- Record progress and decisions in docs/agent-log/issue-<number>.md.

## Memory and state rules
- The source of truth for a task is: the issue, the approved plan, and docs/agent-log/issue-<number>.md.
- At the start of every session, read the plan and the agent log before doing anything else.
- Never contradict a row in the Decisions table. If a decision must change, add a new row that supersedes it and explain why.
- Keep the log short: summarise completed steps in one line each; move anything older than the current task to docs/agent-log/archive/.
- Logs for closed issues are archived when the issue closes; do not reuse them for new tasks.
