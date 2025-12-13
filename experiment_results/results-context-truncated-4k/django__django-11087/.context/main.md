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

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:10] **swebench-django__django-11087**: Task completed: LimitsExceeded
## Interaction Log

- `21:09:56` ACTION: grep -nR "def delete" django/db/models && sed -n '640,760p' django/db/models/query.py
- `21:09:06` ACTION: grep -nR "def delete" django/db/models || true && sed -n '640,760p' django/db/models/query.py
- `21:08:51` ACTION: sed -n '1,360p' django/db/models/deletion.py
- `21:08:44` ACTION: grep -n "def delete" django/db/models/*.py && sed -n '660,720p' django/db/models/query.py
- `21:08:28` ACTION: grep -n "def delete" django/db/models/*.py && sed -n '600,760p' django/db/models/query.py
- `21:07:18` ACTION: sed -n '640,760p' django/db/models/query.py
- `21:07:07` repro/reproduce_delete_issue.py:59 RuntimeWarning: Model 'repro_app.mymodel' was already registered; script printed: About to delete queryset: SELECT ...
- `21:06:47` ACTION: python3 repro/reproduce_delete_issue.py
- `21:06:33` ACTION: sed -n '640,760p' django/db/models/query.py
- `21:06:00` ACTION: awk '/apps.app_configs\["repro_app"\] = ReproAppConfig/ {print; print "apps. [...]
- `21:05:40` ACTION: sed -n '1,240p' repro/reproduce_delete_issue.py
- `21:05:03` ACTION: python3 repro/reproduce_delete_issue.py
- `21:04:56` ACTION: python3 - <<'PY'
- `21:04:26` ACTION: sed -n '1,240p' repro/reproduce_delete_issue.py
- `21:04:02` ACTION: Reading file: <<'PY'
- `21:03:49` reproduce_delete_issue.py: apps.app_configs assignment raised ImproperlyConfigured: The app module 'repro_app' has no filesystem location, you must co...
- `21:03:42` ACTION: mkdir -p repro_app && touch repro_app/__init__.py && python3 repro/reproduce_delete_issue.py
- `21:03:31` reproduce_delete_issue.py: django.setup() failed: ModuleNotFoundError: No module named 'repro_app' when apps.populate processed INSTALLED_APPS
- `21:03:22` ACTION: python3 repro/reproduce_delete_issue.py
- `21:03:15` ACTION: Reading file: <<'PY'
