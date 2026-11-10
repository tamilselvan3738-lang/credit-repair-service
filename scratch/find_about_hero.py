import json

with open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        if "04:0" in data.get("created_at", "") or "04:1" in data.get("created_at", ""):
            if "about-company-hero" in json.dumps(data):
                print(f"Step {data.get('step_index')}: {data.get('source')}, {data.get('type')}")
                if data.get('tool_calls'):
                    for tc in data.get('tool_calls'):
                        print("  TC:", tc.get('name'), str(tc.get('args'))[:150])
