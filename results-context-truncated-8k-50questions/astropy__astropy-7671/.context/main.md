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

- [2025-12-03 03:05] **swebench-astropy__astropy-7671**: Task completed: Submitted
## Interaction Log

- `03:05:44` ACTION: Submitting solution
- `03:05:35` repro_minversion.py output after patch: have_version: 1.14dev; minversion(m,'1.14') -> False; minversion(m,'1.13') -> True; minversion(m,'1.14', inclu...
- `03:05:15` ACTION: python3 -m py_compile astropy/utils/introspection.py && python3 repro_minversion.py
- `03:04:24` LooseVersion treats '1.14dev' > '1.14'; pkg_resources.parse_version and packaging.version.parse treat '1.14dev' < '1.14' (observed via comparison outp...
- `03:04:08` ACTION: python3 - <<'PY'
- `03:03:44` minversion located: astropy/utils/introspection.py:91-145; implementation uses LooseVersion(have_version) >= or > LooseVersion(version)
- `03:03:35` ACTION: nl -ba astropy/utils/introspection.py | sed -n '90,150p'
- `03:03:26` repro_minversion.py output: have_version: 1.14dev; minversion(m,'1.14') -> True; minversion(m,'1.13') -> True; minversion(m,'1.14', inclusive=False) -...
- `03:03:14` ACTION: grep -n "LooseVersion(" -R astropy || true
- `03:03:01` ACTION: Reading file: <<'PY'
- `03:02:43` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,240p'
- `03:02:33` ACTION: grep -n "def minversion" -R astropy || true
- `03:02:28` ACTION: ls -la
- `03:02:26` RESULT: grep: testbed: No such file or directory
- `03:02:24` ACTION: grep -n "def minversion" -R testbed || true
- `03:02:16` TASK STARTED: minversion failures
