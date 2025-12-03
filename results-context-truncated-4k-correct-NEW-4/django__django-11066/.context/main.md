# Project Goals

**Current Task:** RenameContentType._rename() doesn't save the content type on the correct database

<details>
<summary>Full description</summary>

RenameContentType._rename() doesn't save the content type on the correct database
Description
	
The commit in question:
​https://github.com/django/django/commit/f179113e6cbc8ba0a8d4e87e1d4410fb61d63e75
The specific lines in question:
​https://github.com/django/django/blob/586a9dc4295357de1f5ad0590ad34bf2bc008f79/django/contrib/contenttypes/management/__init__.py#L27
with transaction.atomic(using=db): 
	content_type.save(update_fields={'model'})
The issue:
For some background, we run a dynamic database router and have no "real" databases configured in the settings file, just a default sqlite3 backend which is never actually generated or used. We forked the migrate.py management command and modified it to accept a dictionary containing database connection parameters as the --database argumen...
</details>


## TODO List

<!-- 
Add detailed, specific TODOs when starting a task. Good examples:
- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:45` ACTION: sed -n '1,240p' tests/contenttypes_tests/test_operations.py
- `18:35:27` ACTION: sed -n '1,240p' django/contrib/contenttypes/management/__init__.py
- `18:35:25` ACTION: sed -n '1,240p' tests/contenttypes_tests/test_operations.py
- `18:34:55` ACTION: perl -0777 -pe "s/content_type\.save\(update_fields=\{\s*'model'\s*\}\)/content_type. [...]
- `18:34:31` ACTION: sed -n '1,240p' django/contrib/contenttypes/management/__init__.py
- `18:34:17` ACTION: sed -n '1,240p' tests/contenttypes_tests/test_operations.py
- `18:34:09` ACTION: sed -n '1,240p' django/contrib/contenttypes/management/__init__.py
- `18:34:05` ACTION: git grep -n "RenameContentType" || git grep -n "rename_content_type" || true
- `18:33:50` TASK STARTED: RenameContentType._rename() doesn't save the content type on the correct database
