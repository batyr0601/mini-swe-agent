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

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:07] **swebench-django__django-10097**: Task completed: Submitted
## Interaction Log

- `03:07:54` ACTION: Submitting solution
- `03:07:45` repro.py after fix: VALID: http://userid:password@example.com:8080; INVALID: http://userid:pass/word@example.com; INVALID: http://user/name:password@e...
- `03:07:25` ACTION: python3 repro.py
- `03:07:17` Replaced pattern in django/core/validators.py: r'(?:\\S+(?::\\S*)?@)?' -> r'(?:[^\\s:@/]+(?::[^\\s:@/]*)?@)?'; file now shows r'(?:[^\\s:@/]+(?::[^\\s...
- `03:06:57` ACTION: python3 - <<'PY'
- `03:06:28` ACTION: sed -n '92,102p' django/core/validators.py
- `03:06:08` ACTION: python3 - <<'PY'
- `03:05:25` ACTION: Reading file: <<'PY'
- `03:04:57` ACTION: grep -nE "://.*@|user:pass|username:password|auth@" -n tests -R || true
- `03:04:49` ACTION: nl -ba django/core/validators.py | sed -n '1,240p'
- `03:04:36` ACTION: ls -la && grep -R "URLValidator" -n || true
- `03:04:28` TASK STARTED: Make URLValidator reject invalid characters in the username and password
