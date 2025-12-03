# Project Goals

**Current Task:** InheritDocstrings metaclass doesn't work for properties

<details>
<summary>Full description</summary>

InheritDocstrings metaclass doesn't work for properties
Inside the InheritDocstrings metaclass it uses `inspect.isfunction` which returns `False` for properties.

</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `18:35:11` ACTION: sed -n '440,640p' astropy/utils/misc.py
- `18:34:55` ACTION: sed -n '460,640p' astropy/utils/misc.py
- `18:34:08` ACTION: python3 - <<'PY'
- `18:32:53` ACTION: sed -n '480,560p' astropy/utils/misc.py
- `18:32:32` ACTION: python3 - <<'PY'
- `18:31:36` ACTION: sed -n '492,540p' astropy/utils/misc.py
- `18:31:13` repro: A.prop.__doc__='Base property doc', B.prop.__doc__=None
- `18:31:07` RESULT: A.prop.__doc__: 'Base property doc'
B.prop.__doc__: None
- `18:31:06` ACTION: python3 - <<'PY'
- `18:30:48` ACTION: sed -n '480,560p' astropy/utils/misc.py
- `18:30:44` Found InheritDocstrings implementation at astropy/utils/misc.py:497; referenced in astropy/utils/tests/test_misc.py:78, astropy/visualization/interval...
- `18:30:35` ACTION: grep -R -n "InheritDocstrings" . || true
- `18:30:26` TASK STARTED: InheritDocstrings metaclass doesn't work for properties
