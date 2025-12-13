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
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:30] **swebench-django__django-11163**: Task completed: Submitted
## Interaction Log

- `14:30:05` ACTION: Submitting solution
- `14:29:58` repro.py output: '{}' — model_to_dict returns empty dict for empty fields list; AttributeError no longer occurs; root cause: 'if fields' treated empty...
- `14:29:42` RESULT: {}
- `14:29:41` ACTION: python3 repro.py
- `14:29:19` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,160p' django/forms/models. [...]
- `14:28:50` ACTION: grep -RnE "repro|reproduce|minimal|model_to_dict" . || true
- `14:28:34` django/forms/models.py: changed 'if fields and f.name not in fields' to 'if fields is not None and f.name not in fields' at hunks @@ -83 and @@ -431 (...
- `14:28:19` ACTION: perl -0777 -pe "s/if fields and f\.name not in fields:/if fields is not None and f. [...]
- `14:28:01` Found model_to_dict in django/forms/models.py:69; contains 'if fields and f.name not in fields' which treats empty list as False (should check for Non...
- `14:27:42` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,140p' django/forms/models.py
- `14:27:36` repro.py: model_to_dict returned {} for fields=[]
- `14:27:30` RESULT: {}
- `14:27:21` repro.py: AttributeError \"'DummyMeta' object has no attribute 'concrete_fields'\" at /testbed/django/forms/models.py:83
- `14:27:12` ACTION: Reading file: <<'PY'
- `14:26:54` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,400p' django/forms/models.py
- `14:26:32` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,320p' django/forms/models.py
- `14:26:06` ACTION: line=$(grep -n "def model_to_dict" django/forms/models. [...]
- `14:23:20` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,320p' django/forms/models.py
- `14:23:02` ACTION: sed -n '1,400p' django/forms/models.py
- `14:22:47` ACTION: grep -n "def model_to_dict" django/forms/models.py && sed -n '1,300p' django/forms/models.py
