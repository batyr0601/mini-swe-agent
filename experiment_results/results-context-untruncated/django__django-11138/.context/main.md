# Project Goals

**Current Task:** TIME_ZONE value in DATABASES settings is not used when making dates timezone-aware on MySQL, SQLite, and Oracle.

<details>
<summary>Full description</summary>

TIME_ZONE value in DATABASES settings is not used when making dates timezone-aware on MySQL, SQLite, and Oracle.
Description
	 
		(last modified by Victor Talpaert)
	 
(We assume the mysql backends)
I can set TIME_ZONE several times in settings.py, one for the global django app, and one for each database (see ​https://docs.djangoproject.com/en/1.11/ref/settings/#time-zone (ref1))
Typical usage would be for a legacy database where datetimes are not stored in UTC.
No date lookup
Querying my database takes this setting into account, e.g. :
In settings.py
USE_TZ = True
TIME_ZONE = 'Europe/Paris' # tz1
DATABASES = {
	'legacy': {
		'ENGINE': 'django.db.backends.mysql',
		'OPTIONS': {
			'read_default_file': '....cnf',
		},
		'TIME_ZONE': 'Europe/Paris', # tz2
	},
	'default' : {
		'ENGINE': 'djan...
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

- [2025-12-03 00:35] **swebench-django__django-11138**: Task completed: Submitted
## Interaction Log

- `00:35:07` ACTION: Submitting solution
- `00:35:00` ACTION: python3 - <<'PY'
- `00:34:41` RESULT: patched
- `00:34:40` ACTION: python3 - <<'PY'
- `00:34:15` RESULT: error: unrecognized input
- `00:34:14` ACTION: git apply -p0 <<'PATCH'
- `00:34:01` ACTION: nl -ba django/db/backends/mysql/operations.py | sed -n '1,240p'
- `00:33:51` ACTION: grep -nR "CONVERT_TZ\|\\'UTC\\'\|\"UTC\"" django/db/backends | sed -n '1,200p'
- `00:33:46` ACTION: ls -la
- `00:33:43` TASK STARTED: TIME_ZONE value in DATABASES settings is not used when making dates timezone-aware on MySQL, SQLite, and Oracle.
