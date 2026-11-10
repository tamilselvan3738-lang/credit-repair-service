from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

def create_hud_badge(draw, x, y, text, font, fill_bg, outline_col, text_col, pad_x=12, pad_y=6, radius=8):
    bbox = font.getbbox(text)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.rounded_rectangle([x, y, x + tw + pad_x*2, y + th + pad_y*2], radius=radius, fill=fill_bg, outline=outline_col, width=1)
    draw.text((x + pad_x, y + pad_y - bbox[1]), text, font=font, fill=text_col)
    return x + tw + pad_x*2

def create_glow_bar(draw, x, y, w, h, fill_col, glow_col, radius=6):
    draw.rounded_rectangle([x-2, y-2, x+w+2, y+h+2], radius=radius+2, fill=glow_col)
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill_col)

# Fonts
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 16)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 14)
font_mono_lg = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 28)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)

# =========================================================================
# IMAGE 1: home2-hero-executive-wealth.webp
# High-Stakes Credit Telemetry & Black Card, 850 FICO, 3-Bureau synchronous score
# =========================================================================
def build_image_1():
    base = Image.open("images/services-hero-command-center.jpg").convert("RGBA")
    w, h = base.size # 1376, 768
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Cinematic HUD Panel on right
    x0, y0, x1, y1 = 40, 40, 520, 240
    draw.rounded_rectangle([x0, y0, x1, y1], radius=16, fill=(3, 10, 24, 210), outline=(6, 182, 212, 190), width=2)
    
    draw.text((x0+20, y0+16), "TIER-1 WEALTH SUITE • BUREAU GATEWAY", font=font_mono_bold, fill=(56, 189, 248, 255))
    draw.line([(x0+20, y0+42), (x1-20, y0+42)], fill=(6, 182, 212, 80), width=1)
    
    # 3 Bureau scores
    bureaus = [("EXP", "848", (56, 189, 248)), ("EQF", "850", (16, 185, 129)), ("TRU", "850", (129, 140, 248))]
    bx = x0 + 20
    for name, score, col in bureaus:
        draw.rounded_rectangle([bx, y0+55, bx+135, y0+145], radius=10, fill=(8, 20, 42, 220), outline=col, width=1)
        draw.text((bx+15, y0+65), name, font=font_mono_bold, fill=col)
        draw.text((bx+15, y0+88), score, font=font_mono_lg, fill=(255, 255, 255, 255))
        draw.text((bx+15, y0+122), "▲ PRIME", font=font_mono, fill=(16, 185, 129, 255))
        bx += 150
        
    draw.text((x0+20, y0+165), "CURRENT TELEMETRY: 2.8% REVOLVING UTILIZATION", font=font_mono_bold, fill=(52, 211, 153, 255))
    draw.text((x0+20, y0+195), "FCRA § 611 COMPLIANT • 14ms DIRECT REPOSITORY LATENCY", font=font_mono, fill=(148, 163, 184, 255))

    # Top right badge
    rx0, ry0 = w - 420, 40
    draw.rounded_rectangle([rx0, ry0, rx0+380, ry0+75], radius=14, fill=(3, 10, 24, 210), outline=(16, 185, 129, 200), width=2)
    draw.text((rx0+20, ry0+14), "FICO® SCORE 850 PRIME", font=font_subtitle, fill=(52, 211, 153, 255))
    draw.text((rx0+20, ry0+42), "EXECUTIVE RESTORATION PROTOCOL ACTIVE", font=font_mono, fill=(56, 189, 248, 255))

    final = Image.alpha_composite(base, overlay).convert("RGB")
    final.save("images/home2-hero-executive-wealth.webp", "WEBP", quality=95)
    print("Generated home2-hero-executive-wealth.webp")

# =========================================================================
# IMAGE 2: home2-forensic-audit-scanner.webp
# Automated 3-Bureau Forensic Scanner Matrix, 42 parameters
# =========================================================================
def build_image_2():
    base = Image.open("images/services-report-analysis.jpg").convert("RGBA")
    w, h = base.size # 1376, 768
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Floating Header Banner
    x0, y0 = 40, 40
    draw.rounded_rectangle([x0, y0, x0+580, y0+90], radius=14, fill=(4, 12, 26, 220), outline=(6, 182, 212, 200), width=2)
    draw.text((x0+20, y0+14), "AI FORENSIC SCANNER MATRIX", font=font_title, fill=(56, 189, 248, 255))
    draw.text((x0+20, y0+52), "42 TRADELINE PARAMETERS • 3-BUREAU SYNCHRONOUS FEED", font=font_mono_bold, fill=(52, 211, 153, 255))
    
    # Forensic Confidence Callout (Right)
    rx0, ry0 = w - 380, 40
    draw.rounded_rectangle([rx0, ry0, rx0+340, ry0+90], radius=14, fill=(4, 12, 26, 220), outline=(16, 185, 129, 200), width=2)
    draw.text((rx0+20, ry0+14), "SCAN CONFIDENCE: 99.8%", font=font_subtitle, fill=(52, 211, 153, 255))
    draw.text((rx0+20, ry0+52), "DOLA RE-AGING AUDIT: 14 FLAGS EXPUNGED", font=font_mono, fill=(248, 113, 113, 255))

    final = Image.alpha_composite(base, overlay).convert("RGB")
    final.save("images/home2-forensic-audit-scanner.webp", "WEBP", quality=95)
    print("Generated home2-forensic-audit-scanner.webp")

