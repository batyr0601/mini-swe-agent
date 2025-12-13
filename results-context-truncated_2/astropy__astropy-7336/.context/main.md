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
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: run PoC example to observe AttributeError when return_annotation is None
- [ ] 2. Locate the code: search repository for
- [ ] 3. Root cause analysis: inspect decorator logic where it inspects return_annotation and may call .to()
- [ ] 4. Implement fix: modify decorator to skip return unit conversion when return_annotation is None (or typing.None) and add appropriate tests
- [ ] 5. Verify fix: run the PoC script and existing tests to ensure the AttributeError no longer occurs

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:44] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `20:43:59` ACTION: Submitting solution
- `20:43:52` Root cause: wrapper unconditionally called return_.to(...) when return_annotation is present. An explicit '-> None' makes return_annotation None (not ...
- `20:43:41` poc.py: created: <__main__.PoC object at 0x7fffff333a58>
- `20:43:31` RESULT: created: <__main__.PoC object at 0x7fffff333a58>
- `20:43:30` ACTION: Reading file: poc.py
- `20:43:24` Patched astropy/units/decorators.py: replaced unconditional return_.to(...) with checks that wrapped_signature.return_annotation is not inspect.Signat...
- `20:43:18` RESULT: patched
- `20:43:17` ACTION: python3 - <<'PY'
- `20:42:58` astropy/units/decorators.py: wrapper lines 220-226: after calling wrapped_function(), code checks if wrapped_signature.return_annotation is not inspec...
- `20:42:46` ACTION: nl -ba astropy/units/decorators.py | sed -n '1,320p'
- `20:42:40` ACTION: grep -Rn "quantity_input" . || true
- `20:42:26` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
