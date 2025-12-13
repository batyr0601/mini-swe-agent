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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 12:00] **swebench-django__django-10914**: Task completed: LimitsExceeded
## Interaction Log

- `12:00:13` ACTION: sed -n '280,330p' django/conf/global_settings.py && sed -n '1,260p' django/core/files/storage.py
- `12:00:07` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSIONS" -e "FILE_UPLOAD_PERMISSION" django || true
- `11:59:51` ACTION: sed -n '160,320p' django/core/files/storage.py
- `11:59:45` ACTION: grep -nE "chmod|FILE_UPLOAD_PERMISSION|FILE_UPLOAD_PERMISSIONS" django/core/files/storage.py || true
- `11:59:28` ACTION: sed -n '1,360p' django/core/files/storage.py
- `11:59:22` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" -e "chmod(" -e "os. [...]
- `11:58:43` ACTION: sed -n '1,420p' django/core/files/storage.py
- `11:58:37` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" -e "chmod(" -e "os. [...]
- `11:58:20` ACTION: sed -n '1,320p' django/core/files/storage.py
- `11:58:15` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" django || true
- `11:58:02` ACTION: sed -n '1,320p' django/core/files/storage.py
- `11:57:54` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSIONS" -e "FILE_UPLOAD_PERMISSION" -e "chmod(" django/core/files || t [...]
- `11:57:36` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" -e "file_upload" django || true && [...]
- `11:57:22` ACTION: sed -n '1,320p' django/core/files/storage.py
- `11:57:17` grep results: django/conf/global_settings.py:307 FILE_UPLOAD_PERMISSIONS = None; django/core/files/storage.py:193 and 217 reference FILE_UPLOAD_PERMIS...
- `11:57:07` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSIONS" -e "FILE_UPLOAD_PERMISSION" django || true
- `11:56:53` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" -e "file_upload" django || true && [...]
- `11:56:37` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" django || true && sed -n '1,320p'  [...]
- `11:56:20` ACTION: sed -n '1,320p' django/core/files/storage.py
- `11:56:15` ACTION: grep -nR -e "FILE_UPLOAD_PERMISSION" -e "FILE_UPLOAD_PERMISSIONS" django || true
