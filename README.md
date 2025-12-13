# Arbor & Experimental Results
**Arbor** is a context management system that persists agent state and reasoning outside the conversation window, enabling better performance when context is truncated.

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


<div align="center">
<a href="https://mini-swe-agent.com/latest/"><img src="https://github.com/SWE-agent/mini-swe-agent/raw/main/docs/assets/mini-swe-agent-banner.svg" alt="mini-swe-agent banner" style="height: 7em"/></a>
</div>

# The 100 line AI agent that solves GitHub issues & more

📣 [Gemini 3 Pro reaches 74% on SWE-bench verified with mini-swe-agent!](https://x.com/KLieret/status/1991164693839270372)<br/>
📣 [New blogpost: Randomly switching between GPT-5 and Sonnet 4 boosts performance](https://www.swebench.com/SWE-bench/blog/2025/08/19/mini-roulette/)

[![Docs](https://img.shields.io/badge/Docs-green?style=for-the-badge&logo=materialformkdocs&logoColor=white)](https://mini-swe-agent.com/latest/)
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://join.slack.com/t/swe-bench/shared_invite/zt-36pj9bu5s-o3_yXPZbaH2wVnxnss1EkQ)
[![PyPI - Version](https://img.shields.io/pypi/v/mini-swe-agent?style=for-the-badge&logo=python&logoColor=white&labelColor=black&color=deeppink)](https://pypi.org/project/mini-swe-agent/)

In 2024, [SWE-bench](https://github.com/swe-bench/SWE-bench) & [SWE-agent](https://github.com/swe-agent/swe-agent) helped kickstart the coding agent revolution.

We now ask: **What if SWE-agent was 100x smaller, and still worked nearly as well?**

`mini` is for

- **Researchers** who want to **[benchmark](https://swe-bench.com), [fine-tune](https://swesmith.com/) or RL** without assumptions, bloat, or surprises
- **Developers** who like their tools like their scripts: **short, sharp, and readable**
- **Engineers** who want something **trivial to sandbox & to deploy anywhere**

Here's some details:

- **Minimal**: Just [100 lines of python](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/agents/default.py) (+100 total for [env](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/environments/local.py),
[model](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/models/litellm_model.py), [script](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/run/hello_world.py)) — no fancy dependencies!
- **Powerful:** Resolves >74% of GitHub issues in the [SWE-bench verified benchmark](https://www.swebench.com/) ([leaderboard](https://swe-bench.com/)).
- **Convenient:** Comes with UIs that turn this into your daily dev swiss army knife!
- **Deployable:** In addition to local envs, you can use **docker**, **podman**, **singularity**, **apptainer**, and more
- **Tested:** [![Codecov](https://img.shields.io/codecov/c/github/swe-agent/mini-swe-agent?style=flat-square)](https://codecov.io/gh/SWE-agent/mini-swe-agent)
- **Cutting edge:** Built by the Princeton & Stanford team behind [SWE-bench](https://swebench.com) and [SWE-agent](https://swe-agent.com).

<details>

<summary>More motivation (for research)</summary>

[SWE-agent](https://swe-agent.com/latest/) jump-started the development of AI agents in 2024. Back then, we placed a lot of emphasis on tools and special interfaces for the agent.
However, one year later, as LMs have become more capable, a lot of this is not needed at all to build a useful agent!
In fact, mini-SWE-agent

- **Does not have any tools other than bash** — it doesn't even use the tool-calling interface of the LMs.
  This means that you can run it with literally any model. When running in sandboxed environments you also don't need to take care
  of installing a single package — all it needs is bash.
- **Has a completely linear history** — every step of the agent just appends to the messages and that's it.
  So there's no difference between the trajectory and the messages that you pass on to the LM.
  Great for debugging & fine-tuning.
- **Executes actions with `subprocess.run`** — every action is completely independent (as opposed to keeping a stateful shell session running).
  This makes it trivial to execute the actions in sandboxes (literally just switch out `subprocess.run` with `docker exec`) and to
  scale up effortlessly. Seriously, this is [a big deal](https://mini-swe-agent.com/latest/faq/#why-no-shell-session), trust me.

This makes it perfect as a baseline system and for a system that puts the language model (rather than
the agent scaffold) in the middle of our attention.
You can see the result on the [SWE-bench (bash only)](https://www.swebench.com/) leaderboard, that evaluates the performance of different LMs with `mini`.

</details>

<details>
<summary>More motivation (as a tool)</summary>

Some agents are overfitted research artifacts. Others are UI-heavy frontend monsters.

`mini` wants to be a hackable tool, not a black box.

- **Simple** enough to understand at a glance
- **Convenient** enough to use in daily workflows
- **Flexible** to extend

Unlike other agents (including our own [swe-agent](https://swe-agent.com/latest/)), it is radically simpler, because it:

- **Does not have any tools other than bash** — it doesn't even use the tool-calling interface of the LMs.
  Instead of implementing custom tools for every specific thing the agent might want to do, the focus is fully on the LM utilizing the shell to its full potential.
  Want it to do something specific like opening a PR?
  Just tell the LM to figure it out rather than spending time to implement it in the agent.
- **Executes actions with `subprocess.run`** — every action is completely independent (as opposed to keeping a stateful shell session running).
  This is [a big deal](https://mini-swe-agent.com/latest/faq/#why-no-shell-session) for the stability of the agent, trust me.
- **Has a completely linear history** — every step of the agent just appends to the messages that are passed to the LM in the next step and that's it.
  This is great for debugging and understanding what the LM is prompted with.

</details>

<details>
<summary>Should I use SWE-agent or mini-SWE-agent?</summary>

You should use `mini-swe-agent` if

- You want a quick command line tool that works locally
- You want an agent with a very simple control flow
- You want even faster, simpler & more stable sandboxing & benchmark evaluations
- You are doing FT or RL and don't want to overfit to a specific agent scaffold

You should use `swe-agent` if

- You need specific tools or want to experiment with different tools
- You want to experiment with different history processors
- You want very powerful yaml configuration without touching code

What you get with both

- Excellent performance on SWE-Bench
- A trajectory browser

</details>

<table>
<tr>
<td width="50%">
<a href="https://mini-swe-agent.com/latest/usage/mini/"><strong>Simple UI</strong></a> (<code>mini</code>)
</td>
<td>
<a href="https://mini-swe-agent.com/latest/usage/mini_v/"><strong>Visual UI</strong></a> (<code>mini -v</code>)
</td>
</tr>
<tr>
<td width="50%">

  ![mini](https://github.com/SWE-agent/swe-agent-media/blob/main/media/mini/gif/mini.gif?raw=true)

</td>
<td>

  ![miniv](https://github.com/SWE-agent/swe-agent-media/blob/main/media/mini/gif/mini2.gif?raw=true)

</td>
</tr>
<tr>
  <td>
    <a href="https://mini-swe-agent.com/latest/usage/swebench/"><strong>Batch inference</strong></a>
  </td>
  <td>
    <a href="https://mini-swe-agent.com/latest/usage/inspector/"><strong>Trajectory browser</strong></a>
  </td>
<tr>
<tr>

<td>

![swebench](https://github.com/SWE-agent/swe-agent-media/blob/main/media/mini/gif/swebench.gif?raw=true)

</td>

<td>

![inspector](https://github.com/SWE-agent/swe-agent-media/blob/main/media/mini/gif/inspector.gif?raw=true)

</td>

</tr>
<td>
<a href="https://mini-swe-agent.com/latest/advanced/cookbook/"><strong>Python bindings</strong></a>
</td>
<td>
<a href="https://mini-swe-agent.com"><strong>More in the docs</strong></a>
</td>
</tr>
<tr>
<td>

```python
agent = DefaultAgent(
    LitellmModel(model_name=...),
    LocalEnvironment(),
)
agent.run("Write a sudoku game")
```
</td>
<td>

* [Quick start](https://mini-swe-agent.com/latest/quickstart/)
* [`mini`](https://mini-swe-agent.com/latest/usage/mini/)
* [FAQ](https://mini-swe-agent.com/latest/faq/)
* [Global configuration](https://mini-swe-agent.com/latest/advanced/global_configuration/)
* [Yaml configuration files](https://mini-swe-agent.com/latest/advanced/yaml_configuration/)
* [Power up](https://mini-swe-agent.com/latest/advanced/cookbook/)

</td>
</tr>
</table>

## Let's get started!

**Option 1:** If you just want to try out the CLI (package installed in anonymous virtual environment)

```bash
pip install uv && uvx mini-swe-agent [-v]
# or
pip install pipx && pipx ensurepath && pipx run mini-swe-agent [-v]
```

**Option 2:** Install CLI & python bindings in current environment

```bash
pip install mini-swe-agent
mini -v  # run the CLI
```

**Option 3:** Install from source (developer setup)

```bash
git clone https://github.com/SWE-agent/mini-swe-agent.git
cd mini-swe-agent && pip install -e .
mini [-v]  # run the CLI
```

Read more in our [documentation](https://mini-swe-agent.com/latest/):

* [Quick start guide](https://mini-swe-agent.com/latest/quickstart/)
* More on [`mini`](https://mini-swe-agent.com/latest/usage/mini/) and [`mini -v`](https://mini-swe-agent.com/latest/usage/mini_v/)
* [Global configuration](https://mini-swe-agent.com/latest/advanced/global_configuration/)
* [Yaml configuration files](https://mini-swe-agent.com/latest/advanced/yaml_configuration/)
* [Power up with the cookbook](https://mini-swe-agent.com/latest/advanced/cookbook/)
* [FAQ](https://mini-swe-agent.com/latest/faq/)
* [Contribute!](https://mini-swe-agent.com/latest/contributing/)

## Attribution

If you found this work helpful, please consider citing the [SWE-agent paper](https://arxiv.org/abs/2405.15793) in your work:

```bibtex
@inproceedings{yang2024sweagent,
  title={{SWE}-agent: Agent-Computer Interfaces Enable Automated Software Engineering},
  author={John Yang and Carlos E Jimenez and Alexander Wettig and Kilian Lieret and Shunyu Yao and Karthik R Narasimhan and Ofir Press},
  booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems},
  year={2024},
  url={https://arxiv.org/abs/2405.15793}
}
```

Our other projects:

<div align="center">
  <a href="https://github.com/SWE-agent/SWE-agent"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/sweagent_logo_text_below.svg" alt="SWE-agent" height="120px"></a>
   &nbsp;&nbsp;
  <a href="https://github.com/SWE-agent/SWE-ReX"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/swerex_logo_text_below.svg" alt="SWE-ReX" height="120px"></a>
   &nbsp;&nbsp;
  <a href="https://github.com/SWE-bench/SWE-bench"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/swebench_logo_text_below.svg" alt="SWE-bench" height="120px"></a>
  &nbsp;&nbsp;
  <a href="https://github.com/SWE-bench/SWE-smith"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/swesmith_logo_text_below.svg" alt="SWE-smith" height="120px"></a>
  &nbsp;&nbsp;
  <a href="https://github.com/codeclash-ai/codeclash"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/codeclash_logo_text_below.svg" alt="CodeClash" height="120px"></a>
  &nbsp;&nbsp;
  <a href="https://github.com/SWE-bench/sb-cli"><img src="https://raw.githubusercontent.com/SWE-agent/swe-agent-media/refs/heads/main/media/logos_banners/sbcli_logo_text_below.svg" alt="sb-cli" height="120px"></a>
</div>
