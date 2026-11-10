import json

with open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\c8172477-1eaf-490a-83c5-d5bb149bcbd8\.system_generated\logs\transcript_full.jsonl", "r", encoding="utf-8") as f:
    for i in range(10):
        line = f.readline()
        if not line: break
        data = json.loads(line)
        print(f"Line {i}: source={data.get('source')}, type={data.get('type')}")
        if data.get('tool_calls'):
            print("  tool_calls:", data.get('tool_calls'))
