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
1. Log your findings as you work: `context_log "Found issue in X: [details]"`
2. Log important decisions: `context_log "Decision: Using approach X because Y"`
3. When done, mark complete: `context_todos --complete N` (this auto-commits)

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
| `context_todos --complete N` | Mark TODO #N done (auto-commits) |
| `context_log "message"` | Log a finding, decision, or observation |
| `context_commit --message "..."` | Manual checkpoint at a milestone |
| `context_summary` | **Primary recovery command** - shows progress |

### What to Log (Summaries, Not Full Content)

**DO log:**
- `context_log "Found bug in astropy/coordinates/sky_coordinate.py:245 - __getattr__ returns wrong error"`
- `context_log "Root cause: when attr not found, raises misleading AttributeError instead of proper message"`
- `context_log "Fix approach: check if attr is a valid frame attribute before generic getattr"`
- `context_log "TESTED: reproduced bug with subclass test case"`

**DON'T log:**
- Full file contents
- Copy-pasted error messages
- Entire command outputs

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

### Example Session

```
# 1. After receiving task about SkyCoord subclass bug:
context_todos --add "1. Reproduce: create subclass of SkyCoord, access 'ra' attribute"
context_todos --add "2. Locate: find __getattr__ in SkyCoord class"
context_todos --add "3. Analyze: understand why AttributeError message is wrong"
context_todos --add "4. Fix: correct error handling to show proper attribute name"
context_todos --add "5. Test: verify fix with subclass example"

# 2. While working:
context_log "Found SkyCoord.__getattr__ at sky_coordinate.py:890"
context_log "Bug: line 901 catches AttributeError but re-raises with wrong attr name"

# 3. After completing TODO 1:
context_todos --complete 1

# 4. If context gets truncated later:
context_summary  # Shows your TODOs and what you've done
```

### Remember
- TODOs persist across context truncation - they're your roadmap
- Logs are your memory - be concise but capture key details
- Completing a TODO = automatic milestone commit
- When confused, `context_summary` is your friend
"""
