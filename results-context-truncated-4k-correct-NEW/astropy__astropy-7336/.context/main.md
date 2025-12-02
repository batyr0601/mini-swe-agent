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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 11:58] **swebench-astropy__astropy-7336**: Task completed: LimitsExceeded
## Interaction Log

- `11:57:57` repro.py: ran successfully; output: 'repro ran'; no AttributeError for __init__ annotated -> None; decorator now skips .to when return_ is None
- `11:57:44` RESULT: repro ran
- `11:57:43` ACTION: printf '%s\n' 'from astropy import units as u' 'from astropy. [...]
- `11:57:24` ACTION: Reading file: <<'PY'
- `11:56:56` python3 repro.py failed: can't open file 'repro.py': [Errno 2] No such file or directory
- `11:56:50` RESULT: python3: can't open file 'repro.py': [Errno 2] No such file or directory
- `11:56:50` ACTION: python3 repro.py
- `11:56:41` patched decorators.py: replaced return_.to condition; output: 'patched' and then bash: -c: line 25: syntax error near unexpected token `&&' when attem...
- `11:56:31` ACTION: python3 - <<'PY'
- `11:56:05` ACTION: grep -nR "@quantity_input" astropy || true
- `11:55:51` ACTION: grep -n "return_.to" astropy/units/decorators.py && sed -n '200,260p' astropy/units/decorators.py
- `11:55:37` ACTION: grep -nE "quantity_input|return_.to|wrapped_signature" astropy/units/decorators. [...]
- `11:55:15` ACTION: grep -n "return_.to" astropy/units/decorators.py || true && sed -n '1,320p' astropy/units/decorators [...]
- `11:54:58` ACTION: sed -n '1,320p' astropy/units/decorators.py
- `11:54:45` ACTION: grep -n "return_.to" astropy/units/decorators.py && sed -n '1,320p' astropy/units/decorators.py
- `11:54:32` ACTION: grep -nR "return_.to" astropy || true && grep -nR "wrapped_signature. [...]
- `11:53:40` ACTION: grep -n "return_.to" astropy/units/decorators.py && sed -n '1,320p' astropy/units/decorators.py
- `11:53:14` ACTION: sed -n '1,320p' astropy/units/decorators.py
- `11:52:49` ACTION: grep -n "return_.to" astropy/units/decorators.py || true && sed -n '1,320p' astropy/units/decorators [...]
- `11:52:32` ACTION: grep -n "return_.to" astropy/units/decorators.py && sed -n '1,320p' astropy/units/decorators.py
