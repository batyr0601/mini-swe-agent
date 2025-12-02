"""Template snippet for context management commands in system prompts."""

# Warning shown when context is artificially limited
LIMITED_CONTEXT_WARNING = """
## ⚠️ Limited Context Window

Your context window is limited to {max_context_tokens} tokens. As the conversation grows, older messages will be dropped.

**CRITICAL: Your context persists outside the conversation window. Use it!**

Your TODO list, logs, and commits are stored in `.context/` and survive context truncation.
When you feel lost or the conversation seems incomplete, run `context_summary` to recall your progress.
"""

CONTEXT_COMMANDS_TEMPLATE = """
## Context Management - TODO-Driven Workflow

You have a persistent context system that survives conversation truncation. **Follow this workflow strictly.**

### ⚡ REQUIRED Workflow

**STEP 1: ANALYZE & PLAN (First thing after receiving a task)**
Before writing any code, create a detailed TODO list:
```
context_todos --add "1. Understand the bug: [specific description of what to investigate]"
context_todos --add "2. Locate the code: [specific files/functions to find]"
context_todos --add "3. Root cause analysis: [what to analyze]"
context_todos --add "4. Implement fix: [specific changes to make]"
context_todos --add "5. Verify fix: [how to test the fix]"
```

**STEP 2: WORK ON EACH TODO**
For each TODO:
1. **After each command**, log a summary of what you learned
2. Log your findings and decisions
3. When done, mark complete: `context_todos --complete N` (saves progress to context)

**CRITICAL: Log in a SEPARATE step AFTER seeing output.**

The `context_log` command is intercepted before bash runs, so `$(...)` and `$VAR` will NOT be expanded.

✗ **WRONG** - bash variables won't work:
```bash
result=$(grep foo file.py) && context_log "found: $result"  # $result is literal text!
```

✓ **RIGHT** - run command first, then log separately:
```bash
# Step N: run command and see output
grep -n "__getattr__" astropy/coordinates/*.py
```
Then in your NEXT response, after seeing the output:
```bash
# Step N+1: log with actual values you observed
context_log "grep __getattr__: sky_coordinate.py:869,898 frame.py:234"
```

**Always use literal values you saw in the output, never bash variables or substitutions.**

**STEP 3: RECOVER WHEN LOST**
If context was truncated and you feel lost:
```
context_summary
```
This shows your TODOs, milestones, and recent activity.

### Commands Reference

| Command | Purpose |
|---------|---------|
| `context_todos` | View your TODO list |
| `context_todos --add "task"` | Add a TODO (be specific!) |
| `context_todos --complete N` | Mark TODO #N done (saves to context) |
| `context_log "message"` | Log a finding, decision, or observation |
| `context_commit --message "..."` | Manual checkpoint at a milestone |
| `context_summary` | **Primary recovery command** - shows progress |

### What to Log (Real Values From Output)

**In a SEPARATE response after seeing command output, log what you found:**

| After seeing... | In NEXT response, log... |
|-----------------|--------------------------|
| grep output | `context_log "grep __getattr__: sky_coordinate.py:869,898 frame.py:234"` |
| file content | `context_log "sky_coordinate.py:860-920: __getattr__ catches AttributeError at 898"` |
| error message | `context_log "repro.py: AttributeError 'no attr prop' at line 898"` |
| test results | `context_log "test_sky_coord.py: 47 passed, 2 failed"` |

**Also log key insights:**
- `context_log "Root cause: __getattr__ catches property's AttributeError, re-raises with wrong attr"`
- `context_log "Fix: check class descriptors first, let their errors propagate"`

**NEVER use:** `$VAR`, `$(...)`, `${...}` - these won't be expanded!

### TODO Guidelines (Be Specific!)

**Good TODOs:**
- "Reproduce the bug using SkyCoord subclass example from issue"
- "Find __getattr__ method in sky_coordinate.py causing AttributeError"
- "Fix error message to show actual missing attribute name"
- "Test fix with provided test case"

**Bad TODOs:**
- "Fix the bug" (too vague)
- "Look at code" (not actionable)
- "Debug" (not specific)

### Example Session (Each box = one response)

```
# Response 1: Create TODO list
context_todos --add "1. Reproduce bug" && context_todos --add "2. Locate __getattr__" && context_todos --add "3. Fix" && context_todos --add "4. Test"
```

```
# Response 2: Run grep (just the command, no context_log yet)
grep -n "__getattr__" astropy/coordinates/*.py
```

```
# Response 3: AFTER seeing grep output, log what you found with actual values
context_log "grep __getattr__: sky_coordinate.py:869,898,906 frame.py:234"
```

```
# Response 4: Read the file
sed -n '860,920p' astropy/coordinates/sky_coordinate.py  
```

```
# Response 5: AFTER seeing file content, log what you learned
context_log "sky_coordinate.py:869-920: __getattr__ catches AttributeError at 898, re-raises with wrong attr"
```

```
# Response 6: Run repro script
python3 repro.py
```

```
# Response 7: AFTER seeing error, log it and mark TODO complete
context_log "repro.py: AttributeError 'no attr prop' at line 898" && context_todos --complete 1
```

```
# If context truncated later, recover with:
context_summary
```

### Remember
- TODOs persist across context truncation - they're your roadmap
- Logs are your memory - be concise but capture key details
- Completing a TODO = automatic context checkpoint (NOT a git commit)
- When confused, `context_summary` is your friend
- **NEVER run `git commit` before the final submission** - it will cause your patch to be empty
"""
