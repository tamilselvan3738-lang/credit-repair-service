import glob

for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    count = c.count('M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z')
    print(f"{f}: {count} occurrences of old moon path")
