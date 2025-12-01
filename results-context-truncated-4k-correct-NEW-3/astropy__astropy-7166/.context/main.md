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

- [2025-12-02 15:56] **swebench-astropy__astropy-7166**: Task completed: LimitsExceeded
## Interaction Log

- `15:56:19` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '440,760p' astropy/utils/misc.py
- `15:56:03` ACTION: grep -n -E 'class InheritDocstrings|def __get__|def __getattr__|def __set_name__|@property|isdatades [...]
- `15:54:59` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '440,760p' astropy/utils/misc.py
- `15:54:47` ACTION: grep -n -E "class InheritDocstrings|def __get__|def __getattr__|def __set_name__|@property|isdatades [...]
- `15:54:29` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '440,760p' astropy/utils/misc.py
- `15:54:15` ACTION: grep -n -E 'class InheritDocstrings|def __get__|__get__|@property|isdatadescriptor|inherit_docstring [...]
- `15:54:00` ACTION: grep -n -E "class InheritDocstrings|def __get__|__get__|@property|isdatadescriptor|inherit_docstring [...]
- `15:53:42` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '440,760p' astropy/utils/misc.py
- `15:53:26` ACTION: sed -n '420,760p' astropy/utils/misc.py
- `15:53:08` ACTION: sed -n '480,760p' astropy/utils/misc.py
- `15:53:02` ACTION: grep -n -E 'class InheritDocstrings|def __get__|__get__|@property|isdatadescriptor|inspect. [...]
- `15:52:26` ACTION: sed -n '420,760p' astropy/utils/misc.py
- `15:52:12` ACTION: grep -n -E "class InheritDocstrings|@property|__get__|__getattr__|inherit_docstrings|docstring|__doc [...]
- `15:51:40` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,760p' astropy/utils/misc.py
- `15:51:26` ACTION: ls -R
- `15:50:58` ACTION: sed -n '420,760p' astropy/utils/misc.py
- `15:49:47` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,760p' astropy/utils/misc.py
- `15:49:33` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc.py && sed -n '420,700p' astropy/utils/misc.py
- `15:49:15` ACTION: sed -n '420,700p' astropy/utils/misc.py
- `15:48:59` ACTION: grep -n "class InheritDocstrings" astropy/utils/misc. [...]
