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
- [x] 6. Search the codebase for
- [x] 7. Update the code that builds the combined template so it ensures a space exists between %(distinct)s and %(expressions)s when rendering the FILTER template
- [x] 8. Search codebase for

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 11:59] **swebench-django__django-10880**: Task completed: Submitted
## Interaction Log

- `11:59:03` ACTION: Submitting solution
- `11:58:58` grep results: ./repro.py:2:template = '%(function)s(%(distinct)s%(expressions)s)' | ./django/db/models/aggregates.py:17:    template = '%(function)s(%...
- `11:58:47` ACTION: grep -R --line-number --exclude-dir=.git -e "%(distinct)s%(expressions)s" . || true
- `11:58:41` ACTION: grep -R --line-number --no-color --exclude-dir=.git -e "%(distinct)s%(expressions)s" . || true
- `11:58:31` patched django/db/models/aggregates.py; repro output: Combined template: %(function)s(%(distinct)s%(expressions)s) FILTER (WHERE %(filter)s) | Without...
- `11:58:17` ACTION: python3 - <<'PY'
- `11:57:11` ACTION: grep -n "filter_template" -n django/db/models/aggregates. [...]
- `11:56:51` repro.py: Combined template: %(function)s(%(distinct)s%(expressions)s) ; Without trailing space: COUNT(DISTINCTfield) FILTER (WHERE 1=1) ; With traili...
- `11:56:38` ACTION: python3 repro.py
- `11:56:23` ACTION: grep -n "template" django/db/models/aggregates.py && sed -n '1,160p' django/db/models/aggregates. [...]
- `11:56:09` ACTION: Submitting solution
- `11:55:42` grep '%%(filter)s': repro.py:3: filter_template = '%s FILTER (WHERE %%(filter)s)'; django/db/models/aggregates.py:20: filter_template = '%s FILTER (WH...
- `11:55:13` ACTION: grep -R --line-number --fixed-strings '%(filter)s' || true && sed -n '1,240p' django/db/models/aggre [...]
- `11:54:58` ACTION: grep -R --line-number --fixed-strings '%(distinct)s%(expressions)s' || true && sed -n '1,240p' djang [...]
- `11:54:41` repro.py: Combined template: %(function)s(%(distinct)s%(expressions)s) FILTER (WHERE %(filter)s); Without trailing space: COUNT(DISTINCTfield) FILTER ...
- `11:54:33` ACTION: python3 repro.py
- `11:54:23` ACTION: sed -n '1,240p' django/db/models/aggregates.py
- `11:54:07` repro.py output: Combined template: %(function)s(%(distinct)s%(expressions)s) FILTER (WHERE %(filter)s); Without trailing space: COUNT(DISTINCTfield) ...
- `11:53:48` ACTION: sed -i "s/%(distinct)s%(expressions)s /%(distinct)s %(expressions)s /g" django/contrib/postgres/aggr [...]
- `11:52:56` ACTION: sed -n '1,160p' django/contrib/postgres/aggregates/general.py
