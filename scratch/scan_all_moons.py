import os, glob, re

files = glob.glob("*.html")
print(f"Total HTML files: {len(files)}")

for fpath in sorted(files):
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Check for IconMoon
    has_icon_moon = "IconMoon" in content
    # Check for theme toggle / isDark
    has_theme = "isDark" in content
    # Check for rotate: isDark ? 0 : 180
    rotations = re.findall(r"rotate:\s*isDark\s*\?\s*[^,}]+", content)
    # Check all places where IconMoon is called
    moon_calls = re.findall(r"<IconMoon[^>]*>", content)
    # Check if there are other moon SVGs or moon classes
    other_moons = re.findall(r"(<svg[^>]*>.*?moon.*?</svg>)", content, re.IGNORECASE | re.DOTALL)
    
    print(f"\n=== {fpath} ===")
    print(f"  has IconMoon: {has_icon_moon}")
    print(f"  moon_calls: {len(moon_calls)} -> {moon_calls}")
    print(f"  rotations: {rotations}")
    if other_moons:
        print(f"  other_moons: {len(other_moons)}")
