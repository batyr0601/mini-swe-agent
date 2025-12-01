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
- [ ] 1. Analyze the codebase: find and read relevant files
- [ ] 2. Create a minimal script to reproduce the issue
- [ ] 3. Edit source code to resolve the issue
- [ ] 4. Verify fix works by running the reproduction script once
- [ ] 5. Submit immediately if verification passes

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 11:58] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `11:58:32` ACTION: Submitting solution
- `11:58:09` Root cause: empty list for 'fields' is falsy, so the 'fields' filter was skipped for fields=[]; fix checks 'fields is not None' to allow empty lists
- `11:58:09` Applied patch: replaced with 'if fields is not None and f.name not in fields:'; program output after patch: {}
- `11:58:09` File django/forms/models.py showed 'if fields and f.name not in fields:' at line 86
- `11:58:09` Initial reproduction printed: {'a': 1, 'b': 2}
- `11:57:31` ACTION: Reading file: <<'PY'
- `11:56:51` ACTION: nl -ba django/forms/models.py | sed -n '60,140p'
- `11:56:44` RESULT: 69:def model_to_dict(instance, fields=None, exclude=None):
- `11:56:44` ACTION: grep -n "def model_to_dict" -n django/forms/models.py || true
- `11:56:29` ACTION: nl -ba django/forms/models.py | sed -n '1,220p'
- `11:56:26` ACTION: grep -Rn "model_to_dict" || true
- `11:56:20` TASK STARTED: model_to_dict() should return an empty dict for an empty list of fields.
