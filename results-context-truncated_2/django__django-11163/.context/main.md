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
- [ ] 1. Understand the bug: reproduce model_to_dict(instance, fields=[]) returning all fields instead of empty dict
- [ ] 2. Locate the code: find definition of model_to_dict in the repository files
- [ ] 3. Root cause analysis: inspect occurrences of \
- [ ] 4. Implement fix: change condition to \
- [ ] 5. Verify fix: run a reproduction script and relevant tests to ensure model_to_dict(..., fields=[]) returns {}

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:14] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `21:14:28` ACTION: Submitting solution
- `21:14:19` verified fix: fields=[] returns empty dict; fields=None returns all fields; fields=['a'] returns only 'a
- `21:14:19` found problematic condition at django/forms/models.py:86,434: 'if fields and f.name not in fields' (empty list treated as falsy)
- `21:14:19` located model_to_dict at django/forms/models.py:69
- `21:14:19` repro: model_to_dict outputs: fields=None => {'a': 1, 'b': 2, 'c': 3}; fields=[] => {}; fields=['a'] => {'a': 1}
- `21:14:00` RESULT: fields=None => {'a': 1, 'b': 2, 'c': 3}
fields=[] => {}
fields=['a'] => {'a': 1}
- `21:13:59` ACTION: Reading file: test_model_to_dict.py
- `21:13:31` Replaced in django/forms/models.py (lines ~86 and ~434): 'if fields and f.name not in fields:' -> 'if fields is not None and f.name not in fields:
- `21:13:23` ACTION: sed -i "s/if fields and f.name not in fields:/if fields is not None and f. [...]
- `21:13:14` ACTION: nl -ba django/forms/models.py | sed -n '400,460p'
- `21:13:09` grep 'if fields and f.name not in fields': django/forms/models.py:86, django/forms/models.py:434
- `21:12:55` ACTION: grep -nR "if fields and f.name not in fields" || true
- `21:12:49` ACTION: nl -ba django/forms/models.py | sed -n '1,240p'
- `21:12:46` grep def model_to_dict: django/forms/models.py:69
- `21:12:37` ACTION: grep -nR "def model_to_dict" || true
- `21:12:25` TASK STARTED: model_to_dict() should return an empty dict for an empty list of fields.
