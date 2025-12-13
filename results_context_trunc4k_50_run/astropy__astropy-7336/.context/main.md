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

- [2025-12-02 20:49] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `20:49:38` ACTION: Submitting solution
- `20:49:33` patched astropy/units/decorators.py: replaced return conversion block to guard None and missing .to; repro.py output: INSTANCED_OK; root cause: wrappe...
- `20:49:06` RESULT: patched decorators.py
INSTANCED_OK
bash: line 32: context_log: command not found
- `20:49:05` ACTION: python3 - <<'PY'
- `20:48:14` ACTION: sed -n '180,260p' astropy/units/decorators.py
- `20:48:09` repro.py: AttributeError 'NoneType' object has no attribute 'to' at /testbed/astropy/units/decorators.py:224; call originated from repro.py:8; root ca...
- `20:47:54` ACTION: Reading file: <<'PY'
- `20:47:38` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
