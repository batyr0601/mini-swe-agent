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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:31] **swebench-django__django-10097**: Task completed: Submitted
## Interaction Log

- `00:31:27` ACTION: Submitting solution
- `00:31:22` repro.py after fix: INVALID: http://foo/bar@example.com; VALID: http://user:pass@example.com; INVALID: http://user:pa:ss@example.com; VALID: http://us...
- `00:31:03` Changed URLValidator userinfo regex to disallow unencoded ':' '@' '/' in username/password. repro.py results: INVALID: http://foo/bar@example.com, VAL...
- `00:30:47` ACTION: python3 - <<'PY'
- `00:30:12` ACTION: nl -ba django/core/validators.py | sed -n '88,106p'
- `00:30:06` ACTION: python3 - <<'PY'
- `00:29:45` Root cause: URLValidator's user:pass regex at line 97 uses '\\S+(?::\\S*)?@', which allows unencoded ':' '@' or '/' in username/password
- `00:29:29` repro.py: URLValidator accepted 'http://foo/bar@example.com' and 'http://user:pa:ss@example.com'; encoded slash 'http://user%2Fname:pass@example.com' ...
- `00:29:16` ACTION: Reading file: repro.py
- `00:28:59` Found URLValidator regex user:pass pattern at line 97: '(?:\\S+(?::\\S*)?@)?
- `00:28:45` ACTION: nl -ba django/core/validators.py | sed -n '1,260p'
- `00:28:28` ACTION: grep -R --line-number "URLValidator" . || true
- `00:28:24` RESULT: grep: testbed: No such file or directory
- `00:28:24` ACTION: grep -R --line-number "URLValidator" testbed || true
- `00:28:16` TASK STARTED: Make URLValidator reject invalid characters in the username and password
