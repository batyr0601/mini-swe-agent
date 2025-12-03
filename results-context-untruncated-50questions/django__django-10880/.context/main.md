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

- [2025-12-03 00:33] **swebench-django__django-10880**: Task completed: Submitted
## Interaction Log

- `00:33:06` ACTION: Submitting solution
- `00:33:01` reproduce.py verification: with_space: COUNT(DISTINCT CASE WHEN 1=1 THEN 1 ELSE 0 END)
- `00:32:48` Implemented fix: django/db/models/aggregates.py now sets extra_context['distinct'] = 'DISTINCT ' (with trailing space) to avoid 'COUNT(DISTINCTCASE......
- `00:32:39` reproduce.py output: no_space: COUNT(DISTINCTCASE WHEN 1=1 THEN 1 ELSE 0 END) | with_space: COUNT(DISTINCT CASE WHEN 1=1 THEN 1 ELSE 0 END)
- `00:32:31` ACTION: python3 reproduce.py
- `00:32:29` ACTION: Reading file: <<'PY'
- `00:32:06` Updated django/db/models/aggregates.py: extra_context['distinct'] now 'DISTINCT ' (trailing space) to prevent 'COUNT(DISTINCTCASE...)'.
- `00:31:55` ACTION: sed -i "s/extra_context\['distinct'\] = 'DISTINCT' if self. [...]
- `00:31:31` ACTION: grep -nR "%(distinct)" -n django | sed -n '1,200p'
- `00:31:23` Found Aggregate.template '%(function)s(%(distinct)s%(expressions)s)' and as_sql sets extra_context['distinct'] = 'DISTINCT' if self.distinct else ''. ...
- `00:31:07` ACTION: nl -ba django/db/models/aggregates.py | sed -n '1,240p'
- `00:30:57` ACTION: grep -nR "DISTINCT" django | sed -n '1,200p'
- `00:30:53` ACTION: ls -la
- `00:30:49` RESULT: grep: testbed: No such file or directory
- `00:30:49` ACTION: grep -nR -i "distinct" testbed || true
- `00:30:32` TASK STARTED: Query syntax error with condition and distinct combination
