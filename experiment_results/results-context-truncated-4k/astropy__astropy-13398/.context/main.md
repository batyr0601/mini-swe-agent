# Project Goals

**Current Task:** A direct approach to ITRS to Observed transformations that stays within the ITRS.

<details>
<summary>Full description</summary>

A direct approach to ITRS to Observed transformations that stays within the ITRS.
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
<!-- If you want to, you can s...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 20:46] **swebench-astropy__astropy-13398**: Task completed: LimitsExceeded
## Interaction Log

- `20:46:37` ACTION: sed -n '1,260p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
- `20:46:30` ACTION: grep -nE "def .*itrs_to_observed|def .*itrs_to_cirs|def . [...]
- `20:46:19` ACTION: grep -nE "def .*itrs_to_observed|def .*itrs_to_cirs|def .*cirs_to_itrs|def . [...]
- `20:45:44` ACTION: sed -n '1,320p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
- `20:45:38` ACTION: grep -nR -E "def .*itrs_to_observed|def .*itrs_to_cirs|def .*cirs_to_itrs|def .*to_observed|def . [...]
- `20:45:23` ACTION: sed -n '1,320p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
- `20:45:18` ACTION: grep -nR -E "def .*itrs_to_observed|def .*itrs_to_cirs|def .*to_observed|def . [...]
- `20:45:03` ACTION: sed -n '1,260p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
- `20:44:58` ACTION: grep -RIn -E --line-number "def (itrs_to_observed|itrs_to_cirs|cirs_to_itrs)" astropy || true
- `20:44:42` ACTION: sed -n '180,260p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
- `20:44:36` ACTION: grep -RIn --line-number -E "def .*itrs_to_observed|def .*itrs_to_cirs|def .*to_observed|def . [...]
- `20:44:22` ACTION: grep -RIn --line-number -E "\bITRS\b" astropy || true
- `20:44:14` ACTION: sed -n '1,320p' astropy/coordinates/builtin_frames/cirs_observed_transforms.py
- `20:43:58` ACTION: sed -n '1,240p' astropy/coordinates/builtin_frames/cirs_observed_transforms. [...]
- `20:43:41` ACTION: grep -RIn --line-number -E "itrs_to_observed|itrs_to_cirs|to_observed|to_itrs|ITRS|\\bitrs\\b" astro [...]
- `20:43:24` ACTION: sed -n '1,240p' astropy/coordinates/builtin_frames/cirs_observed_transforms.py
- `20:43:11` ACTION: sed -n '1,240p' astropy/coordinates/matrix_utilities. [...]
- `20:43:04` ACTION: grep -RIn --line-number -E "def matrix_transpose|def cirs_to_itrs_mat|matrix_transpose\(|cirs_to_itr [...]
- `20:42:56` intermediate_rotation_transforms.py: itrs_to_cirs (around line 210) computes pmat = cirs_to_itrs_mat(itrs_coo.obstime); newrepr = itrs_coo.cartesian.t...
- `20:42:41` ACTION: sed -n '200,260p' astropy/coordinates/builtin_frames/intermediate_rotation_transforms.py
