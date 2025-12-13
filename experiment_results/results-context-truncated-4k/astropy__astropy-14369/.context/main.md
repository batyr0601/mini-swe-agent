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
- [ ] Find the function causing the error (look in X module)
- [ ] Understand why Y happens when Z is called
- [ ] Implement fix by changing A to B
- [ ] Test the fix with the original reproduction case
- [x] 1. Analyze the codebase: read astropy/io/ascii/cds.py around unit parsing and related unit handling in astropy.units
- [ ] 2. Create/confirm a minimal script to reproduce the issue (repro.py already used) and ensure it triggers the empty-table behavior
- [ ] 3. Edit source code to fix CDS unit parsing in astropy/io/ascii/cds.py (make parsing robust for CDS unit strings, e.g. handle empty/invalid units without causing empty output)
- [ ] 4. Verify the fix by running the minimal reproduction script once (python3 repro.py)
- [ ] "5.

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-02 20:56] **swebench-astropy__astropy-14369**: Task completed: LimitsExceeded
## Interaction Log

- `20:56:30` ACTION: sed -n '100,140p' astropy/io/ascii/cds.py
- `20:56:23` ACTION: grep -n -E "Unit|unit|parse_unit|parse_units|units\." astropy/io/ascii/cds.py || true
- `20:56:07` ACTION: sed -n '120,420p' astropy/io/ascii/cds.py
- `20:56:01` ACTION: sed -n '1,120p' astropy/io/ascii/cds.py
- `20:55:42` repro.py output: '<No columns>
- `20:55:29` RESULT: <No columns>
- `20:55:28` ACTION: python3 repro.py
- `20:55:22` astropy/io/ascii/cds.py: lines 120-140: column unit parsed; "---" -> col.unit=None; else Unit(unit, format="cds", parse_strict="warn")
- `20:55:05` ACTION: sed -n '116,140p' astropy/io/ascii/cds.py
- `20:54:58` ACTION: grep -n -E "Unit\\(|format=\"cds\"|---" astropy/io/ascii/cds.py || true
- `20:54:12` ACTION: sed -n '100,160p' astropy/io/ascii/cds.py
- `20:54:08` grep astropy/io/ascii/cds.py: 18: from astropy.units import Unit; 113: regex group '(?P<units> \\S+)'; 129: unit = match.group(\"units\"); 130-131: if...
- `20:53:56` ACTION: grep -n -E "unit|Unit|units|Units|parse" astropy/io/ascii/cds.py || true
- `20:53:46` repro.py output: '<No columns>' - ascii.read('repro_cds.mrt', format='cds') produced an empty Table with no columns
- `20:53:41` RESULT: <No columns>
- `20:53:40` ACTION: python3 repro.py
- `20:53:36` repro.py: reads 'repro_cds.mrt' with ascii.read(format='cds'); prints table and itercols showing Column name, unit, dtype
- `20:53:27` ACTION: sed -n '1,200p' repro.py
- `20:53:16` ACTION: grep -RIn --exclude-dir=.git -e "Byte-by-byte" .
- `20:52:54` repro.py: astropy.io.ascii.read(format='cds') produced '<No columns>' when parsing repro_cds.mrt; CDS parser failed to detect column definitions — tes...
