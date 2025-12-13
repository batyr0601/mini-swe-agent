# Project Goals

**Current Task:** Allow migrations directories without __init__.py files

<details>
<summary>Full description</summary>

Allow migrations directories without __init__.py files
Description
	 
		(last modified by Tim Graham)
	 
Background: In python 3 a package with no __init__.py is implicitly a namespace package, so it has no __file__ attribute. 
The migrate command currently checks for existence of a __file__ attribute on the migrations package. This check was introduced in #21015, because the __file__ attribute was used in migration file discovery. 
However, in #23406 migration file discovery was changed to use pkgutil.iter_modules (), instead of direct filesystem access. pkgutil. iter_modules() uses the package's __path__ list, which exists on implicit namespace packages.
As a result, the __file__ check is no longer needed, and in fact prevents migrate from working on namespace packages (implicit or other...
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

- [2025-12-02 23:37] **swebench-django__django-11141**: Task completed: Submitted
## Interaction Log

- `23:37:54` ACTION: Submitting solution
- `23:37:46` Removed __file__ check in django/db/migrations/loader.py (previously lines ~87-91) to allow namespace package migrations
- `23:37:46` Reproduced namespace-package migrations: loader.load_disk() produced migrated_apps: {'fakeapp'}
- `23:37:26` RESULT: unmigrated_apps: set()
migrated_apps: {'fakeapp'}
- `23:37:09` ACTION: Reading file: <<'PY'
- `23:36:39` RESULT: 1	class Migration:\n    dependencies = []\n    operations = []\n
- `23:36:39` ACTION: nl -ba tmp_pkg/fakeapp_package/migrations/0001_initial.py
- `23:36:26` ACTION: Reading file: <<'PY'
- `23:35:56` ACTION: nl -ba django/db/migrations/loader.py | sed -n '100,140p'
- `23:35:52` ACTION: Reading file: <<'PY'
- `23:35:25` ACTION: nl -ba repro_namespace.py | sed -n '1,240p'
- `23:34:18` ACTION: Reading file: <<'PY'
- `23:33:55` Removed __file__ check in django/db/migrations/loader.py (deleted lines 87-91) to allow namespace package migrations
- `23:33:45` ACTION: sed -i '87,91d' django/db/migrations/loader.py && nl -ba django/db/migrations/loader. [...]
- `23:33:36` ACTION: nl -ba django/db/migrations/loader.py | sed -n '80,100p'
- `23:33:33` RESULT: pattern not found; no change made
- `23:33:32` ACTION: python3 - <<'PY'
- `23:33:05` ACTION: nl -ba django/db/migrations/loader.py | sed -n '1,240p'
- `23:32:58` ACTION: grep -Rn "__file__" django
