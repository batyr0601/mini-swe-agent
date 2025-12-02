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
- [ ] 1. Understand the bug: reproduce SQL that shows COUNT(DISTINCTCASE WHEN ...) missing space when Count has Case condition and distinct=True
- [ ] 2. Locate the code: search repository for code that generates COUNT(DISTINCT and concatenates DISTINCT with expressions (look for
- [ ] 3. Create repro script: add or run a small repro that builds a Count with Case and distinct=True to show the missing space in generated SQL
- [ ] 4. Implement fix: modify source that concatenates DISTINCT and expressions so it inserts a space before
- [ ] 5. Verify fix: run the repro and/or tests to confirm SQL now contains

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:48] **swebench-django__django-10880**: Task completed: Submitted
## Interaction Log

- `20:48:40` ACTION: Submitting solution
- `20:48:29` repro.py verification: distinct=True -> COUNT(DISTINCT CASE WHEN x>0 THEN x ELSE NULL END); distinct=False -> COUNT(CASE WHEN x>0 THEN x ELSE NULL END...
- `20:48:23` ACTION: python3 repro.py
- `20:48:16` Located DISTINCT handling in django/db/models/aggregates.py: template = '%(function)s(%(distinct)s%(expressions)s)' and as_sql sets extra_context['dis...
- `20:48:04` Root cause: Aggregate.template '%(distinct)s%(expressions)s' and extra_context['distinct'] was 'DISTINCT' without trailing space, causing 'DISTINCTCAS...
- `20:47:51` repro.py: distinct=True -> COUNT(DISTINCT CASE WHEN x>0 THEN x ELSE NULL END); distinct=False -> COUNT(CASE WHEN x>0 THEN x ELSE NULL END)
- `20:47:43` ACTION: Reading file: repro.py
- `20:47:26` django/db/models/aggregates.py: as_sql sets extra_context['distinct'] = 'DISTINCT ' if self.distinct else '' (added trailing space to avoid 'DISTINCTC...
- `20:47:19` ACTION: sed -i "s/'DISTINCT' if self.distinct else ''/'DISTINCT ' if self. [...]
- `20:47:07` ACTION: nl -ba django/db/models/aggregates.py | sed -n '1,240p'
- `20:47:03` ACTION: grep -nRi "DISTINCT" . || true && grep -nRi "COUNT(" . || true && grep -nRi "distinct=" . || true
- `20:46:58` ACTION: grep -nRi "DISTINCT" testbed || true && grep -nRi "COUNT(" testbed || true && grep -nRi "distinct="  [...]
- `20:46:41` TASK STARTED: Query syntax error with condition and distinct combination
