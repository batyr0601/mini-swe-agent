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

- [2025-12-03 00:34] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `00:34:52` ACTION: Submitting solution
- `00:34:48` Found get_inline_instances: django/contrib/admin/options.py:583-596; root cause: no get_inlines hook to allow choosing inline classes without copying ...
- `00:34:28` Reproduction script created and verified get_inlines override works (returned InlineB)"; context_todos --complete 1
- `00:34:25` RESULT: ['InlineB']
OK
- `00:34:24` ACTION: python3 - <<'PY'
- `00:34:06` Updated ModelAdmin.get_inline_instances to iterate over get_inlines(request, obj) and added default get_inlines method returning self.inlines
- `00:34:03` RESULT: modified django/contrib/admin/options.py
- `00:34:03` ACTION: python3 - <<'PY'
- `00:33:40` RESULT: error: unrecognized input
- `00:33:39` ACTION: git apply -p0 << 'PATCH'
- `00:33:30` ACTION: nl -ba django/contrib/admin/options.py | sed -n '520,640p'
- `00:33:22` ACTION: grep -nR -e "class ModelAdmin" -e "get_inline_instances" -e "get_inlines" . || true
- `00:33:07` RESULT: grep: testbed: No such file or directory
- `00:33:07` ACTION: grep -nR -e "get_inline_instances" -e "get_inlines" -e "class ModelAdmin" testbed || true
- `00:32:51` TASK STARTED: add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.
