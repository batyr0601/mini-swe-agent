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

- [2025-12-03 00:35] **swebench-django__django-11099**: Task completed: Submitted
## Interaction Log

- `00:35:28` ACTION: Submitting solution
- `00:35:23` Verification: UnicodeUsernameValidator 'user' VALID; 'user\\n' INVALID; ASCIIUsernameValidator 'user' VALID; 'user\\n' INVALID
- `00:34:47` Replaced ^[\\w.@+-]+$ with \\A[\\w.@+-]+\\Z in django/contrib/auth/validators.py (lines 10 and 20)
- `00:34:34` ACTION: python3 - <<'PY'
- `00:34:16` django/contrib/auth/validators.py: ASCIIUsernameValidator regex at line 10: ^[\w.@+-]+$; UnicodeUsernameValidator regex at line 20: ^[\w.@+-]+$
- `00:34:02` Repro: UnicodeUsernameValidator accepted 'user' and 'user\\n' (both VALID)
- `00:33:50` RESULT: 'user' VALID
'user\n' VALID
- `00:33:49` ACTION: python3 - <<'PY'
- `00:33:35` ACTION: nl -ba django/contrib/auth/validators.py | sed -n '1,160p'
- `00:33:30` ACTION: grep -nR -E "UsernameValidator|ASCIIUsernameValidator|UnicodeUsernameValidator|contrib/auth/validato [...]
- `00:33:26` RESULT: grep: testbed: No such file or directory
- `00:33:25` ACTION: grep -nR "UsernameValidator\|ASCIIUsernameValidator\|UnicodeUsernameValidator\|contrib/auth/validato [...]
- `00:33:09` TASK STARTED: UsernameValidator allows trailing newline in usernames
