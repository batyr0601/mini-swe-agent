# Project Goals

**Current Task:** Use Python stdlib html.escape() to in django.utils.html.escape()

<details>
<summary>Full description</summary>

Use Python stdlib html.escape() to in django.utils.html.escape()
Description
	
The function django.utils.html.escape() partially duplicates the Python stdlib function html.escape(). We can replace this duplication with wider community developed version.
html.escape() has been available since Python 3.2:
​https://docs.python.org/3/library/html.html#html.escape
This function is also faster than Django's. As Python bug ​https://bugs.python.org/issue18020 concludes, using .replace() can be faster than .translate(). This function gets called numerous times when rendering templates. After making the change locally, I saw the following improvement:
master:
$ python -m timeit -s 'from django.utils.html import escape' 'escape(copyright)'
50000 loops, best of 5: 4.03 usec per loop
branch:
$ python -...
</details>


## TODO List

- [x] Reproduce the bug with a minimal test case
- [x] Find the function causing the error (look in X module)
- [x] Understand why Y happens when Z is called
- [x] Implement fix by changing A to B
- [x] Test the fix with the original reproduction case
- [ ] 1. Understand the bug: Replace django.utils.html.escape with stdlib html.escape() for correctness and performance, but preserve previous
- [ ] 2. Locate the code: find file(s) that implement django.utils.html.escape in the testbed repo
- [ ] 3. Root cause analysis: inspect current implementation to see how it escapes characters and why it used its approach (e.g., translate vs replace), and confirm mapping for single quote
- [ ] 4. Implement fix: modify django.utils.html.escape to call html.escape(..., quote=True) and post-process to replace
- [ ] 5. Verify fix: run searches for usages, create small reproduction script to compare outputs before/after and run relevant tests or smoke checks

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-01 21:19] **swebench-django__django-11276**: Task completed: Submitted
## Interaction Log

- `21:19:23` ACTION: Submitting solution
- `21:19:18` Verification: escape(\"'\") -> '&#39;'; '\"' -> '&quot;'; '&' -> '&amp;'; '<' -> '&lt;'; '>' -> '&gt;'; timeit 100000 loops: 0.21328975000142236 sec
- `21:19:18` django/utils/html.py: _html_escapes mapping ord(\"'\") -> '&#39;'; original escape used str(text).translate(_html_escapes)
- `21:19:18` grep def escape: ./django/utils/html.py:37:def escape
- `21:18:53` ACTION: python3 - <<'PY'
- `21:18:45` Updated django/utils/html.py: replaced escape implementation to use stdlib html.escape as _stdlib_html_escape and post-processed '&#x27;' to '&#39' to...
- `21:18:35` RESULT: Updated django/utils/html.py
- `21:18:35` ACTION: python3 - <<'PY'
- `21:17:59` ACTION: nl -ba django/utils/html.py
- `21:17:50` ACTION: grep -nR "def escape" . || true
- `21:17:30` TASK STARTED: Use Python stdlib html.escape() to in django.utils.html.escape()
