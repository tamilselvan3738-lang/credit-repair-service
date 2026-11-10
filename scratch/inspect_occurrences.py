import re

files = ['index.html', 'login.html', '404.html', 'admin-dashboard.html', 'user-dashboard.html']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    print('='*50)
    print(fn)
    pos = c.find('IconMoon')
    while pos != -1:
        start = max(0, pos - 150)
        end = min(len(c), pos + 250)
        print(f"--- Occurrence at {pos} ---")
        print(c[start:end])
        pos = c.find('IconMoon', pos + 1)
