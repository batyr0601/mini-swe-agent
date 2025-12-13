# Project Goals

**Current Task:** ModelBackend.authenticate() shouldn't make a database query when username is None

<details>
<summary>Full description</summary>

ModelBackend.authenticate() shouldn't make a database query when username is None
Description
	
It's easier to explain my issue by adding a comment in the current implementation of ModelBackend.authenticate():
	def authenticate(self, request, username=None, password=None, **kwargs):
		if username is None:
			username = kwargs.get(UserModel.USERNAME_FIELD)
		# At this point, username and password can be None,
		# typically if credentials are provided for another backend.
		# Continuing makes a useless database query and runs
		# the password hasher needlessly (which is expensive).
		try:
			user = UserModel._default_manager.get_by_natural_key(username)
		except UserModel.DoesNotExist:
			# Run the default password hasher once to reduce the timing
			# difference between an existing and a no...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:28] **swebench-django__django-11451**: Task completed: Submitted
## Interaction Log

- `14:28:12` ACTION: Submitting solution
- `14:28:06` repro.py: authenticate returned 'None' when username=None; no DB query observed
- `14:27:55` RESULT: authenticate returned: None
- `14:27:55` ACTION: python3 repro.py
- `14:27:40` ACTION: sed -n '1,240p' django/contrib/auth/backends.py
- `14:27:20` ACTION: sed -n '1,120p' django/contrib/auth/backends.py
- `14:27:13` ACTION: grep -nE "class ModelBackend|def authenticate" django/contrib/auth/backends.py
- `14:26:45` ACTION: grep -nE "class ModelBackend|def authenticate" django/contrib/auth/backends. [...]
- `14:26:27` ACTION: sed -n '1,160p' django/contrib/auth/backends.py
- `14:26:22` ACTION: grep -n "def authenticate" django/contrib/auth/backends.py
- `14:25:52` ACTION: sed -n '1,120p' django/contrib/auth/backends.py
- `14:25:47` ACTION: grep -nE "class ModelBackend|def authenticate" django/contrib/auth/backends.py
- `14:25:27` ACTION: grep -R "repro" -n || true && grep -R "reproduce" -n || true && grep -R "ModelBackend" -n || true && [...]
- `14:25:03` Implemented fix: return None when username is None after kwargs fallback in django/contrib/auth/backends.py (inserted 'if username is None: return Non...
- `14:24:54` Inserted 'if username is None: return None' after 'username = kwargs.get(UserModel.USERNAME_FIELD)' in django/contrib/auth/backends.py (PATCH_APPLIED)...
- `14:24:32` ACTION: python3 - <<'PY'
- `14:23:51` ACTION: sed -n '34,120p' django/contrib/auth/backends.py
- `14:23:46` ACTION: grep -nE "class ModelBackend|def authenticate" django/contrib/auth/backends.py
- `14:23:31` ACTION: grep -n "def authenticate" django/contrib/auth/backends. [...]
- `14:23:17` ACTION: sed -n '1,240p' django/contrib/auth/backends.py
