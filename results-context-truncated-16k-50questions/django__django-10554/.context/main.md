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
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:34] **swebench-django__django-10554**: Task completed: Submitted
## Interaction Log

- `23:34:17` ACTION: Submitting solution
- `23:34:11` repro_union_test.py: RESULT: [1, 9]; PASS
- `23:34:00` RESULT: RESULT: [1, 9]
PASS
- `23:33:58` ACTION: Reading file: <<'PY'
- `23:33:24` RESULT: runtests.py not found in repo root
- `23:33:24` ACTION: if [ -f runtests.py ]; then python3 runtests.py tests.queries.test_qs_combinators. [...]
- `23:32:57` Attempted to run pytest for tests/queries/test_qs_combinators.py::QuerySetSetOperationTests::test_union_with_values_list_on_annotated_and_unannotated ...
- `23:32:44` RESULT: bash: line 1: pytest: command not found
- `23:32:43` ACTION: pytest -q tests/queries/test_qs_combinators.py::QuerySetSetOperationTests::test_union_with_values_li [...]
- `23:32:30` ACTION: nl -ba tests/queries/test_qs_combinators.py | sed -n '1,260p'
- `23:32:04` ACTION: grep -n "union(" -R tests || true
- `23:31:51` Inserted compiler.query.clear_ordering(True) after set_values in django/db/models/sql/compiler.py (prevents subqueries keeping ORDER BY when setting v...
- `23:31:26` ACTION: python3 - <<'PY'
- `23:30:52` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '424,436p'
- `23:29:54` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '400,460p'
- `23:29:29` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '320,520p'
- `23:29:18` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1820,1885p'
- `23:29:16` ACTION: nl -ba django/db/models/sql/query.py | sed -n '1,260p'
- `23:29:10` ACTION: grep -n "clear_ordering\|combined_queries\|combinator" -n django -R || true
