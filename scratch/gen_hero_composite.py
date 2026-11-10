from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

def create_glow_line(draw, points, color, width=3, glow_color=(6, 182, 212, 60)):
    # Draw thicker semi-transparent lines underneath for neon glow
    for w, a in [(width+6, 25), (width+4, 60), (width+2, 120), (width, 255)]:
        c = (color[0], color[1], color[2], a)
        draw.line(points, fill=c, width=w)

def generate_hero_image():
    # Base: services-hero-command-center.jpg or about-company-hero.jpg
    base_path = "images/services-hero-command-center.jpg"
    img = Image.open(base_path).convert("RGBA")
    w, h = img.size # 1376, 768

    # Create an overlay layer for holographic HUD
    hud = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(hud)

    # Fonts
    font_bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
    font_large = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
    font_xl = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 52)
    font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
    font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 17)
    font_sm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)

    # Holographic HUD Panel coordinates (centered above desk)
    x0, y0, x1, y1 = 280, 110, 1100, 560

    # Draw semi-transparent glass backdrop
    glass_box = Image.new("RGBA", (x1 - x0, y1 - y0), (4, 15, 30, 175))
    hud.paste(glass_box, (x0, y0))

    # Glass border with neon cyan / emerald gradient effect
    draw.rounded_rectangle([x0, y0, x1, y1], radius=20, outline=(6, 182, 212, 190), width=2)
    draw.rounded_rectangle([x0+2, y0+2, x1-2, y1-2], radius=18, outline=(16, 185, 129, 90), width=1)

    # Header bar
    draw.line([(x0+20, y0+55), (x1-20, y0+55)], fill=(6, 182, 212, 100), width=1)
    
    # Title & Badge
    draw.text((x0+30, y0+20), "TIER-1 WEALTH SUITE • REAL-TIME BUREAU GATEWAY", font=font_mono_bold, fill=(56, 189, 248, 255))
    draw.rounded_rectangle([x1-230, y0+16, x1-30, y0+44], radius=8, fill=(16, 185, 129, 35), outline=(16, 185, 129, 160), width=1)
    draw.text((x1-215, y0+22), "FICO® SCORE 850 PRIME", font=font_mono_bold, fill=(52, 211, 153, 255))

    # Left Section: 3-Bureau synchronous score cards
    card_y = y0 + 80
    bureaus = [
        ("EXPERIAN", "848", "+214 PTS", (56, 189, 248)),
        ("EQUIFAX", "850", "+236 PTS", (16, 185, 129)),
        ("TRANSUNION", "850", "+198 PTS", (129, 140, 248))
    ]

    bx = x0 + 30
    bw = 145
    bh = 110
    for name, score, pts, col in bureaus:
        draw.rounded_rectangle([bx, card_y, bx+bw, card_y+bh], radius=14, fill=(8, 22, 45, 200), outline=(col[0], col[1], col[2], 140), width=1)
        draw.text((bx+15, card_y+12), name, font=font_mono_bold, fill=(col[0], col[1], col[2], 255))
        draw.text((bx+15, card_y+36), score, font=font_xl, fill=(255, 255, 255, 255))
        draw.text((bx+15, card_y+85), f"▲ {pts}", font=font_mono_bold, fill=(16, 185, 129, 255))
        bx += bw + 18

    # Right Section: Executive Black Card
    card_x0, card_y0 = x0 + 510, card_y
    card_x1, card_y1 = x1 - 30, card_y + 190
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=16, fill=(11, 17, 30, 235), outline=(56, 189, 248, 180), width=2)
    # Card details
    draw.text((card_x0+25, card_y0+20), "EXECUTIVE WEALTH BLACK CARD", font=font_mono, fill=(148, 163, 184, 255))
    draw.text((card_x0+25, card_y0+42), "CREDIT REPAIR SERVICE", font=font_bold, fill=(255, 255, 255, 255))
    
    # Golden Chip
    chip_x, chip_y = card_x1 - 65, card_y0 + 25
    draw.rounded_rectangle([chip_x, chip_y, chip_x+40, chip_y+30], radius=5, fill=(217, 119, 6, 230), outline=(251, 191, 36, 255), width=1)

    # Card number
    draw.text((card_x0+25, card_y0+105), "••••  ••••  ••••  8500", font=font_large, fill=(241, 245, 249, 255))
    
    # Authorized client & limit
    draw.text((card_x0+25, card_y0+152), "AUTHORIZED CLIENT: MARCUS V. STERLING", font=font_mono, fill=(148, 163, 184, 255))
    draw.text((card_x1-150, card_y0+152), "$250,000 USD", font=font_mono_bold, fill=(52, 211, 153, 255))

    # Bottom Area of HUD: Upward Score Surge Trajectory Chart
    chart_y0 = y0 + 225
    chart_h = 160
    draw.rounded_rectangle([x0+30, chart_y0, x0+480, chart_y0+chart_h], radius=14, fill=(8, 22, 45, 180), outline=(6, 182, 212, 100), width=1)
    draw.text((x0+45, chart_y0+14), "ALGORITHMIC ASCENSION TRAJECTORY (580 → 850)", font=font_mono_bold, fill=(56, 189, 248, 255))

    # Chart curve
    pts = [
        (x0+50, chart_y0+125),
        (x0+120, chart_y0+115),
        (x0+190, chart_y0+90),
        (x0+260, chart_y0+75),
        (x0+330, chart_y0+45),
        (x0+420, chart_y0+35),
        (x0+460, chart_y0+30),
    ]
    create_glow_line(draw, pts, (16, 185, 129), width=3)
    # Data points
    for p in pts:
        draw.ellipse([p[0]-4, p[1]-4, p[0]+4, p[1]+4], fill=(255, 255, 255, 255), outline=(16, 185, 129, 255), width=2)

    # Bottom metrics
    draw.text((x0+50, chart_y0+135), "OCT: 580", font=font_mono, fill=(148, 163, 184, 255))
    draw.text((x0+230, chart_y0+135), "DEC: 720", font=font_mono, fill=(148, 163, 184, 255))
    draw.text((x0+400, chart_y0+135), "MAR: 850 PRIME", font=font_mono_bold, fill=(52, 211, 153, 255))

    # Utilization bar
    util_x0 = x0 + 510
    draw.rounded_rectangle([util_x0, y0+300, x1-30, y0+385], radius=14, fill=(8, 22, 45, 180), outline=(16, 185, 129, 100), width=1)
    draw.text((util_x0+20, y0+312), "REVOLVING CREDIT UTILIZATION COMPRESSION", font=font_mono_bold, fill=(56, 189, 248, 255))
    draw.text((util_x0+20, y0+334), "OPTIMAL: 2.8% of $1,450,000 Capacity (Reduced from 78%)", font=font_sm, fill=(203, 213, 225, 255))
    # progress bar
    draw.rounded_rectangle([util_x0+20, y0+360, x1-50, y0+372], radius=6, fill=(15, 23, 42, 255), outline=(51, 65, 85, 255), width=1)
    draw.rounded_rectangle([util_x0+20, y0+360, util_x0+50, y0+372], radius=6, fill=(16, 185, 129, 255))

    # Footer status line
    draw.text((x0+35, y1-30), "● FCRA § 611 COMPLIANT • 100% REGULATORY SANCTIONED • 14ms REPOSITORY LATENCY", font=font_mono, fill=(100, 116, 139, 255))

    # Composite HUD onto base image
    final_img = Image.alpha_composite(img, hud).convert("RGB")
    final_img.save("scratch/test_hero_composite.webp", "WEBP", quality=95)
    print("Saved scratch/test_hero_composite.webp")

generate_hero_image()
