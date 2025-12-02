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
- [ ] 1. Understand the bug: locate where get_inline_instances is implemented and how inlines are determined (search for get_inline_instances and inlines usage)
- [ ] 2. Locate code: find ModelAdmin class implementation in testbed package (likely admin.py or similar) and identify related methods
- [ ] 3. Design API: add ModelAdmin.get_inlines(self, request, obj=None) that returns list/tuple of inline classes (defaulting to self.inlines)
- [ ] 4. Implement change: modify get_inline_instances to call get_inlines and then instantiate inline instances (preserve existing behavior and backward compatibility)
- [ ] 5. Verify fix: run tests or create a small script to ensure get_inlines hook works and no regressions

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:02] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `21:02:00` ACTION: Submitting solution
- `21:01:49` Verified get_inlines returns admin.inlines and get_inline_instances instantiates classes; simple test passed
- `21:01:46` ACTION: python3 - <<'PY'
- `21:01:36` RESULT: fixed
- `21:01:36` ACTION: python3 - <<'PY'
- `21:01:19` ACTION: nl -ba django/contrib/admin/options.py | sed -n '540,610p'
- `21:01:15` ACTION: python3 - <<'PY'
- `21:01:02` Added get_inlines to django/contrib/admin/options.py before get_inline_instances; get_inline_instances now iterates over get_inlines(request, obj) ins...
- `21:00:56` RESULT: patched
- `21:00:56` ACTION: python3 - <<'PY'
- `21:00:42` get_inline_instances found: django/contrib/admin/options.py:583-596; inlines attribute at line 555
- `21:00:24` ACTION: nl -ba django/contrib/admin/options.py | sed -n '520,620p'
- `21:00:18` ACTION: grep -nR "get_inline_instances\|class ModelAdmin\|\\binlines\\b" django || true
- `21:00:13` ACTION: ls -la
- `21:00:11` RESULT: grep: testbed: No such file or directory
- `21:00:11` ACTION: grep -nR "get_inline_instances\|class ModelAdmin\|\\binlines\\b" testbed || true
- `20:59:55` TASK STARTED: add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.
