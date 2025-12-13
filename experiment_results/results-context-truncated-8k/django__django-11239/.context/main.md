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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:20] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `03:20:48` ACTION: Submitting solution
- `03:20:42` repro_runshell.py output: ARGS: ['psql', '-U', 'dbuser', '-h', 'dbhost', '-p', '5432', 'mydb']; PGPASSWORD='dbpass'; PGSSLMODE='require'; PGSSLROOTCER...
- `03:20:23` ACTION: python3 - <<'PY'
- `03:20:07` ACTION: Reading file: <<'PY'
- `03:19:47` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `03:19:05` staged diff: inserted PGSSLMODE/PGSSLROOTCERT/PGSSLCERT/PGSSLKEY env exports into django/db/backends/postgresql/client.py after PGPASSWORD
- `03:18:52` ACTION: git --no-pager diff --staged -- django/db/backends/postgresql/client.py
- `03:18:43` git --no-pager diff --staged --name-only: django/db/backends/postgresql/client.py (staged)
- `03:18:37` RESULT: django/db/backends/postgresql/client.py
- `03:18:33` ACTION: if grep -q "PGSSLMODE" django/db/backends/postgresql/client.py; then
- `03:18:01` grep PGPASSWORD: django/db/backends/postgresql/client.py:32: subprocess_env['PGPASSWORD'] = str(passwd) (location identified to insert PGSSLMODE/PGSSL...
- `03:17:49` ACTION: grep -n -C 5 "PGPASSWORD" django/db/backends/postgresql/client.py
- `03:17:37` git --no-pager diff --staged --name-only: <empty> (no files staged after attempted patch)
- `03:17:26` ACTION: git --no-pager diff --staged --name-only
- `03:16:18` ACTION: nl -ba django/db/backends/postgresql/base.py | sed -n '120,200p'
- `03:16:11` ACTION: nl -ba django/db/backends/postgresql/base.py | sed -n '1,320p'
- `03:16:06` ACTION: grep -Rn "get_connection_params" -n django | sed -n '1,200p'
- `03:16:01` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '1,240p'
- `03:15:45` ACTION: grep -Rn "dbshell\|psql\|sslcert\|sslkey" -n django | sed -n '1,200p'
- `03:15:37` ACTION: ls -la
