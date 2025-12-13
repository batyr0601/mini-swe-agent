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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 18:37] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `18:37:30` ACTION: Submitting solution
- `18:37:20` repro.py printed 0 indicating get_inline_instances returned no instances when get_inlines() returns []
- `18:37:12` RESULT: 0
- `18:36:51` ACTION: Reading file: <<'PY'
- `18:36:31` Replaced 'for inline_class in self.inlines:' with 'for inline_class in self.get_inlines(request, obj):' in django/contrib/admin/options.py; verified g...
- `18:36:21` ACTION: sed -i 's/for inline_class in self.inlines:/for inline_class in self. [...]
- `18:35:55` ACTION: awk 'BEGIN{inserted=0}
- `18:35:32` ACTION: sed -n '560,640p' django/contrib/admin/options.py
- `18:35:24` ACTION: grep -R -n "get_inline_instances" -n || true
- `18:35:07` ACTION: sed -n '520,640p' django/contrib/admin/options.py
- `18:35:02` ACTION: grep -R -n -e 'class ModelAdmin' -e 'get_inline_instances' || true
- `18:34:56` RESULT: grep: testbed: No such file or directory
- `18:34:56` ACTION: grep -R -n -e 'class ModelAdmin' -e 'get_inline_instances' testbed || true
- `18:34:48` TASK STARTED: add ModelAdmin.get_inlines() hook to allow set inlines based on the request or model instance.
