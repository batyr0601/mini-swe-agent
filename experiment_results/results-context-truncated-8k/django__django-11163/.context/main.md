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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:14] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `03:14:11` ACTION: Submitting solution
- `03:13:59` repro output: model_to_dict(inst, fields=None) => {'id': 'value_id', 'name': 'value_name', 'score': 'value_score'}; model_to_dict(inst, fields=[]) => ...
- `03:13:42` ACTION: Reading file: repro_model_to_dict.py
- `03:13:31` Replaced 'if fields and f.name not in fields:' with 'if fields is not None and f.name not in fields:' in django/forms/models.py to allow empty list of...
- `03:13:25` ACTION: sed -i "s/if fields and f.name not in fields:/if fields is not None and f. [...]
- `03:13:12` ACTION: nl -ba django/forms/models.py | sed -n '1,220p'
- `03:12:51` ACTION: grep -nR --exclude-dir=.git "model_to_dict" . || true
- `03:12:48` RESULT: grep: testbed: No such file or directory
- `03:12:47` ACTION: grep -nR "model_to_dict" testbed || true
- `03:12:39` TASK STARTED: model_to_dict() should return an empty dict for an empty list of fields.
