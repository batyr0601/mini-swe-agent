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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 14:21] **swebench-astropy__astropy-14309**: Task completed: LimitsExceeded
- [2025-12-02 14:21] **swebench-astropy__astropy-14309**: Task completed: LimitsExceeded
## Interaction Log

- `14:21:38` ACTION: git grep -n "identify_format" && sed -n '1,360p' astropy/io/registry/base.py
- `14:21:27` identify_format found in astropy/io/registry.py: loops through _identifiers and calls each identifier with (origin, path, fileobj, *args, **kwargs); c...
- `14:21:25` ACTION: sed -n '340,520p' astropy/io/registry/base.py
- `14:21:21` ACTION: sed -n '240,340p' astropy/io/registry/base.py
- `14:21:17` ACTION: sed -n '340,420p' astropy/io/registry.py
- `14:21:13` ACTION: git grep -n "identify_format" || true
- `14:21:10` RESULT: sed: can't read astropy/io/registry/base.py: No such file or directory
- `14:21:09` ACTION: sed -n '240,320p' astropy/io/registry/base.py
- `14:21:06` ACTION: sed -n '340,460p' astropy/io/registry/base.py
- `14:21:03` ACTION: sed -n '240,340p' astropy/io/registry/base.py
- `14:20:58` ACTION: sed -n '340,460p' astropy/io/registry.py
- `14:20:51` ACTION: git grep -n "identify_format" || true
- `14:20:50` ACTION: sed -n '1,260p' astropy/io/registry/core.py && echo '---core. [...]
- `14:20:47` RESULT: sed: can't read astropy/io/registry/base.py: No such file or directory
- `14:20:47` ACTION: sed -n '1,420p' astropy/io/registry/base.py
- `14:20:41` ACTION: grep -nR "_get_valid_format" .
- `14:20:35` ACTION: sed -n '1,260p' astropy/io/registry.py
- `14:20:29` ACTION: sed -n '260,400p' astropy/io/registry/base.py
- `14:20:24` ACTION: sed -n '340,460p' astropy/io/registry.py
- `14:20:23` ACTION: git grep -n "_get_valid_format" || true && git grep -n "identify_format(" || true
