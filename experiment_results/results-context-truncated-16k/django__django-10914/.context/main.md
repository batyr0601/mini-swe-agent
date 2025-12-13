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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:31] **swebench-django__django-10914**: Task completed: Submitted
## Interaction Log

- `23:31:07` ACTION: Submitting solution
- `23:31:02` Verified FILE_UPLOAD_PERMISSIONS is 0o644 (decimal 420) via python import check
- `23:30:52` RESULT: 420
0o644
- `23:30:52` ACTION: python3 - <<'PY'
- `23:30:36` Updated default FILE_UPLOAD_PERMISSIONS to 0o644 in django/conf/global_settings.py
- `23:30:26` ACTION: sed -i 's/^FILE_UPLOAD_PERMISSIONS = None/FILE_UPLOAD_PERMISSIONS = 0o644/' django/conf/global_setti [...]
- `23:29:59` ACTION: nl -ba django/core/files/storage.py | sed -n '1,260p'
- `23:29:54` ACTION: nl -ba django/conf/global_settings.py | sed -n '1,360p'
- `23:29:46` ACTION: grep -RIn --line-number -e "FILE_UPLOAD_PERMISSIONS" -e "FileSystemStorage" -e "tempfile. [...]
- `23:29:40` ACTION: ls -la
- `23:29:37` RESULT: grep: testbed: No such file or directory
- `23:29:37` ACTION: grep -RIn --line-number -e "FILE_UPLOAD_PERMISSIONS" -e "FILE_UPLOAD_PERMISSION" -e "FileSystemStora [...]
- `23:29:19` TASK STARTED: Set default FILE_UPLOAD_PERMISSION to 0o644.
