# Project Goals

**Current Task:** Subclassed SkyCoord gives misleading attribute access message

<details>
<summary>Full description</summary>

Subclassed SkyCoord gives misleading attribute access message
I'm trying to subclass `SkyCoord`, and add some custom properties. This all seems to be working fine, but when I have a custom property (`prop` below) that tries to access a non-existent attribute (`random_attr`) below, the error message is misleading because it says `prop` doesn't exist, where it should say `random_attr` doesn't exist.

```python
import astropy.coordinates as coord


class custom_coord(coord.SkyCoord):
    @property
    def prop(self):
        return self.random_attr


c = custom_coord('00h42m30s', '+41d12m00s', frame='icrs')
c.prop
```

raises
```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    c.prop
  File "/Users/dstansby/miniconda3/lib/python3.7/site-packa...
</details>


**Current Task:** Subclassed SkyCoord gives misleading attribute access message

<details>
<summary>Full description</summary>

Subclassed SkyCoord gives misleading attribute access message
I'm trying to subclass `SkyCoord`, and add some custom properties. This all seems to be working fine, but when I have a custom property (`prop` below) that tries to access a non-existent attribute (`random_attr`) below, the error message is misleading because it says `prop` doesn't exist, where it should say `random_attr` doesn't exist.

```python
import astropy.coordinates as coord


class custom_coord(coord.SkyCoord):
    @property
    def prop(self):
        return self.random_attr


c = custom_coord('00h42m30s', '+41d12m00s', frame='icrs')
c.prop
```

raises
```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    c.prop
  File "/Users/dstansby/miniconda3/lib/python3.7/site-packa...
</details>


**Current Task:** Subclassed SkyCoord gives misleading attribute access message

<details>
<summary>Full description</summary>

Subclassed SkyCoord gives misleading attribute access message
I'm trying to subclass `SkyCoord`, and add some custom properties. This all seems to be working fine, but when I have a custom property (`prop` below) that tries to access a non-existent attribute (`random_attr`) below, the error message is misleading because it says `prop` doesn't exist, where it should say `random_attr` doesn't exist.

```python
import astropy.coordinates as coord


class custom_coord(coord.SkyCoord):
    @property
    def prop(self):
        return self.random_attr


c = custom_coord('00h42m30s', '+41d12m00s', frame='icrs')
c.prop
```

