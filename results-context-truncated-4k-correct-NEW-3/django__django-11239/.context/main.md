# Project Goals

**Current Task:** Add support for postgresql client certificates and key to dbshell.

<details>
<summary>Full description</summary>

Add support for postgresql client certificates and key to dbshell.
Description
	
This bug is very similar to the #28322
A common security procedure for DB access is to require mutual TLS for the DB connection.
This involves specifying a server certificate, client certificate, and client key when connecting.
Django already supports this configuration, it looks like this:
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': os.environ.get('POSTGRES_DB_NAME'),
		'USER': os.environ.get('POSTGRES_DB_USER'),
		'HOST': 'postgres',
		'PORT': '5432',
		'SCHEMA': os.environ.get('POSTGRES_DB_SCHEMA'),
		'OPTIONS': {
			 'sslmode': 'verify-ca',
			 'sslrootcert': os.environ.get('POSTGRES_CLI_SSL_CA', 'ca.crt'),
			 'sslcert': os.environ.get('POSTGRES_CLI_SSL_CRT', 'client...
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

- [2025-12-02 16:00] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `16:00:34` ACTION: Submitting solution
- `16:00:30` Repro after patch: FAKE_RUN printed PGSSLCERT='/tmp/client-cert.pem' and PGSSLKEY='/tmp/client-key.pem
- `16:00:30` Applied patch: set subprocess_env['PGSSLCERT'] and subprocess_env['PGSSLKEY'] from conn_params in runshell_db
- `16:00:30` Found runshell_db in django/db/backends/postgresql/client.py which set PGPASSWORD but did not set PGSSLCERT/PGSSLKEY
- `16:00:30` Repro before patch: FAKE_RUN printed PGSSLCERT=None and PGSSLKEY=None
- `15:59:51` ACTION: python3 - <<'PY'
- `15:59:39` RESULT: PATCH_APPLIED
- `15:59:39` ACTION: python3 - <<'PY'
- `15:59:17` ACTION: sed -n '1,320p' django/db/backends/postgresql/client.py
- `15:59:09` ACTION: python3 - <<'PY'
- `15:58:44` pytest: command not found when running tests/dbshell/test_postgresql.py; will run minimal reproduction script invoking DatabaseClient.runshell_db dire...
- `15:58:33` RESULT: bash: line 1: pytest: command not found
- `15:58:33` ACTION: pytest -q tests/dbshell/test_postgresql.py
- `15:58:23` Added PGSSLCERT and PGSSLKEY env vars from conn_params 'sslcert' and 'sslkey' to django/db/backends/postgresql/client.py; inserted after PGPASSWORD as...
- `15:57:34` django/db/backends/postgresql/client.py: runshell_db builds psql args and sets PGPASSWORD; will add PGSSLCERT and PGSSLKEY from conn_params (sslcert, ...
- `15:57:23` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `15:57:04` ACTION: sed -n '1,240p' tests/dbshell/test_postgresql.py
- `15:57:01` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `15:56:56` ACTION: grep -RIn --line-number "dbshell" . || true && grep -RIn --line-number "psql" . [...]
- `15:56:40` RESULT: grep: testbed: No such file or directory
