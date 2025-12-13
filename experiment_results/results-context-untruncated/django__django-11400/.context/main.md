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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 00:45] **swebench-django__django-11400**: Task completed: Submitted
## Interaction Log

- `00:45:06` ACTION: Submitting solution
- `00:44:52` Root cause: RelatedOnlyFieldListFilter omitted ordering kwarg and RelatedFieldListFilter used empty tuple when related ModelAdmin.get_ordering() retur...
- `00:44:52` Repro script result: OK: both filters passed expected ordering; RelatedFieldListFilter used ModelAdmin ordering ('admin_order'); RelatedOnlyFieldListF...
- `00:44:35` RESULT: OK: both filters passed expected ordering
- `00:43:11` ACTION: python3 - <<'PY'
- `00:42:50` ACTION: nl -ba django/db/models/fields/__init__.py | sed -n '760,860p' && nl -ba django/db/models/fields/rev [...]
- `00:42:46` ACTION: grep -nR "def get_choices" django | sed -n '1,200p'
- `00:42:38` ACTION: nl -ba django/contrib/admin/utils.py | sed -n '1,240p'
- `00:42:27` ACTION: nl -ba tests/admin_filters/tests.py | sed -n '240,340p'
- `00:41:44` ACTION: python3 - <<'PY'
- `00:41:15` ACTION: Reading file: <<'PY'
- `00:41:05` ACTION: python3 -m unittest tests.admin_filters.tests.ListFiltersTests. [...]
- `00:41:00` RESULT: bash: line 1: pytest: command not found
- `00:40:59` ACTION: pytest -q tests/admin_filters/tests.py::ListFiltersTests::test_relatedfieldlistfilter_foreignkey_ord [...]
- `00:40:34` ACTION: grep -nE '^class .+' tests/admin_filters/tests.py
- `00:40:17` ACTION: nl -ba tests/admin_filters/tests.py | sed -n '1,120p'
- `00:40:11` ACTION: nl -ba tests/admin_filters/tests.py | sed -n '540,600p'
- `00:40:01` Patched django/contrib/admin/filters.py: RelatedFieldListFilter.field_choices now prefers related ModelAdmin.get_ordering(request) and falls back to r...
- `00:39:52` RESULT: Patched django/contrib/admin/filters.py
- `00:39:51` ACTION: python3 - <<'PY'
