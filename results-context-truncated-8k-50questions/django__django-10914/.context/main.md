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

- [2025-12-03 03:09] **swebench-django__django-10914**: Task completed: Submitted
## Interaction Log

- `03:09:11` ACTION: Submitting solution
- `03:09:04` verification run: global_settings.FILE_UPLOAD_PERMISSIONS=420; settings.FILE_UPLOAD_PERMISSIONS=420; FileSystemStorage()._file_permissions_mode=None
- `03:08:30` python verification: accessing settings.FILE_UPLOAD_PERMISSIONS raised ImproperlyConfigured ('Requested setting FILE_UPLOAD_PERMISSIONS, but settings ...
- `03:08:08` ACTION: python3 - <<'PY'
- `03:07:41` django/conf/global_settings.py: FILE_UPLOAD_PERMISSIONS changed from None to 0o644 (git diff shown)
- `03:07:30` ACTION: perl -0777 -pe "s/FILE_UPLOAD_PERMISSIONS = None/FILE_UPLOAD_PERMISSIONS = 0o644/" -i django/conf/gl [...]
- `03:07:09` ACTION: nl -ba django/conf/global_settings.py | sed -n '1,360p'
- `03:06:51` ACTION: grep -R --line-number "FILE_UPLOAD_PERMISSIONS" || true
- `03:06:42` ACTION: ls -la
- `03:06:39` RESULT: ls: cannot access 'testbed': No such file or directory
- `03:06:36` ACTION: ls -la testbed
- `03:06:29` TASK STARTED: Set default FILE_UPLOAD_PERMISSION to 0o644.
