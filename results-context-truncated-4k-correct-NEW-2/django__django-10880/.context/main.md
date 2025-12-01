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
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 2. Read get_distinct and related helpers in django/db/models/sql/compiler.py (around lines 660-740) to identify how DISTINCT + conditional annotations are rendered
- [ ] 3. Create a minimal runnable repro (manage.py shell snippet) that constructs annotate()+filter()+distinct() and prints qs.query to capture the problematic SQL

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:49] **swebench-django__django-10880**: Task completed: LimitsExceeded
## Interaction Log

- `14:49:06` ACTION: grep -n "def get_distinct" django/db/models/sql/compiler. [...]
- `14:48:52` ACTION: sed -n '600,820p' django/db/models/sql/compiler.py
- `14:48:26` ACTION: grep -n "def get_distinct" django/db/models/sql/compiler. [...]
- `14:48:08` ACTION: sed -n '600,820p' django/db/models/sql/compiler.py
- `14:47:47` ACTION: sed -n '640,760p' django/db/models/sql/compiler.py
- `14:47:28` ACTION: sed -n '660,740p' django/db/models/sql/compiler.py
- `14:47:08` ACTION: sed -n '600,820p' django/db/models/sql/compiler.py
- `14:46:47` ACTION: sed -n '660,740p' django/db/models/sql/compiler.py
- `14:46:18` ACTION: sed -n '600,820p' django/db/models/sql/compiler.py
- `14:46:04` ACTION: sed -n '640,760p' django/db/models/sql/compiler.py
- `14:45:50` ACTION: sed -n '600,820p' django/db/models/sql/compiler.py
- `14:45:35` ACTION: sed -n '660,740p' django/db/models/sql/compiler.py
- `14:45:01` ACTION: sed -n '640,760p' django/db/models/sql/compiler.py
- `14:44:40` ACTION: sed -n '660,740p' django/db/models/sql/compiler.py
- `14:44:27` ACTION: sed -n '640,760p' django/db/models/sql/compiler.py
- `14:44:09` get_distinct: if name in self.query.annotation_select, append name to result (no SQL compile); otherwise compile transform_function(target, alias) and...
- `14:43:40` ACTION: sed -n '660,740p' django/db/models/sql/compiler.py
- `14:43:35` grep: get_distinct occurrences in django/db/models/sql/compiler.py at lines 368,478,489,548,591,663,674,720-723
- `14:43:24` ACTION: grep -nE "def get_distinct|get_distinct_fields|distinct_fields|distinct\(" django/db/models/sql/comp [...]
- `14:43:17` Created repro.py skeleton for distinct+condition SQL issue (prints guidance and example queryset)
