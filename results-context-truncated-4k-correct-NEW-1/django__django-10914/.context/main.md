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
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Inspect django/core/files/storage.py around file_permissions_mode and save methods (lines ~150-320)
- [ ] 2. Implement minimal patch if file_permissions_mode is not an int when passed to os.chmod
- [ ] 3. Run the minimal reproduction script once to verify permissions are applied
- [ ] 4. Submit the change if verification passes
- [ ] 1. Open django/core/files/storage.py and inspect file_permissions_mode, directory_permissions_mode, and _save to confirm how os.chmod is called
- [ ] 2. Create a minimal reproduction script repro_chmod.py that sets FILE_UPLOAD_PERMISSIONS to a string like
- [ ] 3. Modify django/core/files/storage.py to coerce string permission values to int using int(value, 8) in file_permissions_mode and directory_permissions_mode, and ensure non-string, non-int values raise a clear TypeError
- [ ] 4. Run the minimal reproduction script once to verify the TypeError is resolved
- [ ] 5. If verification passes, mark the relevant TODOs complete and submit the patch

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:23] **swebench-django__django-10914**: Task completed: LimitsExceeded
## Interaction Log

- `14:21:27` ACTION: sed -n '150,320p' django/core/files/storage.py
- `14:21:14` ACTION: sed -n '1,400p' django/core/files/storage.py
- `14:20:31` ACTION: sed -n '150,320p' django/core/files/storage.py
- `14:20:02` ACTION: grep -n -E "def (file_permissions_mode|directory_permissions_mode|_save)\b" django/core/files/storag [...]
- `14:19:43` django/core/files/storage.py: file_permissions_mode and directory_permissions_mode cached_property return settings values unchanged; _save calls os.ch...
- `14:17:12` django/core/files/storage.py: file_permissions_mode cached_property returns raw value (constructor or settings.FILE_UPLOAD_PERMISSIONS); _save calls o...
- `14:17:01` ACTION: sed -n '150,320p' django/core/files/storage.py
- `14:16:48` ACTION: grep -RIn -E "file_permissions_mode|FILE_UPLOAD_PERMISSIONS" django || true
- `14:16:38` Reproducer saved_path: tmp_storage_test/test.txt; mode_octal: 0o644; file_permissions_mode_attr: 420
- `14:16:11` ACTION: python3 - <<'PY'
- `14:15:48` django/core/files/storage.py lines 240-520: save writes file using os.open + locks in a loop; after successful save, if self.file_permissions_mode is ...
- `14:15:30` ACTION: sed -n '240,520p' django/core/files/storage.py
- `14:15:24` ACTION: sed -n '160,240p' django/core/files/storage.py
- `14:15:18` grep FILE_UPLOAD_PERMISSIONS: django/conf/global_settings.py:307, django/core/files/storage.py:193,217
- `14:15:11` ACTION: grep -RIn "FILE_UPLOAD_PERMISSIONS" django || true
- `14:15:03` global_settings.FILE_UPLOAD_PERMISSIONS = 420
- `14:14:54` RESULT: 420
- `14:14:54` ACTION: python3 -c 'import django.conf.global_settings as g; print(repr(g.FILE_UPLOAD_PERMISSIONS))'
- `14:14:33` ACTION: perl -0777 -pe 's/FILE_UPLOAD_PERMISSIONS = None/FILE_UPLOAD_PERMISSIONS = 0o644/' -i django/conf/gl [...]
- `14:14:21` ACTION: sed -n '270,320p' django/conf/global_settings.py
