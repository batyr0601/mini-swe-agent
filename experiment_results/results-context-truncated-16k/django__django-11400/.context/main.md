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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:42] **swebench-django__django-11400**: Task completed: Submitted
## Interaction Log

- `23:42:15` ACTION: Submitting solution
- `23:42:03` RESULT: FOUND_OK
- `23:42:01` ACTION: Reading file: <<'PY'
- `23:40:47` RESULT: FOUND_OK
- `23:40:46` ACTION: Reading file: <<'PY'
- `23:40:15` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '120,220p'
- `23:39:56` django/contrib/admin/filters.py: RelatedFieldListFilter.field_choices at lines 196-203 uses ordering=None, gets related_admin.get_ordering(request), a...
- `23:39:45` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '188,206p' && nl -ba django/contrib/admin/filters. [...]
- `23:39:40` RESULT: MISSING
- `23:39:40` ACTION: python3 repro_check.py
- `23:39:37` ACTION: Reading file: <<'PY'
- `23:39:10` Updated filters.py: RelatedFieldListFilter.field_choices now uses related_admin.get_ordering(request) and only passes ordering to field.get_choices if...
- `23:38:59` RESULT: UPDATED
- `23:38:58` ACTION: python3 - <<'PY'
- `23:38:29` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '392,460p'
- `23:38:24` RESULT: 419:class RelatedOnlyFieldListFilter(RelatedFieldListFilter):
- `23:38:24` ACTION: grep -n "RelatedOnlyFieldListFilter" -n django/contrib/admin/filters.py
- `23:38:17` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '1,500p' | sed -n '1,260p' | sed -n '1,260p'
- `23:38:07` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1,240p'
- `23:38:04` ACTION: grep -n "def get_ordering" -R django | sed -n '1,200p'
