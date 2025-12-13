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

- [2025-12-03 00:28] **swebench-astropy__astropy-7336**: Task completed: Submitted
## Interaction Log

- `00:28:15` ACTION: Submitting solution
- `00:28:12` poc.py executed with no AttributeError: constructor annotated -> None handled correctly. Root cause was return_annotation handling in astropy/units/de...
- `00:27:43` ACTION: Reading file: poc.py
- `00:27:33` Edited astropy/units/decorators.py: added explicit check 'if return_ is None: return return_' before calling .to on function return value
- `00:27:19` ACTION: perl -0777 -i -pe 's/with add_enabled_equivalencies\(self. [...]
- `00:26:55` ACTION: nl -ba astropy/units/decorators.py | sed -n '1,400p'
- `00:26:50` ACTION: grep -nR "quantity_input" astropy || true
- `00:26:48` ACTION: grep -nR "def quantity_input" astropy || true
- `00:26:45` ACTION: ls -la
- `00:26:36` TASK STARTED: units.quantity_input decorator fails for constructors with type hinted return value -> None
