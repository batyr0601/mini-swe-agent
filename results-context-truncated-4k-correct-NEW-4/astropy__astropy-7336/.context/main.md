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

- [2025-12-02 18:32] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `18:32:35` ACTION: Submitting solution
- `18:32:31` Root cause: wrapper in astropy/units/decorators.py called .to() even when return_annotation is literal None; fix: guard with 'is not None' before call...
- `18:32:31` repro.py: after patch, constructing C(3*m) succeeded; observed output: 'Constructing C with 3 m' then 'Constructed OK
- `18:32:10` RESULT: Constructing C with 3 m
Constructed OK
- `18:32:10` ACTION: python3 repro.py
- `18:32:03` decorators.py patched: replaced return conversion guard to skip when return_annotation is None; observed 'patched' from replacement script
- `18:31:50` decorators.py: wrapper calls return_.to(wrapped_signature.return_annotation); if return_annotation is None this causes AttributeError 'NoneType' objec...
- `18:31:24` ACTION: sed -n '200,260p' astropy/units/decorators.py
- `18:31:12` ACTION: Reading file: <<'PY'
- `18:30:54` ACTION: grep -RIn "quantity_input" . || true
- `18:30:48` ACTION: grep -RIn "def quantity_input" || true
- `18:30:36` ACTION: grep -RIn "quantity_input" || true
- `18:30:26` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
