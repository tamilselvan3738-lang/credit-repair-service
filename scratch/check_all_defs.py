import glob, re

files = sorted(glob.glob("*.html"))
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    defs = re.findall(r"const IconMoon = [^;]+;", c)
    rotates = re.findall(r"rotate:\s*isDark\s*\?\s*[^,}]+", c)
    print(f"=== {f} ===")
    for d in defs:
        # print path
        p = re.findall(r'<path[^>]+>', d)
        print("  def:", p)
    if rotates:
        print("  rotates:", rotates)
