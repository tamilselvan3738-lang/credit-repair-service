from PIL import Image
import os

src = r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.user_uploaded\media_1794292205602_6bdca0ef.jpg"
dst_webp = r"images\home2-concierge-vip-results.webp"
dst_jpg = r"images\home2-concierge-vip-results.jpg"

im = Image.open(src)
# Save as high-quality webp
im.save(dst_webp, "WEBP", quality=95)
# Also save as jpg
im.save(dst_jpg, "JPEG", quality=95)

print(f"Saved {dst_webp} ({os.path.getsize(dst_webp)} bytes)")
print(f"Saved {dst_jpg} ({os.path.getsize(dst_jpg)} bytes)")
