import glob, re

for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    moons = [m.start() for m in re.finditer(r'moon', c, re.IGNORECASE)]
    print(f"=== {f}: {len(moons)} occurrences of 'moon' ===")
    for idx in moons:
        print("  ", repr(c[max(0, idx-30):min(len(c), idx+40)]))
