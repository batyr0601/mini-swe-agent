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
- [ ] 1. Reproduce the bug: create/run a small script that imports minversion and calls minversion(
- [ ] 2. Locate the minversion function: grep for
- [ ] 3. Root cause analysis: inspect the implementation for use of distutils.version.LooseVersion or removed pkg_resources.parse_version and determine how comparisons are done
- [ ] 4. Implement fix: modify minversion to use packaging.version.parse (fallback to pkg_resources.parse_version, then LooseVersion) to correctly compare
- [ ] 5. Verify fix: run repro script and additional edge cases, ensure no TypeError and correct logical results
- [ ] 6. Finalize: add/commit changes and prepare diff for submission (do not git commit before final submit step)

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:46] **swebench-astropy__astropy-7671**: Task completed: Submitted
## Interaction Log

- `20:46:24` ACTION: Submitting solution
- `20:46:09` astropy_helpers/utils.py verification: Module fake_module __version__='1.14.3' -> ah.minversion(..., '1.14dev') -> True; ah.minversion(..., '1.14.3') ...
- `20:46:09` introspection.py verification: Module fake_module __version__='1.14.3' -> minversion(..., '1.14dev') -> True; minversion(..., '1.14.3') -> True; minve...
- `20:45:59` Implemented fix: updated astropy/utils/introspection.py and astropy_helpers/astropy_helpers/utils.py to add _version_ge/_version_gt helpers that prefe...
- `20:45:51` Root cause: distutils.version.LooseVersion can mix int and str in parts causing TypeError when comparing versions like '1.14.3' vs '1.14dev'. Fix: pre...
- `20:45:42` grep def minversion: astropy/utils/introspection.py:91, astropy_helpers/astropy_helpers/utils.py:559
- `20:45:35` Reproduced bug: minversion(ModuleType with __version__='1.14.3', required '1.14dev') raised TypeError \"<' not supported between instances of 'int' an...
- `20:45:24` ACTION: python3 - <<'PY'
- `20:44:57` ACTION: nl -ba astropy_helpers/astropy_helpers/utils.py | sed -n '620,760p'
- `20:44:50` ACTION: nl -ba astropy_helpers/astropy_helpers/utils.py | sed -n '520,620p'
- `20:44:36` Patched introspection.py successfully; attempted verification script did not run due to heredoc chaining error
- `20:44:02` introspection.py: minversion imports LooseVersion and compares LooseVersion(have_version) >= LooseVersion(version); reproducer using ModuleType with _...
- `20:43:46` ACTION: python3 - <<'PY'
- `20:43:34` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,220p'
- `20:43:29` ACTION: grep -nR "def minversion" . || true
- `20:43:10` TASK STARTED: minversion failures
