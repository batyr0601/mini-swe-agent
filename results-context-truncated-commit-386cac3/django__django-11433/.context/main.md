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
- [ ] 1. Understand the bug: reproduce case where a model field has a default and form.cleaned_data should overwrite that default even if the field is missing from the submitted data
- [ ] 2. Locate the code: find form/model form processing functions that apply defaults or populate model instances (e.g., ModelForm.save, populate_instance, _post_clean) in testbed
- [ ] 3. Root cause analysis: inspect logic that sets missing fields from model defaults instead of using cleaned_data when provided by form.clean()
- [ ] 4. Implement fix: modify the population logic to prefer values in cleaned_data over model defaults even when the field wasn
- [ ] 5. Verify fix: create a small reproduction script using a model with a default and a ModelForm that derives a value in clean(), then run it to confirm cleaned_data overwrites the model default

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:34] **swebench-django__django-11433**: Task completed: LimitsExceeded
- [2025-12-01 21:32] **swebench-django__django-11433**: Finalize: complete TODOs and record final verification of construct_instance fix
## Interaction Log

- `21:34:34` ACTION: true
- `21:34:27` RESULT: afb41ab458 Allow cleaned_data to overwrite model defaults in construct_instance (skip defaults only when omitted from POST and not in cleaned_...
- `21:34:27` ACTION: git --no-pager show --no-patch -s --pretty=format:"%h %s%nAuthor: %an%nDate: %ad" HEAD && echo "Repr [...]
- `21:34:02` ACTION: true
- `21:33:58` RESULT: DONE: commit afb41ab458 applied; repro passed (is_valid=True, cleaned_data={'some_field':10}, instance.some_field=10); repo clean.
- `21:33:57` ACTION: printf "DONE: commit afb41ab458 applied; repro passed (is_valid=True, cleaned_data={'some_field':10} [...]
- `21:33:51` RESULT: FINAL VERIFIED: repro passed (is_valid=True, cleaned_data={'some_field':10}, instance.some_field=10); commit afb41ab458 updated django/forms/m...
- `21:33:51` ACTION: printf "FINAL VERIFIED: repro passed (is_valid=True, cleaned_data={'some_field':10}, instance. [...]
- `21:33:43` RESULT: Verified: repro passed; commit afb41ab458 updated django/forms/models.py and added repro.py; repo is clean.
- `21:33:42` ACTION: echo "Verified: repro passed; commit afb41ab458 updated django/forms/models.py and added repro. [...]
- `21:33:36` RESULT: Repro passed: is_valid=True, cleaned_data={'some_field': 10}, instance.some_field=10
- `21:33:35` ACTION: echo "Repro passed: is_valid=True, cleaned_data={'some_field': 10}, instance.some_field=10"
- `21:33:28` RESULT: is_valid: True
cleaned_data: {'some_field': 10}
instance.some_field: 10
- `21:33:27` ACTION: python3 repro.py || true
- `21:33:01` ACTION: true
- `21:32:43` All TODOs completed: implemented and committed construct_instance fix allowing cleaned_data to override model defaults; added repro.py; verified behav...
- `21:32:31` RESULT: (64 lines of output) First: afb41ab458 Allow cleaned_data to overwrite model d...
- `21:32:30` ACTION: git --no-pager show --stat --patch --pretty=format:"%h %s%nAuthor: %an%nDate: %ad%n" HEAD && git sta [...]
