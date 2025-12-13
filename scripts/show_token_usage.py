#!/usr/bin/env python3
"""Extract token usage information from a trajectory file."""

import json
import sys
from pathlib import Path


def analyze_tokens(traj_path: Path):
    """Analyze token usage from trajectory file."""
    with open(traj_path) as f:
        data = json.load(f)
    
    # Get summary stats
    info = data.get("info", {})
    model_stats = info.get("model_stats", {})
    
    print("=" * 60)
    print("TOKEN USAGE SUMMARY")
    print("=" * 60)
    print(f"Instance: {info.get('instance_id', 'unknown')}")
    print(f"Exit Status: {info.get('exit_status', 'unknown')}")
    print()
    print("Overall Stats:")
    print(f"  Total Cost: ${model_stats.get('instance_cost', 0):.6f}")
    print(f"  API Calls: {model_stats.get('api_calls', 0)}")
    print()
    
    # Analyze per-call usage
    messages = data.get("messages", [])
    assistant_messages = [m for m in messages if m.get("role") == "assistant"]
    
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0
    total_reasoning_tokens = 0
    total_cached_tokens = 0
    
    print("Per-Call Breakdown:")
    print("-" * 60)
    
    for i, msg in enumerate(assistant_messages, 1):
        extra = msg.get("extra", {})
        response = extra.get("response", {})
        usage = response.get("usage", {})
        
        if not usage:
            continue
        
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        total_call_tokens = usage.get("total_tokens", 0)
        
        completion_details = usage.get("completion_tokens_details", {})
        reasoning_tokens = completion_details.get("reasoning_tokens", 0)
        
        prompt_details = usage.get("prompt_tokens_details", {})
        cached_tokens = prompt_details.get("cached_tokens", 0)
        
        total_prompt_tokens += prompt_tokens
        total_completion_tokens += completion_tokens
        total_tokens += total_call_tokens
        total_reasoning_tokens += reasoning_tokens
        total_cached_tokens += cached_tokens
        
        print(f"Call {i:2d}: Prompt={prompt_tokens:5d} (cached={cached_tokens:5d}) | "
              f"Completion={completion_tokens:4d} (reasoning={reasoning_tokens:4d}) | "
              f"Total={total_call_tokens:5d}")
    
    print("-" * 60)
    print("Totals:")
    print(f"  Prompt Tokens:     {total_prompt_tokens:6d} (cached: {total_cached_tokens:6d})")
    print(f"  Completion Tokens: {total_completion_tokens:6d} (reasoning: {total_reasoning_tokens:6d})")
    print(f"  Total Tokens:      {total_tokens:6d}")
    print()
    print(f"  Cache Hit Rate:   {(total_cached_tokens / total_prompt_tokens * 100) if total_prompt_tokens > 0 else 0:.1f}%")
    print(f"  Reasoning Ratio:   {(total_reasoning_tokens / total_completion_tokens * 100) if total_completion_tokens > 0 else 0:.1f}%")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python show_token_usage.py <trajectory.json>")
        sys.exit(1)
    
    traj_path = Path(sys.argv[1])
    if not traj_path.exists():
        print(f"Error: File not found: {traj_path}")
        sys.exit(1)
    
    analyze_tokens(traj_path)

