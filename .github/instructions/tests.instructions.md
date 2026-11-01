---
applyTo: "tests/**/*.py"
---
- Use pytest fixtures, not unittest setUp methods.
- Use fixed dates such as date(2026, 1, 1); never date.today().
- One behaviour per test. Name tests test_<behaviour>.
