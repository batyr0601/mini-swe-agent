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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:27] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `23:27:57` ACTION: Submitting solution
- `23:27:54` poc.py constructed successfully (constructed: True). Reproducer shows patch prevents AttributeError. Root cause: in astropy/units/decorators.py (aroun...
- `23:27:39` RESULT: constructed: True
- `23:27:38` ACTION: Reading file: <<'PY'
- `23:27:28` Patched astropy/units/decorators.py: avoid calling .to on None when return_annotation is None; updated conditional to check annotation is not inspect....
- `23:27:22` RESULT: patched decorators.py
- `23:27:21` ACTION: python3 - <<'PY'
- `23:27:02` ACTION: nl -ba astropy/units/decorators.py | sed -n '1,320p'
- `23:26:59` ACTION: ls -la && grep -nR "quantity_input" -n .
- `23:26:53` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
