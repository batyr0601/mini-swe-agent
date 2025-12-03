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

- [2025-12-02 20:54] **swebench-astropy__astropy-7166**: Task completed: Submitted
## Interaction Log

- `20:54:57` ACTION: Submitting solution
- `20:54:53` Verification: created classes A and B; observed B.__dict__['prop'].__doc__ and B.prop.__doc__ are 'property docstring' after the change
- `20:54:53` Fix implemented: changed condition to (inspect.isfunction(val) or isinstance(val, property)) in InheritDocstrings.__init__ in astropy/utils/misc.py
- `20:54:53` Root cause: inspect.isfunction(val) returns False for property descriptors (they are instances of property), so property docstrings were not inherited
- `20:54:25` Found InheritDocstrings.__init__ in astropy/utils/misc.py: it iterates dct and only handles members where inspect.isfunction(val) is True
- `20:54:00` ACTION: Reading file: \
- `20:53:27` ACTION: python3 - <<'PY'
- `20:53:16` InheritDocstrings __init__: only copies docstrings for inspect.isfunction members; property descriptors are ignored and thus their docstrings are not ...
- `20:53:07` ACTION: awk '/^class InheritDocstrings/{p=1} p{print} /^class [A-Za-z]/{if(p && $0!~/^class InheritDocstring [...]
- `20:52:34` ACTION: ln=$(grep -n "class InheritDocstrings" astropy/utils/misc. [...]
- `20:51:49` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,740p' astropy/utils/misc.py
- `20:51:36` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '1,800p' astropy/utils/misc.py
- `20:51:20` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,740p' astropy/utils/misc.py
- `20:51:05` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '1,800p' astropy/utils/misc.py
- `20:50:49` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,740p' astropy/utils/misc.py
- `20:50:42` repro.py: Base.foo.__doc__ and Child.foo.__doc__ both 'Base foo doc.' — initial repro shows docstring inherited for simple @property case
- `20:50:36` RESULT: Base.foo.__doc__: Base foo doc.
Child.foo.__doc__: Base foo doc.
- `20:50:36` ACTION: Reading file: <<'PY'
- `20:50:18` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,740p' astropy/utils/misc.py
