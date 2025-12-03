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

- [2025-12-02 23:30] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `23:30:27` ACTION: Submitting solution
- `23:30:22` repro_inherit_property.py: Sub.foo.__doc__ == 'FOO'; patched InheritDocstrings to set inherited docstrings on class attributes (properties/classmethod...
- `23:30:04` RESULT: Sub.foo.__doc__: FOO
- `23:30:03` ACTION: python3 repro_inherit_property.py
- `23:29:57` RESULT: Fixed indentation of super().__init__ in astropy/utils/misc.py
- `23:29:56` ACTION: python3 - <<'PY'
- `23:29:39` ACTION: nl -ba astropy/utils/misc.py | sed -n '520,620p'
- `23:29:30` ACTION: python3 repro_inherit_property.py
- `23:29:18` Patched astropy/utils/misc.py: updated InheritDocstrings to set inherited docstrings on class attributes (properties/classmethod/staticmethod) by oper...
- `23:29:10` ACTION: python3 - <<'PY'
- `23:27:53` ACTION: nl -ba astropy/utils/misc.py | sed -n '520,580p'
- `23:27:50` RESULT: Sub.foo.__doc__: None
- `23:27:49` ACTION: Reading file: <<'PY'
- `23:27:39` Patched astropy/utils/misc.py: updated InheritDocstrings to inherit docstrings for properties, classmethod, and staticmethod instead of only inspect.i...
- `23:27:32` RESULT: Patched astropy/utils/misc.py
- `23:27:13` ACTION: python3 - <<'PY'
- `23:26:19` ACTION: nl -ba astropy/utils/tests/test_misc.py | sed -n '1,240p'
- `23:26:08` ACTION: nl -ba astropy/utils/misc.py | sed -n '480,620p'
- `23:25:59` ACTION: grep -RIn "InheritDocstrings" .
- `23:25:55` ACTION: ls -laR
