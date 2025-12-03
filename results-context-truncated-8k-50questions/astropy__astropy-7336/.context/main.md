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

- [2025-12-03 03:02] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `03:02:03` ACTION: Submitting solution
- `03:01:59` Fix: only attempt unit conversion when return_ is not None and has a 'to' attribute; otherwise return the value unchanged.
- `03:01:59` Root cause: QuantityInput wrapper always called return_.to(...) when a return annotation was present; this raised AttributeError for None returns (e.g...
- `03:01:47` decorators.py: patched return handling at lines ~220-226: if return_annotation present -> if return_ is None then return None; elif hasattr(return_, '...
- `03:01:32` ACTION: sed -n '212,228p' astropy/units/decorators.py
- `03:01:26` Reproduction output: OK 1.0 m
- `03:01:10` RESULT: OK 1.0 m
- `03:00:55` Applied patch to astropy/units/decorators.py (output: PATCHED); attempted verification failed to run due to shell syntax error: bash: -c: line 30: syn...
- `03:00:42` ACTION: python3 - <<'PY'
- `03:00:04` ACTION: nl -ba astropy/units/decorators.py | sed -n '1,400p'
- `02:59:55` ACTION: grep -nR "quantity_input" astropy | sed -n '1,200p'
- `02:59:40` ACTION: ls -la
- `02:59:38` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
