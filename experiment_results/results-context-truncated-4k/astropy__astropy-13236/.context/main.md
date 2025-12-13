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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 20:47] **swebench-astropy__astropy-13236**: Task completed: LimitsExceeded
## Interaction Log

- `20:47:09` ACTION: sed -n '1,480p' astropy/table/column.py
- `20:47:04` ACTION: grep -nR --exclude-dir=.git -E "structured[ _-]?column|auto-?transfor|structured_column|structured-c [...]
- `20:46:49` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured|structured_column|structured-column" astropy [...]
- `20:46:34` ACTION: sed -n '1,240p' astropy/table/ndarray_mixin.py
- `20:46:29` ACTION: grep -nR "class NdarrayMixin" astropy | sed -n '1,120p' && sed -n '1,240p' astropy/table/mixins/ndar [...]
- `20:46:19` ACTION: sed -n '1200,1260p' astropy/table/table.py
- `20:46:06` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured[ _-]?column|structured_column|auto-?transfor [...]
- `20:45:53` ACTION: sed -n '1200,1610p' astropy/table/table.py && sed -n '3880,3960p' astropy/table/table. [...]
- `20:45:46` ACTION: grep -nR --exclude-dir=.git -E "def (get_mixin_handler|_is_mixin_for_table|get_mixin_for|register_mi [...]
- `20:45:31` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured[ _-]?column|structured_column|auto-?transfor [...]
- `20:45:17` ACTION: sed -n '1,240p' astropy/table/mixins/registry.py && sed -n '1568,1608p' astropy/table/table. [...]
- `20:45:09` ACTION: grep -nR --exclude-dir=.git -E "def (get_mixin_handler|_is_mixin_for_table|get_mixin_for|register_mi [...]
- `20:44:48` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured[ _-]?column|structured_column|auto-?transfor [...]
- `20:44:36` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured[ _-]?column|structured" astropy/table || tru [...]
- `20:44:25` ACTION: sed -n '1,240p' astropy/table/mixins/registry.py && sed -n '1160,1320p' astropy/table/table. [...]
- `20:44:14` ACTION: grep -nR --exclude-dir=.git -E "def (get_mixin_handler|_is_mixin_for_table|get_mixin_for|register_mi [...]
- `20:44:00` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured[ _-]?column|structured_column|auto-?transfor [...]
- `20:43:44` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|_is_mixin_for_table|get_mixin_handler|structured[ _-]?c [...]
- `20:43:29` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|structured column|structured_column|_is_mixin_for_table [...]
- `20:43:14` ACTION: grep -nR --exclude-dir=.git -E "NdarrayMixin|get_mixin_handler|_is_mixin_for_table|structured|auto-? [...]
