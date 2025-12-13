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
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:34] **swebench-django__django-11099**: Task completed: Submitted
## Interaction Log

- `23:34:16` ACTION: Submitting solution
- `23:34:11` RegexValidator.__call__ uses self.regex.search(str(value)) (django/core/validators.py:57). Root cause: $ can match before a trailing newline, allowing...
- `23:33:59` ACTION: nl -ba django/core/validators.py | sed -n '1,240p'
- `23:33:46` repro.py: VALID 'normaluser'; INVALID 'user_with_newline\\n'; newline rejected as expected after replacing r'^[\\w.@+-]+$' with r'\\A[\\w.@+-]+\\Z' in...
- `23:33:19` ACTION: Reading file: repro.py
- `23:33:04` Updated django/contrib/auth/validators.py: replaced r'^[\\w.@+-]+$' with r'\\A[\\w.@+-]+\\Z
- `23:32:53` RESULT: UPDATED
- `23:32:52` ACTION: python3 - <<'PY'
- `23:32:36` ACTION: nl -ba django/contrib/auth/validators.py | sed -n '1,200p'
- `23:32:28` ACTION: grep -nR "UsernameValidator\|contrib/auth/validators. [...]
- `23:32:23` RESULT: grep: testbed: No such file or directory
- `23:32:22` ACTION: grep -nR '\[\\w.@+-\]' testbed || true
- `23:32:01` TASK STARTED: UsernameValidator allows trailing newline in usernames
