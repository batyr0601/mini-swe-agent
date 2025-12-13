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

- [2025-12-02 23:37] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `23:37:23` ACTION: Submitting solution
- `23:37:19` Implemented fix: django/db/backends/postgresql/client.py now sets PGSSLMODE/PGSSLROOTCERT/PGSSLCERT/PGSSLKEY from conn_params; verified with repro.py ...
- `23:37:04` Root cause: DatabaseClient.runshell_db did not export libpq environment variables for SSL options (sslmode, sslrootcert, sslcert, sslkey) from conn_pa...
- `23:36:54` Found function causing dbshell behavior: django/db/backends/postgresql/client.py:DatabaseClient.runshell_db
- `23:36:44` repro.py: ARGS: ['psql', '-U', 'me', '-h', 'localhost', '-p', '5432', 'mydb']; PGPASSWORD: pw; PGSSLMODE: verify-ca; PGSSLROOTCERT: ca.crt; PGSSLCERT:...
- `23:36:33` ACTION: Reading file: repro.py
- `23:36:22` Patched django/db/backends/postgresql/client.py: set PGSSLMODE/PGSSLROOTCERT/PGSSLCERT/PGSSLKEY in subprocess env from conn_params when present
- `23:35:57` ACTION: python3 - <<'PY' && nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `23:35:12` ACTION: nl -ba django/db/backends/postgresql/base.py | sed -n '1,260p'
- `23:35:09` ACTION: grep -nR "get_connection_params" -n django | sed -n '1,200p'
- `23:34:59` ACTION: grep -nR "sslmode\\|sslcert\\|sslkey\\|sslrootcert" -n django | sed -n '1,200p'
- `23:34:54` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `23:34:46` ACTION: grep -nR "dbshell\|psql" django | sed -n '1,200p'
- `23:34:42` ACTION: ls -la
- `23:34:33` TASK STARTED: Add support for postgresql client certificates and key to dbshell.
