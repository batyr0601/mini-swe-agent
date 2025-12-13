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

- [2025-12-02 23:40] **swebench-django__django-11333**: Task completed: Submitted
## Interaction Log

- `23:39:59` ACTION: Submitting solution
- `23:39:53` Verification: with string ROOT_URLCONF get_resolver(None) and get_resolver(ROOT_URLCONF) return same cached object; with list ROOT_URLCONF they are di...
- `23:39:53` Fix: resolve settings.ROOT_URLCONF before calling cached helper; introduce @lru_cache _get_resolver(urlconf) and have get_resolver() call it, falling ...
- `23:39:53` Reproduced TypeError when calling cached helper with unhashable urlconf (list); root cause: lru_cache requires hashable args
- `23:39:36` ACTION: python3 - <<'PY'
- `23:39:31` RESULT: get_resolver updated to handle unhashable urlconf.
- `23:39:04` ACTION: python3 - <<'PY'
- `23:38:55` ACTION: nl -ba django/urls/resolvers.py | sed -n '60,110p'
- `23:38:51` Replaced lru_cache-decorated get_resolver with _get_resolver(urlconf) and wrapper get_resolver that looks up settings.ROOT_URLCONF before calling the ...
- `23:38:45` RESULT: File updated: get_resolver replaced with _get_resolver wrapper.
- `23:38:45` ACTION: python3 - <<'PY'
- `23:38:05` ACTION: nl -ba django/urls/resolvers.py | sed -n '60,80p'
- `23:38:02` RESULT: No replacement made; pattern not found.
- `23:38:01` ACTION: python3 - <<'PY'
- `23:37:35` ACTION: nl -ba django/urls/resolvers.py | sed -n '1,240p'
- `23:37:32` RESULT: django/urls/resolvers.py:67:def get_resolver(urlconf=None):
- `23:37:31` ACTION: grep -n "def get_resolver" -n django -R || true
- `23:37:28` ACTION: ls -la
- `23:37:25` TASK STARTED: Optimization: Multiple URLResolvers may be unintentionally be constructed by calls to `django.urls.resolvers.get_resolver`
