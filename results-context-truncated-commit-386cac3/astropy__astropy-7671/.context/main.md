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
- [ ] 1. Reproduce the bug: run a small script that imports astropy.utils.minversion and calls minversion(
- [ ] 2. Locate the code: find minversion in astropy/utils/introspection.py
- [ ] 3. Analyze: determine why LooseVersion comparison fails for mixed int/str components and evaluate alternatives (pkg_resources.parse_version or packaging.version.parse)
- [ ] 4. Implement fix: update astropy/utils/introspection.py to use a robust version parsing/comparison (prefer packaging.version.parse with fallback) and ensure behavior matches previous semantics
- [ ] 5. Verify fix: run the reproduction script and any relevant tests to ensure minversion works for cases like

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 20:43] **swebench-astropy__astropy-7671**: Task completed: Submitted
## Interaction Log

- `20:43:01` ACTION: Submitting solution
- `20:42:56` Verification completed; minversion comparisons using chosen parser succeeded for cases like '1.14.3' vs '1.14dev' and '1.14' vs '1.14dev
- `20:42:49` Verifying comparisons with chosen parser
- `20:42:27` Patched introspection.minversion to prefer packaging/pkg_resources and fallback to LooseVersion
- `20:42:11` RESULT: (220 lines of output) First: 1	# -*- coding: utf-8 -*-...
- `20:42:10` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,220p'
- `20:42:03` Decision: prefer packaging.version.parse, fallback to pkg_resources.parse_version, else fallback to distutils.LooseVersion
- `20:41:21` RESULT: ERROR: TypeError: '<' not supported between instances of 'int' and 'str'
- `20:41:20` ACTION: python - <<'PY'
- `20:41:06` Found minversion in astropy/utils/introspection.py: uses distutils.version.LooseVersion which can raise TypeError for mixed int/str components (e.g., ...
- `20:40:50` RESULT: (240 lines of output) First: 1	# -*- coding: utf-8 -*-...
- `20:40:50` ACTION: nl -ba astropy/utils/introspection.py | sed -n '1,240p'
- `20:40:47` RESULT: 91:def minversion(module, version, inclusive=True, version_path='__version__'):
- `20:40:46` ACTION: grep -n "def minversion" -n astropy/utils/introspection.py || nl -ba astropy/utils/introspection. [...]
- `20:40:33` RESULT: (38 lines of output) First: total 508...
- `20:40:31` ACTION: ls -la
- `20:40:28` TASK STARTED: minversion failures
