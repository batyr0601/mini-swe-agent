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

- [2025-12-03 03:22] **swebench-django__django-10554**: Task completed: LimitsExceeded
## Interaction Log

- `03:22:05` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '360,500p'
- `03:21:57` ACTION: grep -nR "compound" django/db/models/sql || true && grep -nR "union(" django/db/models/sql | sed -n  [...]
- `03:21:54` ACTION: grep -nR "Compound" django/db/models/sql | sed -n '1,200p'
- `03:21:45` ACTION: grep -n "CompoundSelect" django/db/models/sql/compiler.py
- `03:21:41` ACTION: grep -n "class CompoundSelect" -n django/db/models/sql/compiler. [...]
- `03:21:30` ACTION: nl -ba tests/queries/test_qs_combinators.py | sed -n '1,320p'
- `03:21:10` ACTION: ls -la tests
- `03:21:01` test run failed: ImproperlyConfigured: Requested setting TEST_RUNNER; settings not configured. Need DJANGO_SETTINGS_MODULE or settings.configure()
- `03:20:53` ACTION: python -m django test tests.queries.test_qs_combinators.QuerySetSetOperationTests. [...]
- `03:20:28` ACTION: nl -ba tests/queries/test_qs_combinators.py | sed -n '1,320p'
- `03:20:16` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '320,460p'
- `03:20:11` ACTION: grep -nR "union" django/db/models/sql | sed -n '1,200p' && grep -nR "combine" django/db/models/sql | [...]
- `03:19:57` ACTION: ls -la django/db/models/sql
- `03:19:50` ACTION: grep -nRE "Compound" django/db | sed -n '1,120p'
- `03:19:36` ACTION: nl -ba tests/queries/test_qs_combinators.py | sed -n '1,260p'
- `03:19:20` ACTION: grep -nR "CompoundSelect" django | sed -n '1,200p'
- `03:19:13` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '760,1400p'
- `03:18:51` ACTION: grep -nR "union(" tests | sed -n '1,200p'
- `03:18:39` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '320,760p'
- `03:18:18` ACTION: nl -ba django/db/models/sql/compiler.py | sed -n '240,320p'
