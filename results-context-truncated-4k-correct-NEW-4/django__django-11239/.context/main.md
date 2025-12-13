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

- [2025-12-02 18:42] **swebench-django__django-11239**: Task completed: Submitted
## Interaction Log

- `18:42:48` ACTION: Submitting solution
- `18:42:37` runshell_db test: ARGS: ['psql', '-U', 'me', '-h', 'localhost', '-p', '5432', 'mydb']; PGPASSWORD: pw; PGSSLCERT: /path/to/cert.pem; PGSSLKEY: /path/t...
- `18:42:27` ACTION: python3 - <<'PY'
- `18:42:08` RESULT: patched
- `18:42:08` ACTION: python3 - <<'PY'
- `18:41:49` ACTION: grep -n -e "runshell_db" -e "subprocess_env" -e "sslcert" -e "sslkey" -e "PGSSLCERT" django/db/backe [...]
- `18:41:39` runshell_db fake_run: ARGS: ['psql', '-U', 'me', '-h', 'localhost', '-p', '5432', 'mydb']; PGPASSWORD: pw; PGSSLCERT: None; PGSSLKEY: None
- `18:41:28` ACTION: python3 - <<'PY'
- `18:41:16` patched: added PGSSLCERT/PGSSLKEY support in runshell_db; edit command output was 'patched
- `18:40:26` ACTION: sed -n '1,240p' django/db/backends/postgresql/client.py
- `18:40:19` ACTION: grep -nR --line-number -e "dbshell" -e "psql" -e "sslcert" -e "sslkey" -e "sslmode" .
- `18:40:06` TASK STARTED: Add support for postgresql client certificates and key to dbshell.
