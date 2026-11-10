import re

with open("home-2.html", "r", encoding="utf-8") as f:
    c = f.read()

# Find all <img ...> tags
img_tags = re.findall(r'<img[^>]*>', c, re.IGNORECASE)

print(f"Total img tags found: {len(img_tags)}")
for i, tag in enumerate(img_tags):
    src_match = re.search(r'src=["\']([^"\']+)["\']', tag)
    alt_match = re.search(r'alt=["\']([^"\']+)["\']', tag)
    src = src_match.group(1) if src_match else "none"
    alt = alt_match.group(1) if alt_match else "none"
    
    pos = c.find(tag)
    # search backwards for nearest heading or section
    snippet_before = c[max(0, pos-400):pos]
    headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', snippet_before, re.DOTALL)
    heading = headings[-1].strip() if headings else "none"
    
    print(f"\n--- Image {i+1} ---")
    print(f"  Tag: {tag}")
    print(f"  src: {src}")
    print(f"  alt: {alt}")
    print(f"  Heading before: {heading}")