raises
```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    c.prop
  File "/Users/dstansby/miniconda3/lib/python3.7/site-packa...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create and run a minimal repro script that demonstrates misleading AttributeError for subclassed SkyCoord property
- [ ] 2. Locate __getattr__: search the testbed for __getattr__ implementations in sky_coordinate.py or similar files
- [x] 3. Root cause analysis: inspect the __getattr__ code to see how AttributeError is caught and re-raised and identify why the wrong attribute name is used
- [x] 4. Implement fix: modify __getattr__ to detect AttributeError from property access and re-raise with the correct missing attribute name (or re-raise original exception)
- [x] 5. Verify fix: run the repro script and existing tests to confirm the AttributeError message now refers to the actual missing attribute and that no other behavior regressed
- [x] 3. Root cause analysis: inspect _is_name and __getattr__ to see why a missing .name on _sky_coord_frame causes AttributeError before delegation
- [ ] 4. Propose fix: change _is_name to use getattr(self.frame,
- [ ] 5. Validate fix: implement change and run minimal repro to confirm AttributeError references missing attribute from property access, and run relevant tests
- [ ] 1. Modify _is_name in astropy/coordinates/sky_coordinate.py to use getattr(self.frame,
- [ ] 2. Edit astropy/coordinates/sky_coordinate.py to implement the change
- [ ] 3. Run targeted tests for coordinates to verify behavior (e.g., pytest -q astropy/coordinates/tests/test_sky_coord.py -q) and capture failures
- [ ] 4. Log file diff and test output, then mark the edit and tests TODOs complete
- [ ] 1. Clarify task/bug with user: request repository path, failing test name or exact error message, and exact steps to reproduce
- [ ] 2. Set up environment: clone/open repo, install dependencies, and ensure tests can be run locally
- [ ] 3. Reproduce the bug: run the provided repro script or failing test(s) and capture full traceback/output
- [ ] 4. Locate relevant code: grep for error keywords, find implicated files/functions, and inspect implementation
- [ ] 5. Implement & verify fix: make minimal code changes, add/adjust tests to cover the bug, run full test suite and document the change
- [ ] 1. Reproduce the bug: run the provided minimal repro script (e.g., python3 repro.py) to reproduce the misleading AttributeError for a subclassed SkyCoord
- [ ] 2. Run targeted tests: run pytest on coordinates tests to capture failing test(s) (e.g., pytest -q astropy/coordinates/tests/test_sky_coord.py)
- [ ] 3. Inspect code: open and review astropy/coordinates/sky_coordinate.py (around _is_name and __getattr__) to identify where AttributeError is generated and how it
- [ ] 4. Implement fix: modify __getattr__ (or related helpers) to avoid masking AttributeError from frame property access — consider re-raising original exception or using object.__getattribute__/descriptor checks
- [ ] 5. Add regression test & verify: add a test for the subclassed SkyCoord case, run tests, and ensure no regressions; then mark todos complete and commit changes
- [ ] 1. Reproduce the bug: run repro.py or the failing test(s) to capture the exact traceback and error message
- [ ] 2. Locate the code: grep for __getattr__, __getattribute__, and relevant descriptors in the codebase (e.g., astropy/coordinates/*.py) to find candidate files/functions
- [ ] 3. Root cause analysis: inspect the found implementations to identify where AttributeError is caught/re-raised incorrectly and list specific lines and behavior
- [ ] 4. Implement fix: modify the attribute-access logic to check descriptors/properties first and ensure the original missing-attribute name is preserved in exceptions; add a focused unit test reproducing the original failure
- [x] 5. Verify fix: run repro.py and the full test suite (or at least the affected tests), confirm the failing case is fixed, and document results
- [ ] 2. Locate the code: inspect discretize_model in astropy/convolution/utils.py lines ~120-180 to identify exact checks for x_range and y_range
- [ ] 3. Root cause analysis: determine why float(np.diff(x_range)).is_integer() triggers DeprecationWarning and choose robust replacement (e.g., use np.diff(x_range)[0] or explicit scalar extraction and tolerant integer check)
- [ ] 4. Implement fix: update checks to extract scalar diff = np.diff(x_range)[0] and use either float(diff).is_integer() or np.isclose(diff, round(diff)); apply same to y_range and run unit tests
- [ ] 5. Verify fix: run pytest for astropy/convolution tests (at least test_convolve_kernels.py) to ensure collection and tests pass
- [ ] 34. Run pytest for astropy/convolution tests to verify no regressions (pytest -q astropy/convolution/tests)
- [ ] 1. Reproduce the bug: create or run a minimal repro that demonstrates the error and capture the exact exception message and stack trace
- [ ] 2. Locate the code: search for relevant files and functions (e.g., __getattr__, descriptors, property accessors) that could cause the observed exception
- [ ] 3. Root cause analysis: inspect the located code paths, identify where exceptions are caught or re-raised, and determine why the wrong attribute/name is reported
- [ ] 4. Implement fix: modify code to handle descriptor/property errors correctly (e.g., check class descriptors first, avoid masking original AttributeError) and add unit tests covering the repro
- [ ] 5. Verify fix: run unit tests and the minimal repro, ensure original failing case is fixed and no regressions occur; document changes and mark TODOs complete
- [ ] 1. Reproduce the issue: obtain reproduction steps or failing test, capture full traceback, and run the failing test/script locally to reproduce the error
- [ ] 2. Locate the code: grep the repository for symbols from the traceback (e.g. function/class names) and common suspects like
- [ ] 3. Inspect & analyze root cause: open implicated files, read surrounding code, identify the exact cause (e.g. improper AttributeError handling or wrong attribute name in re-raise)
- [ ] 4. Implement fix & tests: make minimal code change to correct behavior, add unit test(s) that reproduce the bug and assert the correct behavior, and run the test(s)
- [ ] 5. Verify & finalize: run targeted failing tests then full test suite, log results with context_log, mark TODOs complete with context_todos --complete N and create a context_commit describing the fix
- [ ] 1. Understand the bug: reproduce AttributeError raised with incorrect/misleading message when accessing attributes via SkyCoord.__getattr__
- [ ] 2. Locate the code: open astropy/coordinates/sky_coordinate.py and find the __getattr__ implementation and related helper methods
- [ ] 3. Root cause analysis: inspect try/except blocks in __getattr__ to see where AttributeError is caught and how the error message/attribute name is constructed or lost
- [ ] 4. Implement fix: update __getattr__ so it preserves original AttributeError details (or raises AttributeError mentioning the actual missing attribute) and add unit tests for the message
- [ ] 5. Verify fix: run targeted tests (astropy/coordinates/tests/*) that assert AttributeError behavior and run pytest on sky_coordinate tests
- [ ] 3. Inspect baseframe __getattr__ at lines 1726 and 2025 to find try/except behavior
- [ ] 4. Read astropy/coordinates/baseframe.py around 1680-1760 and 1980-2060 to see exact code
- [ ] 5. Determine whether AttributeError raised by frame descriptors is being caught and replaced with a generic message
- [ ] 6. Implement fix: modify exception handling to preserve original AttributeError or only catch AttributeError from specific getattr calls
- [ ] 7. Run repro and relevant tests to verify the fix
- [ ] 8. Inspect astropy/coordinates/earth.py around 240-260 to see the except AttributeError and what it catches/re-raises
- [ ] 9. Determine whether the except AttributeError can catch descriptor/property AttributeError and thus mask original errors
- [ ] 10. Propose change: narrow exception scope or preserve original AttributeError (re-raise without new message)
- [ ] 11. Run repro/tests after change to verify descriptor AttributeError messages are preserved
- [ ] 1. Inspect astropy/coordinates/sky_coordinate.py: review _is_name and __getattr__ implementations to understand how attribute names are classified and why accessing .name might occur
- [ ] 2. Inspect astropy/coordinates/baseframe.py: review __getattr__ implementations to see how delegation to _sky_coord_frame is performed and where .name is accessed
- [ ] 3. Reproduce the issue: create a minimal repro where _sky_coord_frame lacks .name or where accessing .name raises AttributeError, and show that __getattr__ raises wrong AttributeError before delegation
- [ ] 4. Implement fix: change checks to safely detect missing .name (use getattr(..., None) or catch AttributeError from descriptor access and treat as missing) and update code accordingly
- [ ] 5. Verify fix: run the minimal repro and affected tests to ensure AttributeError chaining/behavior is correct and no regressions
- [ ] 2. Locate the problematic code: inspect _is_name and __getattr__ in astropy/coordinates/sky_coordinate.py (around lines 860-920) to confirm how frame.name is accessed
- [ ] 3. Reproduce the bug: create a minimal repro where a frame
- [ ] 4. Implement fix: modify _is_name to safely access self.frame.name (wrap getattr in try/except AttributeError) so descriptor-raised AttributeError does not escape
- [ ] 5. Verify fix: run the minimal repro and relevant tests to ensure AttributeError no longer leaks and behavior remains correct
- [ ] 4. Root cause analysis: investigate why getattr(self.frame,
- [ ] 5. Locate relevant code paths: inspect frame_transform_graph.lookup_name, frame.is_transformable_to, and frame attribute definitions on frame classes (frame_attributes, name handling)
- [ ] 6. Implement fix: modify _is_name to catch AttributeError from descriptor access and treat it as None; ensure __getattr__ probing of self.frame attributes also handles descriptor-raised AttributeError appropriately
- [ ] 7. Add tests: create a unit test that monkey-patches a frame class with a
- [ ] 8. Verify fix: run repro.py and relevant unit tests to confirm the bug is resolved
- [ ] 1. Reproduce the bug with the provided custom SkyCoord snippet (create repro.py in /testbed)
- [ ] 2. Locate the __getattr__ method in sky_coordinate.py under /testbed to find where AttributeError is raised
- [ ] 3. Root cause analysis: inspect __getattr__ exception handling to determine if it masks AttributeError from properties/descriptors
- [ ] 4. Implement fix: modify __getattr__ to avoid catching AttributeError raised by property/descriptors (let such errors propagate or re-raise original error)
- [ ] 5. Verify fix: run repro.py and any relevant tests to ensure the error message refers to the actual missing inner attribute, not the property name
- [ ] 1. Understand the bug: Investigate AttributeError raised by SkyCoord.__getattr__ (wrong/masked attribute errors or incorrect message)
- [ ] 2. Locate the code: Inspect astropy/coordinates/sky_coordinate.py around lines 860-960 to find __getattr__ implementation
- [ ] 3. Root cause analysis: Determine if __getattr__ is catching AttributeError from descriptors/properties and re-raising incorrectly
- [ ] 4. Implement fix: Modify __getattr__ to prioritize class descriptors and only raise AttributeError when attribute truly missing; add unit test reproducing the issue
- [ ] 5. Verify fix: Run coordinate-related tests and a minimal repro to confirm the AttributeError behavior is corrected
- [ ] 1. Understand the issue: determine how frame_transform_graph.frame_attributes are used and whether attribute descriptors
- [ ] 1. Reproduce the bug: run the provided repro script or failing test to capture the full traceback and identify the exact failing assertion or exception
- [ ] 2. Locate the code: search the repository for symbols and methods mentioned in the traceback (e.g.,
- [ ] 3. Root cause analysis: inspect the located implementations (open the surrounding source lines), identify where AttributeError is caught or masked, and determine why the wrong attribute name/message is produced
- [ ] 4. Implement fix: modify the implementation to avoid masking descriptor/property errors (e.g., check class descriptors first or preserve original AttributeError), update code with clear comment and add a minimal unit/regression test
- [ ] 5. Verify fix: run the repro and full test suite (pytest -q), confirm the regression test passes, and run linters/static checks before committing the change
- [ ] 1. Clarify task: Ask user for repository path, target branch, steps to reproduce, and expected vs actual behavior
- [ ] 2. Set up environment: Identify required files, tests, and dependencies to run locally
- [ ] 3. Reproduce the issue: Run provided reproduction steps or project test suite to capture errors
- [ ] 4. Locate problematic code: Grep for relevant symbols, open candidate files, and identify failing lines or exceptions
- [ ] 5. Root cause analysis: Trace stack, inspect related functions/attributes, and determine why the failure occurs
- [ ] 6. Implement fix: Modify code with minimal, well-documented change and add/adjust tests
- [ ] 7. Verify fix: Run unit tests, linters, and reproduce previously failing case to confirm resolution
- [ ] 8. Document and commit: Summarize the change, prepare commit message, and record any remaining follow-ups
- [ ] 1. Understand the bug: reproduce the issue by running the provided repro script (e.g. python3 repro.py) and capture the full traceback and environment (Python version, deps)
- [ ] 2. Locate the code: search repository for likely handlers (e.g. grep -n \
- [ ] 3. Root cause analysis: inspect the identified functions/files (sed -n to view ranges), add targeted prints or run under pdb to determine where AttributeError originates and whether descriptor errors are being caught incorrectly
- [ ] 4. Implement fix: modify the offending code to avoid swallowing descriptor AttributeError (adjust exception handling or check for descriptors), add a unit test reproducing the original failure, and run linters
- [ ] 5. Verify fix: run the repro script and full test suite (pytest -q), confirm the original traceback is resolved and error message/behavior is correct; then mark TODOs complete as each step finishes

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:46:03` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
- `01:46:03` TASK STARTED: Query syntax error with condition and distinct combination
- `01:38:35` ACTION: python3 --version && pip --version && python3 repro.py
- `01:38:07` ACTION: printf "Please provide the following so I can reproduce and fix the bug:\n\n1) Repository location a [...]
- `01:37:39` ACTION: grep -nR "__getattr__" . || true
- `01:37:31` <frozen importlib._bootstrap>:228: RuntimeWarning: numpy.ndarray size changed, may indicate binary incompatibility. Expected 80 from C header, got 96 ...
- `01:37:16` ACTION: pytest -q
- `01:36:05` ACTION: grep -R "frame_transform_graph" -n || true
- `01:36:00` grep hasattr(self._sky_coord_frame): astropy/coordinates/sky_coordinate.py: lines 889, 908, 935
- `01:35:54` ACTION: grep -n "hasattr(self._sky_coord_frame" astropy/coordinates/sky_coordinate.py || true
- `01:35:36` sky_coordinate.py:860-960: __getattr__ checks for _sky_coord_frame; if attr is an alias returns self; if attr in frame_transform_graph.frame_attribute...
- `01:35:17` ACTION: sed -n '860,960p' astropy/coordinates/sky_coordinate.py
- `01:35:01` ACTION: grep -nR "__getattr__" astropy || true
- `01:34:55` ACTION: ls -la
- `01:34:52` RESULT: grep: testbed: No such file or directory
- `01:34:52` ACTION: grep -nR "__getattr__" testbed || true
- `01:34:36` TASK STARTED: Subclassed SkyCoord gives misleading attribute access message
- `01:33:20` sky_coordinate.py: _is_name uses getattr(self.frame, 'name', None) (returns None if attribute access raises AttributeError); SkyCoord.__getattr__ dele...
- `01:32:46` ACTION: sed -n '840,920p' astropy/coordinates/sky_coordinate. [...]
- `01:32:34` grep: astropy/coordinates/baseframe.py:1726 def __getattr__(self, attr); astropy/coordinates/baseframe.py:2025 def __getattr__(self, name); astropy/co...
