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
- [x] 1. Understand the bug: migrate command rejects namespace packages because it checks for migrations.__file__ which does not exist for implicit namespace packages
- [x] 2. Locate the code: search repository for checks of
- [x] 3. Reproduce the bug: create a minimal package without __init__.py (namespace package) and run the migrate/discovery code to observe the failure
- [x] 4. Implement fix: modify migration discovery to not require __file__ (use pkgutil.iter_modules and package.__path__ instead), update relevant source files under testbed
- [x] 5. Verify fix: run the repro script and unit tests related to migrations, ensure migrate works with namespace packages
- [x] Update verification: configure Django settings before importing apps and run ask_initial against a namespace-package migrations dir
- [x] 1. Inspect django/utils/module_loading.py for getattr(module,
- [x] 2. Inspect django/apps/config.py for getattr(module,
- [x] 3. Implement fix in any additional locations where __file__ checks prevent namespace-package migrations, using pkgutil.iter_modules and __path__ where appropriate; follow loader/questioner approach
- [x] 4. Verify changes: run the ns_test reproduction and relevant migration unit tests to ensure no regressions and that namespace-package migrations are discovered correctly
- [ ] 1. Push branch fix/namespace-migrations to remote and open a PR (requires remote URL); if approved, push branch and create PR
- [ ] 1. Install pytest in the test environment (pip install pytest)
- [ ] 2. Run migration-related tests: python3 -m pytest tests/migrations/ -q
- [ ] 3. After tests complete, record results with context_log and mark the test TODO complete
- [ ] 4. Configure test settings: set DJANGO_SETTINGS_MODULE or call settings.configure() for pytest runs, then re-run migration tests (python3 -m pytest tests/migrations/ -q)
- [ ] 5. Add
- [ ] 6. Add
- [ ] 7. Investigate why tests import as top-level
- [ ] 8. Re-run migration tests by invoking pytest on the tests package root (pytest tests -q) after django.setup()
- [ ] 9. Run migration tests as a package using pytest --pyargs tests.migrations after django.setup()
- [ ] 10. Add explicit Meta.app_label =
- [ ] 10b. Patch tests/migrations/models.py using utf-8 read/write to add Meta.app_label =
- [ ] 11. Remove any top-level migrations package (not tests/migrations) that causes duplicate model registration, then re-run pytest --pyargs tests.migrations

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:36] **swebench-django__django-11141**: Task completed: LimitsExceeded
- [2025-12-01 21:16] **swebench-django__django-11141**: Allow namespace-package migrations: remove __file__ check in django/db/migrations/loader.py and use ...
## Interaction Log

- `21:36:21` ACTION: python3 - <<'PY'
- `21:35:53` ACTION: sed -n '1,40p' tests/migrations/models.py && python3 - <<'PY'
- `21:35:31` ACTION: python3 - <<'PY'
- `21:34:13` ACTION: sed -n '1,200p' tests/migrations/models.py
- `21:32:40` ACTION: Reading file: <<'PY'
- `21:32:23` ACTION: rm -f migrations/__init__.py migrations/apps.py && \
- `21:31:56` ACTION: ls -la tests || true && ls -la tests/migrations || true && echo "==== tests/migrations/__init__. [...]
- `21:31:36` pytest tests/migrations: collection failed with RuntimeError: Model class migrations.models.ModelWithCustomBase doesn't declare an explicit app_label ...
- `21:30:40` ACTION: Reading file: <<'PY'
- `21:30:16` ACTION: printf "\nINSTALLED_APPS += ['migrations']\n" >> tests/test_settings.py && python3 - <<'PY'
- `21:30:05` pytest tests/migrations/: collection failed with RuntimeError: Model class migrations.models.ModelWithCustomBase doesn't declare an explicit app_label...
- `21:29:30` ACTION: python3 - <<'PY'
- `21:29:19` ACTION: Reading file: <<'PY'
- `21:28:50` ACTION: echo "Searching for test settings under tests/..." && \
- `21:28:28` pytest tests/migrations/: collection failed with 6 errors - django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS; set DJANGO_...
- `21:28:03` ACTION: python3 -m pytest tests/migrations/ -q
- `21:27:54` Installed pytest: Name=pytest, Version=7.0.1, Location=/opt/miniconda3/envs/testbed/lib/python3.6/site-packages
- `21:27:36` ACTION: python3 -m pip install pytest && python3 -m pip show pytest
- `21:27:11` RESULT: /opt/miniconda3/envs/testbed/bin/python3: No module named pytest
- `21:27:11` ACTION: python3 -m pytest tests/migrations/ -q
