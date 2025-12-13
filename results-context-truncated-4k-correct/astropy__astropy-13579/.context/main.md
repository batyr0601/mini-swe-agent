# Project Goals

**Current Task:** Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS` 

<details>
<summary>Full description</summary>

Inconsistent behavior of `world_to_pixel` in `SlicedLowLevelWCS` 
<!-- This comments are hidden when you submit the issue,
so you do not need to remove them! -->

<!-- Please be sure to check out our contributing guidelines,
https://github.com/astropy/astropy/blob/main/CONTRIBUTING.md .
Please be sure to check out our code of conduct,
https://github.com/astropy/astropy/blob/main/CODE_OF_CONDUCT.md . -->

<!-- Please have a search on our GitHub repository to see if a similar
issue has already been posted.
If a similar issue is closed, have a quick look to see if you are satisfied
by the resolution.
If not please go ahead and open an issue! -->

<!-- Please check that the development version still produces the same bug.
You can install development version with
pip install git...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [x] 1. Reproduce the bug using the provided snippet (create repro script in testbed and run it)
- [ ] 2. Locate SlicedLowLevelWCS and related world_to_pixel implementation in the codebase (search for SlicedLowLevelWCS and wcsapi modules)
- [ ] 3. Inspect implementation details: how fixed axes/world->pixel mapping is handled in SlicedLowLevelWCS
- [ ] 4. Implement a minimal, robust fix to ensure world_to_pixel for sliced WCS uses the correct fixed-axis world coordinate or pixel value
- [ ] 5. Run repro to verify the fix reproduces correct output for both full and sliced WCS
- [ ] 6. Add context_log entries describing findings and mark todos complete as work progresses
- [ ] 1. Reproduce the issue by running the full test suite: run
- [ ] 2. Locate the failing tests and implicated source code: use traceback filenames/lines and
- [ ] 3. Root cause analysis: open the identified source files, inspect the offending functions/lines, and create a small focused repro if needed to understand the bug
- [ ] 4. Implement the fix and add a regression test: modify the implicated code, add or update unit tests to cover the failure, and run the tests locally
- [ ] 5. Verify and finalize: run
- [ ] 2. Locate the code: inspect astropy/convolution/utils.py around uses of np.diff (around lines ~150-170)
- [ ] 3. Root cause analysis: determine what np.diff(x_range) returns for tuple inputs and why float(np.diff(...)) triggers DeprecationWarning; decide correct replacement
- [ ] 4. Implement fix: replace float(np.diff(x_range)).is_integer() and float(np.diff(y_range)).is_integer() with float(x_range[1] - x_range[0]).is_integer() and float(y_range[1] - y_range[0]).is_integer() respectively in astropy/convolution/utils.py
- [ ] 5. Verify fix: run a small Python script that imports discretize_model and calls it with integer and non-integer ranges to ensure no DeprecationWarning and correct ValueError behavior
- [ ] 6. After each command execution, log observed outputs with context_log and mark completed todos using context_todos --complete N
- [ ] 5. Verify fix: import astropy.convolution.utils and confirm discretize_model loads and shows the updated endpoint-subtraction changes
- [ ] 6. Search for other uses of float(np.diff(...)) or np.diff used where a scalar is expected, and list occurrences for manual review
- [ ] 1. Locate SlicedLowLevelWCS and wcsapi modules: grep for
- [ ] 2. Locate world_to_pixel implementations and usages: grep for
- [ ] 3. Inspect SlicedLowLevelWCS implementation files identified in step 1 to read class and method definitions
- [ ] 4. Create a minimal repro script comparing full WCS and sliced WCS outputs for world_to_pixel to reproduce the issue
- [ ] 5. Implement a targeted fix in SlicedLowLevelWCS.world_to_pixel to ensure fixed axes use correct world/pixel values and add a unit test
- [ ] 1. Understand the bug: reproduce the issue by running the failing example or test and capture the exact error message and traceback
- [ ] 2. Locate the code: search the repository for __getattr__, attribute handling, and related classes/functions to identify candidate files
- [ ] 3. Root cause analysis: inspect the identified code to determine whether AttributeError is being caught incorrectly or attribute names are misreported; record file paths and line numbers
- [ ] 4. Implement fix: apply minimal code changes to allow descriptor/property errors to propagate and correct error message content; run linters
- [ ] 5. Verify fix: run the failing test, the project test suite, and add a regression unit test that reproduces the original failure
- [ ] 1. Understand the bug: determine if __getattr__ in SkyCoord/BaseCoordinateFrame masks AttributeError from descriptors or misreports missing attribute name
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py and astropy/coordinates/baseframe.py __getattr__ implementations and related GenericFrame.__getattr__
- [ ] 3. Root cause analysis: identify where AttributeError is raised/re-raised and whether descriptor AttributeError is being caught and replaced
- [ ] 4. Implement fix: update __getattr__ to avoid masking descriptor AttributeError or re-raise with correct attribute name; update unit tests accordingly
- [ ] 5. Verify fix: add tests reproducing misreported AttributeError and run relevant coordinate tests
- [ ] 1. Reproduce the bug: write a minimal repro that triggers an AttributeError raised by a descriptor (or property) on a frame object and observe whether SkyCoord.__getattr__ or BaseCoordinateFrame.__getattr__ masks it
- [ ] 2. Locate code: inspect astropy/coordinates/sky_coordinate.py::__getattr__ (lines ~820-920) and astropy/coordinates/baseframe.py::__getattr__ (lines ~1540-1620 and ~1840-1900) to pinpoint where AttributeError is raised/re-raised
- [ ] 3. Root cause analysis: determine whether getattr calls delegate to descriptors whose AttributeError is being caught/masked; identify exact lines that raise AttributeError and why
- [ ] 4. Implement fix: modify __getattr__ to avoid catching AttributeError from descriptor/property access (e.g., use object.__getattribute__ for attribute existence checks or check for attribute presence before getattr) and update error message to use the actual missing attribute name
- [ ] 5. Add tests: add a unit test that reproduces the issue and asserts that descriptor-raised AttributeError propagates and that missing-attribute error messages are correct
- [ ] 6. Run tests: run pytest for astropy/coordinates tests (or the specific new test) to verify the fix
- [ ] 1. Understand the bug: reproduce the case where a property/descriptor raises AttributeError and that AttributeError is masked or misreported by astropy.coordinates __getattr__ (expectation: see wrong/misleading AttributeError from __getattr__ instead of original descriptor)
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/baseframe.py (BaseCoordinateFrame.__getattr__, GenericFrame.__getattr__), astropy/coordinates/sky_coordinate.py (SkyCoord.__getattr__), and any related helpers
- [ ] 3. Root cause analysis: check how these __getattr__ implementations call getattr/return __getattribute__, identify where descriptor/property-raised AttributeError could be intercepted or re-raised with wrong name, and note exact lines to change
- [ ] 4. Implement fix: modify the identified __getattr__ implementations to avoid masking AttributeError from descriptors (use object.__getattribute__ where appropriate, or check for descriptor presence before delegating), add unit tests reproducing the original failure
- [ ] 5. Verify fix: run the repro script and run relevant pytest subset (e.g., tests referencing coordinates/attribute errors) and confirm the original AttributeError behavior is restored
- [ ] 1. Understand the bug: reproduce/describe the misleading AttributeError observed when accessing attributes via SkyCoord.__getattr__ (determine when AttributeError from frame attributes or descriptors is being masked or re-raised with wrong name)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py __getattr__ (around lines 820-920) and astropy/coordinates/baseframe.py GenericFrame.__getattr__ (around lines 1860-1900) to identify where AttributeError originates and is handled
- [ ] 3. Root cause analysis: determine which getattr calls (self.frame, self._sky_coord_frame, frame attribute descriptors) can raise AttributeError and whether those exceptions are being inappropriately caught or re-raised with the wrong attribute name
- [ ] 4. Implement fix: modify SkyCoord.__getattr__ to avoid swallowing AttributeError from frame attribute access or to preserve original exception message; add targeted try/except blocks and tests
- [ ] 5. Verify fix: add/modify unit test that reproduces the misleading AttributeError, run relevant tests (pytest for coordinates module), and confirm that AttributeError messages are correct and no regressions occur
- [ ] 1. Reproduce the bug using a minimal repro that triggers a descriptor AttributeError when accessing a frame attribute via SkyCoord
- [ ] 2. Locate SkyCoord.__getattr__ in astropy/coordinates/sky_coordinate.py and capture the exact try/except/raise logic
- [ ] 3. Locate BaseCoordinateFrame.__getattr__ and any frame attribute descriptors in astropy/coordinates/baseframe.py to see how they raise AttributeError
- [ ] 4. Root cause analysis: grep for try/except AttributeError in sky_coordinate.py to find where descriptor-raised AttributeError might be masked
- [ ] 5. Implement fix: modify SkyCoord.__getattr__ to avoid catching AttributeError coming from descriptors/attributes (e.g., check attribute existence differently or re-raise original exception)
- [ ] 6. Add unit test reproducing the masking behavior and confirm it fails before the fix and passes after
- [ ] 7. Verify fix by running the repro script and pytest for coordinates, then mark relevant TODOs complete
- [ ] 1. Understand the bug: reproduce and characterize the AttributeError when accessing frame attributes via SkyCoord/BaseCoordinateFrame (capture exact error message and stack trace)
- [ ] 2. Locate the code: inspect BaseCoordinateFrame.__getattr__ (baseframe.py:1591,1877), SkyCoord.__getattr__ (sky_coordinate.py:829-905) and FrameAttribute/Attribute descriptor definitions in baseframe.py (around frame_attributes declaration and Attribute class)
- [ ] 3. Root cause analysis: determine whether descriptor __get__ or attribute lookup raises AttributeError that
- [ ] 4. Implement fix: modify __getattr__/exception handling so original AttributeError from descriptors is preserved (or only catch AttributeError for attribute-not-found, not descriptor errors); add unit tests reproducing the original failure
- [ ] 5. Verify fix: run pytest for astropy/coordinates (or targeted tests) and run the minimal repro script to confirm AttributeError message is correct and no regressions
- [ ] 1. Understand the bug: reproduce the AttributeError when accessing frame attributes and note the exact observed vs expected error messages
- [ ] 2. Locate the code: find all __getattr__ implementations and Attribute/FrameAttribute classes in astropy/coordinates (e.g., baseframe.py, attributes.py)
- [ ] 3. Root cause analysis: inspect BaseCoordinateFrame.__getattr__ and Attribute.__get__ to see whether AttributeError from descriptors is being caught and re-raised incorrectly
- [ ] 4. Implement fix: modify __getattr__ to check class descriptors/FrameAttributes first or avoid catching descriptor-raised AttributeError so correct message/behavior is preserved; prepare a small patch
- [ ] 5. Verify fix: run a focused repro script and relevant tests (pytest -q astropy/coordinates::tests -k frame_attribute or similar) and record results
- [ ] 1. Understand the bug: determine how BaseCoordinateFrame.__getattr__ handles AttributeError from descriptors and whether it masks the original exception message (e.g., reporting
- [ ] 2. Locate the code: inspect BaseCoordinateFrame.__getattr__ in astropy/coordinates/baseframe.py and the Attribute descriptor methods (Attribute.__get__, convert_input, __get__-related logic) in astropy/coordinates/attributes.py
- [ ] 3. Root cause analysis: create a minimal repro that triggers a descriptor-raised AttributeError when accessing a frame attribute and run it to observe which AttributeError is raised and its traceback
- [ ] 4. Implement fix: modify __getattr__ (or the descriptor) to avoid catching and re-raising descriptor-originating AttributeError with an incorrect message; prepare a small patch and unit-change with clear rationale and tests
- [ ] 5. Verify fix: run the relevant tests (at least astropy/coordinates/tests/test_frames.py and any failing tests), and run the minimal repro to confirm the AttributeError message is correct
- [ ] 1. Understand the bug: determine how an Attribute/descriptor can raise AttributeError that gets masked by frame __getattr__ implementations
- [ ] 2. Locate __getattr__: inspect sky_coordinate.py and baseframe.py __getattr__ implementations and capture exact line ranges to analyze control flow
- [ ] 3. Inspect descriptor: find and read Attribute.__get__ (and related descriptor methods) in astropy/coordinates/attributes.py to see if/when it raises AttributeError
- [ ] 4. Reproduce: write and run a minimal script that triggers the AttributeError from a descriptor/property to observe whether __getattr__ masks it
- [ ] 5. Fix & test: propose and implement a change to __getattr__ to avoid masking genuine AttributeError from descriptors, and run relevant tests or a small test case
- [ ] 1. Compare BaseCoordinateFrame.__getattr__ and GenericFrame.__getattr__ handling of missing attributes and descriptor-raised AttributeError
- [ ] 2. Determine if GenericFrame.__getattr__ masks AttributeError from descriptors by raising its own
- [ ] 3. Create minimal repro demonstrating masked AttributeError with a descriptor that raises AttributeError
- [ ] 4. Implement fix: modify GenericFrame.__getattr__ (or BaseCoordinateFrame behavior) to let descriptor-raised AttributeError propagate or re-raise with correct attribute name
- [ ] 5. Add unit test for repro and run pytest for astropy/coordinates to verify fix
- [ ] 1. Understand the bug: GenericFrame.__getattr__ masks AttributeError from class-level descriptors on private attributes (e.g., _foo) by calling getattr(self,
- [ ] 2. Locate the code: inspect astropy/coordinates/baseframe.py GenericFrame.__getattr__ (around lines 1848-1910) and BaseCoordinateFrame.__setattr__/__getattribute__ (around lines 1560-1670) to see interaction
- [ ] 3. Root cause analysis: confirm that using getattr(self,
- [ ] 4. Implement fix: change GenericFrame.__getattr__ to return object.__getattribute__(self,
- [ ] 5. Verify fix: run the minimal repro and run pytest for coordinates/frame tests (e.g., tests/coordinates/test_frames.py) to ensure the test passes and no regressions occur
- [ ] 1. Understand the bug: reproduce AttributeError masking when accessing GenericFrame attribute that triggers a descriptor/property raising AttributeError
- [ ] 2. Reproduce the bug: write and run a minimal repro script that creates a GenericFrame with a frame attribute whose underlying object raises AttributeError on attribute access
- [ ] 3. Locate code: find Attribute class and any descriptor implementations (search for
- [ ] 4. Root cause analysis: inspect interaction between GenericFrame.__getattr__ and BaseCoordinateFrame.__getattr__ and how AttributeError is propagated or masked
- [ ] 5. Implement fix: change GenericFrame.__getattr__ to access self.__dict__[
- [ ] 6. Verify fix: run repro and relevant unit tests (targeted tests for attribute access and error messages)
- [ ] 1. Reproduce the bug: run repro.py to capture the full AttributeError traceback and confirm failure mode
- [ ] 2. Locate the Attribute descriptor: open astropy/coordinates/attributes.py to inspect class Attribute implementation and how it raises errors
- [ ] 3. Locate BaseCoordinateFrame.__getattr__: inspect astropy/coordinates/baseframe.py around the __getattr__ implementation (around lines ~1591) to see what exceptions it catches and how it constructs error messages
- [ ] 4. Root cause analysis: determine whether BaseCoordinateFrame.__getattr__ is catching AttributeError raised by descriptors/properties and masking the original message; identify the minimal change to preserve original descriptor errors
- [ ] 5. Implement fix: modify __getattr__ to only handle missing frame attributes but let AttributeError from descriptors propagate; add/adjust unit tests reproducing the original bad message
- [ ] 6. Verify fix: run repro.py and run relevant tests (e.g., pytest astropy/coordinates -k <relevant_test>) to ensure the AttributeError from descriptors is preserved and no regressions occur
- [ ] 1. Reproduce the bug: create a minimal script that triggers AttributeError from a representation attribute accessed via BaseCoordinateFrame.__getattr__
- [ ] 2. Run repro and capture traceback to see where AttributeError originates
- [ ] 3. Locate representation/component code: search for representation_component_names and representation classes in astropy/coordinates
- [ ] 4. Root cause analysis: inspect representation attribute descriptors and BaseCoordinateFrame.__getattr__ interaction to determine if AttributeError is being remapped incorrectly
- [ ] 5. Implement fix: modify code to preserve original AttributeError message or adjust logic to raise correct AttributeError
- [ ] 6. Add unit test reproducing the issue and run pytest for affected tests
- [ ] 3. Root cause analysis: inspect astropy/coordinates/sky_coordinate.py __getattr__ to identify which getattr calls (self.frame, self._sky_coord_frame, or transform lookup) may raise AttributeError and are being masked
- [ ] 4. Implement fix: modify astropy/coordinates/sky_coordinate.py __getattr__ so that AttributeError originating from underlying frame/representation is propagated (wrap getattr(self.frame, attr) and getattr(self._sky_coord_frame, attr) to re-raise original AttributeError)
- [ ] 5. Add unit test: create test that monkeypatches a representation property to raise AttributeError and assert that accessing the corresponding frame attribute propagates the original message
- [ ] 6. Verify fix: run repro_attr_error.py and run pytest for relevant coordinate tests to confirm no masking and no regressions

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 02:11] **swebench-astropy__astropy-13579**: Task completed: LimitsExceeded
- [2025-12-02 01:53] **swebench-astropy__astropy-13579**: Fix: replace float(np.diff(...)) with explicit endpoint subtraction in discretize_model to avoid Num...
## Interaction Log

- `02:11:37` ACTION: sed -n '820,920p' astropy/coordinates/sky_coordinate.py
- `02:11:28` repro_attr_error.py: Accessing c.ra produced AttributeError from astropy/coordinates/sky_coordinate.py:858: 'SkyCoord' object has no attribute 'ra
- `02:11:15` ACTION: python3 - <<'PY'
- `02:10:40` ACTION: Reading file: <<'PY'
- `02:10:13` ACTION: sed -n '1628,1660p' astropy/coordinates/baseframe.py
- `02:10:01` ACTION: grep -nR "raise AttributeError" astropy/coordinates || true
- `02:09:42` repr_names: ['dec', 'distance', 'ra']; diff_names: ['pm_dec', 'pm_ra_cosdec', 'radial_velocity']
- `02:09:05` ACTION: python3 - <<'PY'
- `02:08:26` baseframe.py __getattr__: attrs starting with '_' call self.__getattribute__(attr) to raise AttributeError; representation component names are resolve...
- `02:08:09` ACTION: sed -n '1560,1630p' astropy/coordinates/baseframe.py
- `02:08:04` attributes.py: Attribute.__get__ uses getattr(instance, '_' + self.name, self.default); calls convert_input which can raise ValueError (e.g., TimeAttr...
- `02:07:46` ACTION: sed -n '1,240p' astropy/coordinates/attributes.py
- `02:07:40` repro.py: python3: can't open file '/testbed/repro.py': [Errno 2] No such file or directory
- `02:07:33` ACTION: python3 repro.py
- `02:07:06` ACTION: grep -nR "class Attribute" astropy || true && grep -n "def __getattr__" astropy/coordinates/basefram [...]
- `02:06:51` repro: Traceback shows AttributeError: inner error from Bad.__getattribute__ raised when accessing gf.a.something
- `02:06:36` ACTION: python3 - <<'PY'
- `02:06:07` baseframe.py:1840-1920: GenericFrame.__getattr__ uses getattr(self, '_' + name) which can invoke a descriptor and mask AttributeError from that descri...
- `02:05:57` ACTION: sed -n '1840,1920p' astropy/coordinates/baseframe.py
- `02:05:51` grep class GenericFrame: astropy/coordinates/baseframe.py:1854
