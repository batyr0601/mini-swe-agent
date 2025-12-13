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

Add detailed, specific TODOs when starting a task. Good examples:
-->

## Key Milestones

<!-- Auto-populated when TODOs are completed -->

- [2025-12-03 03:19] **swebench-django__django-11276**: Task completed: Submitted
## Interaction Log

- `03:18:57` ACTION: Submitting solution
- `03:18:50` escape(\"O'Reilly & \\\"test\\\" <tag>\") returned O&#39;Reilly &amp; &quot;test&quot; &lt;tag&gt;; replaced stdlib '&#x27;' with '&#39;' to preserve ...
- `03:18:20` sed corrupted escape(): django/utils/html.py line 47 contains incorrect replace string 'return mark_safe(_stdlib_escape(str(text), quote=True))#x27;'....
- `03:17:45` ACTION: sed -i "s/return mark_safe(_stdlib_escape(str(text), quote=True))/return mark_safe(_stdlib_escape(st [...]
- `03:17:20` RESULT: O&#x27;Reilly &amp; &quot;test&quot; &lt;tag&gt;
- `03:17:15` ACTION: python3 - <<'PY'
- `03:16:36` ACTION: sed -i "/from html.parser import HTMLParser/a from html import escape as _stdlib_escape" django/util [...]
- `03:16:13` ACTION: nl -ba django/utils/html.py | sed -n '1,240p'
- `03:16:01` ACTION: grep -n "def escape" -R django || true
- `03:15:59` ACTION: ls -la
- `03:15:55` RESULT: grep: testbed: No such file or directory
- `03:15:52` ACTION: grep -R --line-number "def escape" testbed || true
- `03:15:45` TASK STARTED: Use Python stdlib html.escape() to in django.utils.html.escape()
