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

- [2025-12-03 00:36] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `00:36:50` ACTION: Submitting solution
- `00:36:42` Verification: repro.py shows model_to_dict with fields=[] returns {} and with fields=None returns all fields
- `00:36:42` Change made: replaced conditional with 'if fields is not None and f.name not in fields' in django/forms/models.py
- `00:36:42` Root cause: empty list is falsy; conditional skipped when fields==[] leading to returning all fields
- `00:36:42` Located model_to_dict in django/forms/models.py: lines 69-91; fields check at line 86 used 'if fields and f.name not in fields
- `00:36:21` ACTION: python3 repro.py
- `00:36:16` ACTION: sed -i "s/if fields and f.name not in fields:/if fields is not None and f. [...]
- `00:36:06` ACTION: nl -ba django/forms/models.py | sed -n '80,92p'
- `00:35:51` repro.py: model_to_dict with fields=None: {'a': 'value_a', 'b': 'value_b'}; model_to_dict with fields=[] returned {'a': 'value_a', 'b': 'value_b'} (em...
- `00:35:35` ACTION: Reading file: repro.py
- `00:35:11` ACTION: nl -ba django/forms/models.py | sed -n '1,220p'
- `00:35:02` grep model_to_dict: django/forms/models.py:69,290; tests/model_forms/tests.py:15,1816,2414,2909; docs/releases/1.10.txt:910
- `00:34:55` ACTION: grep -nR "model_to_dict" .
- `00:34:46` TASK STARTED: model_to_dict() should return an empty dict for an empty list of fields.
