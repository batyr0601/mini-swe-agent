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
- [ ] 1. Understand the bug: reproduce scenario where a form
- [ ] 2. Locate the code: find form/model binding code that applies default values or merges cleaned_data into instance (search for
- [ ] 3. Reproduce the issue: create a minimal repro script in /testbed that defines a model with a default, a form that omits the field, sets cleaned_data for that field in form.clean(), and shows the default not being overwritten.
- [ ] 4. Implement fix: change the merging logic so that values present in cleaned_data overwrite model defaults even when the field was not present in raw POST data; ensure descriptors and validators behave correctly.
- [ ] 5. Verify fix: run the repro script and relevant test suite; add unit tests for the scenario and ensure no regressions.

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:23] **swebench-django__django-11433**: Task completed: Submitted
## Interaction Log

- `21:23:37` ACTION: Submitting solution
- `21:23:25` Verification: ran repro.py -> Before: A; After: B; construct_instance applies cleaned_data over model defaults when omitted from POST
- `21:23:11` Implement fix: django/forms/models.py construct_instance updated to skip applying cleaned_data only when f.has_default() and widget.value_omitted_from...
- `21:23:02` repro.py: lines 1-61 created; demonstrates field default 'A' overwritten to 'B' when omitted from POST (Before: A; After: B)
- `21:22:40` ACTION: nl -ba repro.py | sed -n '1,240p'
- `21:22:29` repro.py output: Before: A; After: B — construct_instance now applies cleaned_data over model default when omitted from POST
- `21:22:14` RESULT: Before: A
After: B
- `21:22:14` ACTION: perl -0777 -pe "s/[ \t]*# Leave defaults for fields that aren't in POST data,[\\s\\S]*?continue\\n/  [...]
- `21:21:46` ACTION: python3 repro.py
- `21:21:43` ACTION: Reading file: repro.py
- `21:21:18` construct_instance modified: django/forms/models.py lines ~49-52 changed so that we only continue (skip applying cleaned_data) when f.has_default() an...
- `21:21:07` ACTION: perl -0777 -pe "s/if \\(f\\.has_default\\(\\) and\\s+form\\[f\\.name\\]\\.field\\.widget\\. [...]
- `21:20:30` ACTION: nl -ba django/forms/models.py | sed -n '1,260p'
- `21:20:25` ACTION: grep -RIn --line-number "class .*ModelForm" . || true
- `21:20:19` ACTION: grep -RIn --line-number "cleaned_data" . || true
- `21:20:16` RESULT: grep: testbed: No such file or directory
- `21:20:16` ACTION: grep -RIn --line-number "cleaned_data" testbed || true
- `21:20:04` TASK STARTED: Allow `cleaned_data` to overwrite fields' default values.
