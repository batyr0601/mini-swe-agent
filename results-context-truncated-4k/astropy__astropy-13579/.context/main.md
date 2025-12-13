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
- [ ] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: create a reproducer script in testbed using the PR example to show world_to_pixel mismatch for SlicedLowLevelWCS
- [ ] 2. Locate the SlicedLowLevelWCS world_to_pixel code: search for SlicedLowLevelWCS and world_to_pixel in the repository (testbed)
- [ ] 3. Root cause analysis: inspect world_to_pixel/pixel_to_world implementations for axis ordering and handling of fixed axes in SlicedLowLevelWCS
- [ ] 4. Implement fix: modify SlicedLowLevelWCS.world_to_pixel to account for fixed axes mapping similar to pixel_to_world behavior
- [ ] 5. Verify fix: run the reproducer script and ensure results match the full WCS world_to_pixel/pixel_to_world behavior
- [ ] 6. Run tests and commit changes
- [ ] 1. Clarify & reproduce: obtain reproduction steps or failing test names from user; attempt to reproduce the failure locally (run provided repro script or test subset)
- [ ] 2. Locate code: search repository for likely culprit(s) (e.g., grep for
- [ ] 3. Root cause analysis: inspect the located code sections, trace exception flow, and identify why the wrong AttributeError/message is raised or why behavior differs from expectation
- [ ] 4. Implement fix: modify the minimal code to preserve correct exception origins (e.g., avoid catching descriptor AttributeError, adjust except handling) and add targeted unit tests reproducing the bug
- [ ] 5. Verify fix: run the relevant unit tests and the full test suite if feasible; confirm failing tests now pass and no regressions introduced
- [ ] 6. Document & commit: summarize the root cause and fix in a commit message and update any relevant changelog or issue tracker entry
- [ ] 1. Reproduce the bug: run the full test suite (pytest -q) and any provided repro scripts (e.g. python3 repro.py) to capture failing tests and exact tracebacks
- [ ] 2. Locate the code: use grep to find symbols/names from tracebacks and search likely files (e.g. grep -n
- [ ] 3. Root cause analysis: open the identified source ranges, inspect exception handling and descriptor/property usage, and run focused unit tests or small reproducer to determine which line raises the unexpected exception
- [ ] 4. Implement fix: make minimal code change (e.g. narrow except clauses, check descriptor behavior, or validate inputs), add a new unit test that reproduces the bug before the fix and passes after, and run linters/formatters
- [ ] 5. Verify fix: run pytest -q, run the repro script(s), update changelog/commit message, and mark the related TODOs complete once CI-local tests pass
- [ ] 2. Locate the code: grep repository for
- [ ] 3. Root cause analysis: inspect astropy/convolution/utils.py around discretize_model to confirm np.diff(x_range) returns an array and understand inputs (tuple/list/ndarray)
- [ ] 4. Implement fix: modify discretize_model to avoid float(np.diff(...)) by using a safe check like delta = np.diff(x_range); if not np.allclose(delta, np.round(delta)): raise ValueError(...); apply same for y_range
- [ ] 5. Verify fix: run pytest for astropy/convolution tests (start with pytest -q astropy/convolution/tests/test_convolve_kernels.py) and confirm no DeprecationWarning/collection errors
- [ ] 6. Check for other occurrences: grep for similar float(np.diff(...)) patterns and update as needed
- [ ] 7. Commit checkpoint: context_commit with a message describing the fix after tests pass
- [ ] 3. Root cause analysis: test np.diff behavior for inputs (tuple, list, numpy array, numpy scalar) to see when float(np.diff(...)).is_integer() can fail
- [ ] 4. Implement fix: replace float(np.diff(x_range)).is_integer() / float(np.diff(y_range)).is_integer() with a robust check using np.allclose(np.diff(range), np.rint(np.diff(range))) and handle scalar vs array diffs
- [ ] 5. Run tests: create and run small python snippets calling discretize_model with various x_range/y_range types (ints, floats, numpy arrays, dtype=object) to verify behavior
- [ ] 6. Apply patch: edit astropy/convolution/utils.py to implement the fix, run unit tests (or targeted tests), and log results
- [ ] 1. Reproduce the bug: run astropy/convolution/tests/test_discretize.py and create a minimal repro calling discretize_model with (a) tuple/list with numpy scalar elements and (b) a numpy scalar to observe DeprecationWarning/ValueError from float(np.diff(...)).is_integer()
- [ ] 2. Locate the code: open astropy/convolution/utils.py and inspect the integer-range checks around the float(np.diff(...)).is_integer() lines
- [ ] 3. Design a robust fix: create a helper that safely computes the difference for sequences and numpy objects (use np.atleast_1d or np.asarray and handle ndim==0) and checks whether the difference is an integer without converting an array directly to a scalar
- [ ] 4. Implement the fix: modify astropy/convolution/utils.py to replace float(np.diff(...)).is_integer() with the new helper, add docstring and unit tests covering tuples, lists, numpy arrays, object-dtype arrays, and numpy scalars
- [ ] 5. Verify the fix: run the discretize tests (pytest astropy/convolution/tests/test_discretize.py) and any other affected tests, and log results
- [ ] 1. Understand the bug: reproduce the issue by running the project
- [ ] 2. Locate the code: search the codebase for functions/classes mentioned in stack traces (e.g., grep for
- [ ] 3. Root cause analysis: inspect the implicated functions/methods, trace execution paths, and identify why the error is raised (include checking descriptors/properties and exception handling)
- [ ] 4. Implement fix: make minimal, well-tested code changes to address the root cause (preserve API, handle descriptors correctly, and adjust error messages/propagation as needed)
- [ ] 5. Verify fix: run the failing repro and full test suite, add regression test(s) reproducing the bug, and mark TODOs complete when tests pass
- [ ] 2. Confirm offending expression
- [ ] 3. Root cause analysis: explain why float(np.diff(x_range)) on a numpy array triggers DeprecationWarning and choose safe scalar extraction (.item() or [0])
- [ ] 4. Implement fix: replace float(np.diff(x_range)).is_integer() and float(np.diff(y_range)).is_integer() with safe scalar extraction (e.g., float(np.diff(x_range).item()).is_integer() or float(np.diff(x_range)[0]).is_integer()) and prepare patch
- [ ] 5. Verify fix: run pytest astropy/convolution/tests/test_convolve_kernels.py (or full test collection) to ensure no collection errors and that behavior is unchanged
- [ ] 1. Understand the bug: gather reproduction steps, expected vs actual behavior from user report or failing test
- [ ] 2. Reproduce the bug: create a minimal repro script or run the failing test to get stack trace and exact error
- [ ] 3. Locate the code: search repository for relevant symbols (e.g., __getattr__, property names, or function names from stack) to find candidate files/functions
- [ ] 4. Root cause analysis: inspect the identified functions/files and trace how the error arises (read code around stack frames and add instrumenting prints if needed)
- [ ] 5. Implement and verify fix: make minimal code change, add a unit test reproducing the bug, run test suite and verify fix
- [ ] 1. Understand bug: DeprecationWarning from numpy.product used in convolve_fft; confirm numpy deprecates np.product and that np.prod is the recommended replacement
- [ ] 2. Find all np.product occurrences in the repo and decide which should be updated (start with astropy/convolution/convolve.py:687,780,792-797 and other matches from grep)
- [ ] 3. Implement fix: replace np.product(...) with np.prod(...) in affected source files, starting with astropy/convolution/convolve.py
- [ ] 4. Verify fix: run the specific failing test astropy/convolution/tests/test_convolve.py::TestConvolve1D::test_unity_1_none[convolve_fft-wrap] and ensure no DeprecationWarning and test passes
- [ ] 5. Regression: run relevant convolution tests (or full test suite if feasible), then context_commit a checkpoint and mark TODOs complete as appropriate
- [ ] 1. Search repository for remaining uses of np.product
- [ ] 2. Search repository for other
- [ ] 3. Run a small Python import and call to astropy.convolution.convolve_fft to check for DeprecationWarning from np.product
- [ ] 4. Inspect astropy/convolution/convolve.py to confirm all np.product replaced with np.prod
- [ ] 1. Locate matrix_product function: open astropy/coordinates/matrix_utilities.py and inspect implementation
- [ ] 2. Search for direct np.product usages: run grep -n
- [ ] 3. Inspect astropy/modeling/tests/test_core.py around line 734 to see how np.product(shape) is used (reshape/data creation)
- [ ] 4. Root cause analysis: determine whether np.product on astropy.units.Quantity (or other types) causes incorrect behavior and why
- [ ] 5. Implement fix: change offending uses to np.prod or to use Quantity.prod (or add wrapper) and update code/tests accordingly
- [ ] 6. Verify fix: run pytest for affected tests/modules (start with astropy/modeling and astropy/units tests)
- [ ] 2. Inspect occurrences of np.product in files reported by grep
- [ ] 3. Open astropy/units/tests/test_quantity_non_ufuncs.py around the np.product usage to see test expectations for Quantity
- [ ] 4. Inspect astropy/units/quantity_helper/function_helpers.py to see how np.product is wrapped/handled for Quantity
- [ ] 5. Check astropy/modeling/tests/test_core.py and astropy/utils/masked/tests/test_function_helpers.py contexts for their np.product usage
- [ ] 1. Clarify scope: ask user for repository path, failing test name or error message, and exact steps to reproduce
- [ ] 2. Reproduce the issue: run the project
- [ ] 3. Locate relevant code: search for symbols/stacktrace lines from the failure (grep -n
- [ ] 4. Root cause analysis: inspect the candidate files, add focused prints or run a debugger to produce a minimal repro and determine why the error occurs
- [ ] 5. Implement fix: propose and apply minimal code changes, add unit tests that reproduce the bug then pass, and run linters
- [ ] 6. Verify & finalize: run full test suite, create context_commit with a summary, and mark each TODO complete as their steps finish
- [ ] 1. Reproduce the bug: run the project
- [ ] 2. Locate the code: search the repository for likely failure points (e.g., grep for __getattr__, property decorators, or filenames referenced in the stack trace)
- [ ] 3. Root cause analysis: inspect the identified source files and surrounding code to determine why the error is raised and whether exceptions are being masked or misreported
- [ ] 4. Implement fix: modify the minimal lines needed to correct the behavior (e.g., adjust exception handling, check descriptors before catching AttributeError), and add/adjust unit tests that reproduce the failure
- [ ] 5. Verify fix: run the specific failing test(s) and full test suite locally, confirm regressions are fixed and no other tests break
- [ ] 6. Commit & document: create a context_commit with a clear message describing the fix and update changelog or comments explaining the root cause
- [ ] 1. Reproduce the failure: run pytest for the failing doctest (astropy.coordinates.erfa_astrom.ErfaAstromInterpolator) to capture full traceback and confirm it
- [ ] 2. Locate auto_open: open astropy/utils/iers/iers.py and find the LeapSeconds.auto_open implementation
- [ ] 3. Inspect iers.auto_open: read lines around 960-1080 in astropy/utils/iers/iers.py to examine the IERSStaleWarning at line ~1074
- [ ] 4. Locate update_leap_seconds and _check_leapsec: open astropy/time/core.py lines ~2840-2895 to see how auto_open is called
- [ ] 5. Root cause analysis: determine why auto_open warns (expired leap-second file) during doctest and whether bundled
- [ ] 6. Implement fix: decide whether to suppress the warning when using bundled data or to have update_leap_seconds catch and handle IERSStaleWarning appropriately; make code changes
- [ ] 7. Add/adjust tests: update tests to reflect intended behavior (no unexpected AstropyWarning) and add regression test
- [ ] 8. Verify fix: run the minimal failing doctest and relevant time/iers tests to ensure warning no longer causes test failure
- [ ] 1. Reproduce the issue by calling astropy.time.update_leap_seconds() to see what warnings/exceptions are emitted
- [ ] 2. Run a small Python script to call update_leap_seconds() and capture warnings and stderr to observe exact warning classes and messages
- [ ] 3. Inspect astropy/utils/iers/iers.py around LeapSeconds.auto_open to confirm it uses warn(...) with IERSStaleWarning and does not raise
- [ ] 4. Decide whether update_leap_seconds should let IERSStaleWarning through, convert it to AstropyWarning, or handle it specially; document rationale
- [ ] 5. Implement & test fix: modify update_leap_seconds to handle IERSStaleWarning appropriately and run tests or the repro script to verify behavior
- [ ] 1. Confirm where IERSStaleWarning related to leap-seconds is issued in astropy/utils/iers/iers.py
- [ ] 2. Inspect _read_leap_seconds and _substitute_iers_b implementations to see whether they warn or raise on expired leap-second file
- [ ] 3. Decide fix: change warn(
- [ ] 4. Implement code change in astropy/utils/iers/iers.py to raise instead of warn for expired leap-second file
- [ ] 5. Run relevant tests or a small repro to verify the change

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

## Interaction Log

- `01:33:13` ACTION: sed -n '720,840p' astropy/utils/iers/iers.py && sed -n '1040,1088p' astropy/utils/iers/iers.py
- `01:33:05` ACTION: grep -n "IERSStaleWarning" astropy/utils/iers/iers.py || true && grep -n "warn(" astropy/utils/iers/ [...]
- `01:32:46` ACTION: grep -n -E "class LeapSeconds|def auto_open" astropy/utils/iers/iers. [...]
- `01:32:39` update_leap_seconds repro: astropy version 5.2.dev362+g0df94ff70.d20250910; returned 0; WARN[0]: category=RuntimeWarning message='numpy.ndarray size c...
- `01:32:27` ACTION: python3 - <<'PY'
- `01:32:00` ACTION: grep -n -E "update_leap_seconds|_check_leapsec" astropy/time/core. [...]
- `01:31:54` sed 960-1080: LeapSeconds.auto_open implementation found; warning emitted with warn('leap-second file is expired.', IERSStaleWarning) when self.expire...
- `01:31:54` grep auto_open: astropy/utils/iers/iers.py lines observed: 937, 998
- `01:31:42` ACTION: grep -n "auto_open" astropy/utils/iers/iers.py && sed -n '960,1080p' astropy/utils/iers/iers.py
- `01:31:15` ACTION: grep -nR -e "update_leap_seconds" -e "_check_leapsec" -e "IERSStaleWarning" -e "auto_open" astropy | [...]
- `01:31:04` pytest failure: doctest astropy.coordinates.erfa_astrom.ErfaAstromInterpolator raised AstropyWarning: leap-second auto-update failed due to IERSStaleW...
- `01:30:36` ACTION: pytest -q astropy/coordinates/erfa_astrom.py::astropy.coordinates.erfa_astrom.ErfaAstromInterpolator
- `01:29:17` ACTION: pytest -x
- `01:29:07` pytest timed out; partial output included 'RuntimeWarning: numpy.ndarray size changed, may indicate binary incompatibility. Expected 80 from C header,...
- `01:27:55` ACTION: pytest -q
- `01:27:02` ACTION: sed -n '600,680p' astropy/units/tests/test_quantity_non_ufuncs. [...]
- `01:26:52` grep np.product: astropy/modeling/tests/test_core.py:734:    data = np.arange(np.product(shape)).reshape(shape) * u.m / u.s; astropy/utils/masked/test...
- `01:26:32` ACTION: grep -nR "np.product" astropy || true
- `01:26:25` matrix_utilities.py: matrix_product defined at line 13; implementation: returns reduce(np.matmul, matrices)
- `01:26:17` ACTION: sed -n '1,240p' astropy/coordinates/matrix_utilities.py
