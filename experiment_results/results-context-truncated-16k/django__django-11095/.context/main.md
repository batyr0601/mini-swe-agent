# Project Goals

**Current Task:** add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.

<details>
<summary>Full description</summary>

add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.
Description
	
add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.
Currently, We can override the method get_inline_instances to do such a thing, but a for loop should be copied to my code. So I wished add a hook get_inlines(request, obj=None)

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

- [2025-12-02 23:39] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `23:39:17` ACTION: Submitting solution
- `23:38:57` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1,140p'
- `23:38:36` pytest error: ImproperlyConfigured - Requested setting INSTALLED_APPS; tests require DJANGO_SETTINGS_MODULE or settings.configure() when running tests...
- `23:38:15` ACTION: pip install --disable-pip-version-check -q pytest && python -m pytest -q tests/modeladmin/tests. [...]
- `23:37:54` RESULT: /opt/miniconda3/envs/testbed/bin/python: No module named pytest
- `23:37:54` ACTION: python -m pytest -q tests/modeladmin/tests.py::ModelAdminTests::test_inline_has_add_permission_uses_ [...]
- `23:37:39` Added ModelAdmin.get_inlines at django/contrib/admin/options.py:557; get_inline_instances iterates over get_inlines at django/contrib/admin/options.py...
- `23:37:23` ACTION: grep -nE "def get_inlines|for inline_class in self.get_inlines" django/contrib/admin/options. [...]
- `23:36:50` ACTION: python -m py_compile django/contrib/admin/options.py
- `23:36:41` ACTION: python3 - <<'PY'
- `23:35:33` ACTION: nl -ba django/contrib/admin/options.py | sed -n '548,568p'
- `23:35:24` ACTION: python -m py_compile django/contrib/admin/options.py
- `23:35:16` ACTION: nl -ba tests/modeladmin/tests.py | sed -n '480,820p'
- `23:35:06` ACTION: grep -nE "def get_inlines|for inline_class in self.get_inlines" django/contrib/admin/options. [...]
- `23:34:57` ACTION: python3 - <<'PY'
- `23:34:10` ACTION: nl -ba django/contrib/admin/options.py | sed -n '540,600p'
- `23:33:38` RESULT: 585:        for inline_class in self.inlines:
- `23:33:38` ACTION: grep -nE "def get_inlines|for inline_class in self.inlines" django/contrib/admin/options.py || true
- `23:31:57` ACTION: nl -ba django/contrib/admin/options.py | sed -n '500,860p'
- `23:31:51` ACTION: ls -la && grep -R --line-number "class ModelAdmin" . [...]
