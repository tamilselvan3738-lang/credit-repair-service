import re

with open("home-2.html", "r", encoding="utf-8") as f:
    c = f.read()

imgs = re.findall(r'<img[^>]+>', c)
for i, tag in enumerate(imgs):
    m = re.search(r'src=["\']([^"\']+)["\']', tag)
    alt = re.search(r'alt=["\']([^"\']+)["\']', tag)
    print(f"Image {i+1}:")
    print(f"  src: {m.group(1) if m else 'none'}")
    print(f"  alt: {alt.group(1) if alt else 'none'}")
