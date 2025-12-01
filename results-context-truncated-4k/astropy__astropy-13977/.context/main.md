# Project Goals

**Current Task:** Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?

<details>
<summary>Full description</summary>

Should `Quantity.__array_ufunc__()` return `NotImplemented` instead of raising `ValueError` if the inputs are incompatible?
### Description
I'm trying to implement a duck type of `astropy.units.Quantity`. If you are interested, the project is available [here](https://github.com/Kankelborg-Group/named_arrays). I'm running into trouble trying to coerce my duck type to use the reflected versions of the arithmetic operators if the left operand is not an instance of the duck type _and_ they have equivalent but different units. Consider the following minimal working example of my duck type.

```python3
import dataclasses
import numpy as np
import astropy.units as u


@dataclasses.dataclass
class DuckArray(np.lib.mixins.NDArrayOperatorsMixin):
    ndarray: u.Quantity

    @property
...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Reproduce the bug: create a minimal script using DuckArray and astropy Quantity to trigger the ValueError
- [ ] 2. Locate the code: find the implementation of Quantity.__array_ufunc__ in the codebase to inspect where it raises ValueError
- [ ] 3. Root cause analysis: Identify why incompatible inputs cause a ValueError instead of returning NotImplemented and which checks/converters are responsible
- [ ] 4. Implement fix: modify Quantity.__array_ufunc__ (or related converter logic) to return NotImplemented for incompatible inputs so reflected ops can run
- [ ] 5. Verify fix: run the reproduction script and relevant tests to ensure __radd__ is used and no regressions occur
- [ ] 1. Reproduce the bug: create a small repro that triggers a numpy ufunc with a Quantity and a non-Quantity such that the operation currently raises ValueError instead of returning NotImplemented
- [ ] 2. Locate relevant helpers: find definitions/usages of converters_and_unit, check_output, _to_own_unit, _new_view, and _result_as_quantity in astropy/units/ and related files
- [ ] 3. Inspect superclass behavior: run a minimal case to see what super().__array_ufunc__ returns when another operand
- [ ] 4. Root cause analysis: identify where a ValueError is raised instead of returning NotImplemented and whether the check_output or converters logic causes it
- [ ] 5. Implement fix: modify __array_ufunc__ (or helpers) to return NotImplemented in the appropriate mixed-type cases and add comments explaining rationale
- [ ] 6. Add tests: write a unit test reproducing the original issue, asserting that the ufunc returns NotImplemented (or that Python falls back) rather than raising ValueError
- [ ] 7. Verify fix: run the new test and the relevant subset of astropy tests (ufunc/units related) and mark TODOs complete as steps finish
- [ ] 1. Read Quantity.__array_ufunc__ usage: inspect astropy/units/quantity.py around lines 600-740 to see how converters_and_unit, check_output, _to_own_unit, _new_view, _result_as_quantity are called
- [ ] 2. Open converters_and_unit & check_output implementations: inspect astropy/units/quantity_helper/converters.py to understand their logic and edge cases
- [ ] 3. Inspect related helpers: read astropy/units/quantity_helper/helpers.py for get_converters_and_unit and helper_twoarg_invariant behavior
- [ ] 4. Search for other uses: grep for _to_own_unit, _new_view, _result_as_quantity across astropy to find all call sites to ensure consistent behavior
- [ ] 5. Summarize findings and plan a fix: based on the above, draft the root cause, proposed code change, and tests to run
- [ ] 2. Read remaining lines of astropy/units/quantity_helper/converters.py to inspect the
- [ ] 3. Locate the check_output function definition in converters.py and inspect its implementation
- [ ] 4. Determine how
- [ ] 5. Search repository for other references to check_output to find callers and ensure consistent behavior
- [ ] 1. Read astropy/units/quantity.py lines 630-680 to inspect call at line 652: out_array = check_output(out, unit, inputs, function=function) and determine types/values of
- [ ] 2. Read astropy/units/quantity.py lines 1896-1944 to inspect call at line 1923: kwargs[
- [ ] 3. Trace what callers pass as
- [ ] 4. Implement fix: either adjust callers to pass correct unit or modify check_output to accept plain arrays for dimensionless outputs; prepare patch.
- [ ] 5. Create/modify a minimal repro or unit test and run relevant tests to verify the fix.
- [ ] 1. Understand the bug: confirm check_output currently rejects plain numpy ndarray outputs when unit is None (dimensionless output) and reproduce minimal failing case
- [ ] 2. Locate the code: check_output in astropy/units/quantity_helper/converters.py and its callers in astropy/units/quantity.py (__array_ufunc__ and _wrap_function)
- [ ] 3. Root cause analysis: inspect all branches of check_output to see why plain ndarray output is disallowed for unit is None, and identify exact condition and error message triggered
- [ ] 4. Implement fix: modify check_output so that when unit is None a plain ndarray output is accepted (and only Quantity outputs require compatible units); update error message to clarify when non-quantity outputs are disallowed
- [ ] 5. Verify fix: run the minimal reproduction script and relevant unit tests (numpy/astropy ufunc-related tests) to ensure no regressions
- [ ] 1. Understand the bug: inspect how Quantity.__array_ufunc__ and _wrap_function pass the
- [ ] 2. Locate the code: open astropy/units/quantity_helper/converters.py to find the check_output implementation
- [ ] 3. Root cause analysis: read check_output to determine whether it returns ndarray views or Quantity objects and how it handles tuples/None
- [ ] 4. Reproduce the issue: create/run a minimal Python repro that calls a ufunc and _wrap_function with out as a Quantity and as an ndarray to observe the behavior
- [ ] 5. Implement fix & verify: propose specific change (either in check_output or _result_as_quantity), apply it, and run relevant unit tests for astropy/units/quantity.py
- [ ] 1. Reproduce bug: run minimal repro where out is q.view(np.ndarray) and observe UnitTypeError
- [ ] 2. Locate __array_ufunc__: find implementation in astropy/units/quantity.py and inspect how it calls check_output
- [ ] 3. Inspect check_output callsites: verify what
- [ ] 4. Implement fix: modify converters.check_output to treat ndarray outputs whose .base has __quantity_subclass__ as Quantity-backed and return appropriate ndarray view without raising UnitTypeError
- [ ] 5. Add unit test: create test that uses out=q.view(np.ndarray) with a ufunc and asserts no error and that q is updated and return value type is appropriate
- [ ] 6. Run unit tests for astropy.units to verify fixes and resolve any regressions
- [ ] 3. Analyze converters.check_output: inspect branches (tuple, __quantity_subclass__, else) to identify exact condition causing UnitTypeError for numpy ndarray outputs
- [ ] 4. Reproduce minimal case: run a short python snippet that uses a ufunc (e.g., np.add) with Quantity inputs and a numpy.ndarray out to print types/values and reproduce the UnitTypeError
- [ ] 5. Implement fix: modify astropy/units/quantity_helper/converters.py to correctly handle ndarray outputs (ensure Quantity outputs are converted to ndarray views, and plain ndarray out raises a clearer error only when unit is not None), and add a regression test
- [ ] 6. Run targeted tests (tests for units/quantity ufuncs or a small pytest invocation) to verify the fix
- [ ] 1. Reproduce the bug: create a minimal script using DuckArray and astropy Quantity to trigger the ValueError in Quantity.__array_ufunc__
- [ ] 1. Understand the bug: Reproduce the failing behavior for Quantity.__array_ufunc__ using a minimal example or provided repro
- [ ] 2. Locate the code: Open __array_ufunc__ in astropy/units/quantity.py and related implementations in astropy/coordinates/angles.py, astropy/coordinates/spectral_quantity.py, astropy/units/function/core.py, and astropy/uncertainty/core.py
- [ ] 3. Root cause analysis: Inspect how inputs,
- [ ] 4. Implement fix: Update astropy/units/quantity.py (and other affected files if needed) to correctly handle
- [ ] 5. Verify fix: Run unit tests for astropy/units and astropy/coordinates, run the repro/minimal example, and ensure no regressions
- [ ] 1. Reproduce the bug: minimal repro showing UnitTypeError when using np.add with out=np.empty(...) and Quantity inputs
- [ ] 2. Locate check_output: open astropy/units/quantity_helper/converters.py around the check_output implementation
- [ ] 3. Root cause analysis: analyze check_output logic to determine why it rejects non-Quantity outs for this ufunc case and whether that is correct
- [ ] 4. Implement fix: update check_output to allow compatible ndarray outs when safe (e.g., dimensionless results) or convert/accept dtype appropriately, add tests
- [ ] 5. Verify fix: run the minimal repro and relevant unit tests to confirm behavior and ensure no regressions
- [ ] Run unit tests for quantity_helper to ensure no regressions
- [ ] If tests fail, collect failures and debug converters.py changes
- [ ] 1. Locate Quantity.__array_ufunc__: grep for
- [ ] 2. Inspect check_output: open astropy/units/quantity_helper/converters.py and locate the check_output implementation to understand handling of ndarray outputs and unit=None cases
- [ ] 3. Reproduce minimal error: run the minimal repro script using DuckArray and astropy Quantity to trigger the ValueError and capture the full traceback
- [ ] 4. Run targeted tests: run pytest astropy/units -k
- [ ] 1. Read full check_output implementation in astropy/units/quantity_helper/converters.py to find handling of outputs with unit=None
- [ ] 2. Search repository for other usages of check_output and patterns when unit=None is used for outputs
- [ ] 3. Create a minimal repro for ndarray output with unit=None to observe current behavior
- [ ] 4. Implement fix in converters.py to correctly handle ndarray outputs with unit=None
- [ ] 5. Run targeted unit tests or a minimal test script to verify the fix
- [ ] 2. Locate check_output definition: open astropy/units/quantity_helper/converters.py and inspect the implementation around the check_output function (focus on handling for unit is None and Quantity outputs)
- [ ] 3. Inspect callers passing unit=None: review astropy/units/quantity.py (lines ~600 and ~1920), and other call sites from grep to see how they expect check_output to behave
- [ ] 4. Reproduce exact traceback: run the minimal repro/test that triggers the TypeError when check_output receives unit=None for a Quantity subclass output and capture full traceback
- [ ] 5. Implement fix: modify check_output logic to correctly handle unit=None for Quantity vs non-Quantity outputs, ensure correct exception types/messages, and add unit tests covering the case
- [ ] 6. Verify fix: run pytest for affected tests (at least astropy/units/tests/test_quantity_non_ufuncs.py and other unit tests referencing check_output) and iterate until all pass
- [ ] 1. Understand the bug: inspect check_output behavior for cases where `unit` is None but `output` is a Quantity (or where `unit` is a Unit but `output` is a plain ndarray), and determine which exceptions (UnitTypeError/TypeError) are raised and why
- [ ] 2. Locate the code: display the full check_output function in astropy/units/quantity_helper/converters.py to inspect all branches and early returns
- [ ] 3. Root cause analysis: identify the conditional(s) that incorrectly classify outputs (e.g., treating Quantity vs ndarray vs tuple inconsistently), note exact lines and conditions
- [ ] 4. Implement fix: modify check_output to correctly handle (a) unit is None with Quantity output (allow or convert as appropriate), (b) unit is Unit but output is ndarray (raise UnitTypeError), and ensure tuple outputs are handled consistently; prepare a small patch
- [ ] 5. Verify fix: add/modify unit tests or run a repro script demonstrating the original failure and confirm it passes; run pytest for astropy.units related tests
- [ ] 1. Understand the behavior of check_output: determine how it handles plain ndarray outputs when unit is not None or not dimensionless, and what exceptions/messages are produced
- [ ] 2. Locate check_output implementation in astropy/units/quantity_helper/converters.py and identify the exact branches and error messages to change
- [ ] 3. Create a minimal repro script that calls check_output with representative inputs to trigger the problematic branch for non-Quantity outputs
- [ ] 4. Run the repro to capture the exact exception type and traceback
- [ ] 5. Implement a targeted fix in converters.py (adjust branch logic or error message formatting) and add unit tests covering the case
- [ ] 6. Run relevant unit tests (units/quantity helper related) and iterate until passing, then create a context_commit checkpoint
- [ ] 1. Locate UnitTypeError message in astropy/units/quantity_helper/converters.py: find
- [ ] 2. Edit converters.py: insert a space so message reads
- [ ] 3. Run repros: repro.py (function None) and repro_func.py (with function provided) to verify error messages and behavior
- [ ] 4. Run quick syntax check (python -m py_compile astropy/units/quantity_helper/converters.py) to ensure no syntax errors
- [ ] 5. context_commit --message

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 01:26] **swebench-astropy__astropy-13977**: Allow plain ndarray outputs for dimensional units when dtype can safely hold the ufunc result; add d...
## Interaction Log

- `01:33:24` converters.py: replaced '{}in a' with '{} in a' around line 399; sed shows UnitTypeError message now 'Cannot store quantity with dimension {} in a non...
- `01:32:55` ACTION: cp astropy/units/quantity_helper/converters.py astropy/units/quantity_helper/converters.py. [...]
- `01:32:39` ACTION: sed -n '388,412p' astropy/units/quantity_helper/converters.py
- `01:32:35` RESULT: 399:                "Cannot store quantity with dimension "
- `01:32:34` ACTION: grep -n "Cannot store quantity with dimension" astropy/units/quantity_helper/converters.py
- `01:32:06` ACTION: sed -n '360,520p' astropy/units/quantity_helper/converters.py
- `01:31:54` repro.py: Called check_output with plain ndarray output and unit m; observed output: 'Calling check_output with plain ndarray output and unit = m' fol...
- `01:31:44` ACTION: Reading file: <<'PY'
- `01:31:26` check_output (converters.py:293-360): defined at line 293; handles tuple output and None; if hasattr(output, '__quantity_subclass__') true -> if unit ...
- `01:31:14` ACTION: sed -n '280,360p' astropy/units/quantity_helper/converters.py
- `01:31:09` grep def check_output: astropy/units/quantity_helper/converters.py:293; occurrences/calls: astropy/units/quantity.py:652, astropy/units/quantity.py:19...
- `01:30:59` ACTION: grep -n "def check_output" astropy -R || true && grep -n "check_output(" astropy -R || true
- `01:30:34` ACTION: sed -n '1,400p' astropy/units/quantity_helper/converters.py
- `01:30:09` ACTION: grep -n "def check_output" astropy/units/quantity_helper/converters. [...]
- `01:29:10` ACTION: grep -nR "check_output(" . || true && grep -nR "unit=None" . || true
- `01:29:04` check_output: for Quantity outputs (has __quantity_subclass__), if unit is None raises TypeError \"Cannot store non-quantity output...\"; otherwise va...
- `01:28:49` ACTION: sed -n '280,420p' astropy/units/quantity_helper/converters.py
- `01:28:20` ACTION: grep -nR "def check_output" astropy || true && sed -n '1,240p' astropy/units/quantity_helper/convert [...]
- `01:28:12` grep __array_ufunc__: astropy/units/quantity.py:620,672-678; astropy/units/function/core.py:618,628; astropy/units/structured.py:444; binary matches i...
- `01:28:01` ACTION: grep -nR "__array_ufunc__" astropy/units || true
