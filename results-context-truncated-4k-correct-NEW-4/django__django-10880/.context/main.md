# Project Goals

**Current Task:** Query syntax error with condition and distinct combination

<details>
<summary>Full description</summary>

Query syntax error with condition and distinct combination
Description
	
A Count annotation containing both a Case condition and a distinct=True param produces a query error on Django 2.2 (whatever the db backend). A space is missing at least (... COUNT(DISTINCTCASE WHEN ...).

</details>


## TODO List

<!-- 
Add detailed, specific TODOs when starting a task. Good examples:
- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:32` ACTION: sed -n '1,320p' django/db/models/aggregates.py
- `18:35:18` ACTION: grep -n "class Count" django/db/models/aggregates.py || true && sed -n '1,240p' django/db/models/agg [...]
- `18:35:01` ACTION: sed -n '1,240p' django/db/models/aggregates.py
- `18:34:56` RESULT: django/db/models/aggregates.py:104:class Count(Aggregate):
- `18:34:55` ACTION: grep -nR "class Count" django || true
- `18:34:39` ACTION: sed -n '1,320p' django/db/models/aggregates.py
- `18:34:20` ACTION: grep -nR "Count(" . || true && grep -nR "distinct" . || true && grep -nR "filter=" . || true
- `18:33:33` ACTION: sed -n '1,320p' django/db/models/aggregates.py
- `18:33:08` ACTION: grep -nR "class Count" django || true && sed -n '1,240p' django/db/models/aggregates.py
- `18:32:53` ACTION: sed -n '1,240p' django/db/models/aggregates.py
- `18:32:49` ACTION: grep -R --line-number -n "Count(" django || true
- `18:32:32` ACTION: grep -nR "class Count" django || true && sed -n '1,320p' django/db/models/aggregates.py
- `18:32:13` ACTION: sed -n '1,240p' django/db/models/aggregates.py
- `18:32:08` grep class Count: django/db/models/aggregates.py:104
- `18:32:04` RESULT: django/db/models/aggregates.py:104:class Count(Aggregate):
- `18:32:03` ACTION: grep -nR "class Count" django || true
- `18:31:32` ACTION: grep -R --line-number -n "distinct(" . || true
- `18:31:12` ACTION: sed -n '1,240p' django/db/models/aggregates.py
- `18:30:55` ACTION: sed -n '1,200p' django/db/models/aggregates.py
- `18:30:49` ACTION: grep -R --line-number -n "DISTINCT" django || true
