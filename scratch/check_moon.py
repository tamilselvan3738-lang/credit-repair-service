import re
from PIL import Image

# Let's inspect the user uploaded image
im = Image.open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.user_uploaded\media_1794291325719_528d3bfe.png")
print("User image dimensions:", im.size)

# Let's find every occurrence of the theme toggle and IconMoon across all HTML files
html_files = [
    '404.html', 'about.html', 'admin-dashboard.html', 'contact.html', 
    'credit-repair.html', 'home-2.html', 'index.html', 'login.html', 
    'navbar.html', 'plans.html', 'registeration.html', 'registration.html', 
    'resources.html', 'services.html', 'user-dashboard.html'
]

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        continue
    
    # Check for rotate: isDark ? 0 : 180 or similar
    rotations = re.findall(r'rotate:\s*isDark\s*\?\s*[^,}]+', content)
    # Check for IconMoon definitions
    moon_defs = re.findall(r'const IconMoon = [^;]+;', content)
    # Check for IconMoon usages
    moon_uses = re.findall(r'<IconMoon[^/>]*/>', content)
    
    print(f"File {filename}:")
    if rotations:
        print(f"  Rotations: {rotations}")
    if moon_defs:
        print(f"  Moon Def: {moon_defs[0][:80]}...")
    if moon_uses:
        print(f"  Moon Uses count: {len(moon_uses)}")
