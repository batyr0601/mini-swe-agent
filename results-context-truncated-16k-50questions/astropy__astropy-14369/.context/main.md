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

- [2025-12-02 23:32] **swebench-astropy__astropy-14369**: Task completed: Submitted
## Interaction Log

- `23:32:00` ACTION: Submitting solution
- `23:31:52` Patched combined_units to left-recursive; test output: 'm/s/Hz' -> parsed: Unit(\"m / (Hz s)\"), cds string: m.Hz-1.s-1; 'm/s/s' -> parsed: Unit(\"m /...
- `23:31:31` ACTION: python3 - <<'PY'
- `23:31:05` ACTION: git checkout -- astropy/units/format/cds.py && nl -ba astropy/units/format/cds. [...]
- `23:30:51` ACTION: python3 - <<'PY'
- `23:30:26` ACTION: nl -ba astropy/units/format/cds.py | sed -n '136,200p'
- `23:30:11` ACTION: python3 - <<'PY'
- `23:29:32` ACTION: nl -ba astropy/units/format/cds.py | sed -n '160,220p'
- `23:28:54` ACTION: python3 - <<'PY'
- `23:28:22` ACTION: nl -ba astropy/units/format/cds.py | sed -n '150,220p'
- `23:28:12` Test output: m/s/Hz -> parsed: Unit(\"Hz m / s\"), cds string: Hz.m.s-1; m/s/s -> parsed: Unit(\"m\"), cds string: m; m/s/Hz/Hz -> parsed: Unit(\"m / ...
- `23:28:12` Patched astropy/units/format/cds.py: replaced combined/product/division productions
- `23:27:40` ACTION: rm -f astropy/units/format/cds_lextab.py astropy/units/format/cds_parsetab.py && python3 - <<'PY'
- `23:26:16` ACTION: python3 - <<'PY'
- `23:25:46` ACTION: nl -ba astropy/units/format/cds.py | sed -n '136,220p'
- `23:25:28` ACTION: nl -ba astropy/units/format/cds.py | sed -n '1,360p'
- `23:25:21` ACTION: nl -ba astropy/io/ascii/cds.py | sed -n '108,200p'
- `23:25:17` ACTION: grep -n "\.unit" -n astropy/io/ascii/mrt.py || true
- `23:25:14` ACTION: nl -ba astropy/io/ascii/mrt.py | sed -n '1,260p'
- `23:25:08` ACTION: nl -ba astropy/io/ascii/cds.py | sed -n '1,260p'
