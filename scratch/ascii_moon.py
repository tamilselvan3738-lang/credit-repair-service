from PIL import Image

im = Image.open(r"C:\Users\Tamiluuu\.gemini\antigravity\brain\dc5ba851-cba5-42f4-aea1-34a4dcdbf3a6\.user_uploaded\media_1794291325719_528d3bfe.png")
im = im.convert('RGBA')
w, h = im.size

# Let's print ASCII art where non-white pixels are '#' or '*'
lines = []
for y in range(h):
    row = ""
    for x in range(w):
        r, g, b, a = im.getpixel((x, y))
        # check if it's the blue/purple icon (b > 150 and r < 150)
        if b > 140 and r < 140:
            row += "@"
        elif r > 200 and g > 200 and b > 200:
            # check border
            if r < 230:
                row += "."
            else:
                row += " "
        else:
            row += "#"
    lines.append(row)

print("\n".join(lines))
