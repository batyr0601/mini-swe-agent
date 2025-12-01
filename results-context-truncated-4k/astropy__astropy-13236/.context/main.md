# Project Goals

**Current Task:** Consider removing auto-transform of structured column into NdarrayMixin

<details>
<summary>Full description</summary>

Consider removing auto-transform of structured column into NdarrayMixin
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
<!-- If you want to, you can suggest a d...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce how adding a structured numpy.ndarray to a Table becomes an NdarrayMixin and confirm current behavior
- [ ] 2. Locate the code: find source files that reference NdarrayMixin or view(...NdarrayMixin) and identify exact clause to change
- [ ] 3. Root cause analysis: inspect the logic and rationale around converting structured ndarray to NdarrayMixin and decide exact change (add FutureWarning, keep behavior for now)
- [ ] 4. Implement fix: modify the clause to emit a FutureWarning advising users to wrap in Column and plan to remove conversion in future release
- [ ] 5. Verify fix: add/ run a small repro script demonstrating the FutureWarning and ensure no other functionality breaks; update logs and mark todos complete
- [ ] 1. Add regression unit test: create astropy/table/tests/test_structured_deprecation.py that asserts a FutureWarning is emitted when adding a structured numpy.ndarray to a Table and verifies behavior is preserved (column is NdarrayMixin with structured dtype)
- [ ] 2. Run full test suite for astropy/table locally (pytest -q astropy/table) and record results
- [ ] 3. Add changelog entry describing the deprecation, suggested workaround (wrap in astropy.table.Column(...)), and link to issue/PR
- [ ] 4. Prepare PR: create branch, include code change, unit test, changelog, and compose PR description with diff and test results
- [ ] 5. Run CI checklist: run linters and any required pre-commit checks locally and fix any issues before opening PR
- [ ] 6. Notify maintainers/reviewers in PR and reference the issue number for context
- [ ] 1. Understand failures: capture list of failed tests and full error traces for each failure (start with the first failure shown by pytest)
- [ ] 2. Reproduce first failure: run the single failing test astropy/table/tests/test_column.py::TestColumn::test_quantity_comparison[MaskedColumn] to get concise failure output
- [ ] 3. Locate relevant code: inspect astropy/table/column.py (especially _compare) and astropy/units/quantity.py (__array_ufunc__/converters_and_unit) to find where Quantity vs Column comparisons are handled
- [ ] 4. Root cause analysis: determine why Column comparison with Quantity triggers numpy/Quantity __array_ufunc__ path leading to the error and why other table tests (structured ndarray deprecation, values_equal, mixins) are failing
- [ ] 5. Implement fix: update Column._compare to properly handle Quantity operands (e.g., convert other to Quantity or call unit-aware comparison helper), add/adjust tests and warnings if needed
- [ ] 6. Verify fix: run the affected tests individually and then run the astropy/table test subset; log results and mark todos complete as progress is made
- [ ] 3. Reproduce the failure locally: run pytest for astropy/table/tests/test_column.py::TestColumn::test_quantity_comparison[MaskedColumn] and capture full traceback/output
- [ ] 4. Locate code paths: inspect Column._compare (astropy/table/column.py) and Quantity.__array_ufunc__/converters_and_unit (astropy/units/quantity.py) and converters helpers (astropy/units/quantity_helper/converters.py) to map flow during comparisons
- [ ] 5. Create minimal repro scripts: craft small scripts comparing Column/MaskedColumn with Quantity and plain arrays to observe converters list and can_have_arbitrary_unit decisions
- [ ] 6. Root cause analysis: run repros, print converters and units and identify why converters contains False and why can_have_arbitrary_unit returned False (TypeError) for MaskedColumn or other types
- [ ] 7. Implement fix: modify converters_and_unit (or can_have_arbitrary_unit) to correctly handle MaskedColumn/Column/ndarray subclasses (e.g., use getattr(...,
- [ ] 8. Verify fix: run failing pytest test and relevant test suite (astropy/table tests) and log results
- [ ] 1. Understand the bug: determine why UnitConversionError is raised when comparing a MaskedColumn (numpy.ma.MaskedArray-backed) to a plain float/array in the quantity ufunc path (converters contains False and can_have_arbitrary_unit returned False)
- [ ] 2. Locate the code: inspect astropy/units/quantity_helper/converters.py (converters_and_unit, can_have_arbitrary_unit) and astropy/table/column.py (BaseColumn._compare / Column._compare) to see how MaskedColumn objects are treated
- [ ] 3. Reproduce the bug: write a minimal repro script (repro_masked_compare.py) that creates a MaskedColumn from a numpy.ma.MaskedArray and performs a comparison that triggers UnitConversionError
- [ ] 4. Root cause analysis: run targeted grep/sed on the located functions, capture exact lines and behavior, and log observations with context_log
- [ ] 5. Implement fix & verify: update can_have_arbitrary_unit (or converters handling) to correctly handle MaskedArray/MaskedColumn, run the repro and relevant unit tests to confirm the issue is resolved
- [ ] 1. Understand which command produced the
- [ ] 2. Locate the source file containing the
- [ ] 3. Inspect the first and last ~200 lines of that file to get context without overflowing output (use sed -n
- [ ] 4. Search the repository for definitions of
- [ ] 5. Re-run the previous long-output command but limit output (head/sed) and optionally save the full output to a file for later examination
- [ ] 1. Analyze converters.py: inspect converters_and_unit and check_output for unit conversion and error paths
- [ ] 2. Create minimal repro that triggers the suspected unit/ufunc error
- [ ] 3. Run targeted unit tests related to Quantity ufunc handling
- [ ] 4. Implement fix in astropy/units/quantity_helper/converters.py if bug found
- [ ] 5. Verify fix with the repro and run the full test suite
- [ ] 1. Inspect converters_and_unit implementation: view lines ~133-282 of astropy/units/quantity_helper/converters.py
- [ ] 1. Inspect converters_and_unit implementation: view lines ~130-240 of astropy/units/quantity_helper/converters.py
- [ ] 2. Inspect check_output implementation: view lines ~360-540 of astropy/units/quantity_helper/converters.py
- [ ] 3. Locate UFUNC_HELPERS and helper functions referenced by converters_and_unit (search in astropy/units/quantity_helper and astropy/units)
- [ ] 4. Reproduce the failing case or run unit tests related to ufunc handling / quantity output to observe exact error message
- [ ] 5. Identify root cause (formatting bug or wrong exception type) and implement minimal fix with tests
- [ ] 6. Run targeted tests to verify fix and mark TODOs complete
- [ ] 1. Inspect UfuncHelpers class and UFUNC_HELPERS usage: open astropy/units/quantity_helper/converters.py (around top, lines ~1-200) to see UfuncHelpers implementation and __getitem__/registration behavior
- [ ] 2. Inspect helper registry and helper functions: open astropy/units/quantity_helper/helpers.py to see how helpers are defined and mapped to ufuncs
- [ ] 3. Trace error message construction: find occurrences of the string
- [ ] 4. Locate tests referencing UFUNC_HELPERS: open astropy/units/tests/test_quantity_ufuncs.py to find tests that exercise UFUNC_HELPERS behavior and any failing cases
- [ ] 5. Reproduce failing ufunc scenario: prepare to run the specific test(s) or a small repro that triggers the error once the relevant code sections are understood
- [ ] 1. Locate UFUNC_HELPERS and UNSUPPORTED_UFUNCS definitions in astropy/units (which file and line)
- [ ] 2. Find code that populates UFUNC_HELPERS (search for assignments, registrations, or updates to that object)
- [ ] 3. Inspect UfuncHelpers.__missing__ implementation in astropy/units/quantity_helper/converters.py to confirm how it matches ufuncs and imports helper modules
- [ ] 4. Reproduce the incorrect UFUNC_HELPERS lookup with a minimal repro case to observe the error and key used
- [ ] 5. Implement and test a fix: modify __missing__ or registration so lookups succeed for ufunc objects; run unit tests for quantity helper ufunc behavior
- [ ] 1. Understand the current behavior: inspect UfuncHelpers.__missing__, UfuncHelpers.__setitem__, and the UFUNC_HELPERS.UNSUPPORTED set to determine how unsupported ufuncs are recorded and detected
- [ ] 2. Locate uses: search repository for usages of UFUNC_HELPERS, UNSUPPORTED_UFUNCS, and UfuncHelpers.register_module to find all code paths that rely on this registry
- [ ] 3. Reproduce problematic case: create minimal repro that triggers TypeError from UFUNC_HELPERS[ufunc] for a module-registered ufunc and capture the exact exception and traceback
- [ ] 4. Root cause analysis & implement fix: based on repro, modify __missing__ or __setitem__ (or related registration/import logic) to correctly distinguish unsupported ufuncs vs unknown ufuncs and ensure thread-safety
- [ ] 5. Verify fix: run relevant unit tests (units/quantity_helper, ufunc-related tests), add regression test for the reproduced case, and mark TODOs complete when passing
- [ ] 1. Reproduce the bug: create a minimal repro that triggers the TypeError related to UfuncHelpers.__setitem__ (likely from using a non-hashable key) and capture the exact traceback
- [ ] 2. Locate the code: search for all uses of UFUNC_HELPERS[...] and places that set entries (e.g., assignment to UFUNC_HELPERS, register_module importers); inspect astropy/units/quantity_helper/converters.py and any helper modules
- [ ] 3. Root cause analysis: inspect __setitem__, __missing__, register_module, and importer functions to determine what types are being used as keys and why a non-hashable key might be passed
- [ ] 4. Implement fix: modify code to ensure only hashable keys are used (e.g., convert keys to ufunc objects or use key.__name__ consistently) and add defensive checks/clear error messages; update importers if they return non-hashable keys
- [ ] 5. Verify fix: add a unit test reproducing the error, run the relevant tests (or minimal repro), and ensure the TypeError is resolved and no regressions occur
- [ ] 1. Clarify task: ask user for repository location (local path or remote URL), branch, and exact steps to reproduce the issue or the desired change
- [ ] 2. Obtain repository: clone or switch to provided repo/branch and install dependencies (specify commands to run)
- [ ] 3. Reproduce the bug: run provided reproduction steps and run the test suite (pytest) to capture failures
- [ ] 4. Locate failing code: identify failing tests, grep for relevant functions/files, and open the implicated source sections
- [ ] 5. Root cause analysis: inspect code paths, add temporary prints or run debugger to determine cause
- [ ] 6. Implement fix: modify code with minimal change and add/adjust tests that cover the issue
- [ ] 7. Verify fix: run unit tests and linters, ensure all tests pass locally
- [ ] 8. Prepare patch: run context_commit with a descriptive message and prepare a PR or patch file for review
- [ ] 1. Clarify the bug/task: ask user for repository path, failing test or reproduction steps, and expected behavior
- [ ] 2. Reproduce the bug: run the provided repro script or pytest to observe the failure and capture the exact error/traceback
- [ ] 3. Locate the code: search the repository for files/functions mentioned in the error/traceback and relevant symbols
- [ ] 4. Root cause analysis: inspect implicated functions, run targeted experiments, and identify the precise cause
- [ ] 5. Implement fix: modify code accordingly, add or update unit tests that exercise the failing behavior
- [ ] 6. Verify fix and cleanup: run full test suite, ensure all tests pass, create context_commit, and mark each TODO complete as steps finish
- [ ] 1. Reproduce the bug using the provided repro script or unit test
- [ ] 2. Locate the offending code: search repository for relevant functions/files and error text (use grep/rg)
- [ ] 3. Root cause analysis: inspect the identified code paths, exception handling, and failing tests to determine exact cause
- [ ] 4. Implement fix: modify the identified file(s), add/update unit/regression test(s), and document the change
- [ ] 5. Verify fix: run the repro and pytest for affected tests, record results, and mark TODOs complete with context_log entries
- [ ] 1. Clarify task: ask user to provide repository path or code, example input, expected behavior, and any failing tests or error messages
- [ ] 2. Prepare environment: once repo provided, install dependencies and run test suite (pytest) to reproduce failures
- [ ] 3. Locate failing code: search for stack traces, failing tests, or suspect functions/files to inspect
- [ ] 4. Root cause analysis: identify exact lines and logic causing the failure and propose a minimal change
- [ ] 5. Implement fix: modify the identified files/functions, run unit tests locally
- [ ] 6. Verify and document: run full test suite, produce patch/diff, and summarize changes for review
- [ ] 1. Reproduce the bug: run the provided repro script(s) or targeted pytest to obtain the exact stack trace and error message (e.g., repro.py or tests failing)
- [ ] 2. Locate the code: search the repository for __getattr__, __getattribute__, and related attribute-access code (grep -n \
- [ ] 3. Root cause analysis: inspect the found implementations for places that catch AttributeError (or swallow descriptor exceptions), identify where the wrong attribute name or exception is raised, and note interacting descriptors/properties
- [ ] 4. Implement fix: modify the attribute-access logic to allow descriptor/attribute-specific AttributeError to propagate (or detect true missing attribute), update error message to include correct attribute name, and add unit tests reproducing the original failure
- [ ] 5. Verify fix: run the repro script and full test suite (pytest), record results, and mark todos complete as each step finishes
- [ ] 1. Gather information from user: request reproduction steps, exact error messages/tracebacks, failing test names, and any relevant files or repro script
- [ ] 2. Reproduce the bug locally: run provided repro script or run the failing tests to get the exact failure
- [ ] 3. Locate the code: search repository for symbols/functions/classes mentioned in the traceback or error (e.g., __getattr__, function names)
- [ ] 4. Inspect candidate files: open code regions around grep hits to understand control flow and exception handling
- [ ] 5. Root cause analysis: determine where the error originates, whether exceptions are masked, and identify minimal code change to fix
- [ ] 6. Implement fix: make a minimal, well-documented code change and add a targeted unit test reproducing the bug
- [ ] 7. Verify fix: run full test suite and the repro to ensure no regressions; record test results
- [ ] 8. Prepare patch/PR: create a descriptive commit message and a PR description, but do not commit until final review step
- [ ] 1. Understand the bug: reproduce the reported AttributeError with a minimal test or repro script
- [ ] 2. Locate the code: search for __getattr__ and related attribute access in repository (e.g., astropy/coordinates/sky_coordinate.py, frame.py)
- [ ] 3. Root cause analysis: inspect __getattr__/property descriptors, identify where AttributeError is caught and potentially masked; determine if descriptors
- [ ] 4. Implement fix: adjust __getattr__ to check class descriptors first and ensure correct AttributeError is raised with the actual missing attribute name; add code comments explaining rationale
- [ ] 5. Verify fix: add regression tests reproducing the failure and run pytest (or relevant test subset) to confirm the fix and that no other tests regress
- [ ] 3. Root cause analysis: Inspect SkyCoord.__getattr__ in astropy/coordinates/sky_coordinate.py to determine whether it masks AttributeError raised by descriptors/properties (check getattr(self.frame, attr) and getattr(self,
- [ ] 4. Reproduce the bug: Create a minimal reproducer where a frame has a property/descriptor that raises AttributeError when accessed to see if SkyCoord.__getattr__ hides the original exception
- [ ] 5. Implement fix: Modify SkyCoord.__getattr__ to avoid catching/transforming AttributeError from descriptor/property access (e.g., check attribute existence on the class/type first or use object.__getattribute__ to detect presence) and add a comment explaining rationale
- [ ] 6. Verify fix: Run the minimal reproducer and relevant unit tests to ensure the original AttributeError is propagated and no regressions occur
- [ ] 1. Understand the bug: reproduce the AttributeError when accessing frame attribute descriptors (capture a minimal repro case and exact error message)
- [ ] 2. Locate the code: find TransformGraph.frame_attributes and all usages in astropy/coordinates (start with baseframe.py, sky_coordinate_parsers.py, sky_coordinate.py, and builtin_frames)
- [ ] 3. Root cause analysis: inspect TransformGraph.frame_attributes implementation and any frame attribute descriptors in BaseCoordinateFrame subclasses to see if accessing them triggers AttributeError
- [ ] 4. Implement fix: modify code to avoid invoking descriptor __get__ that can raise AttributeError (options: check names without getattr, adjust frame_attributes to store plain names, or catch and re-raise appropriate errors)
- [ ] 5. Verify fix: run targeted unit tests for coordinates and the failing repro case (e.g., pytest -q astropy/coordinates/tests/test_sky_coord.py::... and other tests referencing frame_transform_graph)
- [ ] 1. Understand the bug: ask user for reproduction steps and exact error/stack trace; attempt to reproduce locally by running the provided repro script or the test(s) that fail
- [ ] 2. Locate the code: search the repository for symbols/names in the stack trace (use grep -n for function/class names and filenames); identify candidate files and line ranges to inspect
- [ ] 3. Root cause analysis: open the identified files, inspect the surrounding code (especially exception handling, descriptors, and __getattr__-like methods), and note the exact line causing the error
- [ ] 4. Implement fix: make a minimal, well-documented code change to fix the root cause, add a unit test that reproduces the bug before the fix, and run linters/formatters
- [ ] 5. Verify fix: run the failing test(s) and the full test suite, confirm all tests pass, update changelog/commit message, and mark TODOs complete as steps finish
- [ ] 1. Understand the task: ask user for repository (git URL or path), failing test or error message, reproduction steps, target branch, and expected behavior
- [ ] 2. Prepare environment: identify language/runtime, list required tools, and ensure tests can be run (e.g., run pytest or provided repro script)
- [ ] 3. Reproduce the bug: run provided repro steps or test suite to observe failure and capture full error output
- [ ] 4. Locate the code: grep for error strings, related function/class names, and open relevant source files for inspection
- [ ] 5. Root cause analysis: trace stack, inspect inputs/outputs, and identify minimal failing code path
- [ ] 6. Implement fix: make minimal, well-documented change and add/adjust tests to cover the case
- [ ] 7. Verify fix: run full test suite, linting, and any repro scripts to ensure no regressions
- [ ] 8. Checkpoint: context_commit with a descriptive message and mark completed TODOs as steps finish
- [ ] 1. Understand the bug: reproduce how adding a structured numpy.ndarray to an astropy.table.Table causes the data to be auto-converted into an NdarrayMixin column; create a minimal repro script and capture exact observed behavior
- [ ] 2. Locate the code: search the repo for
- [ ] 3. Root cause analysis: inspect the identified conversion logic to determine why structured dtype triggers conversion; record exact file/line ranges and rationale for change (deprecate auto-conversion vs preserve behavior)
- [ ] 4. Implement fix: modify the conversion clause to emit a FutureWarning advising users to wrap structured ndarrays with astropy.table.Column(...), keep current behavior for now, and prepare a minimal patch with comments linking to the issue
- [ ] 5. Verify fix: add astropy/table/tests/test_structured_deprecation.py that asserts a FutureWarning when adding structured ndarray and verifies column remains NdarrayMixin; run pytest -q astropy/table and record results
- [ ] 2. Locate the code: inspect astropy/table/table.py around the warning at line ~1247 and astropy/table/ndarray_mixin.py to find where view(NdarrayMixin) is used and how NdarrayMixin is defined
- [ ] 3. Root cause analysis: analyze why structured numpy.ndarray is being viewed as NdarrayMixin, what behavior that preserves, and why it
- [ ] 4. Implement fix: change the code path to wrap structured arrays in astropy.table.Column(...) instead of viewing them as NdarrayMixin, preserving dtype and behavior where reasonable; update warning text if needed
- [ ] 5. Verify fix: run repro.py to ensure no FutureWarning and correct column type/behavior, and run astropy/table/tests/test_structured_deprecation.py (and related mixin tests) to confirm no regressions

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 01:15] **swebench-astropy__astropy-13236**: Record structured-array test results: 8 passed, 2 skipped, 2114 deselected
- [2025-12-02 01:15] **swebench-astropy__astropy-13236**: Insert FutureWarning when viewing structured numpy.ndarray as NdarrayMixin in astropy/table/table.py...
## Interaction Log

- `01:33:21` ACTION: python3 - <<'PY'
- `01:33:04` ndarray_mixin.py:1-240: defines NdarrayMixin as subclass of np.ndarray; info = NdarrayMixinInfo; __new__ uses np.array(obj,...).view(cls); __array_fin...
- `01:33:04` table.py:1200-1260: shows FutureWarning 'Viewing a structured numpy.ndarray as an NdarrayMixin is deprecated and will be removed in a future release. ...
- `01:32:50` ACTION: sed -n '1200,1260p' astropy/table/table.py && sed -n '1,240p' astropy/table/ndarray_mixin.py
- `01:32:28` ACTION: (grep -nR "Viewing a structured numpy.ndarray as an NdarrayMixin" astropy || true) && (grep -nR "Nda [...]
- `01:32:20` repro.py: class MRO of column: ('NdarrayMixin', 'ndarray', 'object')
- `01:32:20` repro.py: isinstance(..., NdarrayMixin): True
- `01:32:20` repro.py: t['col'] repr: NdarrayMixin([(1, 2.), (3, 4.)], dtype=[('x', '<i4'), ('y', '<f8')])
- `01:32:20` repro.py: t['col'] type: <class 'astropy.table.ndarray_mixin.NdarrayMixin'>
- `01:32:20` repro.py warning: /testbed/astropy/table/table.py:1247: FutureWarning: Viewing a structured numpy.ndarray as an NdarrayMixin is deprecated and will be...
- `01:32:06` ACTION: Reading file: <<'PY'
- `01:31:13` ACTION: printf "Please fill this template and paste it back:\n\n1) Repository (git URL or local path):\n\n2) [...]
- `01:31:03` ACTION: printf "Please provide the following so I can reproduce and fix the issue:\n\n1) Repository git URL  [...]
- `01:30:38` ACTION: echo "Please provide: 1) repository git URL or local path, 2) failing test name or full error output [...]
- `01:30:16` ACTION: grep -nR -e "__getattr__" -e "__getattribute__" astropy || true
- `01:30:06` ACTION: ls -la
- `01:29:42` ACTION: grep -Rn "frame_attributes" . || true && grep -Rn "class TransformGraph" . || true
- `01:29:15` ACTION: grep -n "frame_transform_graph" -R astropy/coordinates || true
- `01:28:57` ACTION: sed -n '800,920p' astropy/coordinates/sky_coordinate.py
- `01:28:51` grep __getattr__: ./astropy/coordinates/sky_coordinate.py:829, ./astropy/coordinates/sky_coordinate.py:862, ./astropy/coordinates/sky_coordinate.py:87...
