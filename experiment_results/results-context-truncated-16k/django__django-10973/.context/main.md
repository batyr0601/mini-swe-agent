# Project Goals

**Current Task:** Use subprocess.run and PGPASSWORD for client in postgres backend

<details>
<summary>Full description</summary>

Use subprocess.run and PGPASSWORD for client in postgres backend
Description
	
​subprocess.run was added in python 3.5 (which is the minimum version since Django 2.1). This function allows you to pass a custom environment for the subprocess.
Using this in django.db.backends.postgres.client to set PGPASSWORD simplifies the code and makes it more reliable.

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

- [2025-12-02 23:32] **swebench-django__django-10973**: Task completed: Submitted
## Interaction Log

- `23:32:38` ACTION: Submitting solution
- `23:31:58` ACTION: Reading file: <<'PY'
- `23:31:25` ACTION: python3 -m unittest tests.dbshell.test_postgresql -v
- `23:31:09` RESULT: bash: line 1: pytest: command not found
- `23:31:08` ACTION: pytest -q tests/dbshell/test_postgresql.py
- `23:31:02` ACTION: nl -ba tests/dbshell/test_postgresql.py | sed -n '1,240p'
- `23:30:59` ACTION: grep -Rn "PGPASSFILE\\|PGPASSWORD\\|runshell_db" tests || true
- `23:30:50` ACTION: python3 -m py_compile django/db/backends/postgresql/client.py
- `23:30:45` ACTION: Reading file: <<'PY'
- `23:30:13` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `23:30:10` ACTION: ls -la django/db/backends/postgresql
- `23:30:08` ACTION: ls -la django/db/backends
- `23:30:06` RESULT: nl: django/db/backends/postgres/client.py: No such file or directory
- `23:30:05` ACTION: nl -ba django/db/backends/postgres/client.py | sed -n '1,240p'
- `23:30:00` ACTION: ls -la
- `23:29:55` TASK STARTED: Use subprocess.run and PGPASSWORD for client in postgres backend
