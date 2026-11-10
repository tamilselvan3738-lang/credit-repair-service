import glob, re

files = sorted(glob.glob("*.html"))
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    
    matches = re.findall(r'<motion\.div[^>]*rotate[^>]*>.*?</motion\.div>', c, re.DOTALL)
    if matches:
        print(f"=== {f} ===")
        for m in matches:
            print(m)
