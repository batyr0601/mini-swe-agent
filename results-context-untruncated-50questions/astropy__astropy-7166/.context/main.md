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

- [2025-12-03 00:28] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `00:28:44` ACTION: Submitting solution
- `00:28:40` Modified InheritDocstrings to include property/classmethod/staticmethod; repro_property.py shows B.value.__doc__ = 'Base doc
- `00:28:38` RESULT: A.value.__doc__: 'Base doc'
B.value.__doc__: 'Base doc'
- `00:28:37` ACTION: sed -i "s/if (inspect.isfunction(val) and/if ((inspect. [...]
- `00:28:18` Root cause: InheritDocstrings uses inspect.isfunction which is False for property/classmethod/staticmethod; their docstrings are ignored
- `00:27:52` ACTION: python3 - <<'PY'
- `00:27:34` found inspect.isfunction in astropy/utils/misc.py at line 531
- `00:27:12` RESULT: 531:            if (inspect.isfunction(val) and
- `00:27:12` ACTION: grep -n "inspect.isfunction" astropy/utils/misc.py || true
- `00:27:07` repro_property.py: A.value.__doc__ = 'Base doc'; B.value.__doc__ = None
- `00:26:45` RESULT: A.value.__doc__: 'Base doc'
B.value.__doc__: None
- `00:26:44` ACTION: Reading file: repro_property.py
- `00:26:17` ACTION: nl -ba astropy/utils/misc.py | sed -n '460,620p'
- `00:26:12` ACTION: grep -R --line-number "InheritDocstrings" . || true
- `00:26:03` RESULT: grep: testbed: No such file or directory
- `00:26:03` ACTION: grep -Rn "InheritDocstrings" -n testbed || true
- `00:25:50` TASK STARTED: InheritDocstrings metaclass doesn't work for properties
