with open("home-2.html", "r", encoding="utf-8") as f:
    c = f.read()

import re

# Find sections
sections = re.findall(r'<section\b[^>]*>(.*?)</section>', c, re.DOTALL)
print(f"Total sections found: {len(sections)}")

for i, sec in enumerate(sections):
    # find id
    sec_id = re.search(r'id=["\']([^"\']+)["\']', sec)
    id_str = sec_id.group(1) if sec_id else f"section-{i+1}"
    # find h1, h2, h3
    h_tags = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', sec, re.DOTALL)
    clean_h = [re.sub(r'<[^>]+>', '', h).strip() for h in h_tags]
    # find p tags
    p_tags = re.findall(r'<p[^>]*>(.*?)</p>', sec, re.DOTALL)
    clean_p = [re.sub(r'<[^>]+>', '', p).strip() for p in p_tags]
    # find img
    img = re.search(r'<img[^>]*>', sec)
    img_tag = img.group(0) if img else "NO IMG"
    
    print(f"\n================ SECTION {i+1}: {id_str} ================")
    print("Headings:", clean_h[:3])
    print("Paragraphs:", clean_p[:2])
    print("Img tag:", img_tag)
