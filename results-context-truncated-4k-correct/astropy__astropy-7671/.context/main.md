# Project Goals

**Current Task:** minversion failures

<details>
<summary>Full description</summary>

minversion failures
The change in PR #7647 causes `minversion` to fail in certain cases, e.g.:
```
>>> from astropy.utils import minversion
>>> minversion('numpy', '1.14dev')
TypeError                                 Traceback (most recent call last)
<ipython-input-1-760e6b1c375e> in <module>()
      1 from astropy.utils import minversion
----> 2 minversion('numpy', '1.14dev')

~/dev/astropy/astropy/utils/introspection.py in minversion(module, version, inclusive, version_path)
    144
    145     if inclusive:
--> 146         return LooseVersion(have_version) >= LooseVersion(version)
    147     else:
    148         return LooseVersion(have_version) > LooseVersion(version)

~/local/conda/envs/photutils-dev/lib/python3.6/distutils/version.py in __ge__(self, other)
     68
...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: reproduce TypeError using minversion(
- [ ] 2. Locate the code: find the minversion function implementation in the repo (e.g., astropy/utils/introspection.py or equivalent in testbed)
- [ ] 3. Root cause analysis: inspect how versions are compared and where LooseVersion is used; check for removal of pkg_resources.parse_version
- [ ] 4. Implement fix: modify minversion to use packaging.version.parse (with fallback to pkg_resources or safe parsing) and update imports
- [ ] 5. Verify fix: run the reproduction script and relevant tests to ensure comparisons with
- [ ] 1. Understand the bug: investigate duplicate minversion definitions and how they differ (version parsing, version_path handling)
- [ ] 2. Locate the code: find exact files and line ranges for all minversion implementations (introspection.py and astropy_helpers/utils.py)
- [ ] 3. Determine runtime behavior: find which minversion is actually imported/used at runtime and why (module import order, shadowing)
- [ ] 4. Implement fix: consolidate/remove duplicate, ensure parse_version from pkg_resources used when available and version_path resolution is consistent
- [ ] 5. Verify fix: run unit tests that exercise minversion and any import-time checks; add a regression test for dotted version_path handling
- [ ] 1. Confirm duplicate minversion definitions: grep for
- [ ] 2. Inspect both implementations in astropy/utils/introspection.py: open the file ranges containing both definitions to compare code and docstrings
- [ ] 3. Inspect astropy_helpers/astropy_helpers/utils.py minversion: open surrounding lines to compare behavior (version resolution and parse method)
- [ ] 4. Decide canonical implementation and implement fix: remove duplicate definition in introspection.py or refactor to a single shared implementation (prefer the one using pkg_resources.parse_version), update imports and docstrings accordingly
- [ ] 5. Verify fix: run grep to ensure only one
- [ ] 2. Inspect helper minversion implementation in astropy_helpers/astropy_helpers/utils.py (confirm behavior and differences)
- [ ] 3. Compare minversion implementations in astropy/utils/introspection.py and astropy_helpers; enumerate differences (version_path resolution, version parsing function)
- [ ] 4. Decide canonical behavior and implement fix to make implementations consistent
- [ ] 5. Create and run minimal tests to verify minversion behavior (including nested version_path and pkg_resources vs LooseVersion cases)
- [x] 1. Confirm user
- [x] 2. Identify file and location: confirm which file produced the long output (e.g., astropy/utils/introspection.py) and determine target line ranges to view
- [ ] 3. Narrow search: run selective grep for likely keywords (e.g.,
- [ ] 4. Extract relevant sections: use sed/head/tail to display concise line ranges or function definitions once targets are known
- [ ] 5. Report findings and propose next steps (fix, tests, or further inspection) and mark TODOs complete as work progresses
- [ ] 1. Run minimal runtime test to verify _isinstancemethod no longer raises for missing name
- [ ] 2. Run astropy utils tests (if available)
- [ ] 1. Understand test failure: confirm failing test test_timer and exact traceback pointing to np.asscalar usage in astropy/modeling/core.py
- [ ] 2. Locate usages: grep the repo for
- [ ] 3. Inspect target file: open astropy/modeling/core.py around lines ~3260-3300 to review _prepare_outputs_single_model usage of np.asscalar
- [ ] 4. Implement fix: replace np.asscalar(a) with a.item() (or numpy.compat fallback) in modeling/core.py and any other occurrences; ensure compatibility with older numpy versions if needed
- [ ] 5. Verify fix: run pytest for astropy/modeling and astropy/utils to ensure the DeprecationWarning is gone and tests pass
- [ ] 1. Gather reproduction info: ask user for repo path, failing test names or stack trace, exact steps to reproduce, and expected behavior
- [ ] 2. Prepare environment: clone or open repository, install dependencies, identify project root, and run test command to reproduce failure (e.g., pytest -q)
- [ ] 3. Locate failing code: search for functions/classes mentioned in stack trace or tests (use grep/rg), and list candidate files and lines
- [ ] 4. Root cause analysis: run targeted reproducer(s), inspect implicated file regions, and determine why behavior differs from expectation
- [ ] 5. Implement fix & tests: modify code to fix root cause, add or update unit tests covering the failure, and run targeted tests
- [ ] 6. Verify & prepare patch: run full test suite, ensure all tests pass, create a clear changelog/commit message, and prepare patch for review (do not commit before final submission)
- [ ] 1. Reproduce the TypeError: create and run a minimal repro that calls minversion(...) with the failing version_path and capture the full traceback
- [ ] 2. Locate all minversion implementations: grep the repo for
- [ ] 3. Inspect astropy/utils/introspection.py minversion: open the function definition and surrounding lines for comparison
- [ ] 4. Inspect astropy_helpers/astropy_helpers/utils.py minversion: open the function definition and surrounding lines for comparison
- [ ] 5. Root cause analysis: compare parsing logic and version_path handling between implementations; identify where TypeError arises and whether packaging.version.parse vs LooseVersion/pkg_resources is used
- [ ] 6. Implement fix: update the canonical minversion to use packaging.version.parse with a safe fallback and ensure dotted version_path handling is correct; add a regression test for the failing case
- [ ] 7. Verify fix: run the reproduction script and run targeted pytest for astropy/utils and any tests exercising minversion; mark TODOs complete as work progresses
- [ ] 1. Reproduce the TypeError: write a small Python script that calls both astropy.utils.introspection.minversion and astropy_helpers.astropy_helpers.utils.minversion with a module whose __version__ is non-string (e.g. None or a tuple) and run it
- [ ] 2. Compare implementations: inspect both minversion functions to list exact differences in version_path resolution and version parsing logic
- [ ] 3. Root cause analysis: determine why astropy.utils.introspection.minversion raises TypeError (e.g. parsing choice, NoneType passed to LooseVersion) and note where to change behavior
- [ ] 4. Implement fix: modify astropy/utils/introspection.py to use pkg_resources.parse_version when available and coerce or validate have_version to a string with clear error message if invalid
- [ ] 5. Verify fix: run the repro script and relevant tests to confirm the TypeError is resolved and behavior matches astropy_helpers implementation
- [ ] 2. Locate and inspect minversion in astropy/utils/introspection.py: identify how version_path is resolved and which version parser (LooseVersion) is used
- [ ] 3. Locate and inspect minversion in astropy_helpers/astropy_helpers/utils.py: identify how version_path is resolved and which version parser (pkg_resources.parse_version fallback to LooseVersion) is used
- [ ] 4. Identify the behavioral discrepancy: check differences in resolve_name usage when version_path contains dots and how AttributeError/ImportError are handled
- [ ] 5. Create a minimal repro that uses a module with a nested version attribute (e.g. module.submod.__version__) and call both minversion implementations to demonstrate differing outcomes
- [ ] 6. Implement fix: modify the implementation that differs to match the correct resolve_name/version_path handling and parsing behavior (preserve pkg_resources.parse_version fallback if available)
- [ ] 7. Run the minimal repro and relevant tests to verify the fix and then mark TODOs complete as steps finish
- [ ] 1. Understand the discrepancy: compare minversion implementations in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py to identify behavioral differences (version_path resolution, resolve_name usage, and version parsing/fallback).
- [ ] 2. Locate the code: open and record the exact locations (file paths and line ranges) of the minversion functions in both files for side-by-side comparison.
- [ ] 3. Root cause analysis: analyze how each implementation resolves version_path (getattr vs resolve_name call signatures), how they import/choose parse_version vs LooseVersion, and any error handling differences.
- [ ] 4. Implement fix: update the implementation that is incorrect/unified to (a) resolve dotted version_path consistently using resolve_name(module.__name__, version_path) or equivalent, (b) prefer pkg_resources.parse_version with a distutils fallback, and (c) preserve existing API/behavior where necessary.
- [ ] 5. Verify fix: run a focused repro script and targeted tests (e.g. pytest -q tests/*minversion* if present or a small script that imports both modules and calls minversion) to confirm behavior matches expected.
- [ ] 6. Checkpoint: create a context_commit describing the changes and mark the TODOs complete as tasks are finished.
- [ ] 1. Locate all usages of minversion in the repo (grep for
- [ ] 2. Reproduce differences: write and run a small Python repro that imports both implementations and compares their results for edge-case versions (e.g.,
- [ ] 3. Determine preferred behavior: check project tests/documentation to decide whether pkg_resources.parse_version or distutils.LooseVersion should be used and confirm desired resolve_name behavior for dotted version_path
- [ ] 4. Implement fix: update the minversion implementation(s) to use the chosen parsing function and harmonize dotted version_path handling; add unit tests covering edge-case versions
- [ ] 5. Verify fix: run relevant tests or the repro and then mark the TODOs complete when passing
- [ ] 1. Compare minversion implementations in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py
- [ ] 2. Locate exact lines implementing version_path handling in both files
- [ ] 3. Analyze differences: how dotted version_path is resolved and which version parser is used
- [ ] 4. Implement fix: update astropy/utils/introspection.py to use pkg_resources.parse_version when available and correct resolve_name usage for dotted version_path
- [ ] 5. Verify fix: run targeted tests and a small repro that exercises dotted version_path
- [ ] 1. Understand the bug: investigate why minversion behaves differently for dotted version_path (observed two implementations; determine failing behavior to reproduce)
- [ ] 2. Locate the code: find minversion and resolve_name definitions in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py (and any other occurrences)
- [ ] 3. Root cause analysis: compare how resolve_name is invoked in both minversion implementations, check resolve_name signature, and reproduce the incorrect behavior with a small script using a dotted version_path
- [ ] 4. Implement fix: update astropy/utils/introspection.py to call resolve_name(
- [ ] "5.
- [ ] 1. Understand the bug: identify why astropy.utils.introspection.minversion calls resolve_name differently from astropy_helpers.utils.minversion for dotted version_path
- [ ] 2. Locate the code: find the minversion definitions in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py (record exact line ranges)
- [ ] 3. Root cause analysis: inspect how resolve_name is invoked in each implementation and determine which call is correct for dotted version_path values
- [ ] 4. Implement fix: modify astropy/utils/introspection.py to construct the full dotted path before calling resolve_name (or otherwise handle dotted version_path consistently with helpers), update docstring if needed
- [ ] 5. Verify fix: run targeted unit tests or a small repro that uses minversion with a dotted version_path (e.g.
- [ ] 1. Understand the bug: compare astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py minversion implementations to identify how dotted version_path is resolved
- [ ] 2. Locate the code: open full minversion definitions in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py to inspect exact lines
- [ ] 3. Root cause analysis: determine which resolve_name usage is correct (resolve_name(module.__name__, version_path) vs resolve_name(
- [ ] 4. Implement fix: update astropy_helpers implementation to use the correct resolve_name call (or adjust other logic) and run quick local checks
- [ ] 5. Verify fix: run targeted tests or a small repro to confirm minversion handles dotted version_path correctly and log results
- [ ] 1. Understand the discrepancy: reproduce and document behavioral differences between astropy.utils.introspection.minversion and astropy_helpers.utils.minversion (how they obtain and parse version, and how resolve_name is used)
- [ ] 2. Locate the code: open astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py to find the minversion implementations and exact line ranges
- [ ] 3. Root cause analysis: compare implementations for differences (pkg_resources vs LooseVersion, and resolve_name/module attribute resolution), and identify which behavior is preferable/buggy
- [ ] 4. Implement fix: update astropy/utils/introspection.py to use parse_version from pkg_resources if available and to call resolve_name with the correct dotted path for nested version_path; prepare a small patch
- [ ] 5. Verify fix: run a minimal repro (import target modules and call minversion with dotted version_path) and run relevant unit tests to ensure no regressions
- [ ] 1. Compare minversion implementations in astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py
- [ ] 2. Locate resolve_name usage and version parsing differences (pkg_resources.parse_version vs distutils.LooseVersion)
- [ ] 3. Identify which minversion implementation is imported/used by the failing code path
- [ ] 4. Implement fix: make behavior consistent (use parse_version when available and resolve version_path in same way)
- [ ] 5. Run relevant tests or reproduce the original failure to verify the fix
- [ ] 1. Compare minversion in astropy/utils and astropy_helpers: locate the files and line ranges for the minversion implementations
- [ ] 2. Check parse_version import and fallback behavior in both implementations and note any differences
- [ ] 3. Reproduce behavior by running Python snippets calling astropy_helpers.utils.minversion with module as module object and as string, and with different version_path values (including dotted paths and non-string version attributes)
- [ ] 4. Root cause analysis: determine if discrepancies arise from how version_path is resolved, type of have_version, or parse_version usage
- [ ] 5. Implement fix in astropy_helpers/astropy_helpers/utils.py if needed and add tests; verify fix by running the repro snippets and unit tests
- [ ] 1. Inspect minversion in astropy_helpers: read astropy_helpers/astropy_helpers/utils.py around line 559 to understand its implementation and behavior
- [ ] 2. Locate minversion in astropy core: grep the astropy source for
- [ ] 3. Compare implementations: diff the astropy_helpers implementation with astropy
- [ ] 4. Root cause analysis: determine whether differences cause incorrect behavior or tests to fail; identify minimal code change to align behavior or fix bug
- [ ] 5. Implement fix: modify the appropriate file (likely astropy or astropy_helpers) with targeted changes and add/update unit tests that cover the failing behavior
- [ ] 6. Verify fix: run the relevant tests (unit tests for utils/minversion and any failing test suite) and log results; iterate if needed
- [ ] 1. Read astropy_helpers minversion implementation: sed -n
- [ ] 2. Compare astropy_helpers minversion with astropy.utils.introspection.minversion to find behavioral differences
- [ ] 3. Create a small repro to exercise edge cases (module name string import failure, version attribute path with dots, version attribute raising AttributeError)
- [ ] 4. Implement fix in astropy_helpers/astropy_helpers/utils.py to match astropy behavior and robustly handle version resolution
- [ ] 5. Run repro and relevant unit tests to verify the fix
- [ ] 6. Log findings, commit checkpoint with context_commit, and mark todos complete as each step is done

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 02:08] **swebench-astropy__astropy-7671**: Task completed: LimitsExceeded
- [2025-12-02 01:54] **swebench-astropy__astropy-7671**: Fix: _isinstancemethod should return False when name not found instead of raising AttributeError
## Interaction Log

- `02:08:36` ACTION: sed -n '520,600p' astropy_helpers/astropy_helpers/utils.py
- `02:08:31` ACTION: sed -n '1,240p' astropy/utils/introspection.py
- `02:08:21` ACTION: grep -nR "def minversion" astropy || true
- `02:08:00` ACTION: Reading file: -f1)
- `02:07:32` ACTION: grep -nR "def minversion" astropy && sed -n '1,240p' astropy/utils/misc.py
- `02:07:07` ACTION: sed -n '620,760p' astropy_helpers/astropy_helpers/utils.py
- `02:07:00` ACTION: sed -n '520,620p' astropy_helpers/astropy_helpers/utils.py
- `02:06:56` ACTION: sed -n '1,160p' astropy/utils/introspection.py
- `02:06:49` grep def minversion: astropy/utils/introspection.py:91, astropy_helpers/astropy_helpers/utils.py:559
- `02:06:44` ACTION: grep -nR "def minversion" astropy astropy_helpers || true
- `02:06:14` ACTION: sed -n '1,220p' astropy/utils/introspection.py && sed -n '540,640p' astropy_helpers/astropy_helpers/ [...]
- `02:06:07` grep minversion: astropy/utils/introspection.py:91; astropy_helpers/astropy_helpers/utils.py:559
- `02:05:58` ACTION: grep -nR "def minversion" astropy* astropy_helpers* || true
- `02:05:37` ACTION: sed -n '1,200p' astropy/utils/introspection.py && sed -n '520,640p' astropy_helpers/astropy_helpers/ [...]
- `02:05:29` grep def minversion: astropy/utils/introspection.py:91 astropy_helpers/astropy_helpers/utils.py:559
- `02:05:20` ACTION: grep -nR "def minversion" .
- `02:04:56` ACTION: sed -n '1,200p' astropy/utils/introspection.py && sed -n '540,620p' astropy_helpers/astropy_helpers/ [...]
- `02:04:49` grep minversion: astropy/utils/introspection.py:91 astropy_helpers/astropy_helpers/utils.py:559
- `02:04:45` ACTION: grep -nR --include="*.py" "def minversion" astropy astropy_helpers || true
- `02:04:28` ACTION: sed -n '1,220p' astropy/utils/introspection.py && sed -n '520,700p' astropy_helpers/astropy_helpers/ [...]
