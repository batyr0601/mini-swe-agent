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

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 12:01] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `12:01:31` ACTION: Submitting solution
- `12:01:15` repro_min.py: IMPORT_OK
- `12:01:05` RESULT: IMPORT_OK
- `12:01:05` ACTION: python3 repro_min.py
- `12:00:45` options.py diff: added get_inlines(self, request, obj=None) returning self.inlines; changed loop in get_inline_instances to 'for inline_class in self....
- `12:00:37` ACTION: git --no-pager diff -- django/contrib/admin/options.py
- `12:00:31` ACTION: git status --porcelain
- `12:00:24` options.py:570-620: get_inlines returns self.inlines; get_inline_instances builds inline_instances with 'if request:' permission checks and sets inlin...
- `12:00:13` ACTION: sed -n '570,620p' django/contrib/admin/options.py
- `12:00:07` grep get_inlines/get_inline_instances: django/contrib/admin/options.py:583,591
- `12:00:00` ACTION: grep -n -E "def get_inlines|def get_inline_instances" django/contrib/admin/options.py
- `11:59:51` repro_min.py: IMPORT_OK
- `11:59:44` RESULT: IMPORT_OK
- `11:59:43` ACTION: Reading file: <<'PY'
- `11:59:23` RESULT: PATCH_APPLIED
IMPORT_OK
- `11:58:35` ACTION: python3 - <<'PY'
- `11:58:02` ACTION: sed -n '540,620p' django/contrib/admin/options.py
- `11:57:34` ACTION: python3 - <<'PY'
- `11:56:46` ACTION: sed -n '540,620p' django/contrib/admin/options.py
