# Project Goals

**Current Task:** model_to_dict() should return an empty dict for an empty list of fields.

<details>
<summary>Full description</summary>

model_to_dict() should return an empty dict for an empty list of fields.
Description
	
Been called as model_to_dict(instance, fields=[]) function should return empty dict, because no fields were requested. But it returns all fields
The problem point is
if fields and f.name not in fields:
which should be
if fields is not None and f.name not in fields:
PR: ​https://github.com/django/django/pull/11150/files

</details>


## TODO List

- [ ] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:35] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `23:35:00` ACTION: Submitting solution
- `23:34:56` repro shows model_to_dict([]) returns {} and model_to_dict(None) returns full dict; fix verified
- `23:34:52` replaced 'if fields and f.name not in fields' with 'if fields is not None and f.name not in fields' in django/forms/models.py
- `23:34:50` ACTION: sed -i "s/if fields and f.name not in fields:/if fields is not None and f. [...]
- `23:34:30` ACTION: Reading file: repro_model_to_dict.py
- `23:34:14` found model_to_dict in django/forms/models.py: lines 69-91; conditional 'if fields and f.name not in fields' treats fields=[] as False and causes all ...
- `23:34:02` ACTION: nl -ba django/forms/models.py | sed -n '1,240p'
- `23:33:55` ACTION: grep -nR "def model_to_dict" . || true
- `23:33:52` RESULT: grep: testbed: No such file or directory
- `23:33:51` ACTION: grep -nR "def model_to_dict" testbed || true
- `23:33:40` TASK STARTED: model_to_dict() should return an empty dict for an empty list of fields.
