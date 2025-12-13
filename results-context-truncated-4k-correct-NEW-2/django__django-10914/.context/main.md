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

- [2025-12-02 14:43] **swebench-django__django-10914**: Task completed: Submitted
## Interaction Log

- `14:43:22` ACTION: Submitting solution
- `14:43:07` Test verification: saved file /tmp/tmpa2nm_iep/test.txt with mode_octal = 0o644
- `14:42:50` RESULT: /tmp/tmpa2nm_iep/test.txt
mode_octal = 0o644
- `14:42:35` ACTION: python3 - <<'PY'
- `14:42:17` global_settings.py: changed FILE_UPLOAD_PERMISSIONS from None to FILE_UPLOAD_PERMISSIONS = 0o644; runtime FILE_UPLOAD_PERMISSIONS = 420
- `14:42:06` ACTION: perl -pi -e "s/^[ \t]*FILE_UPLOAD_PERMISSIONS\s*=.*$/FILE_UPLOAD_PERMISSIONS = 0o644/" django/conf/g [...]
- `14:41:38` ACTION: grep -nR --line-number --exclude-dir=.git "FILE_UPLOAD_PERMISSIONS" django || true && python3 - <<'P [...]
- `14:41:12` ACTION: grep -nR --line-number --exclude-dir=.git "FILE_UPLOAD_PERMISSIONS" . [...]
- `14:40:56` ACTION: sed -n '280,320p' django/conf/global_settings.py && sed -n '160,240p' django/core/files/storage. [...]
- `14:40:41` ACTION: grep -R --line-number --exclude-dir=.git "FILE_UPLOAD_PERMISSIONS" .
- `14:40:31` TASK STARTED: Set default FILE_UPLOAD_PERMISSION to 0o644.