# =========================================================================
# IMAGE 3: home2-tradeline-builder-vault.webp
# Tier-1 Tradeline Architecture & Utilization Vault
# =========================================================================
def build_image_3():
    base = Image.open("images/plans-tier-showcase.jpg").convert("RGBA")
    w, h = base.size # 1376, 768
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top Center Vault Banner
    bx0, by0, bx1, by1 = (w - 760)//2, 40, (w + 760)//2, 130
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=16, fill=(5, 12, 28, 225), outline=(16, 185, 129, 210), width=2)
    draw.text((bx0+30, by0+16), "TIER-1 TRADELINE ARCHITECTURE & UTILIZATION VAULT", font=font_title, fill=(52, 211, 153, 255))
    draw.text((bx0+30, by0+56), "$1,450,000 TOTAL REVOLVING CAPACITY • 2.8% OPTIMAL UTILIZATION", font=font_mono_bold, fill=(56, 189, 248, 255))

    # Bottom status docket
    bb0, bby0, bb1, bby1 = (w - 820)//2, h - 90, (w + 820)//2, h - 30
    draw.rounded_rectangle([bb0, bby0, bb1, bby1], radius=12, fill=(5, 12, 28, 225), outline=(6, 182, 212, 180), width=1)
    draw.text((bb0+30, bby0+16), "SEASONED PRIMARY REVOLVING TRADELINES • CORPORATE NET-30 INTEGRATION", font=font_mono_bold, fill=(241, 245, 249, 255))

    final = Image.alpha_composite(base, overlay).convert("RGB")
    final.save("images/home2-tradeline-builder-vault.webp", "WEBP", quality=95)
    print("Generated home2-tradeline-builder-vault.webp")

# =========================================================================
# IMAGE 4: home2-bureau-defense-syndicate.webp
# Federal FCRA Statutory Legal Defense Syndicate
# =========================================================================
def build_image_4():
    base = Image.open("images/services-dispute-engine.jpg").convert("RGBA")
    w, h = base.size # 1376, 768
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top Banner
    x0, y0 = 40, 40
    draw.rounded_rectangle([x0, y0, x0+620, y0+95], radius=14, fill=(4, 14, 28, 225), outline=(16, 185, 129, 210), width=2)
    draw.text((x0+20, y0+16), "FEDERAL FCRA STATUTORY DEFENSE SYNDICATE", font=font_title, fill=(52, 211, 153, 255))
    draw.text((x0+20, y0+56), "15 U.S.C. § 1681i STRICT LIABILITY • 30-DAY STATUTORY TIMELINE", font=font_mono_bold, fill=(56, 189, 248, 255))

    # Right badge
    rx0, ry0 = w - 420, 40
    draw.rounded_rectangle([rx0, ry0, rx0+380, ry0+95], radius=14, fill=(4, 14, 28, 225), outline=(245, 158, 11, 200), width=2)
    draw.text((rx0+20, ry0+16), "FORMAL EXPUNGEMENT ORDERS", font=font_subtitle, fill=(251, 191, 36, 255))
    draw.text((rx0+20, ry0+56), "MANDATORY REMOVAL OF UNVERIFIED DEROGATORY MARKS", font=font_mono, fill=(203, 213, 225, 255))

    final = Image.alpha_composite(base, overlay).convert("RGB")
    final.save("images/home2-bureau-defense-syndicate.webp", "WEBP", quality=95)
    print("Generated home2-bureau-defense-syndicate.webp")

# =========================================================================
# IMAGE 5: home2-underwriting-approval-radar.webp
# Institutional Underwriting & Capital Approval Simulator
# =========================================================================
def build_image_5():
    base = Image.open("images/home-credit-success-stories.webp").convert("RGBA")
    w, h = base.size # 1376, 768
    
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Top Banner
    bx0, by0, bx1, by1 = (w - 780)//2, 35, (w + 780)//2, 125
    draw.rounded_rectangle([bx0, by0, bx1, by1], radius=16, fill=(4, 12, 28, 225), outline=(6, 182, 212, 210), width=2)
    draw.text((bx0+30, by0+16), "INSTITUTIONAL UNDERWRITING & CAPITAL APPROVAL", font=font_title, fill=(56, 189, 248, 255))
    draw.text((bx0+30, by0+56), "850 FICO® PRIME • JUMBO MORTGAGES • $1.75M COMMERCIAL CREDIT FACILITIES", font=font_mono_bold, fill=(52, 211, 153, 255))

    final = Image.alpha_composite(base, overlay).convert("RGB")
    final.save("images/home2-underwriting-approval-radar.webp", "WEBP", quality=95)
    print("Generated home2-underwriting-approval-radar.webp")

build_image_1()
build_image_2()
build_image_3()
build_image_4()
build_image_5()
print("All 5 images successfully generated and saved to images/")
