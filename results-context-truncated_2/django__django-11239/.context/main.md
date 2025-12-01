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
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: dbshell for postgresql doesn
- [ ] 2. Locate the code: find dbshell implementation and postgresql client arg construction in the testbed source
- [ ] 3. Root cause analysis: inspect how ssl options (sslmode, sslrootcert) are handled and why sslcert/sslkey are omitted
- [ ] 4. Implement fix: modify dbshell Postgres client argument building to include sslcert and sslkey when present in OPTIONS
- [ ] 5. Verify fix: create/run a repro script that prints the constructed psql command and ensures sslcert/sslkey are present; run relevant tests
- [ ] 6. Finalize: commit changes, run final verification, and submit patch

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:19] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `21:19:24` ACTION: Submitting solution
- `21:19:16` DatabaseClient.runshell_db produced ARGS: ['psql', '-U', 'myuser', '-h', 'db.example.org', '-p', '5432', 'mydb'] and ENV PGPASSWORD: mypw, PGSSLMODE: ...
- `21:18:53` ACTION: python3 - <<'PY'
- `21:18:38` Patched client.py: added env vars PGSSLMODE, PGSSLROOTCERT, PGSSLCERT, PGSSLKEY from conn_params (lines 33-37)
- `21:18:29` ACTION: nl -ba django/db/backends/postgresql/client.py | sed -n '28,60p'
- `21:18:18` ACTION: cp django/db/backends/postgresql/client.py django/db/backends/postgresql/client.py. [...]
- `21:17:46` ACTION: nl -ba django/db/backends/postgresql/base.py | sed -n '1,240p'
- `21:17:44` ACTION: grep -R -n "get_connection_params" django || true
- `21:17:41` ACTION: nl -ba django/db/backends/base/client.py
- `21:17:35` ACTION: nl -ba django/db/backends/postgresql/client.py
- `21:17:30` ACTION: grep -R -n "dbshell" django || true && grep -R -n "psql" django || true && grep -R -n "sslrootcert"  [...]
- `21:17:26` ACTION: ls -la
- `21:17:23` ACTION: grep -R -n "dbshell" testbed || true && grep -R -n "psql" testbed || true && grep -R -n "sslrootcert [...]
- `21:17:18` ACTION: grep -R --line-number --no-color "dbshell" testbed || true && grep -R --line-number --no-color "psql [...]
- `21:17:01` TASK STARTED: Add support for postgresql client certificates and key to dbshell.
