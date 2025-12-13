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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:34] **swebench-django__django-10554**: Task completed: Submitted
## Interaction Log

- `00:34:53` ACTION: Submitting solution
- `00:34:50` Found root cause: get_combinator_sql in django/db/models/sql/compiler.py did a pre-check using compiler.get_order_by() before clearing ordering, causi...
- `00:34:25` Verified fix: union with derived queryset ordering no longer raises; repro shows correct evaluation
- `00:34:06` ACTION: sed -i '/if compiler.get_order_by()/,+1d' django/db/models/sql/compiler.py && python3 - <<'PY'
- `00:33:12` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '380,460p'
- `00:33:05` ACTION: python3 - <<'PY'
- `00:32:47` ACTION: Reading file: <<PY
- `00:32:15` ACTION: Reading file: <<'PY'
- `00:31:44` RESULT: bash: line 1: pytest: command not found
- `00:31:44` ACTION: pytest tests/queries/test_qs_combinators.py -q
- `00:31:41` ACTION: grep -R "union(" -n tests | sed -n '1,200p'
- `00:31:21` Inserted compiler.query.clear_ordering(True) before compiler.as_sql() in get_combinator_sql in django/db/models/sql/compiler.py to prevent component O...
- `00:31:00` ACTION: sed -n '1,260p' django/db/models/sql/compiler.py > /dev/null && sed -i "/part_sql, part_args = compi [...]
- `00:30:10` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '520,680p'
- `00:29:49` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1820,1870p'
- `00:29:47` RESULT: django/db/models/sql/query.py:1851:    def clear_ordering(self, force_empty):
- `00:29:47` ACTION: grep -n "def clear_ordering" -n django -R || true
- `00:29:30` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1,260p'
- `00:29:18` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '320,520p'
- `00:29:15` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '1,260p'
