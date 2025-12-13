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

- [2025-12-02 18:40] **swebench-django__django-11099**: Task completed: Submitted
## Interaction Log

- `18:40:05` ACTION: Submitting solution
- `18:40:00` repro after fix: v('joe\\n') returned INVALID
- `18:40:00` patched validators.py: regex changed from '^[\\w.@+-]+$' to '^[\\w.@+-]+\\Z' (CHANGED)
- `18:40:00` repro before fix: v('joe\\n') returned VALID
- `18:39:27` ACTION: python3 - <<'PY'
- `18:38:13` RESULT: VALID
- `18:38:12` ACTION: python3 - <<'PY'
- `18:37:58` ACTION: sed -n '228,320p' tests/auth_tests/test_validators.py
- `18:37:46` ACTION: sed -n '1,240p' django/contrib/auth/validators.py
- `18:37:40` ACTION: grep -nR "UsernameValidator" . --exclude-dir=.git || true
- `18:37:36` ACTION: grep -nR "class UsernameValidator" -n || true
- `18:37:27` TASK STARTED: UsernameValidator allows trailing newline in usernames
