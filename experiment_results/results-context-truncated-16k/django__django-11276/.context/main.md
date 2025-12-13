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

- [2025-12-02 23:37] **swebench-django__django-11276**: Task completed: Submitted
## Interaction Log

- `23:37:43` ACTION: Submitting solution
- `23:37:25` RESULT: &#39;
- `23:37:24` ACTION: python3 -c "from django.utils.html import escape; print(escape(\"'\"))"
- `23:37:14` Patched django/utils/html.py: added 'import html as _stdlib_html' and replaced return mark_safe(str(text).translate(_html_escapes)) with return mark_s...
- `23:37:07` RESULT: patched
- `23:37:06` ACTION: awk 'BEGIN{inserted=0} { if($0 ~ /import html as _stdlib_html/) inserted=1; if($0 ~ /from html. [...]
- `23:35:37` ACTION: grep -nR "escape(" django tests || true
- `23:35:30` ACTION: nl -ba django/utils/html.py | sed -n '1,240p'
- `23:35:25` ACTION: ls -la
- `23:35:22` RESULT: ls: cannot access 'testbed': No such file or directory
- `23:35:22` ACTION: ls -la testbed
- `23:35:13` TASK STARTED: Use Python stdlib html.escape() to in django.utils.html.escape()
