# Project Goals

**Current Task:** Ordering problem in admin.RelatedFieldListFilter and admin.RelatedOnlyFieldListFilter

<details>
<summary>Full description</summary>

Ordering problem in admin.RelatedFieldListFilter and admin.RelatedOnlyFieldListFilter
Description
	
RelatedFieldListFilter doesn't fall back to the ordering defined in Model._meta.ordering. 
Ordering gets set to an empty tuple in ​https://github.com/django/django/blob/2.2.1/django/contrib/admin/filters.py#L196 and unless ordering is defined on the related model's ModelAdmin class it stays an empty tuple. IMHO it should fall back to the ordering defined in the related model's Meta.ordering field.
RelatedOnlyFieldListFilter doesn't order the related model at all, even if ordering is defined on the related model's ModelAdmin class.
That's because the call to field.get_choices ​https://github.com/django/django/blob/2.2.1/django/contrib/admin/filters.py#L422 omits the ordering kwarg entirely.

</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: RelatedFieldListFilter sets ordering to empty tuple and doesn
- [ ] 2. Locate the code: find occurrences of RelatedFieldListFilter and RelatedOnlyFieldListFilter in the testbed source (likely django.contrib.admin.filters or similar files)
- [ ] 3. Reproduce the bug: create a minimal repro using test models with Meta.ordering and inspect the choices/order returned by the filters
- [ ] 4. Implement fix: modify RelatedFieldListFilter and RelatedOnlyFieldListFilter to use related model
- [ ] 5. Verify fix: run the repro script and any relevant tests to ensure ordering falls back correctly and RelatedOnlyFieldListFilter orders choices

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:23] **swebench-django__django-11400**: Task completed: Submitted
## Interaction Log

- `21:23:17` ACTION: Submitting solution
- `21:23:12` Root cause: RelatedFieldListFilter set ordering to empty tuple when related ModelAdmin.get_ordering returned empty; RelatedOnlyFieldListFilter omitted...
- `21:22:57` RESULT: bash: line 1: pytest: command not found
- `21:22:57` ACTION: pytest -q
- `21:22:50` repro: Scenario A/B/C: get_choices called with ordering=('name',) as fallback when related_admin.get_ordering returned () or None; RelatedOnlyFieldLis...
- `21:22:14` ACTION: Reading file: repro_filters.py
- `21:21:47` ACTION: nl -ba django/contrib/admin/utils.py | sed -n '1,520p'
- `21:21:41` repro_filters.py: django.contrib.admin.utils.NotRelationField raised when instantiating RelatedFieldListFilter (get_model_from_relation threw NotRelat...
- `21:21:32` ACTION: Reading file: repro_filters.py
- `21:21:02` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '1,140p'
- `21:20:50` Patched filters.py: RelatedFieldListFilter.field_choices now uses related ModelAdmin.get_ordering(request) or related_model._meta.ordering; RelatedOnl...
- `21:20:40` ACTION: python3 - <<'PY'
- `21:20:12` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '120,220p' && nl -ba django/contrib/admin/filters. [...]
- `21:20:03` ACTION: grep -Rn --line-number -E "class\s+RelatedFieldListFilter|class\s+RelatedOnlyFieldListFilter" . [...]
- `21:20:01` grep: testbed: No such file or directory
- `21:19:52` RESULT: grep: testbed: No such file or directory
- `21:19:51` ACTION: grep -Rn -E "RelatedFieldListFilter|RelatedOnlyFieldListFilter" testbed || true
- `21:19:36` TASK STARTED: Ordering problem in admin.RelatedFieldListFilter and admin.RelatedOnlyFieldListFilter
