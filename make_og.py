#!/usr/bin/env python3
"""og.png 1200x630 — The Pike — coal & marble bar-room poster.
Charcoal ground, marble-white type band, ember slash, gold rules. Shop identity only."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "public", "og.png")

COAL = (21, 22, 26); COAL2 = (34, 36, 43); MARBLE = (245, 243, 238)
EMBER = (224, 122, 85); GOLD = (201, 162, 75); MIST = (154, 157, 166)

def font(paths, size):
    bases = ["/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/"]
    for b in bases:
        for n in paths:
            p = b + n
            if os.path.exists(p):
                try: return ImageFont.truetype(p, size)
                except Exception: pass
    return ImageFont.load_default()

sans_big = lambda s: font(["Impact.ttf", "HelveticaBold.ttf", "Arial Bold.ttf", "Helvetica.ttc"], s)
sans = lambda s: font(["HelveticaNeue.ttc", "Futura.ttc", "Arial.ttf"], s)

img = Image.new("RGB", (W, H), COAL)
d = ImageDraw.Draw(img)

# lower third band slightly lighter (the marble bar top horizon)
d.rectangle([0, 486, W, H], fill=COAL2)
# gold rules top and bottom
d.rectangle([0, 0, W, 5], fill=GOLD)
d.rectangle([0, H - 5, W, H], fill=GOLD)
# ember diagonal accent — a single slash at left like a plate rim
d.polygon([(74, 130), (120, 130), (98, 430), (52, 430)], fill=EMBER)

def center(text, f, y, fill, tracking=0):
    if tracking:
        widths = [d.textbbox((0, 0), ch, font=f)[2] - d.textbbox((0, 0), ch, font=f)[0] for ch in text]
        tw = sum(widths) + tracking * (len(text) - 1)
        x = (W - tw) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=f, fill=fill)
            x += w + tracking
    else:
        w = d.textlength(text, font=f)
        d.text(((W - w) / 2, y), text, font=f, fill=fill)

# kicker
center("NOW OPENING  ·  CLINTON, CONNECTICUT", sans(26), 84, GOLD, tracking=6)
# big brand — impact condensed uppercase
center("THE PIKE", sans_big(178), 150, MARBLE, tracking=14)
# ember underline
d.rectangle([W/2 - 210, 362, W/2 + 210, 369], fill=EMBER)
# menu line
center("NEW HAVEN-STYLE & GRANDMA-STYLE PIZZA  ·  SMASHBURGERS", sans(31), 396, MARBLE, tracking=3)
center("FRIED CHICKEN  ·  CRAFT COCKTAILS  ·  PITCHERS  ·  POOL TABLE", sans(26), 444, MIST, tracking=3)
# bottom band line
center("OPEN UNTIL 1 A.M.  FRI  ·  SAT  ·  SUN", sans(28), 512, GOLD, tracking=5)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
