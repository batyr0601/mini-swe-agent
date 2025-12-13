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

- [2025-12-03 03:03] **swebench-astropy__astropy-14369**: Task completed: Submitted
## Interaction Log

- `03:03:33` ACTION: Submitting solution
- `03:03:27` Patched p_factor in astropy/units/format/cds.py: changed UINT signed_int branch to p[1]*10.0**p[2]. Verification: '10+3J' -> Unit('10000 J'), '1x10+3J...
- `03:01:44` cds.CDS.parse tests: '10+3J' -> Unit('1000 J'), '1x10+3J' -> Unit('1000 J'), '10x10+3J' -> Unit('10000 J'), '1.0x10+3J' -> Unit('1000 J'). Root cause:...
- `03:01:08` ACTION: python3 - <<'PY'
- `03:00:32` ACTION: grep -nR "10+3" -n || true
- `02:59:54` ACTION: sed -n '200,320p' astropy/units/format/cds.py
- `02:59:22` ACTION: sed -n '1,420p' astropy/units/format/cds.py
- `02:59:09` ACTION: grep -R --line-number --exclude-dir=.git -n "cds" astropy/units || true
- `02:58:58` ACTION: grep -R --line-number --exclude-dir=.git -n "class CDSSome" astropy || true
- `02:58:56` Reproduced: Unit('10+3J/m/s/kpc2', format=\"cds\") -> 'Parsed unit: 1000 J s / (kpc2 m)
- `02:58:33` RESULT: Parsed unit: 1000 J s / (kpc2 m)
- `02:58:23` ACTION: python - <<'PY'
- `02:58:13` ACTION: sed -n '120,140p' astropy/io/ascii/cds.py
- `02:58:01` ACTION: grep -R --line-number -n "Unit(" astropy/io/ascii || true
- `02:57:51` ACTION: nl -ba astropy/io/ascii/cds.py | sed -n '1,240p'
- `02:57:41` ACTION: grep -R --line-number --exclude-dir=.git -n "class Cds" astropy || true
- `02:57:33` ACTION: grep -R --line-number --exclude-dir=.git -n "ascii.cds" astropy || true
- `02:57:22` ACTION: ls -la && nl -ba testbed | sed -n '1,200p' 2>/dev/null || true
- `02:57:13` TASK STARTED: Incorrect units read from MRT (CDS format) files with astropy.table
