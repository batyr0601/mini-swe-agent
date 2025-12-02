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

- [2025-12-02 14:40] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `14:40:29` ACTION: Submitting solution
- `14:40:11` RESULT: OK: 1.0 m
- `14:40:10` ACTION: python3 repro.py
- `14:39:58` Patched astropy/units/decorators.py (pattern replaced). repro.py was not executed due to previous command syntax error: bash: -c: line 22: syntax erro...
- `14:39:43` ACTION: python3 - <<'PY'
- `14:39:09` ACTION: grep -n "return_.to" -R astropy || true && sed -n '200,260p' astropy/units/decorators.py
- `14:38:57` ACTION: Reading file: <<'PY'
- `14:38:38` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
