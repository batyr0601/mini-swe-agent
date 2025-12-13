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

- [2025-12-03 00:39] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `00:39:24` ACTION: Submitting solution
- `00:39:03` DatabaseClient.runshell_db produced args ['psql', '-U', 'someuser', '-h', 'somehost', '-p', '444', 'dbname']; top-level env: PGPASSWORD=somepassword, ...
- `00:38:25` ACTION: python3 - <<'PY'
- `00:37:55` RESULT: patched
- `00:37:55` ACTION: python3 - <<'PY'
- `00:37:21` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '28,52p'
- `00:36:30` ACTION: grep -Rn --line-number -e "sslcert" -e "sslkey" -e "sslrootcert" -e "PGSSL" tests || true
- `00:36:11` ACTION: nl -ba django/db/backends/postgresql/base.py | sed -n '1,240p'
- `00:35:55` ACTION: nl -ba django/db/backends/mysql/client.py | sed -n '1,240p'
- `00:35:51` ACTION: nl -ba tests/dbshell/test_postgresql.py | sed -n '1,240p'
- `00:35:44` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `00:35:41` ACTION: grep -Rn "def runshell" -n django || true
- `00:35:37` ACTION: nl -ba django/core/management/commands/dbshell.py | sed -n '1,240p'
- `00:35:32` ACTION: grep -Rn -e "dbshell" -e "sslcert" -e "sslkey" -e "sslrootcert" -e "sslmode" . || true
- `00:35:19` TASK STARTED: Add support for postgresql client certificates and key to dbshell.
