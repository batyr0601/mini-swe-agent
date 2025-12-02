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
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:13] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `14:13:05` ACTION: Submitting solution
- `14:12:56` astropy/utils/misc.py: Implemented fix - InheritDocstrings now checks (inspect.isfunction(val) or isinstance(val, property)) so property descriptors i...
- `14:12:49` Root cause: InheritDocstrings previously checked only inspect.isfunction(val) so @property descriptors were skipped; now it checks (inspect.isfunction...
- `14:12:42` ACTION: sed -n '520,540p' astropy/utils/misc.py
- `14:12:34` astropy/utils/misc.py: InheritDocstrings condition changed to 'inspect.isfunction(val) or isinstance(val, property)'; repro_prop.py: B.foo.__doc__ = '...
- `14:12:24` ACTION: perl -0777 -pe "s/inspect\.isfunction\(val\) and/(inspect. [...]
- `14:12:03` repro_prop.py: A.foo.__doc__ = 'Doc of foo in A', B.foo.__doc__ = None
- `14:11:56` RESULT: A.foo.__doc__: 'Doc of foo in A'
B.foo.__doc__: None
- `14:11:55` ACTION: Reading file: <<'PY'
- `14:11:40` ACTION: sed -n '480,560p' astropy/utils/misc.py
- `14:11:32` ACTION: grep -Rn "InheritDocstrings" . || true
- `14:11:21` ACTION: ls -la
- `14:11:18` TASK STARTED: InheritDocstrings metaclass doesn't work for properties
