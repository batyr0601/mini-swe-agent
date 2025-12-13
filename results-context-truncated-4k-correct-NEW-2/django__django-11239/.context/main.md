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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:50] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `14:50:09` ACTION: Submitting solution
- `14:50:03` PATCHED: django/db/backends/postgresql/client.py: set PGSSLCERT, PGSSLKEY, PGSSLMODE from conn_params
- `14:49:32` ACTION: python3 - <<'PY'
- `14:49:03` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `14:48:56` ACTION: grep -RIn --line-number -e "dbshell" -e "psql" -e "sslmode" -e "sslcert" -e "sslkey" .
- `14:48:38` TASK STARTED: Add support for postgresql client certificates and key to dbshell.
