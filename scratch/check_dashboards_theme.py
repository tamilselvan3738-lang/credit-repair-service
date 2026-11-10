for fn in ['admin-dashboard.html', 'user-dashboard.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print(f"=== {fn} ===")
    import re
    matches = re.findall(r'<button[^>]*toggleTheme[^>]*>.*?</button>', c, re.DOTALL)
    for m in matches:
        print("  Button:", m[:200])
    # Also check toggleTheme calls
    for m in re.finditer(r'toggleTheme', c):
        pos = m.start()
        print("  Snippet:", c[pos-50:pos+150])
