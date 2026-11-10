with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<button[^>]*toggleTheme[^>]*>.*?</button>', c, re.DOTALL)
for i, m in enumerate(matches):
    print(f"Match {i}:")
    print(m)
