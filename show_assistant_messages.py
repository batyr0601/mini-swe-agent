"""
Show all messages from a trajectory file.

Usage: python show_assistant_messages.py path/to/*.traj.json
"""
#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def main(path: str):
    traj_path = Path(path)
    data = json.loads(traj_path.read_text())

    messages = data.get("messages", [])
    for i, msg in enumerate(messages):
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        ts = msg.get("timestamp")
        role_upper = role.upper()
        header = f"[{role_upper} #{i} @ {ts}]" if ts is not None else f"[{role_upper} #{i}]"
        print("=" * 80)
        print(header)
        print("-" * 80)

        # Print the whole message
        print(content.rstrip())
        print()

        # Quick context-command summary (only for assistant messages)
        if role == "assistant":
            ctx_calls = [line for line in content.splitlines() if "context_" in line]
            if ctx_calls:
                print("  [context commands in this message:]")
                for line in ctx_calls:
                    print("   ", line.strip())
                print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python show_assistant_messages.py path/to/*.traj.json", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])