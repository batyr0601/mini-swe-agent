# Project Goals

**Current Task:** Union queryset with ordering breaks on ordering with derived querysets

<details>
<summary>Full description</summary>

Union queryset with ordering breaks on ordering with derived querysets
Description
	 
		(last modified by Sergei Maertens)
	 
May be related to #29692
Simple reproduction (the exact models are not relevant I think):
>>> Dimension.objects.values_list('id', flat=True)
<QuerySet [10, 11, 12, 13, 14, 15, 16, 17, 18]>
>>> qs = (
	Dimension.objects.filter(pk__in=[10, 11])
	.union(Dimension.objects.filter(pk__in=[16, 17])
	.order_by('order')
)
>>> qs
<QuerySet [<Dimension: boeksoort>, <Dimension: grootboek>, <Dimension: kenteken>, <Dimension: activa>]>
# this causes re-evaluation of the original qs to break
>>> qs.order_by().values_list('pk', flat=True)
<QuerySet [16, 11, 10, 17]>
>>> qs
[breaks]
Traceback:
Traceback (most recent call last):
 File "<input>", line 1, in <module>
	qs
 File "/home/b...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:05] **swebench-django__django-10554**: Task completed: LimitsExceeded
## Interaction Log

- `21:05:36` ACTION: grep -n "def union" django/db/models/query.py && sed -n '720,980p' django/db/models/query.py
- `21:04:50` ACTION: grep -n "def union" django/db/models/query.py && sed -n '760,960p' django/db/models/query.py
- `21:04:35` ACTION: grep -n "def union" django/db/models/query.py && sed -n '820,1040p' django/db/models/query.py
- `21:04:06` ACTION: sed -n '820,1040p' django/db/models/query.py
- `21:03:53` ACTION: grep -n "def union" django/db/models/query.py && sed -n '820,1040p' django/db/models/query.py
- `21:03:04` ACTION: grep -n "def union" django/db/models/query.py && sed -n '840,1040p' django/db/models/query.py
- `21:02:45` ACTION: grep -R --line-number "ORDER BY not allowed in subqueries of compound statements" . [...]
- `21:02:36` repro_union.py: DatabaseError 'ORDER BY not allowed in subqueries of compound statements.' raised when calling union() on an ordered derived queryset
- `21:02:28` ACTION: Reading file: <<'PY'
- `21:01:35` ACTION: grep -n "def union" django/db/models/query.py && sed -n '840,1040p' django/db/models/query.py
- `21:01:18` ACTION: sed -n '840,1040p' django/db/models/query.py
- `21:01:05` ACTION: grep -R --line-number --exclude-dir=.git --exclude-dir=venv --exclude-dir=.venv "union(" . || true
- `21:00:46` ACTION: grep -n "def union" django/db/models/query.py && sed -n '840,1040p' django/db/models/query.py
- `21:00:29` ACTION: sed -n '840,1040p' django/db/models/query.py
- `21:00:13` ACTION: grep -R --line-number --exclude-dir=.git --exclude-dir=venv --exclude-dir=.venv "union(" . || true
- `21:00:08` RESULT: grep: django/tests: No such file or directory
- `21:00:08` ACTION: grep -R --line-number --exclude-dir=.git --exclude-dir=venv --exclude-dir=. [...]
- `20:59:52` ACTION: grep -n "def union" django/db/models/query.py && sed -n '840,1040p' django/db/models/query.py
- `20:59:32` ACTION: grep -R --line-number --exclude-dir=.git --exclude-dir=venv --exclude-dir=.venv "union(" . || true
- `20:59:25` RESULT: grep: django/tests: No such file or directory
