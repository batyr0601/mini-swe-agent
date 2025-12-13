# Project Goals

**Current Task:** Allow `cleaned_data` to overwrite fields' default values.

<details>
<summary>Full description</summary>

Allow `cleaned_data` to overwrite fields' default values.
Description
	
See comments here: ​https://github.com/django/django/pull/7068/files#r289432409
Currently, when submitting a form, if 'some_field' isn't in the data payload (e.g. it wasn't included in the form, perhaps because its value is derived from another field), and 'some_field' has a default value on the model, it cannot be overwritten with 'self.cleaned_data'.
This does not really follow the paradigm of modifying data in 'cleaned_data'. It requires the user to copy and overwrite the raw data submitted with the form.

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

- [2025-12-03 03:21] **swebench-django__django-11433**: Task completed: Submitted
## Interaction Log

- `03:21:47` ACTION: Submitting solution
- `03:21:42` Verification: ran repro_construct_instance.py once -> Before: DEFAULT, After: CLEANED (cleaned_data applied)
- `03:21:42` Implemented fix: construct_instance applies cleaned_data when present even if field.has_default() and widget reports omitted
- `03:21:42` patched django/forms/models.py: changed omission check so fields are skipped only when widget.value_omitted_from_data(...) is True AND f.name not in f...
- `03:21:27` RESULT: patched
Before: DEFAULT
After: CLEANED
- `03:21:26` ACTION: python3 - <<'PY'
- `03:20:41` RESULT: patched
Before: DEFAULT
After: DEFAULT
- `03:20:41` ACTION: python3 - <<'PY'
- `03:19:59` Found root cause: construct_instance in django/forms/models.py (lines 31-64) skips fields when f.has_default() and widget.value_omitted_from_data(...)...
- `03:19:34` repro_construct_instance.py: Before DEFAULT After DEFAULT — construct_instance did not apply cleaned_data['foo']='CLEANED' when f.has_default() is Tru...
- `03:19:14` RESULT: Before: DEFAULT
After: DEFAULT
- `03:19:12` ACTION: Reading file: <<'PY'
- `03:18:31` ACTION: nl -ba django/forms/models.py | sed -n '1,160p'
- `03:18:26` ACTION: grep -nR "construct_instance\\|cleaned_data\\|default=" django | sed -n '1,200p'
- `03:18:20` ACTION: ls -la
