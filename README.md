# Experimental Results

## Overview

We had two setups:
- **Baseline**: No Arbor system
- **Experimental**: With Arbor (context system)

For each system, we tested:
- Untruncated
- 16k truncated (simulated 16K token context window)
- 8k truncated (simulated 8K token context window)
- 4k truncated (simulated 4K token context window)

**Total: 8 experimental setups**

Each setup has:
- A `preds.json` file
- A SWE-bench results JSON file
- Command used to run the experiment
- Success rate (resolved instances / total instances)

---

## Results Summary

1. **Untruncated Context**: 28/50 resolved (56%)
2. **Untruncated Baseline**: 22/50 resolved (44%)
3. **16k Truncated Context**: 24/50 resolved (48%)
4. **16k Truncated Baseline**: 21/50 resolved (42%)
5. **8k Truncated Context**: 22/50 resolved (44%)
6. **8k Truncated Baseline**: 8/50 resolved (16%)
7. **4k Truncated Context**: 6/50 resolved (12%)
8. **4k Truncated Baseline**: 1/50 resolved (2%)

---

## Detailed Results

### 1. Untruncated Context
- **Results**: 28/50 resolved
- **Preds file**: `/Users/batyr/Coding/context/mini-swe-agent/results-context-untruncated-50questions/preds.json`
- **SWE-bench file**: `/Users/batyr/Coding/context/SWE-bench/openai__gpt-5-mini.results-context-untruncated-50questions.json`
- **Command**:
```bash
mini-tool-extra swebench --model openai/gpt-5-mini --subset verified --split test --slice 0:50 -o ./results-context-untruncated-50questions --config /Users/batyr/Coding/context/mini-swe-agent/src/minisweagent_tool/config/extra/swebench_context.yaml --workers 10
```

### 2. Untruncated Baseline
- **Results**: 22/50 resolved
- **Preds file**: `/Users/batyr/Coding/context/mini-swe-agent/results-baseline-untruncated-50questions/preds.json`
- **SWE-bench file**: `/Users/batyr/Coding/context/SWE-bench/openai__gpt-5-mini.results-baseline-untruncated-50questions.json`
- **Notes**: Terribly unlucky run? Also 2 patches were empty??? — is the empty bug in mini swe agent?? Or do we add this much of an improvement on even untruncated?
- **Command**:
```bash
mini-tool-extra swebench --model openai/gpt-5-mini --subset verified --split test --slice 0:50 -o ./results-baseline-untruncated-50questions --workers 10
```

### 3. 16k Truncated Context
- **Results**: 24/50 resolved
- **Preds file**: `/Users/batyr/Coding/context/mini-swe-agent/results-context-truncated-16k-50questions/preds.json`
- **SWE-bench file**: `/Users/batyr/Coding/context/SWE-bench/openai__gpt-5-mini.results-context-truncated-16k-50questions.json`
- **Command**:
```bash
mini-tool-extra swebench --model openai/gpt-5-mini --subset verified --split test --slice 0:50 -o ./results-context-truncated-16k-50questions --config /Users/batyr/Coding/context/mini-swe-agent/src/minisweagent_tool/config/extra/swebench_context.yaml --max-context-tokens 16000 --workers 10
```

### 4. 16k Truncated Baseline
- **Results**: 21/50 resolved
- **Preds file**: `/Users/batyr/Coding/context/mini-swe-agent/results_baseline_truncated/preds.json`
- **SWE-bench file**: `/Users/batyr/Coding/context/SWE-bench/openai__gpt-5-mini.results_baseline_truncated.json`
- **Command**: [no command for this]

### 5. 8k Truncated Context
- **Results**: 22/50 resolved
- **Preds file**: `/Users/batyr/Coding/context/mini-swe-agent/results-context-truncated-8k-50questions/preds.json`
- **SWE-bench file**: `/Users/batyr/Coding/context/SWE-bench/openai__gpt-5-mini.results-context-truncated-8k-50questions.json`
- **Command**:
```bash
mini-tool-extra swebench --model openai/gpt-5-mini --subset verified --split test --slice 0:50 -o ./results-context-truncated-8k-50questions --config /Users/batyr/Coding/context/mini-swe-agent/src/minisweagent_tool/config/extra/swebench_context.yaml --max-context-tokens 8000 --workers 10
```

### 6. 8k Truncated Baseline
- **Results**: 8/50 resolved
- **Preds file**: `/Users/omagr/Documents/Personal/Agents/mini-swe-agent_tool/results_no_context_trunc8k_50_run/preds.json`
- **SWE-bench file**: `/Users/omagr/Documents/Personal/Agents/SWE-bench/openai__gpt-5-mini.trunc_8k_tool_50_run_no_context_1.json`
- **Notes**: A lot of empty patches, idk why
- **Command**:
```bash
mini-tool-extra swebench \
  --model openai/gpt-5-mini \
  --subset verified \
  --split test \
  --slice 0:50 \
  -o ./results_no_context_trunc8k_50_run \
  --max-context-tokens 8000 \
  --workers 10
```

### 7. 4k Truncated Context
- **Results**: 6/50 resolved
- **Preds file**: `/Users/omagr/Documents/Personal/Agents/mini-swe-agent_tool/results_context_trunc4k_50_run/preds.json`
- **SWE-bench file**: `/Users/omagr/Documents/Personal/Agents/SWE-bench/openai__gpt-5-mini.trunc_4k_tool_50_run.json`
- **Command**: [can't find the command to run for some reason]

### 8. 4k Truncated Baseline
- **Results**: 1/50 resolved
- **Preds file**: `/Users/omagr/Documents/Personal/Agents/mini-swe-agent_tool/results_no_context_trunc4k_50_run/preds.json`
- **SWE-bench file**: `/Users/omagr/Documents/Personal/Agents/SWE-bench/openai__gpt-5-mini.trunc_4k_tool_50_run_no_context.json`
- **Command**:
```bash
mini-tool-extra swebench \
  --model openai/gpt-5-mini \
  --subset verified \
  --split test \
  --slice 0:50 \
  -o ./results_no_context_trunc4k_50_run \
  --max-context-tokens 4000 \
  --workers 10
```

---

## Observations

1. **Context system consistently outperforms baseline** across all truncation levels
2. **Performance degrades significantly** as context window decreases (especially below 8k)
3. **Empty patches issue** observed in:
   - Untruncated baseline (2 empty patches)
   - 8k truncated baseline (many empty patches)
4. **Untruncated baseline** (22/50) may have been an unlucky run, as it's lower than expected compared to 16k truncated baseline (21/50)

