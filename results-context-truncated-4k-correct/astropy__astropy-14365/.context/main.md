# Project Goals

**Current Task:** ascii.qdp Table format assumes QDP commands are upper case

<details>
<summary>Full description</summary>

ascii.qdp Table format assumes QDP commands are upper case
### Description

ascii.qdp assumes that commands in a QDP file are upper case, for example, for errors they must be "READ SERR 1 2" whereas QDP itself is not case sensitive and case use "read serr 1 2". 

As many QDP files are created by hand, the expectation that all commands be all-caps should be removed.

### Expected behavior

The following qdp file should read into a `Table` with errors, rather than crashing.
```
read serr 1 2 
1 0.5 1 0.5
```

### How to Reproduce

Create a QDP file:
```
> cat > test.qdp
read serr 1 2 
1 0.5 1 0.5
<EOF>

 > python
Python 3.10.9 (main, Dec  7 2022, 02:03:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a test QDP file with lower-case commands and run Table.read(
- [ ] 2. Locate the code: search the repository for ascii.qdp reader implementation (grep for
- [ ] 3. Root cause analysis: inspect the parser code for where QDP commands are matched and confirm it assumes upper-case; identify exact lines to change
- [ ] 4. Implement fix: modify the parser to treat QDP commands case-insensitively (e.g., compare upper()/lower() or use re.IGNORECASE); update code accordingly
- [ ] 5. Verify fix: run the repro script to ensure lower-case
- [ ] 1. Understand the bug: reproduce the issue and capture the exact error message/output
- [ ] 2. Locate the code: search repository for likely files/functions related to the error (grep filenames and symbols)
- [ ] 3. Root cause analysis: inspect the identified files/lines to determine why the error occurs
- [ ] 4. Implement fix: modify source to fix root cause with minimal, well-documented change
- [ ] 5. Verify fix: run unit tests and reproduce the original failing case to confirm resolution
- [ ] 1. Understand the bug: reproduce the AttributeError raised when accessing a missing attribute on SkyCoord (capture traceback and exact message)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py (around lines 850-940) and astropy/coordinates/baseframe.py (around lines 1700-2050) for __getattr__ implementations and related error handling
- [ ] 3. Root cause analysis: find where AttributeError is raised/caught, check for bare except AttributeError that may mask descriptor errors, and identify the exact line causing misleading message
- [ ] 4. Implement fix: modify __getattr__ to not mask descriptor-raised AttributeError (or to re-raise with correct attribute name), add unit tests covering the repro
- [ ] 5. Verify fix: run the repro script and run relevant tests (astropy/coordinates tests) to ensure the AttributeError message and behavior are correct
- [ ] 2. Locate the code: inspect __getattr__ in astropy/coordinates/sky_coordinate.py and GenericFrame.__getattr__ in astropy/coordinates/baseframe.py
- [ ] 3. Root cause analysis: determine how AttributeError is raised/caught and whether GenericFrame.__getattr__ or SkyCoord.__getattr__ causes misleading AttributeError messages
- [ ] 4. Implement fix: modify SkyCoord.__getattr__ to avoid masking AttributeError from descriptors/underlying frame and ensure correct attribute name in exceptions
- [ ] 5. Verify fix: run repro script and relevant test(s) to ensure correct exception behavior
- [ ] 1. Understand the bug: reproduce case where AttributeError shows wrong name when accessing missing attribute in SkyCoord/BaseFrame __getattr__
- [ ] 2. Locate the code: inspect astropy/coordinates/baseframe.py (around 1680-1760 and 1996-2038) and astropy/coordinates/sky_coordinate.py (around 820-960) to read __getattr__ implementations
- [ ] 3. Root cause analysis: find where AttributeError is created or masked (e.g., __getattribute__ calls, catch/re-raise patterns, descriptor/property interactions) and identify exact lines causing wrong message
- [ ] 4. Implement fix: modify __getattr__ to let descriptor AttributeError propagate or raise AttributeError with correct missing attribute name; update/add unit tests
- [ ] 5. Verify fix: run targeted pytest for astropy/coordinates and run a minimal repro script to confirm AttributeError reports correct attribute name
- [ ] 1. Understand the bug: investigate __getattr__ masking AttributeError in BaseCoordinateFrame/GenericFrame causing wrong/masked attribute errors
- [ ] 2. Locate the code: inspect baseframe.py __getattr__ implementations around lines 1688-1760 and 1988-2040 and relevant parts of sky_coordinate.py
- [ ] 3. Root cause analysis: check final
- [ ] 4. Implement fix: adjust __getattr__ to let correct AttributeError propagate (or re-raise with correct attribute name); add tests
- [ ] 5. Verify fix: run coordinate-related unit tests and reproduce original failing example
- [ ] 1. Inspect SkyCoord.__getattr__ in astropy/coordinates/sky_coordinate.py to find where AttributeError might be masked or re-raised incorrectly
- [ ] 2. Inspect BaseCoordinateFrame.__getattr__ and GenericFrame.__getattr__ in astropy/coordinates/baseframe.py to understand representation/differential attribute handling
- [ ] 3. Root cause analysis: determine if __getattr__ delegates (getattr(self.frame, attr) / getattr(self,
- [ ] 4. Implement fix: change __getattr__ to avoid catching/overwriting AttributeError raised by descriptors or underlying attribute access; ensure only missing-attribute causes AttributeError with correct message
- [ ] 5. Verify fix: add unit test reproducing masked AttributeError, run relevant coordinates tests, and update changelog
- [ ] 1. Understand the bug: Determine whether __getattr__ implementations re-raise or mask AttributeError incorrectly, causing descriptor or property errors to be hidden and wrong
- [ ] 2. Locate the code: Inspect __getattr__ methods in astropy/coordinates/baseframe.py (lines ~1700-2060) and astropy/coordinates/sky_coordinate.py (lines ~840-980) and any helpers they call
- [ ] 3. Root cause analysis: Identify exact statements that convert or re-raise AttributeError (e.g., usage of return self.__getattribute__(attr) or accessing descriptors within try/except) and determine whether descriptor-raised AttributeError is being swallowed
- [ ] 4. Implement fix: Update __getattr__ logic to let descriptor/property AttributeError propagate (only raise AttributeError for truly missing attributes), add comments and minimal code changes, prepare a patch
- [ ] 5. Verify fix: Write a focused unit test that reproduces the masked-AttributeError behavior, run pytest for astropy.coordinates, and confirm the test passes and no regressions occur
- [ ] 1. Understand the bug: reproduce the AttributeError observed when accessing an attribute on SkyCoord/BaseFrame that masks the original missing attribute name (create minimal repro)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py (around lines 858-932) and astropy/coordinates/baseframe.py (around lines 1720 and 2015) to find relevant __getattr__ implementations
- [ ] 3. Root cause analysis: examine the __getattr__ methods for broad except AttributeError blocks that re-raise with the wrong attribute name or swallow descriptor errors; note exact lines and offending code
- [ ] 4. Implement fix: update __getattr__ to check for class descriptors/properties first or to preserve and re-raise the original AttributeError with correct attribute name; prepare a focused patch
- [ ] 5. Verify fix: run targeted coordinate-related tests and the minimal reproduction script to confirm the AttributeError message is correct; mark todos complete as each step finishes
- [ ] 1. Understand the bug: reproduce AttributeError masking when a descriptor raises AttributeError during attribute access on SkyCoord/BaseCoordinateFrame
- [ ] 2. Locate the code: find __getattr__ implementations in astropy/coordinates (baseframe.py, sky_coordinate.py, sky_coordinate.BaseCoordinateFrame) and record exact line ranges
- [ ] 3. Root cause analysis: Inspect __getattr__ implementations for broad exception handling or re-raising that can mask descriptor AttributeError; identify which attribute accesses call descriptors
- [ ] 4. Implement fix: Modify __getattr__ to avoid catching descriptor-raised AttributeError (e.g., check for descriptors explicitly or narrow exception handling) and add a focused unit test reproducing the original incorrect message
- [ ] 5. Verify fix: Run relevant coordinate tests and a small repro script to confirm AttributeError now shows correct missing attribute and no undesired masking
- [ ] 1. Understand the bug: Determine whether BaseCoordinateFrame.__getattr__ (and SkyCoord.__getattr__) can mask AttributeError raised by descriptors/properties when accessing representation components and thus produce the wrong error message
- [ ] 2. Locate the code: Inspect BaseCoordinateFrame.__getattr__ in astropy/coordinates/baseframe.py and related __getattr__ in astropy/coordinates/sky_coordinate.py to see exact control flow and where AttributeError may be transformed
- [ ] 3. Root cause analysis: Reproduce a minimal example where a descriptor/property accessed via a representation raises AttributeError and confirm whether __getattr__ hides the original exception or alters the message
- [ ] 4. Implement fix: Modify __getattr__ to avoid masking descriptor-raised AttributeError (e.g., avoid broad try/except around getattr on representation, or detect descriptor errors and re-raise original exception), update code accordingly
- [ ] 5. Verify fix: Add a unit test reproducing the issue, run the repro and relevant tests (coordinate attribute access tests), and ensure all tests pass
- [ ] 1. Reproduce bug: instantiate IntermediateFrame({
- [ ] 2. Locate code: open and inspect __getattr__ in astropy/coordinates/baseframe.py (around lines 1700 and 1996) and astropy/coordinates/sky_coordinate.py (around line 840-980)
- [ ] 3. Root cause analysis: determine which __getattr__ raises AttributeError(
- [ ] 4. Implement fix: modify IntermediateFrame.__getattr__ to raise AttributeError(name) instead of f
- [ ] 5. Verify fix: run the Python repro to confirm correct exception message and run relevant coordinate tests (pytest astropy/coordinates -q or narrower selection) to ensure no regressions
- [ ] 1. Understand the bug: Investigate whether __getattr__ implementations in SkyCoord and BaseCoordinateFrame mask AttributeError from descriptors/properties, causing incorrect error propagation
- [ ] 2. Locate the code: Inspect __getattr__ in astropy/coordinates/baseframe.py (around 1720 and 2015) and astropy/coordinates/sky_coordinate.py (around 858-980)
- [ ] 3. Root cause analysis: Check where getattr/__getattribute__ are used, whether AttributeError is raised intentionally, and if private attribute fallbacks or transformations swallow underlying descriptor errors
- [ ] 4. Implement fix: Modify __getattr__ to avoid catching AttributeError from property/descriptor access (use object.__getattribute__ or explicit hasattr checks), prepare minimal patch
- [ ] 5. Verify fix: Add a targeted unit test reproducing the masked AttributeError and run pytest for astropy/coordinates to confirm behavior is corrected
- [ ] 1. Reproduce the bug: create a minimal repro that triggers AttributeError when accessing a SkyCoord attribute that comes from the underlying frame (e.g., a frame property/descriptor that raises AttributeError)
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py __getattr__ (around lines 840-1000) and astropy/coordinates/baseframe.py GenericFrame.__getattr__ to compare behaviors
- [ ] 3. Root cause analysis: run the repro, capture the full traceback, and determine whether the AttributeError originates from a descriptor on the frame or from SkyCoord.__getattr__ wrapping it
- [ ] 4. Implement fix: modify SkyCoord.__getattr__ to avoid catching/transforming AttributeError from frame descriptors (e.g., access frame attributes via object.__getattribute__(self.frame, attr) or re-raise original exception) and add a focused unit test
- [ ] 5. Verify fix: run the repro and coordinate-related tests (or a subset) to confirm error messages and behavior are correct; mark the TODOs complete and commit when ready
- [ ] 2. Locate __getattr__: inspect __getattr__ implementations in baseframe.py (around lines 1720 and 2015) and sky_coordinate.py (around lines 858-932)
- [ ] 3. Root cause analysis: examine how __getattr__ catches AttributeError and whether it masks AttributeError from descriptors or properties
- [ ] 4. Implement fix: modify __getattr__ to avoid swallowing descriptor/property AttributeError and to raise correct missing-attribute error
- [ ] 5. Verify fix: run repro.py and relevant unit tests (e.g., test_skycoord) to ensure AttributeError message is correct
- [ ] 1. Reproduce the bug: create/run a minimal repro that triggers the AttributeError when accessing a missing attribute on SkyCoord / Frame (e.g., access non-existent attribute on SkyCoord)
- [ ] 2. Locate the code: find __getattr__ implementations and
- [ ] 3. Root cause analysis: inspect the __getattr__ implementations and any except AttributeError blocks to identify where AttributeError from descriptors/attributes is being caught and re-raised with incorrect message
- [ ] 4. Implement fix: modify the offending code to avoid catching AttributeError from property/descriptors or to re-raise with the correct missing attribute name; prepare a patch and run minimal static checks
- [ ] 5. Verify fix: run the minimal repro and pytest for astropy/coordinates (or relevant tests) to confirm the AttributeError message and behavior are corrected
- [ ] 1. Analyze __getattr__ implementations in BaseCoordinateFrame, GenericFrame, and SkyCoord to identify incorrect AttributeError handling
- [ ] 2. Reproduce the AttributeError with a minimal repro or test
- [ ] 3. Propose and implement a fix in the affected __getattr__ method(s)
- [ ] 4. Run unit tests and repro to verify the fix
- [ ] 1. Understand the bug: reproduce the AttributeError message when accessing a non-existent attribute on SkyCoord/BaseCoordinateFrame to see which __getattr__ is catching and how the exception is formed
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py (SkyCoord and related classes) and astropy/coordinates/baseframe.py (BaseCoordinateFrame and GenericFrame)
- [ ] 3. Root cause analysis: trace attribute lookup paths (frame attributes, representation names, frame_transform_graph lookup) and grep usage sites to find where an AttributeError might be masked or re-raised with wrong attr
- [ ] 4. Implement fix: modify the offending __getattr__ to let AttributeError propagate (or re-raise with the correct attribute name) and add a focused unit test that reproduces the original wrong-message behavior
- [ ] 5. Verify fix: run the repro script and targeted pytest for coordinates (e.g., pytest -q astropy/coordinates -k
- [ ] 1. Understand the bug: inspect how BaseCoordinateFrame.__getattr__ and SkyCoord.__getattr__ handle missing attributes and AttributeError
- [ ] 2. Locate the code: open baseframe.py:1680-1760, 1988-2038 and sky_coordinate.py:840-980 to capture __getattr__ implementations
- [ ] 3. Root cause analysis: identify whether __getattr__ swallows AttributeError from descriptors/properties and re-raises with incorrect message
- [ ] 4. Implement fix: modify __getattr__ to check for attribute existence without invoking descriptor AttributeError, and re-raise original AttributeError if appropriate
- [ ] 5. Verify fix: run failing unit tests or reproduce with minimal script; ensure AttributeError shows correct attribute name
- [ ] 1. Understand the bug: Investigate AttributeError handling in SkyCoord.__getattr__ (astropy/coordinates/sky_coordinate.py) where errors from descriptors/properties may be masked or re-raised with the wrong attribute name
- [ ] 2. Locate the code: Find and open __getattr__ in astropy/coordinates/sky_coordinate.py (~lines 858-932) and the __getattr__ definitions in astropy/coordinates/baseframe.py (around lines ~1720 and ~2015) to inspect implementation
- [ ] 3. Root cause analysis: Reproduce the failing behavior (run a minimal repro or tests), trace where AttributeError is caught, and determine if descriptor exceptions are being swallowed or the wrong name used in re-raise
- [ ] 4. Implement fix: Modify __getattr__ to check for class descriptors first or re-raise the original AttributeError correctly; add unit tests demonstrating the prior failure and the fix
- [ ] 5. Verify fix: Run unit tests for astropy/coordinates, run the repro script, and ensure no regressions; then mark todos complete and create a context commit
- [ ] 1. Reproduce the bug: create a minimal repro script that triggers an AttributeError masked by BaseCoordinateFrame.__getattr__ (e.g., access a frame attribute/property whose descriptor raises)
- [ ] 2. Locate the code: inspect __getattr__ in astropy/coordinates/baseframe.py (around lines 1680-1760 and 1980-2060) and in astropy/coordinates/sky_coordinate.py (around lines 840-980) to confirm exact implementations
- [ ] 3. Root cause analysis: identify where AttributeError from descriptors/properties is being caught or masked, trace call path and pinpoint the line that re-raises the wrong attribute name
- [ ] 4. Implement fix: modify __getattr__ to check class descriptors/property getters first (using type(self) or object.__getattribute__ on the class) and avoid swallowing AttributeError from those descriptors; prepare patch changes in the two files
- [ ] 5. Verify fix: add a unit test reproducing the original failure, run pytest -q astropy/coordinates (or the specific test) and confirm the AttributeError from the descriptor propagates correctly
- [ ] 6. Commit checkpoint: run context_commit --message \
- [ ] 1. Reproduce the AttributeError masking bug: create a minimal repro that accesses a missing attribute on SkyCoord/GenericFrame to observe incorrect/ambiguous error message
- [ ] 2. Locate __getattr__ implementations: inspect astropy/coordinates/baseframe.py (around lines 1680-1760 and 1988-2040) and astropy/coordinates/sky_coordinate.py (around 840-960) to identify exact code paths
- [ ] 3. Root cause analysis: identify where AttributeError is being caught, masked, or re-raised with the wrong attribute name and note exact line numbers to change
- [ ] 4. Implement fix: change __getattr__/__getattribute__ handling so descriptor-induced AttributeError isn
- [ ] 5. Verify fix: add a unit test reproducing the original incorrect message, run pytest for astropy/coordinates (or a minimal test file), and ensure the error message is correct
- [ ] 1. Understand the bug: investigate where __getattr__ catches AttributeError and may mask exceptions from descriptors/properties in astropy/coordinates (baseframe.py and sky_coordinate.py)
- [ ] 2. Reproduce the bug: create a minimal repro that triggers an AttributeError from a descriptor/property when accessed via the coordinate/frame __getattr__
- [ ] 3. Root cause analysis: inspect code paths in BaseCoordinateFrame.__getattr__ and SkyCoord.__getattr__ to identify where AttributeError is being caught or masked and why
- [ ] 4. Implement fix: update __getattr__ logic to not swallow AttributeError from class descriptors/properties (e.g., check for attribute existence on class or use getattr with explicit handling) and run linters
- [ ] 5. Verify fix: run the minimal repro and relevant coordinate tests to confirm original AttributeError propagates correctly and no regressions occur
- [ ] 1. Reproduce the bug: create a minimal repro showing that a frame descriptor/property raising AttributeError is masked when accessed via SkyCoord.<attr>
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py (around 840-960) and astropy/coordinates/baseframe.py (around 1680-2050)
- [ ] 3. Find catch/re-raise locations: grep for
- [ ] 4. Root cause analysis: run the minimal repro and capture the traceback to identify which __getattr__ or descriptor raised the final AttributeError
- [ ] 5. Implement fix: modify the offending __getattr__ to avoid masking underlying AttributeError (preserve and re-raise the original exception) and add a unit test reproducing the original incorrect behavior
- [ ] 6. Verify fix: run the new unit test and the relevant coordinate tests to ensure the exception message now shows the original descriptor error and no longer reports the wrong attribute
- [ ] 1. Understand the bug: reproduce AttributeError masking where a descriptor/property on a coordinate/frame raises AttributeError but __getattr__ incorrectly converts it to
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py, astropy/coordinates/baseframe.py, and any other files with __getattr__ from prior grep results
- [ ] 3. Root cause analysis: identify where getattr()/__getattribute__ usage or broad AttributeError handling could catch descriptor-raised AttributeError and change the error semantics; note exact lines and behavior
- [ ] 4. Implement fix: modify the offending __getattr__ to check class descriptors first (e.g., using object.__getattribute__ on the class or inspect.getattr_static) or to re-raise descriptor AttributeError instead of converting it to
- [ ] 5. Add tests: create unit tests that define a descriptor/property that raises AttributeError and assert that the original AttributeError propagates and that missing attributes still raise the intended
- [ ] 6. Run tests: run pytest for the changed modules and the new tests (focus on coordinate/frame tests) and iterate until passing
- [ ] 1. Understand the bug: reproduce AttributeError where accessing an attribute on SkyCoord/BaseCoordinateFrame masks the real AttributeError (investigate repro and exact error message)
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py (around lines 840-960) and astropy/coordinates/baseframe.py (around lines 1680-1760 and 1980-2048), and GenericFrame.__getattr__
- [ ] 3. Root cause analysis: search for broad except AttributeError or getattr() usages that may catch descriptor-raised AttributeError and determine where to allow original exceptions to propagate
- [ ] 4. Implement fix: modify the __getattr__ logic to only handle missing-attribute cases (use hasattr/dir/lookup or explicit attribute checks) and avoid catching AttributeError from descriptors; add unit tests reproducing previous failure
- [ ] 5. Verify fix: run targeted tests and a small repro script to confirm the AttributeError message is correct and existing tests pass

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 02:09] **swebench-astropy__astropy-14365**: Task completed: LimitsExceeded
## Interaction Log

- `02:09:07` grep __getattr__: astropy/coordinates/baseframe.py:1720,2015; astropy/coordinates/sky_coordinate.py:858,890,905,932
- `02:09:00` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `02:08:42` ACTION: sed -n '840,960p' astropy/coordinates/sky_coordinate. [...]
- `02:08:35` grep __getattr__: astropy/coordinates/sky_coordinate.py:858,890,905,932 astropy/coordinates/baseframe.py:1720,2015
- `02:08:28` ACTION: grep -nR "__getattr__" astropy/coordinates || true
- `02:08:08` ACTION: sed -n '1688,1760p' astropy/coordinates/baseframe.py && sed -n '1996,2048p' astropy/coordinates/base [...]
- `02:08:01` grep __getattr__: astropy/coordinates/baseframe.py:1720,2015; astropy/coordinates/sky_coordinate.py:858,890,905,932; astropy/coordinates/earth.py:252
- `02:07:52` ACTION: grep -n "__getattr__" astropy/coordinates/*.py && grep -n "except AttributeError" astropy/coordinate [...]
- `02:07:16` ACTION: sed -n '840,960p' astropy/coordinates/sky_coordinate. [...]
- `02:07:09` grep __getattr__: astropy/coordinates/sky_coordinate.py:858,890,905,932 astropy/coordinates/baseframe.py:1720,2015
- `02:07:03` ACTION: grep -nR "__getattr__" astropy/coordinates || true
- `02:06:37` ACTION: sed -n '1680,1760p' astropy/coordinates/baseframe.py && sed -n '1988,2040p' astropy/coordinates/base [...]
- `02:06:30` grep __getattr__: astropy/coordinates/baseframe.py:1720,2015; astropy/coordinates/sky_coordinate.py:858 (related comment lines at 890,905,932)
- `02:06:19` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `02:05:59` ACTION: sed -n '1680,1760p' astropy/coordinates/baseframe.py && sed -n '1988,2040p' astropy/coordinates/base [...]
- `02:05:52` grep __getattr__: astropy/coordinates/baseframe.py:1720, astropy/coordinates/baseframe.py:2015, astropy/coordinates/sky_coordinate.py:858, astropy/coo...
- `02:05:40` ACTION: grep -n "__getattr__" astropy/coordinates/*.py
- `02:05:13` ACTION: sed -n '1680,1760p' astropy/coordinates/baseframe.py && sed -n '1980,2060p' astropy/coordinates/base [...]
- `02:05:06` grep __getattr__: astropy/coordinates/baseframe.py:1720,2015 astropy/coordinates/sky_coordinate.py:858,890,905,932
- `02:04:59` ACTION: grep -n "__getattr__" astropy/coordinates/*.py || true
