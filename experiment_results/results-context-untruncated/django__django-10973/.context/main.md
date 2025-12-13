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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:32] **swebench-django__django-10973**: Task completed: Submitted
## Interaction Log

- `00:32:50` ACTION: Submitting solution
- `00:32:45` Verification: repro_runshell.py showed PGPASSWORD set in subprocess env and psql args correct; no temporary .pgpass file used
- `00:32:33` Root cause: original code created a temporary .pgpass file to supply the password to psql (and caught UnicodeEncodeError to fall back to manual input)...
- `00:32:24` Found DatabaseClient.runshell_db in django/db/backends/postgresql/client.py as the function invoking psql and handling password behavior
- `00:32:18` repro_runshell.py: ARGS: ['psql', '-U', 'myuser', '-h', 'localhost', '-p', '5432', 'mydb']; PGPASSWORD present: True; PGPASSWORD value: mypassword
- `00:32:02` ACTION: Reading file: <<'PY'
- `00:31:47` Patched django/db/backends/postgresql/client.py: replaced tempfile PGPASSFILE approach with subprocess.run using env['PGPASSWORD']
- `00:31:37` RESULT: Patched django/db/backends/postgresql/client.py
- `00:31:36` ACTION: python3 - <<'PY'
- `00:31:06` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `00:30:57` ACTION: grep -nR -E "PGPASSWORD|class DatabaseClient|django\.db\.backends\.postgres|postgresql|postgres\. [...]
- `00:30:53` RESULT: grep: testbed: No such file or directory
- `00:30:53` ACTION: grep -nR -E "PGPASSWORD|postgres\.client|django\.db\.backends\.postgres" testbed || true
- `00:30:40` TASK STARTED: Use subprocess.run and PGPASSWORD for client in postgres backend
