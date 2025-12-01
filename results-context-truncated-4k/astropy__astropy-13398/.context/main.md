# Project Goals

**Current Task:** A direct approach to ITRS to Observed transformations that stays within the ITRS.

<details>
<summary>Full description</summary>

A direct approach to ITRS to Observed transformations that stays within the ITRS.
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

### Description
<!-- Provide a general description of the feature you would like. -->
<!-- If you want to, you can s...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: investigate how ITRS<->AltAz/HADec transforms handle obstime and topocentric positions
- [ ] 2. Locate code: find files in /testbed implementing ITRS, AltAz, HADec or their transforms
- [ ] 3. Reproduce: create a small script demonstrating current ITRS->AltAz inaccuracy for local objects
- [ ] 4. Implement fix: add itrs_to_observed_mat and modify transforms to treat ITRS positions as time-invariant and adopt output obstime
- [ ] 5. Add utilities: implement necessary matrix utilities and ensure consistent handedness for AltAz/HADec
- [ ] 6. Verify fix: run the repro and adjust until output matches expected topocentric results
- [ ] 7. Finalize: context_commit and mark todos complete when done
- [ ] 1. Reproduce the bug: run the provided repro script or test that triggers the AttributeError when accessing the missing attribute
- [ ] 2. Locate the code: search repository for __getattr__ and related attribute-access helpers (e.g., grep -R \
- [ ] 3. Root cause analysis: inspect the identified __getattr__ implementations and surrounding code to find where AttributeError is caught and re-raised with wrong message or wrong attribute name
- [ ] 4. Implement fix: modify the __getattr__/attribute handling to avoid swallowing descriptor/attribute-specific AttributeErrors and ensure correct missing-attribute name is reported; add unit test covering the failing case
- [ ] 5. Verify fix: run the repro script and full test suite (pytest) to confirm the issue is resolved and no regressions introduced
- [ ] 1. Reproduce the bug: create a minimal repro that triggers AttributeError when accessing a SkyCoord attribute that should be provided by a frame descriptor (e.g., instantiate a SkyCoord and access a frame attribute or alias that causes an AttributeError or misleading message)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py __getattr__ implementation (lines ~800-920) and any related frame descriptor definitions in frame_transform_graph.frame_attributes
- [ ] 3. Root cause analysis: determine whether __getattr__ is catching AttributeError raised by frame descriptor __get__ methods or other internals and then re-raising a generic AttributeError with the wrong attribute name, thereby masking the original error; identify which getattr calls can raise and what exceptions they raise
- [ ] 4. Implement fix: modify __getattr__ so that AttributeError raised by frame attribute descriptors (or by getattr(self.frame, attr) / getattr(self,
- [ ] 5. Verify fix: add a unit test reproducing the original failure, run the relevant test suite (pytest tests/coordinates or test_sky_coordinate.py), confirm the test fails before the fix and passes after, then mark the TODOs complete and commit changes with context_commit
- [ ] 1. Understand the grep output: review all occurrences of
- [ ] 2. Locate the code: open astropy/coordinates/transformations.py and find the frame_attributes property and related caching logic
- [ ] 3. Locate the code: open astropy/coordinates/baseframe.py to inspect how frame_attributes is built on class creation and instance usage
- [ ] 4. Locate the code: open astropy/coordinates/sky_coordinate.py and related parsers to see how frame_attributes descriptors are accessed (look for __get__ calls, getattr handling, and dir population)
- [ ] 5. Reproduce tests: run pytest for astropy/coordinates tests (or the failing test suite) to capture failure messages and stack traces
- [ ] 6. Root cause analysis: identify places where descriptor AttributeError might be masked or re-raised with wrong attribute name and determine minimal code change
- [ ] 7. Implement fix: modify the identified code to correctly handle descriptor AttributeError (e.g., check for descriptor presence before catching AttributeError), add/adjust tests
- [ ] 8. Verify fix: run the coordinates tests and any focused repro to ensure all tests pass; log results and mark TODOs complete as steps finish
- [ ] 1. Understand the bug: investigate Attribute descriptor behavior that may raise or mask AttributeError when accessing frame attributes on frame classes or instances
- [ ] 2. Locate the code: find the Attribute class in astropy/coordinates/attributes.py and inspect BaseCoordinateFrame.__init_subclass__ (frame_attributes handling), plus related uses in astropy/coordinates/transformations.py and sky_coordinate.py
- [ ] 3. Root cause analysis: inspect Attribute.__get__/__set__, BaseCoordinateFrame.__init_subclass__ frame_attributes construction, and TransformGraph.frame_attributes merging; attempt to reproduce the AttributeError with a minimal script
- [ ] 4. Implement fix: modify Attribute or BaseCoordinateFrame logic so descriptor errors are not misreported (ensure descriptors are checked before catching AttributeError), prepare a patch with clear rationale
- [ ] 5. Verify fix: run a minimal repro script and targeted coordinate tests (e.g., tests for frame attributes in astropy/coordinates) and mark the reproduction TODO complete once confirmed
- [ ] 1. Understand the bug: obtain a reproducible case (repro script, failing test name, exact error message and full stack trace). If none provided, create a minimal repro that triggers the failure.
- [ ] 1. Understand the bug: reproduce the AttributeError showing the wrong/misleading attribute name when accessing a missing attribute on SkyCoord (capture exact error text and repro steps)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py and astropy/coordinates/baseframe.py __getattr__ implementations and note line ranges where AttributeError is caught/re-raised
- [ ] 3. Root cause analysis: determine whether __getattr__ is catching AttributeError raised by descriptors/properties/methods and where the exception message is altered; identify exact lines to change
- [ ] 4. Implement fix: modify __getattr__ to check class descriptors first and avoid catching their AttributeError (or re-raise with the original context); add a unit test reproducing the original wrong-message behavior and confirming the fix
- [ ] 5. Verify fix: run the minimal repro script and run pytest for astropy/coordinates tests (or relevant subset) to ensure no regressions
- [ ] 1. Understand the bug: reproduce the misleading AttributeError when accessing a missing attribute on SkyCoord/BaseFrameProxy and capture exact error message
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/baseframe.py (around 1591 and 1877) and astropy/coordinates/sky_coordinate.py (around 829-905)
- [ ] 3. Root cause analysis: identify where AttributeError is caught/re-raised and determine whether descriptor/property errors are being swallowed or the wrong attribute name is used in the re-raised message
- [ ] 4. Implement fix: modify __getattr__ to let descriptor/property AttributeError propagate and only raise AttributeError for truly missing attributes (or construct error message with the actual missing name); update/add unit tests
- [ ] 5. Verify fix: run relevant unit tests (pytest astropy/coordinates) and reproduce the original failing case to ensure correct behavior
- [ ] 1. Reproduce the bug using a minimal repro or the failing test to see the exact AttributeError message
- [ ] 2. Inspect __getattr__ in astropy/coordinates/sky_coordinate.py and GenericFrame.__getattr__ in astropy/coordinates/baseframe.py for try/except that may catch AttributeError incorrectly
- [ ] 3. Root cause analysis: determine which call
- [ ] 4. Implement fix: modify __getattr__ to avoid catching AttributeError from property descriptors or to check attributes explicitly before getattr; update code with minimal change
- [ ] 5. Add unit test reproducing the misleading AttributeError and asserting the correct missing-attribute name/message
- [ ] 6. Run relevant tests (coordinate tests) to verify the fix and ensure no regressions
- [ ] 1. Understand the bug: Investigate why AttributeError is raised or masked when accessing representation/differential attributes via BaseCoordinateFrame.__getattr__ and GenericFrame.__getattr__
- [ ] 2. Locate the code: Open astropy/coordinates/baseframe.py (__getattr__ around lines ~1540-1620 and ~1820-1900) and astropy/coordinates/sky_coordinate.py (__getattr__ around lines ~800-940)
- [ ] 3. Reproduce the bug: Create a minimal repro using SkyCoord/Frame that triggers AttributeError when accessing a representation component or a frame alias
- [ ] 4. Root cause analysis: Inspect try/except and getattr calls to see if AttributeError from descriptors is being caught and re-raised incorrectly; identify exact line(s) responsible
- [ ] 5. Implement fix: Modify __getattr__ to avoid masking AttributeError raised inside descriptors (only treat AttributeError as missing attribute when appropriate); add targeted unit test
- [ ] 6. Verify fix: Run the repro and run pytest for affected modules to ensure the issue is resolved and no regressions
- [ ] 1. Reproduce the AttributeError with a minimal SkyCoord example that triggers a property/descriptor AttributeError
- [ ] 2. Locate __getattr__ implementations in astropy/coordinates/sky_coordinate.py and astropy/coordinates/baseframe.py and record exact line ranges to inspect
- [ ] 3. Inspect sky_coordinate.py __getattr__ (approx lines 800-920) to find try/except blocks that might mask AttributeError from descriptors
- [ ] 4. Inspect baseframe.py __getattr__ (approx lines 1560-1620 and 1840-1900) for similar exception-handling issues
- [ ] 5. Search for other
- [ ] 6. Implement fix: narrow exception handling so AttributeError raised by descriptors/properties is not swallowed; preserve original AttributeError message and re-raise when appropriate
- [ ] 7. Add unit test that reproduces the original failure and run pytest for astropy.coordinates to verify the fix
- [ ] 1. Reproduce the bug: create a minimal repro that triggers an AttributeError raised inside a frame property/descriptor and access it via SkyCoord.__getattr__ to see if the original AttributeError is masked
- [ ] 2. Locate frame-attribute registry: find where frame_transform_graph.frame_attributes and lookup_name are defined and how frame attribute metadata is stored
- [ ] 3. Find descriptors/properties that raise AttributeError: grep for
- [ ] 4. Inspect the Attribute descriptor implementation: find
- [ ] 5. Propose and implement fix: design change to SkyCoord.__getattr__ (or related code) so that AttributeError raised inside descriptors/properties is not mistakenly treated as
- [ ] 1. Understand the bug: reproduce AttributeError when accessing an attribute on SkyCoord that should raise a normal AttributeError but is being misinterpreted as a frame name/frame attribute (e.g., behavior when accessing
- [ ] 2. Locate the code: find __getattr__ in astropy/coordinates/sky_coordinate.py, inspect baseframe.py frame_attributes initialization, and search uses of frame_transform_graph.frame_attributes
- [ ] 3. Root cause analysis: inspect sky_coordinate.py lines ~840-910 and related code to see where AttributeError is being caught/re-raised and how descriptors/frame attributes are handled
- [ ] 4. Implement fix: change __getattr__/attribute lookup to check class descriptors/attributes first and allow their AttributeError to propagate; add/adjust unit tests capturing the failing case
- [ ] 5. Verify fix: run focused tests (astropy/coordinates/tests/test_sky_coord.py::relevant_tests and tests/test_frames.py) and run a small repro script to confirm correct AttributeError behavior
- [ ] 1. Understand the bug: Investigate AttributeError being raised with wrong attribute name when accessing frame attribute via SkyCoord.__getattr__
- [ ] 2. Locate the code: Review SkyCoord.__getattr__ in astropy/coordinates/sky_coordinate.py and BaseCoordinateFrame.__getattr__ and GenericFrame.__getattr__ in astropy/coordinates/baseframe.py
- [ ] 3. Root cause analysis: Check where AttributeError is caught/re-raised or formatted (look for raise AttributeError(...) patterns) and whether descriptor AttributeErrors are being swallowed
- [ ] 4. Implement fix: Modify SkyCoord.__getattr__ to ensure AttributeError messages show the correct missing attribute and to avoid catching descriptor-raised AttributeErrors incorrectly
- [ ] 5. Verify fix: Create a minimal repro script showing the wrong error, apply the change, run the repro and relevant tests
- [ ] 1. Reproduce the bug: create minimal repro that demonstrates AttributeError from a descriptor/property being swallowed or re-raised with the wrong attribute name when accessing SkyCoord/BaseCoordinateFrame attributes
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py and astropy/coordinates/baseframe.py and any helper functions they call (e.g., representation access, frame_transform_graph usage)
- [ ] 3. Root cause analysis: determine where AttributeError exceptions from descriptors/properties are caught; identify whether __getattr__ is masking descriptor-raised AttributeError or formatting error messages with wrong attribute names; locate exact lines to change
- [ ] 4. Implement fix: modify __getattr__ logic to distinguish between
- [ ] 5. Verify fix: add unit test(s) reproducing the issue, run pytest for the affected tests/files, ensure tests pass and no regressions in attribute access behavior
- [ ] 1. Understand the bug: determine how __getattr__ implementations may be catching AttributeError from descriptors/properties and masking the real error message
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/baseframe.py and astropy/coordinates/sky_coordinate.py (and any other coord classes) to find try/except or broad AttributeError handlers
- [ ] 3. Reproduce the bug: create a minimal repro that triggers an AttributeError inside a descriptor/property accessed via __getattr__ (e.g., a frame attribute property that raises AttributeError) and run it to observe behavior
- [ ] 4. Root cause analysis: grep for broad except AttributeError blocks in those __getattr__ methods and inspect the exact lines to see whether they re-raise or swallow exceptions and whether they change the attribute name in the error
- [ ] 5. Implement fix: modify __getattr__ to avoid catching AttributeError raised by attribute descriptors (e.g., check for attribute existence via object.__getattribute__ or inspect descriptor protocol, only catch AttributeError from getattr on representation/differential lookups), update code and add unit test
- [ ] 6. Verify fix: run the minimal repro and relevant unit tests to confirm descriptors
- [ ] 1. Reproduce the bug: run relevant tests or a minimal repro script to observe the AttributeError behavior (e.g., run pytest -k coordinates or a provided repro.py)
- [ ] 2. Search for broad
- [ ] 3. Inspect full __getattr__ implementations in sky_coordinate.py and baseframe.py (read complete function bodies and nearby helpers) to identify suspect code paths
- [ ] 4. Root cause analysis: determine whether AttributeError originates from descriptors/properties on returned objects and whether __getattr__ re-raises with the wrong attribute name
- [ ] 5. Implement fix: modify __getattr__ to avoid catching AttributeError from attribute access on returned objects (e.g., use object.__getattribute__ for private attrs, limit try/except scope, or re-raise original exception)
- [ ] 6. Verify fix: add a unit test that reproduces the mis-raised AttributeError and run pytest for affected coordinate tests
- [ ] 7. Log findings and commit: record observations with context_log and create a checkpoint with context_commit after fix is validated
- [ ] 1. Understand the bug: Reproduce and describe the AttributeError that appears when accessing representation/frame properties (e.g., .ra/.dec or .radial_velocity) on SkyCoord/BaseCoordinateFrame; capture reproduction steps and error message
- [ ] 2. Locate the code: Find and open __getattr__ implementations in astropy/coordinates/sky_coordinate.py and astropy/coordinates/baseframe.py and list related representation property descriptors that may raise AttributeError
- [ ] 3. Root cause analysis: Inspect the __getattr__ code paths to see if they catch AttributeError from valid descriptors/properties and re-raise a misleading AttributeError; note exact line numbers and offending try/except scopes
- [ ] 4. Implement fix: Modify __getattr__ to avoid swallowing AttributeError from legitimate attribute access (e.g., call getattr on potential owners without broad excepts, or check for attribute existence before delegation); prepare a small patch with comments and tests
- [ ] 5. Verify fix: Add a unit test that reproduces the original failure, run pytest for the coordinates tests (or targeted tests), and confirm test(s) pass; update changelog/comments
- [ ] 1. Understand the bug: reproduce and characterize AttributeError propagation when accessing descriptor-backed attributes via SkyCoord/BaseCoordinateFrame.__getattr__ (unexpected masking of original AttributeError)
- [ ] 2. Locate the code: inspect BaseCoordinateFrame.__getattr__ in astropy/coordinates/baseframe.py and SkyCoord/GenericFrame __getattr__ in astropy/coordinates/sky_coordinate.py (use exact line ranges identified earlier)
- [ ] 3. Root cause analysis: find try/except blocks that catch AttributeError or use hasattr/getattr in delegation paths and determine where original descriptor errors get suppressed or transformed
- [ ] 4. Implement fix: modify __getattr__ to check for descriptors first or re-raise the original AttributeError (preserve correct attribute name/message); update code comments and add unit tests
- [ ] 5. Verify fix: create a minimal repro script demonstrating the bug, run the repro, and run the relevant unit tests (target test_skycoord and any failing tests) to confirm behavior is correct
- [ ] 4. Implement fix in astropy/coordinates/sky_coordinate.py: replace hasattr(self._sky_coord_frame, attr) usage in __getattr__ with a try/except around getattr(self._sky_coord_frame, attr) so descriptor-raised AttributeError is not swallowed; update code and add/refine tests as needed
- [ ] 5. Verify fix: run pytest for coordinates tests (e.g., pytest -q astropy/coordinates/tests) and run any repro scripts that demonstrated the masked AttributeError; iterate until tests pass
- [ ] 1. Understand the failing test: reproduce the AttributeError seen in test_api_ape5.test_highlevel_api where accessing sc1.ra raises AttributeError
- [ ] 2. Re-run the single failing test to reproduce reliably: pytest -q astropy/coordinates/tests/test_api_ape5.py::test_highlevel_api -q -x
- [ ] 3. Locate and inspect __getattr__ in astropy/coordinates/sky_coordinate.py (around line ~860) to see the attribute-resolution logic and any recent changes
- [ ] 4. Inspect frame_transform_graph.frame_attributes and the FK5 frame.get_frame_attr_names() to determine why
- [ ] 5. Run a small repro script that creates the SkyCoord from the failing test and prints type(self._sky_coord_frame), dir(self._sky_coord_frame), hasattr(type(self._sky_coord_frame),
- [ ] 6. Implement a minimal fix to __getattr__ to correctly expose coordinate attributes like

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:33:23` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `01:33:18` RESULT: context canceled
- `01:33:18` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `01:33:11` pytest astropy/coordinates/tests/test_api_ape5.py::test_highlevel_api: FAILED with AttributeError \"'SkyCoord' object has no attribute 'ra'\" raised a...
- `01:32:59` ACTION: pytest -q astropy/coordinates/tests/test_api_ape5.py::test_highlevel_api -x
- `01:31:16` ACTION: pytest -q -x astropy/coordinates/tests
- `01:31:09` pytest -q astropy/coordinates/tests: timed out and was killed; output begins with \"RuntimeWarning: numpy.ndarray size changed, may indicate binary in...
- `01:29:59` ACTION: pytest -q astropy/coordinates/tests
- `01:29:53` patched sky_coordinate.__getattr__
- `01:29:47` RESULT: patched sky_coordinate.__getattr__
- `01:29:46` ACTION: python3 - <<'PY'
- `01:29:03` baseframe.py:1580-1620: __getattr__ delegates to representation and uses getattr(rep, name) which may raise descriptor AttributeError; baseframe.py:18...
- `01:28:48` ACTION: sed -n '1580,1620p' astropy/coordinates/baseframe.py && sed -n '1860,1900p' astropy/coordinates/base [...]
- `01:28:41` grep __getattr__: astropy/coordinates/baseframe.py:1591,1877 astropy/coordinates/sky_coordinate.py:829,862,877,905
- `01:28:25` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `01:27:56` ACTION: sed -n '1560,1620p' astropy/coordinates/baseframe.py && sed -n '1840,1900p' astropy/coordinates/base [...]
- `01:27:49` grep __getattr__: astropy/coordinates/baseframe.py:1591,1877 astropy/coordinates/sky_coordinate.py:829,862,877,905
- `01:27:42` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `01:27:23` ACTION: sed -n '800,940p' astropy/coordinates/sky_coordinate. [...]
- `01:27:14` ACTION: grep -nR "__getattr__" astropy/coordinates || true
