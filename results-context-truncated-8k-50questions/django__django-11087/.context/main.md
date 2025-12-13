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
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:12] **swebench-django__django-11087**: Task completed: Submitted
## Interaction Log

- `03:12:27` ACTION: Submitting solution
- `03:12:12` RESULT: VERIFICATION_PASSED
- `03:12:05` ACTION: python3 - <<'PY'
- `03:11:50` inspect Collector.related_objects: .only present: True
- `03:11:40` RESULT: True
- `03:11:35` ACTION: python3 - <<'PY'
- `03:11:25` patched django/db/models/deletion.py: related_objects now returns qs.only(related.related_model._meta.pk.name)
- `03:11:16` RESULT: patched
django/db/models/deletion.py
- `03:11:14` ACTION: python3 - <<'PY'
- `03:10:45` git diff -- django/db/models/deletion.py: no changes (empty output)
- `03:10:29` ACTION: git diff -- django/db/models/deletion.py
- `03:09:40` ACTION: sed -n '228,244p' django/db/models/deletion.py
- `03:09:13` ACTION: grep -n "def collect(" -n django/db/models/deletion. [...]
- `03:09:00` ACTION: nl -ba django/db/models/deletion.py | sed -n '1,420p'
- `03:08:53` ACTION: grep -n "def delete(" -n django/db/models -R
- `03:08:46` ACTION: ls -la
- `03:08:44` RESULT: ls: cannot access 'testbed': No such file or directory
- `03:08:43` ACTION: ls -la testbed
- `03:08:33` TASK STARTED: Optimize .delete() to use only required fields.
