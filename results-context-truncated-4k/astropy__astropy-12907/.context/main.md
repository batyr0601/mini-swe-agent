# Project Goals

**Current Task:** Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels

<details>
<summary>Full description</summary>

Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
Consider the following model:

```python
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

cm = m.Linear1D(10) & m.Linear1D(5)
```

It's separability matrix as you might expect is a diagonal:

```python
>>> separability_matrix(cm)
array([[ True, False],
       [False,  True]])
```

If I make the model more complex:
```python
>>> separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5))
array([[ True,  True, False, False],
       [ True,  True, False, False],
       [False, False,  True, False],
       [False, False, False,  True]])
```

The output matrix is again, as expected, the outputs and inputs to th...
</details>


**Current Task:** Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels

<details>
<summary>Full description</summary>

Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
Consider the following model:

```python
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

cm = m.Linear1D(10) & m.Linear1D(5)
```

It's separability matrix as you might expect is a diagonal:

```python
>>> separability_matrix(cm)
array([[ True, False],
       [False,  True]])
```

If I make the model more complex:
```python
>>> separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5))
array([[ True,  True, False, False],
       [ True,  True, False, False],
       [False, False,  True, False],
       [False, False, False,  True]])
```

The output matrix is again, as expected, the outputs and inputs to th...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce separability_matrix behavior for nested CompoundModels using a small script that mirrors the PR description
- [ ] 2. Locate the code: find the separability_matrix implementation and related CompoundModel handling (grep for separability_matrix and CompoundModel)
- [ ] 3. Root cause analysis: inspect how separability_matrix processes CompoundModel children and whether nested compounds are flattened or their blocks combined incorrectly
- [ ] 4. Implement fix: modify separability_matrix to correctly handle nested CompoundModels by flattening or merging separability blocks so nested models
- [ ] 5. Verify fix: create and run a reproduction script from the PR description and run relevant tests to ensure behavior matches expected separability matrices
- [ ] 1. Understand the repository: list top-level files, check git status, and run pytest -q to see failing tests
- [ ] 2. Reproduce the bug: run failing test(s) or provided repro script to get exact error message and stack trace
- [ ] 3. Locate the problematic code: grep the source for
- [ ] 4. Root cause analysis: inspect the identified function(s)/file(s) to determine why AttributeError is being caught and which descriptor is involved
- [ ] 5. Implement fix: update code to let descriptor/descriptor-like AttributeError propagate or check class descriptors first, add minimal code change with explanation
- [ ] 6. Verify fix: run full test suite, add a regression test for the case, and ensure all tests pass
- [ ] 1. Reproduce the bug: run the failing script or test that triggers the AttributeError and capture the full traceback
- [ ] 2. Locate the code: search repository for __getattr__, __getattribute__, descriptors, and the class names shown in the traceback
- [ ] 3. Root cause analysis: inspect implementations to see where AttributeError may be caught/masked (e.g., in __getattr__ or property descriptors) and identify exact failing lines
- [ ] 4. Implement fix: update code to avoid swallowing descriptor AttributeErrors, adjust error message to show actual missing attribute, and add targeted unit tests
- [ ] 5. Verify fix: run the repro script and full test suite, ensure the specific regression test passes and no new failures are introduced
- [ ] 1. Reproduce the bug: run the failing scenario (unit tests or provided repro script) to capture full stack trace and exact error message
- [ ] 2. Locate the code: search the repository for attribute-access implementations (grep for
- [ ] 3. Root cause analysis: inspect the located methods to find where AttributeError is caught or re-raised, determine whether descriptor exceptions are being masked, and create a minimal reproducer
- [ ] 4. Implement fix: modify the offending method(s) to avoid catching AttributeError from descriptors (only catch intended cases), update error message, and add a focused unit/regression test
- [ ] 5. Verify fix: run the new test and full test suite, ensure all tests pass, and document the change and rationale in the log
- [ ] 1. Clarify requirements: ask user to describe the bug/feature, provide repository path, steps to reproduce, expected vs actual behavior, and any error messages
- [ ] 2. Reproduce environment: collect OS, Python and dependency versions, attempt to run provided reproduction scripts or tests, capture failure outputs
- [ ] 3. Locate code: search the repo for files/functions/strings related to the issue (e.g., grep for error messages, class/function names) to identify candidate locations
- [ ] 4. Implement fix: create a branch, edit the located files to address root cause, run linters/formatters, and prepare a clear commit message describing the change
- [ ] 5. Verify fix: add or update tests that reproduce the failure, run the full test suite, record results, and prepare notes for code review
- [ ] 1. Reproduce the bug: create a small repro that triggers the AttributeError from SkyCoord.__getattr__ (access missing/descriptor attribute) and run the failing test(s)
- [ ] 2. Locate the code: find and open astropy/coordinates/sky_coordinate.py __getattr__ implementation and any related descriptor/property code referenced there
- [ ] 3. Root cause analysis: inspect exception handling in __getattr__ (lines ~829-905), identify where AttributeError from descriptors/properties is being masked and determine fix strategy
- [ ] 4. Implement fix: modify __getattr__ to check class descriptors/attributes first or limit exception catching so descriptor AttributeError propagates; write a minimal patch with tests
- [ ] 5. Verify fix: run targeted pytest for astropy/coordinates tests (or the specific failing test), confirm the AttributeError message is correct and no other tests regress
- [ ] 3. Root cause analysis: Inspect __getattr__ implementations in baseframe.py (lines ~1540-1620 and ~1860-1910) and sky_coordinate.py (lines 829-905) to identify any code paths that could mask AttributeError raised by descriptors or properties
- [ ] 4. Reproduce the bug: Create a minimal repro that defines a frame attribute descriptor/property that raises AttributeError and access it via SkyCoord/frame to observe the error message and determine which __getattr__ is responsible
- [ ] 5. Implement fix: Modify sky_coordinate.__getattr__ (or baseframe.__getattr__ if needed) so that attribute access to frame descriptors uses getattr in a way that lets descriptor-raised AttributeError propagate with the correct attribute name; ensure not to swallow AttributeError from descriptors
- [ ] 6. Verify fix: Run the repro and the coordinates unit tests (or targeted tests) to confirm the AttributeError message now names the correct missing attribute and no other tests fail
- [ ] 1. Understand the bug: Investigate how SkyCoord.__getattr__ may mask AttributeError from frame descriptors/properties (why error message shows generic missing-attribute instead of original descriptor error)
- [ ] 2. Locate the code: Find where frame_transform_graph.frame_attributes and the frame Attribute/descriptor are defined; grep for
- [ ] 1. Understand the bug: determine why accessing frame attributes sometimes raises/rewrites AttributeError — focus on behavior around SkyCoord/BaseFrame __getattr__ and Attribute descriptor
- [ ] $'1.
- [ ] 1. Reproduce the bug: write/run a small repro that accesses a representation component (e.g. frame.pm_ra_cosdec or getattr on a representation component) to trigger BaseCoordinateFrame.__getattr__ and capture the exact exception/output
- [ ] 2. Locate the code: open astropy/coordinates/baseframe.py around the __getattr__ implementation (approx lines 1700-1900) and astropy/coordinates/attributes.py and sky_coordinate.py __getattr__ locations to inspect behavior
- [ ] 3. Root cause analysis: inspect BaseCoordinateFrame.__getattr__ to find why there is a stray fallback
- [ ] 4. Implement fix: modify BaseCoordinateFrame.__getattr__ to remove the erroneous fallback, ensure it returns getattr(rep, repr_names[attr]) for known representation names and raises a clear AttributeError otherwise; update/add unit test reproducing the bug
- [ ] 5. Verify fix: run the repro script and run pytest for coordinates (or targeted tests) to ensure the AttributeError is correct and no NameError or incorrect return occurs; mark todos complete as each step is verified
- [ ] 3. Root cause analysis: inspect SkyCoord.__getattr__ and interplay with BaseCoordinateFrame.__getattr__ for pm_lon/pm_lat handling
- [ ] 4. Implement fix: modify sky_coordinate.py to avoid calling represent_as() when no differentials or to map pm_ attrs correctly
- [ ] 5. Verify fix: add a regression test and run the minimal repro and relevant tests
- [ ] 1. Understand the bug: Reproduce the AttributeError observed when accessing an attribute on BaseCoordinateFrame/SkyCoord that is incorrectly raised or has the wrong attribute name in the exception; capture exact repro steps and error message
- [ ] 2. Locate the code: Find all __getattr__ implementations in astropy/coordinates (e.g., sky_coordinate.py and frame.py) and note line numbers to inspect
- [ ] 3. Root cause analysis: Inspect the __getattr__ implementations to see if they catch AttributeError from descriptors or property getters and re-raise with an incorrect attribute name; identify the exact lines and logic causing mask/misreport
- [ ] 4. Implement fix: Update __getattr__ to check class descriptors/attributes first and avoid catching AttributeError raised by descriptors (or re-raise original exceptions appropriately); add/modify unit tests demonstrating correct behavior
- [ ] 5. Verify fix: Run targeted pytest for astropy.coordinates tests and a minimal repro script to confirm the AttributeError is fixed and messages are correct; mark todos complete and create context commits/logs as findings are observed
- [ ] 1. Inspect BaseCoordinateFrame.__getattr__ in astropy/coordinates/baseframe.py (around lines 1540-1620 and 1840-1900) for unexpected returns or exception handling
- [ ] 2. Inspect SkyCoord/BaseCoordinateFrame __getattr__ in astropy/coordinates/sky_coordinate.py (around lines 780-940) to locate the stray
- [ ] 3. Reproduce the error with a minimal Python snippet that accesses the attribute triggering the fallback (to capture exact exception and traceback)
- [ ] 4. Implement fix: remove or correct the erroneous fallback return so missing attributes raise AttributeError or delegate correctly to representation components
- [ ] 5. Verify fix by running the minimal repro and relevant unit tests
- [ ] 1. Understand the bug: inspect BaseCoordinateFrame.__getattr__ which unexpectedly returns a pm_lon/pm_lat stack instead of raising AttributeError or returning the requested representation component
- [ ] 2. Locate the code: confirm all __getattr__ implementations in astropy/coordinates (baseframe.py, sky_coordinate.py, etc.) and note exact line ranges
- [ ] 3. Root cause analysis: determine how pm_lon/pm_lat ended up in BaseCoordinateFrame.__getattr__ (look for accidental paste or leftover code) and whether other code paths rely on that return
- [ ] 4. Implement fix: modify BaseCoordinateFrame.__getattr__ to remove the erroneous np.stack return and ensure it raises AttributeError when attr not found; run static checks
- [ ] 5. Verify fix: run targeted unit tests or repro (import astropy, create frame, access missing attr) and run pytest for coordinates module
- [ ] 1. Understand the bug: inspect BaseCoordinateFrame __getattr__ behavior that returns a stacked pm_lon/pm_lat array
- [ ] 2. Locate related properties: find where pm_lon_coslat/pm_lat are defined and how they map to pm_ra/pm_dec
- [ ] 3. Root cause analysis: determine if return type (np.stack) is wrong or attribute aliasing leads to unexpected structure
- [ ] 4. Implement fix: modify BaseCoordinateFrame to return a Quantity or separate components rather than stacked array
- [ ] 5. Verify fix: run tests astropy/coordinates/tests/test_skyoffset_transformations.py::test_* and a small repro
- [ ] 1. Understand the bug: reproduce the failing behavior or test case (capture exact error message and minimal repro)
- [ ] 2. Locate the code: find relevant files/functions (use grep to locate suspects, open file ranges to inspect implementation)
- [ ] 3. Root cause analysis: identify the code path and condition causing the failure, note any surprising exceptions or handlers
- [ ] 4. Implement fix: make minimal, well-tested code changes with clear rationale and inline comments; run linters/formatters
- [ ] 5. Verify fix: run existing tests and add new regression test(s); document results and mark TODOs complete
- [ ] 1. Reproduce the bug: create a minimal repro that triggers AttributeError with wrong attribute name when a frame descriptor raises AttributeError
- [ ] 2. Locate the code: inspect __getattr__, __setattr__, and places using hasattr(self._sky_coord_frame, attr) in astropy/coordinates/sky_coordinate.py
- [ ] 3. Root cause analysis: determine whether hasattr(self._sky_coord_frame, attr) masks AttributeError raised by frame descriptors and identify where __getattr__ re-raises with the wrong attribute name
- [ ] 4. Implement fix: modify __getattr__ to avoid using hasattr(self._sky_coord_frame, attr) (use safe getattr with try/except and allow descriptor-raised AttributeError to propagate), update __setattr__/__delattr__ symmetrically if needed
- [ ] 5. Add tests: add a unit test that ensures descriptor-raised AttributeError propagates and that missing attributes raise AttributeError mentioning the requested name
- [ ] 6. Verify: run pytest for astropy/coordinates (or targeted tests) and iterate until tests pass
- [ ] 4. Show modified region (lines 832-906) and run syntax check on astropy/coordinates/sky_coordinate.py
- [ ] 5. Run minimal repro to ensure descriptor-raised AttributeError from frame propagates (i.e., hasattr no longer masks it)
- [ ] 1. Understand the bug: reproduce AttributeError from a frame descriptor using a minimal script that accesses a missing attribute on SkyCoord and capture full traceback
- [ ] 2. Locate the code: open astropy/coordinates/sky_coordinate.py and inspect __getattr__ (approx lines 832-906) to find uses of hasattr(self._sky_coord_frame, attr) and related exception handling
- [ ] 3. Root cause analysis: determine how hasattr masks AttributeError from descriptors; identify exact lines where AttributeError is caught/re-raised with the wrong attribute name
- [ ] 4. Implement fix: modify __getattr__ to avoid using hasattr; use try/except around getattr(self._sky_coord_frame, attr) and allow descriptor-raised AttributeError to propagate; prepare a minimal patch and unit test reproducing the failure
- [ ] 5. Verify fix: run the minimal repro script and run pytest for astropy/coordinates (or targeted tests), ensure the regression test passes, then mark related TODOs complete
- [ ] 3. Analyze baseframe __getattr__: check how it handles attribute access and exceptions
- [ ] 4. Decide whether sky_coordinate.__getattr__ should change: identify exact lines to modify
- [ ] 5. Implement fix in astropy/coordinates/sky_coordinate.py to avoid masking descriptor-raised AttributeError
- [ ] 6. Run repro and tests

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:46:03` TASK STARTED: Modeling's `separability_matrix` does not compute separability correctly for nested CompoundModels
- `01:33:18` sky_coordinate.py:820-920: __getattr__ delegates frame-attribute access: if attr in frame_transform_graph.frame_attributes then if attr in self.frame....
- `01:32:55` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `01:32:49` baseframe.py:1560-1620 and 1860-1920: first __getattr__ handles representation names; returns __getattribute__ for attrs starting with '_' to prevent ...
- `01:32:24` ACTION: sed -n '1560,1620p' astropy/coordinates/baseframe.py && sed -n '1860,1920p' astropy/coordinates/base [...]
- `01:32:11` repro: accessing sc.someattr raised AttributeError 'descriptor raised'; traceback shows astropy/coordinates/sky_coordinate.py:857 in __getattr__ calli...
- `01:31:55` ACTION: python3 - <<'PY'
- `01:31:19` ACTION: grep -n "hasattr(self._sky_coord_frame" astropy/coordinates/*.py || true
- `01:31:04` sky_coordinate.py:820-940: __getattr__ checks for _sky_coord_frame, handles alias names, checks frame_transform_graph.frame_attributes and delegates t...
- `01:30:54` ACTION: sed -n '820,940p' astropy/coordinates/sky_coordinate.py
- `01:30:49` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `01:30:25` repro: inspect.getattr_static returned: <__main__.D object at 0x7fffff17cfd0>; hasattr(f, 'prop') -> False; getattr(f, 'prop') raised AttributeError: ...
- `01:30:25` sky_coordinate.py:832-906: __getattr__ checks '_sky_coord_frame' in __dict__; handles _is_name; checks frame_transform_graph.frame_attributes and dele...
- `01:28:28` Root cause: hasattr(self._sky_coord_frame, attr) returns False when a frame descriptor raises AttributeError (repro: getattr(f,'prop') raised 'descrip...
- `01:28:01` repro: AttributeError \"'Outer' object has no attribute 'prop'\"; descriptor-raised AttributeError was masked by hasattr
- `01:27:44` ACTION: python3 - <<'PY'
- `01:27:26` sky_coordinate.py:832-906: __getattr__/__setattr__/__delattr__ use hasattr(self._sky_coord_frame, attr) at lines 849,867,894; __getattr__ delegates fr...
- `01:27:08` ACTION: sed -n '832,906p' astropy/coordinates/sky_coordinate.py
- `01:27:03` grep hasattr(self._sky_coord_frame: astropy/coordinates/sky_coordinate.py:849,867,894
- `01:26:57` ACTION: grep -n "hasattr(self._sky_coord_frame" -R astropy || true
