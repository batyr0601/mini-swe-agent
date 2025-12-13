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
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:21] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `21:21:46` ACTION: Submitting solution
- `21:21:42` repro: ARGS: ['psql', '-U', 'testuser', 'testdb']; PGSSLCERT: '/tmp/cert.pem'; PGSSLKEY: '/tmp/key.pem
- `21:21:27` ACTION: python3 repro.py
- `21:21:22` patched django/db/backends/postgresql/client.py: added PGSSLCERT/PGSSLKEY; repro run did not execute due to shell syntax error after 'patched
- `21:21:07` ACTION: python3 - <<'PY'
- `21:20:37` Found runshell_db in django/db/backends/postgresql/client.py: constructs subprocess_env but does not set PGSSLCERT/PGSSLKEY from conn_params
- `21:20:27` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `21:20:24` grep in client.py: line 12: def runshell_db(cls, conn_params); line 42: DatabaseClient.runshell_db(self.connection.get_connection_params())
- `21:20:15` ACTION: grep -n -E "ssl(cert|key)|PGSSLCERT|PGSSLKEY|runshell_db" django/db/backends/postgresql/client. [...]
- `21:20:07` repro.py: ARGS: ['psql', '-U', 'testuser', 'testdb']; PGSSLCERT: None; PGSSLKEY: None
- `21:19:56` RESULT: ARGS: ['psql', '-U', 'testuser', 'testdb']
PGSSLCERT: None
PGSSLKEY: None
- `21:19:55` ACTION: Reading file: <<'PY'
- `21:19:18` ACTION: python3 -c "from importlib import import_module; mod=import_module('django.db.backends.postgresql. [...]
- `21:17:40` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `21:17:33` RESULT: error: unrecognized input
bash: line 24: pytest: command not found
- `21:17:32` ACTION: git apply -p0 <<'PATCH'
- `21:16:53` ACTION: sed -n '1,240p' tests/dbshell/test_postgresql.py
