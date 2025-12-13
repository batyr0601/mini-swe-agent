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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 23:29] **swebench-astropy__astropy-7671**: Task completed: Submitted
## Interaction Log

- `23:29:57` ACTION: Submitting solution
- `23:29:52` Patched astropy/utils/introspection.py to use parse_version (pkg_resources/packaging/LooseVersion fallback). Verified parse_version('1.14.3') >= parse...
- `23:29:33` ACTION: python3 - <<'PY'
- `23:29:18` RESULT: patched introspection.minversion
- `23:29:17` ACTION: python3 - <<'PY'
- `23:28:56` ACTION: nl -ba astropy_helpers/astropy_helpers/utils.py | sed -n '520,660p'
- `23:28:50` RESULT: minversion numpy 1.14dev: True
- `23:28:49` ACTION: Reading file: repro_minversion.py
- `23:28:08` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,220p'
- `23:28:03` ACTION: grep -nR -e "def minversion" -e "minversion(" .
- `23:27:41` TASK STARTED: minversion failures
