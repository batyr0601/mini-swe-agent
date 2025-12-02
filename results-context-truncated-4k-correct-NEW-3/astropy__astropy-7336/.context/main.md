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
- [ ] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 15:51] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `15:51:16` ACTION: Submitting solution
- `15:51:10` repro.py: ran once, output: 'Instantiating C with 1 m' and 'Instance created, x = 1.0 m
- `15:50:56` RESULT: Instantiating C with 1 m
Instance created, x = 1.0 m
- `15:50:55` ACTION: python3 repro.py
- `15:50:48` ACTION: sed -n '180,260p' astropy/units/decorators.py
- `15:50:30` ACTION: grep -RIn "repro" . || true && grep -RIn "QuantityInput" . || true && test -f repro. [...]
- `15:50:08` Patched astropy/units/decorators.py: guard against calling .to() on None by checking wrapped_signature.return_annotation is not inspect.Signature.empt...
- `15:49:56` RESULT: patched
- `15:49:56` ACTION: python3 - <<'PY'
- `15:49:14` Found in astropy/units/decorators.py: wrapper() calls wrapped_function and then does 'if wrapped_signature.return_annotation is not inspect.Signature....
- `15:48:46` ACTION: sed -n '180,260p' astropy/units/decorators.py
- `15:48:39` repro.py: AttributeError 'NoneType' object has no attribute 'to' when instantiating C; traceback shows astropy/utils/decorators.py:824 -> astropy/unit...
- `15:48:16` repro.py: AttributeError \"'Unit' object has no attribute 'm'\" when importing with 'from astropy.units import u'; cause: 'u' bound to a Unit, not the...
- `15:48:02` ACTION: Reading file: <<'PY'
- `15:47:43` ACTION: sed -n '1,420p' astropy/units/decorators.py
- `15:47:28` ACTION: sed -n '1,240p' astropy/units/decorators.py
- `15:47:24` ACTION: grep -nR "quantity_input" astropy || true
- `15:47:12` ACTION: grep -n "class QuantityInput" astropy/units/decorators. [...]
- `15:47:01` ACTION: grep -nR "quantity_input" astropy || true
