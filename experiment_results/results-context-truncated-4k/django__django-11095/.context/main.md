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
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 21:06] **swebench-django__django-11095**: Task completed: Submitted
## Interaction Log

- `21:06:45` ACTION: Submitting solution
- `21:06:39` test_repro: INLINE_COUNT: 1, INLINE_TYPE: Inline - reproduction passes
- `21:06:22` RESULT: INLINE_COUNT: 1
INLINE_TYPE: Inline
- `21:06:09` repro inline run: AttributeError: type object 'object' has no attribute '_meta' (options.py:576) when calling DummyAdmin(object, None) in test_repro
- `21:06:01` ACTION: python3 - <<'PY'
- `21:05:31` ACTION: Reading file: <<'PY'
- `21:05:07` django/contrib/admin/options.py: added get_inlines(request, obj=None) and updated get_inline_instances to call get_inlines(request, obj) with a TypeEr...
- `21:04:56` ACTION: git add -A && git --no-pager diff --staged -- django/contrib/admin/options.py | sed -n '1,200p'
- `21:04:44` ACTION: python3 - <<'PY'
- `21:04:26` ACTION: git apply <<'PATCH'
- `21:04:01` ACTION: git --no-pager log -n 10 --pretty=oneline -- django/contrib/admin/options. [...]
- `21:03:35` ACTION: nl -ba -w3 -s': ' django/contrib/admin/options.py | sed -n '560,640p'
- `21:03:24` Found misindented get_inlines at django/contrib/admin/options.py:583; moved it out of __str__ to class level and py_compile passed
- `21:03:12` ACTION: perl -0777 -i.bak -pe 's/^[ \t]{8}(def get_inlines\([^\n]*\))/ $1/m' django/contrib/admin/options. [...]
- `21:02:49` ACTION: nl -ba -w3 -s': ' django/contrib/admin/options.py | sed -n '576,600p'
- `21:02:14` django/contrib/admin/options.py: get_inlines inserted inside __str__ causing IndentationError; def get_inlines indented too deep (inside __str__), def...
- `21:01:25` ACTION: sed -n '560,600p' django/contrib/admin/options.py
- `21:01:13` ACTION: cp django/contrib/admin/options.py django/contrib/admin/options.py.bak && python3 - <<'PY'
- `21:00:45` repro_get_inlines.py: has_get_inlines: False
