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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:49] **swebench-django__django-11095**: Task completed: Submitted
- [2025-12-01 20:48] **swebench-django__django-11095**: Add ModelAdmin.get_inlines hook and update get_inline_instances; verified with runtime check
## Interaction Log

- `20:49:01` ACTION: Submitting solution
- `20:48:57` TESTED: runtime check script validated new hook
- `20:48:57` Reproduced the behavior using MAHook and dummy inline: get_inlines can suppress or return inlines
- `20:48:34` RESULT: inline_instances_count: 1
hook_returns_empty: []
hook_returns_nonempty_count: 1
SUCCESS: get_inlines hook present and get_inline_instances use...
- `20:48:33` ACTION: python3 - <<'PY'
- `20:47:53` RESULT: (11 lines of output) First: ./django/contrib/admin/options.py:582:    def get_...
- `20:47:52` ACTION: grep -RIn --exclude-dir=.git -e "get_inlines" -e "get_inline_instances(" .
- `20:47:44` RESULT: (47 lines of output) First: 582:    def get_inlines(self, request, obj=None):...
- `20:47:44` ACTION: grep -n "def get_inlines" django/contrib/admin/options.py && nl -ba django/contrib/admin/options. [...]
- `20:47:31` RESULT: bash: line 1: pytest: command not found
- `20:47:31` ACTION: pytest -q tests/modeladmin/tests.py::ModelAdminTests
- `20:47:24` Implemented get_inlines and updated get_inline_instances
- `20:47:23` Decision: add get_inlines hook returning self.inlines and update get_inline_instances to use it
- `20:47:23` Found ModelAdmin.get_inline_instances in django/contrib/admin/options.py
- `20:46:58` RESULT: (81 lines of output) First: 540	...
- `20:46:57` ACTION: nl -ba django/contrib/admin/options.py | sed -n '540,620p'
- `20:46:52` RESULT: (240 lines of output) First: 1	import copy...
