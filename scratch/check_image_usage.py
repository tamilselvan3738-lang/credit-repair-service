import glob, os, re

html_files = glob.glob("*.html")
all_images = os.listdir("images")

img_usage = {img: [] for img in all_images}

for hf in html_files:
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    for img in all_images:
        if img in c:
            img_usage[img].append(hf)

print("=== UNUSED IMAGES IN images/ ===")
for img, files in sorted(img_usage.items()):
    if not files:
        print(f"UNUSED: {img} ({os.path.getsize(os.path.join('images', img))} bytes)")

print("\n=== USED IMAGES IN images/ ===")
for img, files in sorted(img_usage.items()):
    if files:
        print(f"USED: {img} -> {files}")
