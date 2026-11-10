from bs4 import BeautifulSoup
import re

with open("home-2.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
imgs = soup.find_all("img")

print(f"Total img tags found: {len(imgs)}")
for i, img in enumerate(imgs):
    src = img.get("src", "")
    alt = img.get("alt", "")
    parent_section = img.find_parent("section")
    sec_id = parent_section.get("id", "no-id") if parent_section else "outside-section"
    # Find surrounding context/headings
    prev_h = img.find_previous(["h1", "h2", "h3", "h4"])
    prev_text = prev_h.get_text(strip=True) if prev_h else "none"
    print(f"\n--- Image {i+1} ---")
    print(f"  src: {src}")
    print(f"  alt: {alt}")
    print(f"  section id: {sec_id}")
    print(f"  nearest heading: {prev_text}")
