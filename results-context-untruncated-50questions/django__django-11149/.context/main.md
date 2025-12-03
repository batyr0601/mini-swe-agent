# Project Goals

**Current Task:** Admin inlines for auto-created ManyToManyFields are editable if the user only has the view permission

<details>
<summary>Full description</summary>

Admin inlines for auto-created ManyToManyFields are editable if the user only has the view permission
Description
	
From https://code.djangoproject.com/ticket/8060#comment:34
Replying to Will Gordon:
This seems to have regressed in (at least) 2.1. I have 2 view only permissions. I have a ManyToManyField represented in my main model as a TabularInline. But, my user with view only permissions can now add or remove these items at will!
I am having the same issue, so I assume this is a bug. I did not find Will had created a separate ticket.
models.py:
class Photo(models.Model):
	pass
class Report(models.Model):
	photos = models.ManyToManyField(Photo)
admin.py:
		class ReportPhotoInlineModelAdmin(admin.TabularInline):
			model = Report.photos.through
			show_change_link = True

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

- [2025-12-03 00:40] **swebench-django__django-11149**: Task completed: Submitted
## Interaction Log

- `00:40:16` ACTION: Submitting solution
- `00:40:10` Verified fix: repro_inline_permission.py: VIEW-only user: add/change/delete=False; CHANGE user: add/change/delete=True
- `00:39:59` Found root cause in InlineModelAdmin (django/contrib/admin/options.py:2114-2154): has_add/has_change/has_delete returned has_view_permission for auto_...
- `00:39:46` repro_inline_permission.py: With VIEW-only user: has_add_permission=False, has_change_permission=False, has_delete_permission=False; With CHANGE-permi...
- `00:38:25` ACTION: Reading file: tests/repro_inline_permission.py
- `00:37:54` ACTION: grep -nR "auto_created" tests || true
- `00:37:47` Patched InlineModelAdmin in django/contrib/admin/options.py: changed has_add_permission/has_change_permission/has_delete_permission for auto_created M...
- `00:37:29` RESULT: patched
- `00:37:29` ACTION: python3 - <<'PY'
- `00:36:41` ACTION: nl -ba django/contrib/admin/options.py | sed -n '2108,2160p'
- `00:36:34` ACTION: nl -ba django/contrib/admin/options.py | sed -n '430,520p'
- `00:35:35` ACTION: grep -n "def has_view_permission\|def has_change_permission\|def has_add_permission\|def has_delete_ [...]
- `00:35:30` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1956,2108p'
- `00:35:15` ACTION: grep -nR "class .*InlineModelAdmin" django/contrib/admin -n || true
- `00:35:01` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1068,1140p'
- `00:34:56` ACTION: grep -nR "has_editable_inline_admin_formsets" -n django || true
- `00:34:42` ACTION: nl -ba django/contrib/admin/templatetags/admin_modify.py | sed -n '1,240p'
- `00:34:39` ACTION: nl -ba django/contrib/admin/helpers.py | sed -n '1,340p'
- `00:34:36` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1400,1540p'
- `00:34:24` ACTION: grep -nR "has_add_permission\|has_change_permission\|has_delete_permission\|get_readonly_fields" dja [...]
