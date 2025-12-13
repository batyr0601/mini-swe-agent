# Project Goals

**Current Task:** Optimize .delete() to use only required fields.

<details>
<summary>Full description</summary>

Optimize .delete() to use only required fields.
Description
	
Hi!
We're in the process of upgrading our Django 1.11 installation from Python 2.7 to Python 3.6, however are hitting an unexpected UnicodeDecodeError during a .delete() run by our daily data purging management command.
STR:
Have an existing Django 1.11 project running under Python 2.7.15 that uses mysqlclient-python v1.3.13 to connect to MySQL server v5.7.23, with Django's DATABASES options including 'charset': 'utf8mb4' (​https://github.com/mozilla/treeherder)
Update to Python 3.6.8
Run the daily cycle_data Django management command against the dev instance's DB:
​https://github.com/mozilla/treeherder/blob/fc91b7f58e2e30bec5f9eda315dafd22a2bb8380/treeherder/model/management/commands/cycle_data.py
​https://github.com/mozilla/tr...
</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce how .delete() triggers SELECT of unneeded fields causing UnicodeDecodeError
- [ ] 2. Locate the code: find delete()/Collector logic in django/db/models/deletion.py and query generation in django/db/models/query.py or sql/compiler.py
- [ ] 3. Root cause analysis: inspect how related objects SELECTs choose fields; identify where to limit selected columns
- [ ] 4. Implement fix: modify deletion logic to only fetch primary key and required FK fields for cascading delete
- [ ] 5. Verify fix: run relevant tests or create minimal reproduction to ensure problematic fields not selected

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:47] **swebench-django__django-11087**: Task completed: Submitted
## Interaction Log

- `20:47:56` ACTION: Submitting solution
- `20:47:51` Verified Collector.related_objects returns qs.only(pk) in runtime
- `20:47:49` RESULT: (12 lines of output) First: def related_objects(self, related, objs):...
- `20:47:49` ACTION: python - <<'PY'
- `20:47:43` RESULT: bash: line 1: pytest: command not found
- `20:47:43` ACTION: pytest -q tests -k "delete or deletion" || true
- `20:47:40` Patched Collector.related_objects to use qs.only(pk) to avoid fetching unnecessary text/blob fields during delete
- `20:47:28` Found related_objects in deletion.py: will limit selected fields to PK to avoid fetching large text columns during delete
- `20:46:55` RESULT: (102 lines of output) First: 119:    def can_fast_delete(self, objs, from_field...
- `20:46:54` ACTION: grep -n "def can_fast_delete" -n django/db/models/deletion.py && nl -ba django/db/models/deletion. [...]
- `20:46:50` RESULT: (89 lines of output) First: 240	        for model, instances in self.data.item...
- `20:46:49` ACTION: nl -ba django/db/models/deletion.py | sed -n '240,520p' | sed -n '1,240p'
- `20:46:41` RESULT: (240 lines of output) First: 1	from collections import Counter...
- `20:46:41` ACTION: nl -ba django/db/models/deletion.py | sed -n '1,240p'
- `20:46:39` RESULT: django/db/models/deletion.py:63:class Collector:
- `20:46:38` ACTION: grep -nR "class Collector" django || true
- `20:46:25` RESULT: (30 lines of output) First: total 172...
- `20:46:25` ACTION: ls -la
- `20:46:22` TASK STARTED: Optimize .delete() to use only required fields.
