# Project Goals

**Current Task:** Make URLValidator reject invalid characters in the username and password

<details>
<summary>Full description</summary>

Make URLValidator reject invalid characters in the username and password
Description
	 
		(last modified by Tim Bell)
	 
Since #20003, core.validators.URLValidator accepts URLs with usernames and passwords. RFC 1738 section 3.1 requires "Within the user and password field, any ":", "@", or "/" must be encoded"; however, those characters are currently accepted without being %-encoded. That allows certain invalid URLs to pass validation incorrectly. (The issue originates in Diego Perini's ​gist, from which the implementation in #20003 was derived.)
An example URL that should be invalid is http://foo/bar@example.com; furthermore, many of the test cases in tests/validators/invalid_urls.txt would be rendered valid under the current implementation by appending a query string of the form ?m=foo@e...
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

- [2025-12-02 23:35] **swebench-django__django-10097**: Task completed: Submitted
## Interaction Log

- `23:35:12` ACTION: Submitting solution
- `23:34:50` ACTION: git status --porcelain && git --no-pager diff -- django/core/validators.py
- `23:34:40` ACTION: Reading file: tests/repro_urlvalidator.py
- `23:33:58` ACTION: python3 - <<'PY'
- `23:33:19` ACTION: Reading file: tests/repro_urlvalidator.py
- `23:32:59` ACTION: nl -ba tests/repro_urlvalidator.py
- `23:32:51` ACTION: python3 - <<'PY'
- `23:32:34` ACTION: python3 tests/repro_urlvalidator.py && python3 - <<'PY'
- `23:32:12` ACTION: nl -ba tests/validators/invalid_urls.txt | sed -n '1,200p'
- `23:31:01` ACTION: python3 - <<'PY'
- `23:30:41` ACTION: nl -ba django/core/validators.py | sed -n '92,102p'
- `23:30:31` ACTION: nl -ba django/core/validators.py | sed -n '105,180p'
- `23:30:25` ACTION: python3 tests/repro_urlvalidator.py
- `23:30:22` ACTION: Reading file: <<'PY'
- `23:30:10` repro_urlvalidator.py: SyntaxError: f-strings not supported (invalid syntax at print in tests/repro_urlvalidator.py line 8); will update script to use...
- `23:30:01` ACTION: python3 tests/repro_urlvalidator.py
- `23:29:58` ACTION: Reading file: <<'PY'
- `23:29:53` Replaced URL userinfo pattern in django/core/validators.py: changed r'(?:\\S+(?::\\S*)?@)?' to r'(?:[^:@/\\s]+(?::[^@/\\s]*)?@)?
- `23:29:43` RESULT: Replaced URL userinfo pattern.
- `23:29:43` ACTION: python3 - <<'PY'
