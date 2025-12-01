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

- [2025-12-03 00:30] **swebench-astropy__astropy-7671**: Task completed: Submitted
## Interaction Log

- `00:30:31` ACTION: Submitting solution
- `00:30:23` verification: minversion returned True for m.__version__='1.14.3' vs '1.14dev
- `00:30:04` RESULT: minversion result: True
- `00:30:03` ACTION: python3 - <<'PY'
- `00:29:48` Patched astropy/utils/introspection.py to import pkg_resources.parse_version as _parse_version with fallback to distutils.LooseVersion; replaced Loose...
- `00:29:41` RESULT: patched astropy/utils/introspection.py
- `00:29:40` ACTION: python3 - <<'PY'
- `00:29:20` Root cause: distutils.LooseVersion comparison fails when numeric and non-numeric components are compared (e.g. '1.14.3' vs '1.14dev'); pkg_resources.p...
- `00:28:49` grep LooseVersion: astropy/utils/introspection.py:9,143,145; minversion uses LooseVersion at lines 142-145
- `00:28:42` ACTION: grep -n "LooseVersion" astropy/utils/introspection.py || true
- `00:28:28` Repro: LooseVersion('1.14.3') >= LooseVersion('1.14dev') raised TypeError '<' not supported between instances of int and str
- `00:28:09` RESULT: Raised: TypeError '<' not supported between instances of 'int' and 'str'
- `00:28:08` ACTION: python3 - <<'PY'
- `00:27:42` ACTION: grep -nR "parse_version\|packaging.version" . || true
- `00:27:33` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,220p'
- `00:27:26` ACTION: grep -nR "minversion" . || true
- `00:27:20` RESULT: ls: cannot access 'testbed': No such file or directory
- `00:27:20` ACTION: ls -la testbed
- `00:27:13` TASK STARTED: minversion failures
