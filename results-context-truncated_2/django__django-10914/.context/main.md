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
- [ ] 1. Understand the bug: Reproduce discrepancy in file permissions between MemoryUploadedFile and TemporaryUploadedFile when using FileSystemStorage; create repro script to upload small and large files and inspect permission bits
- [ ] 2. Locate the code: Find FileSystemStorage implementation and any tempfile/os.rename usages in testbed package files
- [ ] 3. Root cause analysis: Inspect save() and _save methods, and temp file handling to see if permissions are preserved or reset; check for calls to tempfile.NamedTemporaryFile and os.rename
- [ ] 4. Implement fix: Ensure that saved files get default permission 0o644 unless overridden by FILE_UPLOAD_PERMISSIONS setting; add os.chmod call in FileSystemStorage._save or equivalent
- [ ] 5. Verify fix: Run repro script to confirm both paths produce files with 0o644; log results and mark todos complete

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:51] **swebench-django__django-10914**: Task completed: Submitted
## Interaction Log

- `20:51:09` ACTION: Submitting solution
- `20:51:03` test_permission.py: tempfile initial mode 0o600; saved from_temp mode 0o644; saved from_stream mode 0o644; MEDIA_DIR was /tmp/media_w0jk5q5_; change t...
- `20:50:23` ACTION: Reading file: test_permission.py
- `20:49:57` Updated default FILE_UPLOAD_PERMISSIONS to 0o644 in django/conf/global_settings.py (line 307)
- `20:49:50` ACTION: sed -i "s/FILE_UPLOAD_PERMISSIONS = None/FILE_UPLOAD_PERMISSIONS = 0o644/" django/conf/global_settin [...]
- `20:49:42` ACTION: nl -ba django/conf/global_settings.py | sed -n '290,320p'
- `20:49:37` Found FileSystemStorage._save: calls os.chmod(full_path, self.file_permissions_mode) at storage.py:283-284 when file_permissions_mode is not None; glo...
- `20:49:27` ACTION: nl -ba django/core/files/storage.py | sed -n '1,320p'
- `20:49:21` ACTION: grep -RIn --line-number -E "FileSystemStorage|FILE_UPLOAD_PERMISSIONS|tempfile\. [...]
- `20:49:16` ACTION: ls -la
- `20:49:13` RESULT: grep: testbed: No such file or directory
- `20:49:12` ACTION: grep -RIn -E "FileSystemStorage|tempfile\.NamedTemporaryFile|NamedTemporaryFile|os\. [...]
- `20:48:49` TASK STARTED: Set default FILE_UPLOAD_PERMISSION to 0o644.
