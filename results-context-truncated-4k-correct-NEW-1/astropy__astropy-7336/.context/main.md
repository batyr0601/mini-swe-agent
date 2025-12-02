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

- [2025-12-02 14:13] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `14:13:56` ACTION: Submitting solution
- `14:13:51` repro.py output: Created A: 1.0 m
- `14:13:43` Implemented fix: replaced 'if wrapped_signature.return_annotation is not inspect.Signature.empty:' with 'if (wrapped_signature.return_annotation is no...
- `14:13:28` Root cause: explicit return_annotation of None (e.g., on __init__) is not inspect.Signature.empty, so wrapper called return_.to(None) causing Attribut...
- `14:12:52` ACTION: cp astropy/units/decorators.py astropy/units/decorators.py.bak && \
- `14:12:36` astropy/units/decorators.py: wrapper (lines ~200-260) calls return_.to(wrapped_signature.return_annotation) when return_annotation is not inspect.Sign...
- `14:12:20` ACTION: sed -n '200,260p' astropy/units/decorators.py
- `14:12:14` repro.py: AttributeError NoneType object has no attribute to at /testbed/astropy/units/decorators.py:224 when __init__ has return_annotation None
- `14:12:03` ACTION: Reading file: <<'PY'
- `14:11:25` ACTION: grep -Rn "quantity_input" . || true
- `14:11:18` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
