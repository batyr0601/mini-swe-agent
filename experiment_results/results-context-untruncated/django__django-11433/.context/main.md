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

- [2025-12-03 00:43] **swebench-django__django-11433**: Task completed: Submitted
## Interaction Log

- `00:43:51` ACTION: Submitting solution
- `00:43:47` test_repro.py output: new_value (cleaned_data overwrote default); verification passed
- `00:43:38` RESULT: new_value
- `00:43:38` ACTION: python3 test_repro.py
- `00:43:30` Implemented fix in django/forms/models.py: construct_instance now skips default-only fields only if f.name not in cleaned_data and widget.value_omitte...
- `00:43:23` Root cause: construct_instance skipped setting fields with defaults whenever widget.value_omitted_from_data(...) returned True, which prevented values...
- `00:43:16` Found construct_instance in django/forms/models.py; original conditional skipped fields with defaults when widget.value_omitted_from_data was True; pa...
- `00:43:09` Repro: cleaned_data overwrites default when widget.value_omitted_from_data is True (got new_value)
- `00:43:07` RESULT: new_value
- `00:43:06` ACTION: Reading file: <<'PY'
- `00:42:34` ACTION: perl -0777 -i -pe 's/if\s*\(\s*f\.has_default\(\)\s*and\s*\n\s*form\[f\.name\]\.field\.widget\. [...]
- `00:39:54` construct_instance: lines 49-53: conditional skips fields with defaults when widget.value_omitted_from_data is True; it does NOT check whether f.name ...
- `00:39:44` ACTION: nl -ba django/forms/models.py | sed -n '31,64p'
- `00:38:56` ACTION: nl -ba django/forms/models.py | sed -n '1,160p;320,520p'
- `00:38:28` ACTION: grep -RIn "cleaned_data" django || true
- `00:38:25` ACTION: ls -la
- `00:38:20` RESULT: grep: testbed: No such file or directory
- `00:38:20` ACTION: grep -RIn "cleaned_data" testbed || true
- `00:38:05` TASK STARTED: Allow `cleaned_data` to overwrite fields' default values.
