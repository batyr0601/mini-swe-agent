# Project Goals

**Current Task:** Query syntax error with condition and distinct combination

<details>
<summary>Full description</summary>

Query syntax error with condition and distinct combination
Description
	
A Count annotation containing both a Case condition and a distinct=True param produces a query error on Django 2.2 (whatever the db backend). A space is missing at least (... COUNT(DISTINCTCASE WHEN ...).

</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:08] **swebench-django__django-10880**: Task completed: Submitted
## Interaction Log

- `03:08:23` ACTION: Submitting solution
- `03:08:18` repro: template: %(function)s(%(distinct)s%(expressions)s; formatted: COUNT(DISTINCT CASE WHEN 1 THEN 2 END)
- `03:07:58` ACTION: python3 - <<'PY'
- `03:07:21` ACTION: grep -R "Count(" -n tests | sed -n '1,200p'
- `03:07:14` patched django/db/models/aggregates.py: replaced extra_context['distinct'] = 'DISTINCT' with 'DISTINCT ' to ensure a space between DISTINCT and follow...
- `03:07:07` RESULT: patched
- `03:07:03` ACTION: python3 - <<'PY'
- `03:06:44` ACTION: nl -ba django/db/models/aggregates.py | sed -n '1,240p'
- `03:06:34` ACTION: grep -n "DISTINCT" -R django | sed -n '1,200p'
- `03:06:28` ACTION: ls -la
- `03:06:25` RESULT: ls: cannot access 'testbed': No such file or directory
- `03:06:22` ACTION: ls -la testbed
- `03:06:11` TASK STARTED: Query syntax error with condition and distinct combination
