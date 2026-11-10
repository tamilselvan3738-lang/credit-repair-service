import json

with open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        idx = data.get("step_index", 0)
        if 184 <= idx <= 195:
            print(f"Step {idx}: {data.get('source')}, {data.get('type')}")
            if data.get('tool_calls'):
                for tc in data.get('tool_calls'):
                    print("  TC:", tc.get('name'), tc.get('args', {}).get('CommandLine', '')[:100])
