# Project Goals

**Current Task:** InheritDocstrings metaclass doesn't work for properties

<details>
<summary>Full description</summary>

InheritDocstrings metaclass doesn't work for properties
Inside the InheritDocstrings metaclass it uses `inspect.isfunction` which returns `False` for properties.

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

- [2025-12-01 20:46] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `20:46:00` ACTION: Submitting solution
- `20:45:53` Fix applied: InheritDocstrings updated to handle property, classmethod, staticmethod, and descriptor fget; repro demonstrates docstrings inherited for...
- `20:45:27` repro_inherit_doc.py: B.meth.__doc__ 'method doc from A'; B.val.__doc__ 'property doc from A'; B.c.__func__.__doc__ 'classmethod doc from A'; B.s.__fu...
- `20:45:17` ACTION: python3 repro_inherit_doc.py
- `20:45:11` RESULT: Replaced property assignment with setattr in astropy/utils/misc.py
- `20:44:50` ACTION: python3 - <<'PY'
- `20:44:37` ACTION: nl -ba astropy/utils/misc.py | sed -n '560,640p'
- `20:44:33` ACTION: nl -ba astropy/utils/misc.py | sed -n '520,560p'
- `20:44:26` ACTION: Reading file: <<'PY'
- `20:44:11` Patched astropy/utils/misc.py: replaced loop to handle functions, classmethod/staticmethod, property, and descriptor fget
- `20:44:01` RESULT: Patched astropy/utils/misc.py
- `20:43:18` ACTION: python3 - <<'PY'
- `20:42:13` ACTION: nl -ba astropy/utils/misc.py | sed -n '480,560p'
- `20:42:08` ACTION: grep -nR "InheritDocstrings" . || true
- `20:42:03` RESULT: grep: testbed: No such file or directory
- `20:42:03` ACTION: grep -nR "InheritDocstrings" testbed || true
- `20:41:47` TASK STARTED: InheritDocstrings metaclass doesn't work for properties
