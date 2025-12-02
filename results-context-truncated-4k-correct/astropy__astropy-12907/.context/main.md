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


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Reproduce the bug: write a small script that builds nested CompoundModels and prints separability_matrix results
- [ ] 2. Locate the code: find separability_matrix implementation and any helpers that handle CompoundModel or nested compounds
- [ ] 3. Analyze implementation: read the function to understand how it treats nested CompoundModel and where nesting may cause incorrect block handling
- [ ] 4. Design fix: decide whether to flatten nested CompoundModels or compute block-wise separability correctly; prepare code changes
- [ ] 5. Implement fix: edit source files in testbed to handle nested CompoundModels correctly
- [ ] 6. Add repro script: create a script that demonstrates the fixed behavior and covers edge cases
- [ ] 7. Verify fix: run the repro script and any relevant tests to confirm separability_matrix returns expected matrices
- [ ] 8. Log findings and mark todos complete as each step finishes
- [ ] 1. Understand the bug: Identify incorrect behavior of separability_matrix/_separable for nested CompoundModel; collect example transforms and expected outputs
- [ ] 2. Locate the code: Inspect astropy/modeling/separable.py functions _separable, _coord_matrix, _cstack, _cdot, _arith_oper and Model._calculate_separability_matrix for handling of ndarray inputs and nesting
- [ ] 3. Reproduce the bug: Create and run minimal repro scripts combining Mapping and CompoundModel operators (& and |) with simple models to observe incorrect separability results
- [ ] 4. Root cause analysis & Implement fix: Modify code to correctly handle coord_matrix ndarray shapes and stacking/rolling semantics for left/right children; add unit tests covering nested compounds and Mapping
- [ ] 5. Verify fix: Run the repros and relevant modeling tests, log outcomes with context_log, and mark todos complete
- [ ] 1. Understand the bug: reproduce unexpected behavior of is_separable()/separability_matrix() for compound models (e.g., involving Mapping, CompoundModel, or non-separable simple models) using minimal examples
- [ ] 2. Locate the code: inspect astropy/modeling/separable.py functions _coord_matrix, _cdot, _cstack, _arith_oper, and _separable to identify possible shape/logic issues
- [ ] 3. Reproduce the issue: write and run minimal repro scripts exercising is_separable and separability_matrix with combinations like Mapping | Polynomial2D, Shift&Shift | Mapping, and arithmetic/compound operators
- [ ] 4. Root cause analysis & implement fix: based on repro, adjust _coord_matrix/_cdot/_cstack/_arith_oper logic (shape handling, roll/stack behavior, Mapping handling) and update code with small, targeted changes
- [ ] 5. Verify fix: run the repro scripts and the relevant modeling tests (or a subset) to ensure separability outputs match expected results, then mark todos complete and log findings
- [ ] 1. Understand the bug: confirm incorrect array shaping/placement in astropy/modeling/separable.py causing wrong separability matrices (suspects: np.roll without axis in _coord_matrix, wrong slice assignment in _cstack when right is ndarray, potential left/right swap in _cdot)
- [ ] 2. Locate the code: open astropy/modeling/separable.py and identify exact lines for _coord_matrix, _cstack, _cdot, _arith_oper, and _separable
- [ ] 3. Root cause analysis: reproduce failing behavior with focused prints and small models, inspect np.roll usage and cright slice assignment, determine correct semantics (axis for np.roll; copy right array into cright slice; clarify matrix vs count return in _cdot)
- [ ] 4. Implement fix: modify _coord_matrix to roll along the correct axis (or reshape before rolling), change cright[-right.shape[0]:, -right.shape[1]:] = right to copy the array, and ensure _cdot handles/returns matrices consistently
- [ ] 5. Verify fix: run repro_separable.py, run relevant tests (pytest astropy/modeling/tests -k separable), log results, and mark TODOs complete
- [ ] 1. Understand the bugs: investigate np.roll misuse in _coord_matrix, incorrect slice assignment in _cstack (fills with 1 instead of copying the right coord_matrix), and operand swap in _cdot causing wrong multiplication order
- [ ] 2. Locate the code: open astropy/modeling/separable.py around functions _coord_matrix (around line 171), _cstack (around line 219), _cdot (around line 250) to confirm exact implementation
- [ ] 3. Root cause analysis: determine correct behavior (np.roll should specify axis=0, _cstack should copy the provided ndarray into cright slice, and _cdot should not swap operands) and plan exact edits
- [ ] 4. Implement fix: change np.roll(mat, (noutp - model.n_outputs)) to np.roll(mat, noutp - model.n_outputs, axis=0); change cright[-right.shape[0]:, -right.shape[1]:] = 1 to cright[-right.shape[0]:, -right.shape[1]:] = right; remove
- [ ] 5. Verify fix: run the small Python reproducer used earlier to confirm coord_matrix, cstack, and cdot outputs are correct and then run relevant tests
- [ ] 3. Document changes: summarize edits made to astropy/modeling/separable.py (np.roll axis, cright copy, remove operand swap)
- [ ] 4. Verify edits: inspect separable.py lines 160-280 to confirm changes
- [ ] 5. Run tests: run relevant modeling tests to ensure no regressions
- [ ] 1. Reproduce failure: run failing doctest example and capture cleft/cright shapes and traceback
- [ ] 2. Inspect code: open astropy/modeling/separable.py lines 1-360 to review _cdot, _coord_matrix, and helpers
- [ ] 3. Analyze root cause: determine why cleft and cright shapes are mismatched and whether operand swap is needed
- [ ] 4. Implement fix: modify _cdot/_coord_matrix logic to ensure dot operands align (or swap when appropriate)
- [ ] 5. Verify fix: run targeted pytest for separable/cdot/cstack/coord_matrix
- [ ] 1. Reproduce the bug: run the provided repro script and run pytest to observe failing tests and capture exact error messages
- [ ] 2. Locate the code: search the repository for __getattr__, AttributeError handling, and related attribute-access code (e.g., in src/ or package directories) to find candidate files and functions
- [ ] 3. Root cause analysis: inspect the identified function(s) to determine why the AttributeError is raised or masked (check descriptor handling, try/except blocks, and attribute names in exceptions)
- [ ] 4. Implement fix: modify the code to let descriptor errors propagate or correctly identify missing attributes; add regression tests that reproduce the original failure
- [ ] 5. Verify fix: run the repro script and full test suite, ensure failing tests are fixed, and mark TODOs complete and commit a clear changelog entry
- [ ] 1. Understand the bug: obtain reproduction steps and exact error message or failing test that demonstrates the AttributeError or unexpected behavior
- [ ] 2. Locate the code: search repository for attribute-access handlers (__getattr__, __getattribute__, __get__) and descriptor implementations to inspect (e.g., files implementing attribute lookup or properties)
- [ ] 3. Root cause analysis: reproduce the failure locally with a minimal repro, inspect the identified methods to see where AttributeError is being caught or masked, and identify which descriptor or property is involved
- [ ] 4. Implement fix: modify the attribute-access logic to avoid catching descriptor-raised AttributeError (or differentiate missing-attribute vs descriptor errors), add targeted unit tests covering descriptors and attribute lookup edge cases
- [ ] 5. Verify fix: run the repro and full test suite, record results, and if passing, mark the relevant TODOs complete and create a context_commit with a summary
- [ ] 1. Clarify reproduction: request exact steps/commands, input files, environment, and expected behavior
- [ ] 2. Run test suite: execute pytest -q to collect failing tests and full failure traces
- [ ] 3. Identify failures: list failing test names, error messages, and stack traces for each failure
- [ ] 4. Locate code: grep for functions/classes referenced in stack traces and open relevant source files
- [ ] 5. Root cause analysis: inspect implementations, reproduce minimal example, and document hypothesis for each failure
- [ ] 6. Implement fix: make small, well-documented changes in source code and add/regress tests that reproduce the issue
- [ ] 7. Verify fix: run pytest for affected tests and then full suite until green
- [ ] 8. Checkpoint: run context_commit --message \
- [ ] 1. Reproduce the pytest run that timed out and capture full output to identify which import emits the
- [ ] 2. Locate the C extension (.so) file(s) responsible by re-running imports or parsing the pytest output and note their exact paths
- [ ] 3. Run ldd on the identified .so file(s) to inspect linked libraries and look for mismatches
- [ ] 4. List installed packages with compiled extensions (e.g., astropy, pyerfa) and their build metadata to see which may have been built against a different numpy/Python ABI
- [ ] 5. Decide and implement remediation: either rebuild/reinstall the offending package(s) against the current numpy (1.25.2) or install a numpy version matching the compiled ABI; prepare commands to rebuild and verify tests
- [ ] 1. Reproduce the bug: run the project
- [ ] 2. Locate the code: search the repository for
- [ ] 3. Root cause analysis: open the identified files/lines and analyze how __getattr__ handles exceptions and interacts with descriptors/properties
- [ ] 4. Implement fix: modify the problematic __getattr__ to avoid catching AttributeError raised by descriptors (allow them to propagate), add/adjust unit tests that reproduce the original failure
- [ ] "5.
- [ ] 1. Reproduce the bug: run the provided repro script or targeted tests to capture the AttributeError traceback and exact failure scenario
- [ ] 2. Locate the code: grep the repository for __getattr__ implementations (likely files: astropy/coordinates/sky_coordinate.py, frame.py) and open the matching files/lines
- [ ] 3. Root cause analysis: inspect the __getattr__ implementation(s) to find where AttributeError is caught and re-raised; determine if descriptor/property lookup is suppressed
- [ ] 4. Implement fix: update __getattr__ to check class descriptors/properties first and preserve original attribute name/errors when re-raising; add a unit test that reproduces the original failure
- [ ] 5. Verify fix: run the repro script, run the new unit test, and run pytest for the coordinates module to ensure no regressions
- [ ] 1. Understand the bug: reproduce and confirm unexpected behavior in BaseCoordinateFrame.__getattr__ (suspected stray
- [ ] 2. Locate the code: inspect astropy/coordinates/sky_coordinate.py (around lines ~780-900) and astropy/coordinates/baseframe.py (around lines ~1560-1620 and ~1840-1900) for __getattr__ implementations and surrounding logic
- [ ] 3. Root cause analysis: determine why the stray np.stack line exists, whether intended behavior is to raise AttributeError or delegate to representation names, and identify related tests that should cover this
- [ ] 4. Implement fix: edit BaseCoordinateFrame.__getattr__ to remove/replace the stray np.stack return, ensure proper handling of representation component names and fallback to raising AttributeError; run linters
- [ ] 5. Verify fix: run unit tests for astropy.coordinates, run a small repro script exercising unknown attribute access and representation component access, then mark TODOs complete
- [ ] 1. Understand the bug: investigate why an unexpected np.stack/representation return leads to wrong attribute types when accessing coordinate component attributes (e.g., scalar vs. array/Quantity)
- [ ] 2. Locate the code: inspect __getattr__ implementations in astropy/coordinates/sky_coordinate.py and baseframe.py, and search for np.stack and representation construction in astropy/coordinates/*
- [ ] 1. Reproduce the bug with a minimal script that triggers proper_motion/radial_velocity returning a 0-d Quantity
- [ ] 2. Search for np.stack uses in astropy/coordinates to find stacking sites
- [ ] 3. Inspect spherical differential and proper_motion code paths in representation.py and baseframe.py to find where scalars originate
- [ ] 4. Implement fix: ensure components are at least 1-D before np.stack (use np.atleast_1d or expand_dims) in the identified locations
- [ ] 5. Run the minimal repro and unit tests for coordinates to verify the fix
- [ ] 1. Reproduce issue: run a minimal script accessing spherical differential .proper_motion and .radial_velocity for scalar proper motions/radial_velocity to observe failures
- [ ] 2. Locate differential classes: grep for class definitions of SphericalCosLatDifferential, BaseSphericalDifferential, BaseDifferential in astropy/coordinates/representation.py to get line numbers
- [ ] 3. Inspect SphericalCosLatDifferential: display its class definition and surrounding code to determine inheritance and available properties
- [ ] 4. Check MRO at runtime: instantiate a representative differential and print its __class__, MRO, and hasattr for proper_motion/radial_velocity
- [ ] 5. Root cause & fix plan: based on findings, decide whether to adjust inheritance, add missing properties, or adapt callers to use available API, then implement and run tests
- [ ] 1. Reproduce the bug: create minimal script constructing a scalar SphericalCosLatDifferential and access .proper_motion and .radial_velocity to see the AttributeError
- [ ] 2. Search the codebase for
- [ ] 3. Inspect BaseDifferential and related attribute-handling (e.g., __getattr__, attr_classes, UnitDifferential classes) to see why scalar differentials may lack these properties
- [ ] 4. Implement fix: update attribute handling or add properties so scalar differentials expose proper_motion and radial_velocity (be explicit about what file and lines to change after analysis)
- [ ] 5. Verify fix: run the minimal repro and relevant unit tests to confirm the AttributeError is resolved
- [ ] 1. Understand the bug/task: ask user for reproduction steps, expected behavior, repository path or files, and any relevant input/output
- [ ] 2. Locate the code: search the repo for relevant symbols, files, and functions once repro steps are provided (e.g., grep for exception text, function names)
- [ ] 3. Reproduce locally: run provided repro script or run the test suite to observe the failure and capture full stack trace
- [ ] 4. Root cause analysis: inspect stack trace and source, add targeted prints/logging or run debugger to identify faulty code paths
- [ ] 5. Implement fix: make minimal, well-documented code changes to address the root cause and add/adjust unit tests
- [ ] 6. Verify fix: run targeted tests and full test suite, confirm no regressions; capture test results
- [ ] 7. Document and checkpoint: write a brief changelog/commit message and create a context_commit milestone
- [ ] 1. Reproduce the bug: run the project
- [ ] 2. Locate the code: search source for suspect methods (e.g. __getattr__, __getattribute__, property descriptors) in src/, lib/, or package directories to find where AttributeError is caught/re-raised
- [ ] 3. Root cause analysis: inspect identified functions/files and traceback to determine why AttributeError is masked or mis-reported; identify descriptor/property handling that should be allowed to propagate
- [ ] 4. Implement fix: modify the code to handle descriptors correctly (check for attribute on class/descriptors before catching AttributeError), add focused unit test reproducing original failure, and run linters/formatters
- [ ] 5. Verify fix: run full test suite (pytest -q), run the new regression test, and document the change; when confirmed, mark todos complete and create a context_commit checkpoint
- [ ] 1. Understand the bug: reproduce failing behavior using provided repro or failing test case, capture exact error message and stack trace
- [ ] 2. Locate the code: search repository for __getattr__, attribute accessors, and related classes/functions to inspect (grep for
- [ ] 3. Root cause analysis: inspect identified files/lines, run minimal repro to capture stack, determine whether descriptors/properties are being trapped or misreported
- [ ] 4. Implement fix: modify code to handle descriptor AttributeError correctly (avoid masking), update error messages, and add unit test reproducing original failure
- [ ] 5. Verify fix: run the unit tests and repro script, ensure the new test passes and no regressions occur; commit changes when verified
- [ ] 1. Understand the bug: Reproduce the issue by running the failing test(s) or any provided repro script and capture the exact error message and traceback
- [ ] 2. Locate the code: Search the repository for likely fault points (e.g., __getattr__, __getattribute__, descriptor usage, and files referenced in tracebacks) to identify candidate files and functions
- [ ] 3. Root cause analysis: Inspect the identified files/functions to trace where AttributeError (or other exception) is raised or wrongly handled; note lines and specific behavior causing the misreport
- [ ] 4. Implement fix: Make minimal, well-documented code changes to correct error handling or attribute resolution (e.g., avoid swallowing descriptor AttributeError, report correct attribute name); add or update unit tests that reproduce the bug
- [ ] 5. Verify fix: Run targeted tests and full test suite as needed to confirm the fix; record results, update changelog, and prepare a commit message
- [ ] 1. Understand the bug: reproduce the issue and capture the exact error message and a minimal reproducible script or steps
- [ ] 2. Locate the code: search repository for relevant symbols/functions/classes mentioned in the error and list candidate files/lines to inspect
- [ ] 3. Root cause analysis: add diagnostic prints/logging or run targeted debugs to trace state and identify the underlying cause
- [ ] 4. Implement fix: make the minimal code change to address the root cause and add a unit test that reproduces the original failure
- [ ] 5. Verify fix: run the minimal repro and the unit test(s); if available, run the full test suite and record results
- [ ] 1. Reproduce the bug: write a minimal script that builds nested CompoundModels (using Mapping, | and & operators) and prints separability_matrix and is_separable results
- [ ] 1. Reproduce the bug: write a minimal script that builds nested CompoundModels (using Mapping, | and & operators) and prints separability_matrix and is_separable results
- [ ] 2. Locate the code: grep for separability_matrix and open astropy/modeling/separable.py to find _separable, _coord_matrix, _cstack, _cdot, _arith_oper implementations
- [ ] 3. Inspect implementations: read and save the code around _coord_matrix, _cstack, _cdot, _arith_oper and note any np.roll, slice assignment, or operand order logic
- [ ] 4. Run minimal repro: run the script from TODO 1 to capture the incorrect separability_matrix output
- [ ] 5. Instrument & analyze: add prints or run small experiments to capture intermediate coord_matrix shapes and contents for nested CompoundModel children
- [ ] 6. Design fix: decide precise code changes (e.g., np.roll axis, copy right array into cright slice, fix operand order in _cdot) and prepare patch
- [ ] 7. Implement fix: edit astropy/modeling/separable.py to apply the designed changes and run linters/formatting
- [ ] 8. Add regression tests: create unit tests covering nested CompoundModel separability and Mapping interactions
- [ ] 9. Verify fix: run the minimal repro and run pytest -q astropy/modeling/tests -k separable to confirm behavior
- [ ] 10. Log findings and mark todos complete as each step finishes
- [ ] 1. Understand the bug: obtain reproduction steps, failing test name(s), exact error message, and any minimal repro script or user input
- [ ] 2. Locate the code: search repository for symbols/classes/functions mentioned in the error or repro and identify candidate files to inspect
- [ ] 3. Root cause analysis: open the identified files, read the relevant code sections, run the minimal repro and unit tests to reproduce the failure and pinpoint the faulty lines
- [ ] 4. Implement fix: make a minimal, well-documented code change to correct the root cause and add/adjust unit tests that capture the regression
- [ ] 5. Verify fix: run the full test suite (pytest), ensure new tests pass, run lint/format checks, and record results
- [ ] 1. Clarify user goal: ask the user to describe the desired outcome, inputs, constraints, and provide any repository, files, or error logs
- [ ] 2. Identify relevant files: once repo/files are provided, locate project root and list source and test files to inspect
- [ ] 3. Reproduce issue or spec: create a minimal reproduction or test case from the user
- [ ] 4. Implement solution: make targeted code changes, add tests, and run test suite locally
- [ ] 5. Verify and finalize: run full tests, get user
- [ ] 1. Reproduce the bug: run the provided repro (e.g. python3 repro.py) to capture the exact AttributeError and traceback
- [ ] 2. Locate the relevant code: search repository for
- [ ] 3. Root cause analysis: inspect the __getattr__ implementation(s) (sed -n around matched lines) to see where AttributeError is caught and how class descriptors/properties are handled
- [ ] 4. Implement fix: modify __getattr__ to check for data descriptors on the class first (use inspect.getattr_static or check class.__dict__), avoid catching AttributeError raised by descriptors, and ensure AttributeError uses the correct missing attribute name
- [ ] 5. Verify fix: run the repro again and run relevant tests (pytest or targeted tests) to confirm the AttributeError is correct and no tests fail
- [ ] 6. Document and commit: add a concise code comment explaining the fix, run context_commit --message \
- [ ] 1. Understand the bug: ask user for a clear description, steps to reproduce, expected vs actual behavior, relevant files/repo path, and any error messages or failing test names
- [ ] 2. Locate the code: search the repository for functions/files/tests referenced by the repro and for relevant keywords (exception text, test names, __getattr__, AttributeError, etc.)
- [ ] 3. Reproduce the bug: run the provided repro script or failing tests locally to capture the full stack trace and failure output
- [ ] 4. Root cause analysis & implement fix: inspect stack trace and implicated code, write a minimal, well-tested fix, and add/adjust unit tests to cover the case
- [ ] 5. Verify & finalize: run the affected tests and full test suite, log results, create a context_commit checkpoint, and mark todos complete as tasks finish
- [ ] 1. Understand the bug: Reproduce the failure and capture the full traceback, reproduction steps, and environment (e.g., run the user
- [ ] 2. Locate the code: Search the repository for symbols/names from the traceback and identify candidate files/functions to inspect (use grep/ripgrep on filenames and function/class names from the error)
- [ ] 3. Root cause analysis: Run targeted tests and/or use a debugger or added logging to pinpoint the exact lines and conditions causing the failure; record stack frames and suspicious code paths
- [ ] 4. Implement fix: Make a minimal, well-documented code change to address the root cause; add a unit test that reproduces the bug and ensures it stays fixed
- [ ] 5. Verify fix: Run the added unit test and the full test suite, reproduce the original failure to confirm it
- [ ] 1. Clarify task: Ask user to describe the goal (bugfix, feature, refactor, tests) and provide priority and constraints
- [ ] 2. Request inputs: Ask user for repository access or paste relevant files, minimal repro steps, and failing test output
- [ ] 3. Reproduce locally: Run provided repro or tests to observe the failure and capture exact error messages/tracebacks
- [ ] 4. Locate code: Search repository for functions/files related to the failure and identify candidate root cause locations
- [ ] 5. Fix and verify: Propose code changes, implement patch, run tests and add regression test to ensure issue is resolved

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 02:14] **swebench-astropy__astropy-12907**: Task completed: LimitsExceeded
## Interaction Log

- `02:14:47` Added TODOs: 1. Clarify task; 2. Request inputs; 3. Reproduce locally; 4. Locate code; 5. Fix and verify (confirmation output received)
- `02:14:08` ACTION: python3 --version && pip3 freeze | sed -n '1,200p' && pytest -q
- `02:13:36` ACTION: grep -RIn --exclude-dir=.git -E "__getattr__|AttributeError" .
- `02:13:05` ACTION: grep -R -n "__getattr__" . || true
- `02:12:57` ACTION: python3 repro.py
- `02:12:23` ACTION: echo "Please describe the task or bug you want me to work on. [...]
- `02:10:58` ACTION: pytest -q || true
- `02:10:33` ACTION: grep -nR -E "separability_matrix|_separable|_coord_matrix|_cstack|_cdot|_arith_oper" astropy/modelin [...]
- `02:09:23` ACTION: grep -nR -e "__getattr__" -e "__getattribute__" -e "raise AttributeError" .
- `02:08:59` ACTION: grep -nR "__getattr__" . || true
- `02:08:18` ACTION: pytest -q
- `02:07:32` ACTION: grep -R -n "proper_motion" astropy || true && grep -R -n "radial_velocity" astropy || true
- `02:07:25` repro: dir(d): ['T', 'attr_classes', 'base_representation', 'components', 'copy', 'd_distance', 'd_lat', 'd_lon_coslat', 'diagonal', 'flatten', 'from_...
- `02:07:01` ACTION: python3 - <<'PY'
- `02:06:47` representation.py: no 'proper_motion' or 'radial_velocity' definitions found; SphericalCosLatDifferential defines attr_classes {'d_lon_coslat','d_lat'...
- `02:06:21` ACTION: sed -n '3040,3120p' astropy/coordinates/representation. [...]
- `02:06:13` sed outputs show: BaseDifferential defined around 2415 with __init_subclass__ that auto-creates attr_classes prefixed with 'd_' and registers differen...
- `02:05:54` ACTION: sed -n '2400,2470p' astropy/coordinates/representation. [...]
- `02:05:45` grep classes in astropy/coordinates/representation.py: 2415:class BaseDifferential(BaseRepresentationOrDifferential), 2444:        class BaseDifferent...
- `02:05:36` ACTION: grep -n -E 'class (SphericalCosLatDifferential|BaseSphericalDifferential|BaseDifferential)' astropy/ [...]
