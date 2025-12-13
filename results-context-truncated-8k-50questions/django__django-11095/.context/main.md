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
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:14] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `03:13:31` ACTION: Submitting solution
- `03:13:26` REPRO_OK: get_inlines present and used in get_inline_instances
- `03:13:11` RESULT: REPRO_OK: get_inlines present and used in get_inline_instances
- `03:13:09` ACTION: Reading file: <<'PY'
- `03:12:38` Updated get_inline_instances to iterate over get_inlines(request, obj); for inline_class found at line 593
- `03:12:28` RESULT: 593:        for inline_class in self.get_inlines(request, obj):
- `03:12:26` ACTION: grep -n "for inline_class in self.get_inlines" django/contrib/admin/options.py || true
- `03:12:01` ACTION: python3 - <<'PY'
- `03:11:47` Inserted get_inlines into django/contrib/admin/options.py; def get_inlines found at line 556
- `03:11:37` RESULT: INSERTED_GET_INLINES
556:    def get_inlines(self, request, obj=None):
- `03:11:34` ACTION: python3 - <<'PY'
- `03:11:14` ACTION: sed -n '540,600p' django/contrib/admin/options.py
- `03:10:58` ACTION: grep -n "def get_inlines" django/contrib/admin/options.py || true
- `03:10:39` RESULT: error: unrecognized input
- `03:10:37` ACTION: git apply -p0 <<'PATCH'
- `03:10:05` ACTION: nl -ba django/contrib/admin/options.py | sed -n '520,820p'
- `03:09:57` ACTION: nl -ba django/contrib/admin/options.py | sed -n '1,260p'
- `03:09:50` ACTION: grep -nR "get_inline_instances\|def get_inlines\|class ModelAdmin" django | sed -n '1,200p'
- `03:09:47` ACTION: ls -la
