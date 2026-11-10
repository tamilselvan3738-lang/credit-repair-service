import json

with open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") == 193:
            tool_calls = data.get("tool_calls", [])
            for tc in tool_calls:
                print("Args:", tc.get("args", {}).get("Path"))
                content = tc.get("args", {}).get("Content", "")
                print("Content snippet:", content[:500])
