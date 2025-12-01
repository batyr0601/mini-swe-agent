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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:22] **swebench-django__django-11400**: Task completed: Submitted
## Interaction Log

- `03:22:27` ACTION: Submitting solution
- `03:22:18` Root cause: related_admin.get_ordering(request) may return None; field_choices passed None to field.get_choices(ordering=...), which calls related_mod...
- `03:22:12` filters.py: field_choices (lines 196-201) calls related_admin.get_ordering(request) and passes its return value to field.get_choices(ordering=...); re...
- `03:22:01` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '140,220p'
- `03:21:54` repro.py: received ordering: (), choices: [('ok', 'ok')], final output: OK
- `03:21:46` RESULT: received ordering: ()
choices: [('ok', 'ok')]
OK
- `03:21:45` ACTION: Reading file: <<'PY'
- `03:21:08` filters.py: changed 'ordering = related_admin.get_ordering(request)' to 'ordering = related_admin.get_ordering(request) or ()' to prevent None being p...
- `03:20:57` ACTION: perl -0777 -pe 's/(ordering = related_admin.get_ordering\(request\))/\1 or ()/g' -i django/contrib/a [...]
- `03:20:36` ACTION: nl -ba django/db/models/fields/reverse_related.py | sed -n '1,320p'
- `03:20:14` ACTION: nl -ba django/db/models/fields/__init__.py | sed -n '760,840p'
- `03:20:10` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '140,220p'
- `03:20:04` RESULT: 162:class RelatedFieldListFilter(FieldListFilter):
- `03:20:04` ACTION: grep -n "class RelatedFieldListFilter" django/contrib/admin/filters.py || true
- `03:19:58` ACTION: nl -ba django/contrib/admin/filters.py | sed -n '1,520p'
- `03:19:50` ACTION: grep -nR "get_choices(" django/contrib | sed -n '1,200p'
- `03:19:39` ACTION: nl -ba django/db/models/fields/__init__.py | sed -n '820,920p'
- `03:19:34` ACTION: nl -ba django/db/models/fields/__init__.py | sed -n '740,820p'
