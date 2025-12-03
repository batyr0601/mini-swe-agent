# Project Goals

**Current Task:** UsernameValidator allows trailing newline in usernames

<details>
<summary>Full description</summary>

UsernameValidator allows trailing newline in usernames
Description
	
ASCIIUsernameValidator and UnicodeUsernameValidator use the regex 
r'^[\w.@+-]+$'
The intent is to only allow alphanumeric characters as well as ., @, +, and -. However, a little known quirk of Python regexes is that $ will also match a trailing newline. Therefore, the user name validators will accept usernames which end with a newline. You can avoid this behavior by instead using \A and \Z to terminate regexes. For example, the validator regex could be changed to
r'\A[\w.@+-]+\Z'
in order to reject usernames that end with a newline.
I am not sure how to officially post a patch, but the required change is trivial - using the regex above in the two validators in contrib.auth.validators.

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

- [2025-12-03 03:15] **swebench-django__django-11099**: Task completed: Submitted
## Interaction Log

- `03:14:14` ACTION: Submitting solution
- `03:14:06` repro.py: UnicodeUsernameValidator and ASCIIUsernameValidator rejected 'foo\\n' after patch
- `03:13:21` patched: replaced old regex with r'\\A[\\w.@+-]+\\Z' in django/contrib/auth/validators.py for ASCIIUsernameValidator and UnicodeUsernameValidator
- `03:12:55` ACTION: python3 - <<'PY'
- `03:12:36` ACTION: sed -n '1,200p' django/contrib/auth/validators.py && python3 - <<'PY'
- `03:12:16` ACTION: nl -ba django/core/validators.py | sed -n '1,300p'
- `03:11:51` ACTION: python3 repro.py
- `03:11:48` Replaced regex in django/contrib/auth/validators.py: changed r'^[\\w.@+-]+$' to r'\\A[\\w.@+-]+\\Z' at ASCIIUsernameValidator and UnicodeUsernameValid...
- `03:11:38` ACTION: sed -i "s|regex = r'^[\\w.@+-]+$'|regex = r'\\\\A[\\\\w. [...]
- `03:11:24` repro.py: UnicodeUsernameValidator accepted 'foo\\n'; ASCIIUsernameValidator accepted 'foo\\n
- `03:11:11` ACTION: Reading file: <<'PY'
- `03:11:02` django/contrib/auth/validators.py: ASCIIUsernameValidator.regex r'^[\\w.@+-]+$' at line 10; UnicodeUsernameValidator.regex r'^[\\w.@+-]+$' at line 20
- `03:10:46` ACTION: nl -ba django/contrib/auth/validators.py | sed -n '1,200p'
- `03:09:56` ACTION: grep -nR -E 'UsernameValidator|ASCIIUsernameValidator|UnicodeUsernameValidator' .
- `03:09:46` TASK STARTED: UsernameValidator allows trailing newline in usernames
