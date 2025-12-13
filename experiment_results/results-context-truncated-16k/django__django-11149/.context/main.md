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

- [ ] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:41] **swebench-django__django-11149**: Task completed: Submitted
## Interaction Log

- `23:41:49` ACTION: Submitting solution
- `23:41:42` ACTION: python3 repro_inline.py
- `23:41:32` ACTION: python3 - <<'PY'
- `23:41:09` ACTION: nl -ba django/contrib/admin/options.py | sed -n '2108,2160p'
- `23:39:37` ACTION: python3 - <<'PY'
- `23:38:54` ACTION: nl -ba django/contrib/admin/options.py | sed -n '2108,2156p'
- `23:38:11` ACTION: Reading file: <<'PY'
- `23:37:46` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1968,2008p'
- `23:37:32` ACTION: Reading file: <<'PY'
- `23:36:44` Patched InlineModelAdmin.has_add/change/delete to require CHANGE permission on the related target model for auto_created through models
- `23:35:40` ACTION: nl -ba django/contrib/admin/options.py | sed -n '2106,2160p'
- `23:35:37` ACTION: grep -nE "def (has_add_permission|has_change_permission|has_delete_permission|has_view_permission|ha [...]
- `23:35:27` ACTION: grep -n "class InlineModelAdmin" django/contrib/admin/options. [...]
- `23:35:03` ACTION: nl -ba django/contrib/admin/options.py | sed -n '560,640p'
- `23:34:48` ACTION: grep -n "def get_inline_instances" django/contrib/admin/options. [...]
- `23:34:24` ACTION: nl -ba django/contrib/admin/options.py | sed -n '220,280p'
- `23:34:17` ACTION: nl -ba django/contrib/admin/helpers.py | sed -n '1,320p'
- `23:34:13` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1400,1500p'
- `23:34:03` ACTION: grep -nR "has_view_permission" django/contrib/admin | sed -n '1,200p'
- `23:33:59` ACTION: grep -nR "ManyToMany" tests | sed -n '1,200p'
