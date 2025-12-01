#!/usr/bin/env python3
"""
Analyze mini-swe-agent run results.

Usage:
    python scripts/analyze_results.py [RESULTS_DIR]

Arguments:
    RESULTS_DIR  Path to results directory (default: ./results)

Examples:
    # Analyze default results directory
    python scripts/analyze_results.py

    # Analyze a specific results directory
    python scripts/analyze_results.py ./my_experiment/results

    # From project root
    python scripts/analyze_results.py results/

    # Get help
    python scripts/analyze_results.py --help

The script reads .traj.json files and minisweagent.log to extract:
    - Total and per-instance costs
    - API call counts
    - Token usage (prompt, completion, cached, reasoning)
    - Exit statuses
    - Timing per instance (from container start to trajectory save)
"""

import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Optional
import re
import typer


def parse_trajectory(traj_file: Path) -> dict:
    """Parse a single trajectory file and extract stats."""
    data = json.loads(traj_file.read_text())
    info = data.get("info", {})
    stats = info.get("model_stats", {})

    # Sum tokens from all messages with responses
    prompt_tokens = 0
    completion_tokens = 0
    cached_tokens = 0
    reasoning_tokens = 0

    for msg in data.get("messages", []):
        extra = msg.get("extra", {})
        response = extra.get("response", {})
        usage = response.get("usage", {})

        prompt_tokens += usage.get("prompt_tokens", 0)
        completion_tokens += usage.get("completion_tokens", 0)

        # Detailed token breakdowns (if available)
        prompt_details = usage.get("prompt_tokens_details", {})
        cached_tokens += prompt_details.get("cached_tokens", 0)

        completion_details = usage.get("completion_tokens_details", {})
        reasoning_tokens += completion_details.get("reasoning_tokens", 0)

    return {
        "instance_id": data.get("instance_id", traj_file.stem),
        "cost": stats.get("instance_cost", 0),
        "api_calls": stats.get("api_calls", 0),
        "exit_status": info.get("exit_status", "unknown"),
        "model": info.get("config", {}).get("model", {}).get("model_name", "unknown"),
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "cached_tokens": cached_tokens,
        "reasoning_tokens": reasoning_tokens,
    }


def parse_log_timing(log_file: Path) -> dict[str, float]:
    """
    Parse log file to extract per-instance timing.
    Returns dict mapping instance_id -> duration in seconds.
    """
    if not log_file.exists():
        return {}

    log_text = log_file.read_text()
    instance_times = {}

    # Find container start times
    # Format: 2025-11-30 21:13:23,304 - ... Starting container ... astropy_1776_astropy-13033:latest
    # The log uses underscores like "astropy_1776_astropy-13033" but traj files use "astropy__astropy-13033"
    container_starts = re.findall(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+.*Starting container.*?(\w+)_\d+_(\w+-\d+):latest",
        log_text,
    )

    # Find trajectory save times
    # Format: 2025-11-30 21:16:46,775 - ... Saved trajectory ... /astropy__astropy-13033.traj.json
    saves = re.findall(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d+.*Saved trajectory.*/(\w+__\w+-\d+)\.traj\.json",
        log_text,
    )

    # Build lookup of start times, normalizing the instance ID format
    # Log format: "astropy_1776_astropy-13033" -> normalize to "astropy__astropy-13033"
    start_times = {}
    for ts, repo, issue in container_starts:
        # Reconstruct canonical instance_id: "astropy__astropy-13033"
        instance_id = f"{repo}__{issue}"
        start_times[instance_id] = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

    # Calculate durations
    for ts, instance_id in saves:
        end_time = datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        if instance_id in start_times:
            duration = (end_time - start_times[instance_id]).total_seconds()
            instance_times[instance_id] = duration

    return instance_times


def main(results_dir: Optional[str] = typer.Argument(None, help="Path to results directory (default: ./results)")):
    """Main analysis function."""
    if results_dir is None:
        # Default: look for results in current dir or project root
        results_dir = Path("results")
        if not results_dir.exists():
            results_dir = Path(__file__).parent.parent.parent / "results"
    else:
        results_dir = Path(results_dir)
    
    if not results_dir.exists():
        print(f"Error: Results directory not found: {results_dir}")
        sys.exit(1)
    # Find all trajectory files
    traj_files = list(results_dir.glob("*/*.traj.json"))

    if not traj_files:
        print(f"No trajectory files found in {results_dir}")
        sys.exit(1)

    # Parse trajectories
    instances = [parse_trajectory(f) for f in traj_files]

    # Parse timing from log
    log_file = results_dir / "minisweagent.log"
    timing = parse_log_timing(log_file)

    # Calculate totals
    total_cost = sum(i["cost"] for i in instances)
    total_api_calls = sum(i["api_calls"] for i in instances)
    total_prompt = sum(i["prompt_tokens"] for i in instances)
    total_completion = sum(i["completion_tokens"] for i in instances)
    total_cached = sum(i["cached_tokens"] for i in instances)
    total_reasoning = sum(i["reasoning_tokens"] for i in instances)
    total_time = sum(timing.values())

    # Group by exit status
    by_status = defaultdict(list)
    for inst in instances:
        by_status[inst["exit_status"]].append(inst["instance_id"])

    # Get model name (assume all same)
    model_name = instances[0]["model"] if instances else "unknown"

    # Print report
    print("=" * 70)
    print("MINI-SWE-AGENT RUN ANALYSIS")
    print("=" * 70)
    print(f"\nResults directory: {results_dir.absolute()}")
    print(f"Model: {model_name}")
    print(f"Instances analyzed: {len(instances)}")

    print("\n" + "-" * 70)
    print("SUMMARY")
    print("-" * 70)
    print(f"  Total cost:            ${total_cost:.4f}")
    print(f"  Total API calls:       {total_api_calls}")
    print(f"  Total tokens:          {total_prompt + total_completion:,}")
    print(f"    - Prompt tokens:     {total_prompt:,}")
    print(f"    - Completion tokens: {total_completion:,}")
    if total_cached:
        print(f"    - Cached tokens:     {total_cached:,}")
    if total_reasoning:
        print(f"    - Reasoning tokens:  {total_reasoning:,}")

    if total_time:
        print(f"\n  Total time:            {total_time / 60:.1f} minutes")
        print(f"  Avg time/instance:     {total_time / len(instances):.0f} seconds")

    print(f"\n  Avg cost/instance:     ${total_cost / len(instances):.4f}")
    print(f"  Avg API calls/instance: {total_api_calls / len(instances):.1f}")

    print("\n" + "-" * 70)
    print("EXIT STATUS BREAKDOWN")
    print("-" * 70)
    for status, ids in sorted(by_status.items()):
        print(f"  {status}: {len(ids)}")

    print("\n" + "-" * 70)
    print("PER-INSTANCE DETAILS")
    print("-" * 70)

    # Sort by instance_id
    for inst in sorted(instances, key=lambda x: x["instance_id"]):
        iid = inst["instance_id"]
        time_str = ""
        if iid in timing:
            t = timing[iid]
            time_str = f"  |  Time: {t:.0f}s"

        print(f"\n{iid}:")
        print(f"  Cost: ${inst['cost']:.4f}  |  Calls: {inst['api_calls']}  |  Status: {inst['exit_status']}{time_str}")
        print(f"  Tokens: {inst['prompt_tokens']:,} prompt + {inst['completion_tokens']:,} completion")
        if inst["cached_tokens"]:
            print(f"  Cached: {inst['cached_tokens']:,} ({inst['cached_tokens']*100/inst['prompt_tokens']:.0f}% of prompt)")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    typer.run(main)

