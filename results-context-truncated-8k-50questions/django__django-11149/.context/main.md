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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:17] **swebench-django__django-11149**: Task completed: Submitted
## Interaction Log

- `03:17:00` ACTION: Submitting solution
- `03:16:55` tests/repro_inline_view_perm.py: Yielded inline forms (has_view_permission=False): [('INLINE', 'extra_form', None), ('INLINE', 'empty_form', None)]
- `03:16:32` ACTION: Reading file: <<'PY'
- `03:16:03` InlineAdminFormSet.__iter__: inserted if self.has_view_permission guard and reindented the initial_forms block so existing inline forms are only yield...
- `03:15:45` ACTION: sed -n '220,300p' django/contrib/admin/helpers.py
- `03:15:27` ACTION: python3 - <<'PY'
- `03:14:55` Inserted has_view_permission guard but indentation broken: 'view_on_site_url' and following 'yield' lines are not indented under the guard; will reind...
- `03:14:38` ACTION: awk '
- `03:14:11` ACTION: sed -n '220,300p' django/contrib/admin/helpers.py
- `03:14:05` RESULT: bash: -c: line 2: syntax error: unexpected end of file
- `03:14:00` ACTION: grep -n "for form, original in zip(self.formset.initial_forms, self.formset. [...]
- `03:13:20` ACTION: grep -n "class InlineAdminFormSet" django/contrib/admin/helpers. [...]
- `03:13:11` ACTION: nl -ba django/contrib/admin/helpers.py | sed -n '1,380p'
- `03:13:02` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1400,1500p'
- `03:12:58` grep has_view_permission: django/contrib/admin/templatetags/admin_modify.py:60,63; django/contrib/admin/helpers.py:230,245; django/contrib/admin/templ...
- `03:12:45` ACTION: grep -nR "has_view_permission" django | sed -n '1,200p'
- `03:12:21` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1920,2060p'
- `03:12:17` ACTION: nl -ba django/contrib/admin/helpers.py | sed -n '1,360p'
- `03:12:03` ACTION: grep -n "class .*Inline" -R django | sed -n '1,200p'
- `03:11:52` ACTION: ls -la
