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

- [2025-12-02 23:39] **swebench-django__django-11433**: Task completed: Submitted
## Interaction Log

- `23:39:47` ACTION: Submitting solution
- `23:39:43` Verified fix: test_repro.py printed 'overwritten_by_cleaned_data
- `23:39:35` Implemented fix: changed construct_instance skip-default condition to also check 'and f.name not in cleaned_data' in django/forms/models.py
- `23:39:33` Root cause: construct_instance treated fields with defaults as omitted if widget.value_omitted_from_data returned True, without checking cleaned_data;...
- `23:39:31` Found construct_instance in django/forms/models.py (lines ~31-64): it skipped assigning fields with defaults when widget.value_omitted_from_data(...) ...
- `23:39:22` test_repro.py: cleaned_data overwrote default; printed 'overwritten_by_cleaned_data
- `23:39:20` RESULT: overwritten_by_cleaned_data
- `23:39:19` ACTION: Reading file: <<'PY'
- `23:38:56` django/forms/models.py: updated construct_instance to allow cleaned_data to overwrite model defaults by adding 'and f.name not in cleaned_data' to the...
- `23:38:49` RESULT: UPDATED
- `23:38:48` ACTION: python3 - <<'PY'
- `23:38:11` ACTION: nl -ba django/forms/models.py | sed -n '1,220p'
- `23:38:05` ACTION: grep -nR "construct_instance\|cleaned_data" django | sed -n '1,200p'
- `23:37:54` ACTION: ls -la
- `23:37:45` TASK STARTED: Allow `cleaned_data` to overwrite fields' default values.
