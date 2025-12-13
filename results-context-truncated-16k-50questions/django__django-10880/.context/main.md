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

- [2025-12-02 23:33] **swebench-django__django-10880**: Task completed: Submitted
## Interaction Log

- `23:33:18` ACTION: Submitting solution
- `23:33:12` DummyCase SQL: COUNT(DISTINCT CASE WHEN 1=1 THEN 1 END) observed; extra_context['distinct'] now includes trailing space; bug fixed
- `23:32:51` RESULT: COUNT(DISTINCT CASE WHEN 1=1 THEN 1 END)
[]
- `23:32:50` ACTION: python3 - <<'PY'
- `23:31:54` ACTION: nl -ba django/db/models/sql/where.py | sed -n '1,240p'
- `23:31:46` ACTION: grep -R "conditional = True\|class Lookup" django | sed -n '1,200p'
- `23:31:26` ACTION: nl -ba django/db/models/expressions.py | sed -n '480,540p'
- `23:31:22` ACTION: nl -ba django/db/models/expressions.py | sed -n '340,420p'
- `23:31:19` ACTION: grep -n "conditional = True\|class Lookup" django/db/models/expressions.py || true
- `23:31:08` ACTION: grep -n "conditional" -n django/db/models/expressions.py || true
- `23:31:05` ACTION: grep -n "__eq__\|class CombinedExpression\|conditional =" django/db/models/expressions.py || true
- `23:30:54` ACTION: nl -ba django/db/models/expressions.py | sed -n '820,940p'
- `23:30:07` ACTION: python3 - <<'PY'
- `23:29:57` ACTION: grep -nR "Count(" tests | sed -n '1,200p'
- `23:29:49` ACTION: sed -i "s/'DISTINCT' if self.distinct else ''/'DISTINCT ' if self. [...]
- `23:29:28` ACTION: nl -ba django/db/models/aggregates.py | sed -n '1,240p'
- `23:29:25` RESULT: django/db/models/aggregates.py:104:class Count(Aggregate):
- `23:29:23` ACTION: grep -nR "DISTINCTCASE\|COUNT(DISTINCT\|class Count" django | sed -n '1,200p'
- `23:29:19` ACTION: ls -la
