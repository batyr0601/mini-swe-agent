# Project Goals

**Current Task:** Incorrect units read from MRT (CDS format) files with astropy.table

<details>
<summary>Full description</summary>

Incorrect units read from MRT (CDS format) files with astropy.table
### Description

When reading MRT files (formatted according to the CDS standard which is also the format recommended by AAS/ApJ) with `format='ascii.cds'`, astropy.table incorrectly parses composite units. According to CDS standard the units should be SI without spaces (http://vizier.u-strasbg.fr/doc/catstd-3.2.htx). Thus a unit of `erg/AA/s/kpc^2` (surface brightness for a continuum measurement) should be written as `10+3J/m/s/kpc2`.

When I use these types of composite units with the ascii.cds reader the units do not come out correct. Specifically the order of the division seems to be jumbled.


### Expected behavior

The units in the resulting Table should be the same as in the input MRT file.

### How to Reproduce
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

- [2025-12-03 00:33] **swebench-astropy__astropy-14369**: Task completed: Submitted
## Interaction Log

- `00:33:12` ACTION: Submitting solution
- `00:33:06` Parsed SBCONT bases/powers: ['J','m','s','kpc'] [1, -1, -1, -2]; Root cause: cds formatter sorted unit pairs by power causing denominators to be group...
- `00:33:06` Reproduction: Table.read('tab.txt', format='ascii.cds') printed SBCONT CDS string: 10+3J/m/s/kpc2; SBLINE CDS string: 10-7J/s/kpc2
- `00:32:43` ACTION: sed -i 's/split_mantissa_exponent(unit.scale)/split_mantissa_exponent(unit.scale, format_spec=". [...]
- `00:32:04` ACTION: nl -ba astropy/units/format/utils.py | sed -n '1,240p'
- `00:31:35` ACTION: grep -RIn "split_mantissa_exponent" . || true
- `00:31:27` ACTION: grep -n "def split_mantissa_exponent" astropy/units/utils.py || true
- `00:30:52` ACTION: python3 - <<'PY'
- `00:29:52` ACTION: nl -ba astropy/units/format/cds.py | sed -n '288,324p'
- `00:29:47` ACTION: awk 'NR<302{print} NR==302{print " @classmethod"; print " def _format_unit_list(cls, units):"; print [...]
- `00:29:07` ACTION: nl -ba astropy/units/utils.py | sed -n '420,540p'
- `00:28:48` ACTION: nl -ba astropy/units/core.py | sed -n '720,820p'
- `00:28:43` ACTION: grep -n "def __str__\|def to_string\|def to_string(" astropy/units/core.py || true
- `00:28:16` ACTION: nl -ba astropy/units/core.py | sed -n '1,320p'
- `00:28:06` ACTION: Reading file: <<'EOF'
- `00:27:47` ACTION: Reading file: repro_inspect.py
- `00:27:26` ACTION: nl -ba astropy/units/utils.py | sed -n '1,260p'
- `00:27:15` ACTION: sed -i '/pairs.sort(key=operator.itemgetter(1), reverse=True)/d' astropy/units/format/cds. [...]
- `00:26:49` ACTION: nl -ba astropy/units/format/cds.py | sed -n '296,340p'
- `00:26:46` ACTION: grep -n "_format_unit_list" -n astropy/units/format/cds.py || true
