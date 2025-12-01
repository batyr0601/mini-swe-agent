# Project Goals

**Current Task:** Set default FILE_UPLOAD_PERMISSION to 0o644.

<details>
<summary>Full description</summary>

Set default FILE_UPLOAD_PERMISSION to 0o644.
Description
	
Hello,
As far as I can see, the ​File Uploads documentation page does not mention any permission issues.
What I would like to see is a warning that in absence of explicitly configured FILE_UPLOAD_PERMISSIONS, the permissions for a file uploaded to FileSystemStorage might not be consistent depending on whether a MemoryUploadedFile or a TemporaryUploadedFile was used for temporary storage of the uploaded data (which, with the default FILE_UPLOAD_HANDLERS, in turn depends on the uploaded data size).
The tempfile.NamedTemporaryFile + os.rename sequence causes the resulting file permissions to be 0o0600 on some systems (I experience it here on CentOS 7.4.1708 and Python 3.6.5). In all probability, the implementation of Python's built-in...
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

- [2025-12-03 00:33] **swebench-django__django-10914**: Task completed: Submitted
## Interaction Log

- `00:33:56` ACTION: Submitting solution
- `00:33:50` Verified fix: repro.py saved file with permissions 0o644; storage applies FILE_UPLOAD_PERMISSIONS via os.chmod
- `00:33:42` Root cause: tempfile creates temporary files with restrictive perms (e.g. 0o600); os.rename preserves those perms so saved files can end up 0o600. Fix...
- `00:33:36` Found django/core/files/move.py: file_move_safe uses os.rename and falls back to copying + copystat; tempfile.NamedTemporaryFile + os.rename can resul...
- `00:33:22` repro.py: saved file had permissions 0o644 as expected
- `00:33:07` RESULT: saved: /tmp/tmpazn07cb3/test_perm.txt
mode: 0o644
OK: permissions are 0o644
- `00:33:06` ACTION: python3 repro.py
- `00:32:57` ACTION: Reading file: repro.py
- `00:32:43` ACTION: python3 repro.py
- `00:32:37` ACTION: Reading file: repro.py
- `00:32:15` ACTION: nl -ba django/core/files/storage.py | sed -n '120,220p'
- `00:32:06` ACTION: nl -ba django/core/files/move.py | sed -n '1,240p'
- `00:31:45` ACTION: nl -ba django/core/files/storage.py | sed -n '1,320p'
- `00:31:33` Changed django/conf/global_settings.py: FILE_UPLOAD_PERMISSIONS from None to 0o644
- `00:31:24` ACTION: sed -i 's/FILE_UPLOAD_PERMISSIONS = None/FILE_UPLOAD_PERMISSIONS = 0o644/' django/conf/global_settin [...]
- `00:31:01` ACTION: nl -ba django/conf/global_settings.py | sed -n '290,320p'
- `00:30:51` ACTION: grep -Rn "FILE_UPLOAD_PERMISSIONS" -n django || true
- `00:30:47` ACTION: ls -la
