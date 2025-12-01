# Project Goals

**Current Task:** units.quantity_input decorator fails for constructors with type hinted return value -> None

<details>
<summary>Full description</summary>

units.quantity_input decorator fails for constructors with type hinted return value -> None
### Summary
I am using the `units.quantity_input` decorator with typing hints for constructors, however when I add the correct return value for the constructor (`None`) then I get an exception, because `None` has no attribute `to`.

### Reproducer
The issue can be reproduced with the following file:
``` Python
import astropy.units as u


class PoC(object):

    @u.quantity_input
    def __init__(self, voltage: u.V) -> None:
        pass


if __name__ == '__main__':
    poc = PoC(1.*u.V)
```
which results in the following error:
```
$ python3 poc.py
Traceback (most recent call last):
  File "poc.py", line 12, in <module>
    poc = PoC(1.*u.V)
  File "/usr/lib64/python3.6/site...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce: create minimal script using units.quantity_input on __init__ with return type None and run it to reproduce the error
- [ ] 2. Locate: find the quantity_input decorator implementation in the repository (search for
- [ ] 3. Analyze: inspect the code path where the decorator handles return_annotation and identify where return_.to(...) is called and why None triggers AttributeError
- [ ] 4. Implement fix: modify the decorator to explicitly check for None (either return annotation is None or the returned value is None) and skip unit conversion/check in that case
- [ ] 5. Verify: run the reproduction script and relevant tests to ensure the fix prevents the AttributeError and preserves existing behavior

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:42] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `20:42:07` ACTION: Submitting solution
- `20:42:02` TESTED: ran poc.py; created PoC instance successfully
- `20:42:02` Found return_.to() in astropy/units/decorators.py; patched to guard .to() call when return_annotation or return_ is None
- `20:42:02` Reproducer: poc.py ran successfully after patch; no AttributeError on __init__ annotated with -> None
- `20:41:51` RESULT: Created PoC: <__main__.PoC object at 0x7fffff333a58>
- `20:41:50` ACTION: printf 'import astropy.units as u\n\nclass PoC(object):\n\n @u. [...]
- `20:41:38` RESULT: bash: -c: line 14: syntax error near unexpected token `&&'
bash: -c: line 14: `&& python3 poc.py'
- `20:41:38` ACTION: Reading file: <<'PY'
- `20:41:22` Decision: only attempt unit conversion if return_annotation is not inspect.Signature.empty, return_annotation is not None, and returned value is not N...
- `20:41:22` Found return_.to() call in astropy/units/decorators.py leading to AttributeError when wrapped function returns None
- `20:40:46` RESULT: (231 lines of output) First: 1	# -*- coding: utf-8 -*-...
- `20:40:45` ACTION: nl -ba astropy/units/decorators.py | sed -n '1,320p'
- `20:40:43` RESULT: (60 lines of output) First: ./CHANGES.rst:1523:- The ``astropy.units.quantity_...
- `20:40:43` ACTION: grep -Rn "quantity_input" . || true
- `20:40:28` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
