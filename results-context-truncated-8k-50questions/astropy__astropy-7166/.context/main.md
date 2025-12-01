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

- [2025-12-03 03:06] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `03:05:52` ACTION: Submitting solution
- `03:02:11` ACTION: python3 - <<'PY'
- `03:01:51` ACTION: nl -ba astropy/utils/misc.py | sed -n '520,600p'
- `03:01:34` ACTION: Reading file: <<'PY'
- `03:01:21` patched: updated astropy/utils/misc.py InheritDocstrings to set __doc__ on underlying functions for property/classmethod/staticmethod; script output: ...
- `03:01:10` RESULT: patched
- `03:00:48` ACTION: python3 - <<'PY'
- `03:00:06` ACTION: nl -ba astropy/utils/misc.py | sed -n '480,620p'
- `02:59:37` ACTION: grep -nR "InheritDocstrings" -n .
- `02:59:30` ACTION: ls -la
- `02:59:26` TASK STARTED: InheritDocstrings metaclass doesn't work for properties
