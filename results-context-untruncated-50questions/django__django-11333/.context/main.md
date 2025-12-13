# Project Goals

**Current Task:** Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`

<details>
<summary>Full description</summary>

Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`
Description
	
Multiple URLResolvers may be constructed by django.urls.resolvers.get_resolver if django.urls.base.set_urlconf has not yet been called, resulting in multiple expensive calls to URLResolver._populate.
​`get_resolver` constructs a new URLResolver, and caches it using functools.lru_cache.
URLResolver instances can pre-compute a large amount of information about routes in ​`URLResolver._populate`, and they store those caches as instance variables.
​`set_urlconf` is called with when ​we first handle a request in `BaseHandler.get_response`.
get_resolver has a number of call-sites. Most notably, ​`reverse`. Like the other call-sites, reverse calls get_resolver w...
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

- [2025-12-03 00:41] **swebench-django__django-11333**: Task completed: Submitted
## Interaction Log

- `00:41:01` ACTION: Submitting solution
- `00:40:56` Root cause: get_resolver used functools.lru_cache directly, so calls with None and with settings.ROOT_URLCONF produced separate cached URLResolver ins...
- `00:40:56` repro: settings.ROOT_URLCONF: myurls; get_resolver(None) is get_resolver(settings.ROOT_URLCONF): True; ids: 140737474928936, 140737474928936
- `00:40:37` ACTION: printf "ROOT_URLCONF = 'myurls'\nSECRET_KEY = 'x'\n" > settings_for_repro. [...]
- `00:40:25` ACTION: echo "ROOT_URLCONF = 'myurls'" > settings_for_repro.py && echo "urlpatterns = []" > myurls. [...]
- `00:40:00` ACTION: Reading file: <<'PY'
- `00:39:39` ACTION: nl -ba django/urls/resolvers.py | sed -n '360,640p'
- `00:39:16` patched django/urls/resolvers.py: replaced lru_cache get_resolver with wrapper delegating to _get_resolver; bound cache_clear and cache_info on public...
- `00:38:38` ACTION: python - <<'PY'
- `00:38:14` RESULT: django/urls/base.py:95:    get_resolver.cache_clear()
- `00:38:13` ACTION: grep -RIn --line-number "get_resolver.cache_clear" -n django || true
- `00:37:59` ACTION: nl -ba django/urls/base.py | sed -n '1,240p'
- `00:37:51` ACTION: nl -ba django/urls/resolvers.py | sed -n '1,220p'
- `00:37:37` ACTION: grep -RIn --line-number -e "def get_resolver" -e "class URLResolver" -e "def set_urlconf" -e "get_re [...]
- `00:37:32` ACTION: ls -la
- `00:37:24` RESULT: grep: testbed: No such file or directory
- `00:37:24` ACTION: grep -RIn --line-number -e "get_resolver" -e "set_urlconf" -e "URLResolver" -e "ROOT_URLCONF" testbe [...]
- `00:37:15` TASK STARTED: Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`
