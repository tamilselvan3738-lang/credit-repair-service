import glob, re

files = sorted(glob.glob("*.html"))

print("SUMMARY OF FILES AND THEIR MOON ICONS:")
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    
    has_old_path = 'd="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"' in c
    has_rotate = 'rotate: isDark ? 0 : 180' in c
    has_icon_moon = 'IconMoon' in c
    print(f"{f}: has_icon_moon={has_icon_moon}, has_old_path={has_old_path}, has_rotate={has_rotate}")
