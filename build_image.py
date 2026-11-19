#!/usr/bin/env python3
"""Build entry.png: a newspaper front page summing up 19 Nov 2026 world news.

Drawn programmatically with PIL (no photos, no AI generation, no network):
crisp vector text and shapes only, so nothing is garbled at any size.
Run:  python3 build_image.py   (writes entry.png next to this script)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "/usr/share/fonts/truetype/noto"

SERIF_BLACK = os.path.join(FONT_DIR, "NotoSerif-Black.ttf")
SERIF_BOLD = os.path.join(FONT_DIR, "NotoSerif-Bold.ttf")
SANS_BLACK = os.path.join(FONT_DIR, "NotoSans-Black.ttf")
SANS_BOLD = os.path.join(FONT_DIR, "NotoSans-Bold.ttf")
SANS = os.path.join(FONT_DIR, "NotoSans-Regular.ttf")

W, H = 1024, 1024
PAPER = (251, 249, 244)      # warm off-white
INK = (20, 20, 20)          # near-black
GREY = (90, 90, 86)
RULE = (20, 20, 20)
LIGHT_RULE = (180, 175, 165)
RED = (179, 38, 30)
BLUE = (26, 79, 138)
TEAL = (14, 107, 92)
PURPLE = (91, 45, 142)
AMBER = (178, 106, 0)
GREEN = (46, 107, 46)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    """Draw wrapped paragraph; returns y just below the last line."""
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def hrule(draw, x0, x1, y, width=2, color=RULE):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def burst(draw, cx, cy, r, color):
    """Simple 8-point starburst (drawn shape, lead-story icon)."""
    import math
    outer, inner = [], []
    for i in range(16):
        ang = math.pi * i / 8 - math.pi / 2
        rad = r if i % 2 == 0 else r * 0.45
        outer.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    draw.polygon(outer, fill=color)


def circles3(draw, x, y, r, colors):
    for i, c in enumerate(colors):
        draw.ellipse([x + i * (2 * r + 6), y, x + i * (2 * r + 6) + 2 * r,
                      y + 2 * r], fill=c, outline=INK, width=2)


def chip(draw, x, y, s, color):
    """Compact chip: rounded square with an inner die, no pins (pins would
    reach into the headline below)."""
    draw.rounded_rectangle([x, y, x + s, y + s], radius=6, fill=color,
                           outline=INK, width=2)
    inner = s // 3
    draw.rectangle([x + inner, y + inner, x + s - inner, y + s - inner],
                   outline=(255, 255, 255), width=2)


def bridge(draw, x, y, w, h, color):
    draw.arc([x, y, x + w, y + 2 * h], start=180, end=360, fill=color, width=6)
    draw.line([(x, y + h), (x + w, y + h)], fill=color, width=4)
    for i in range(1, 5):
        bx = x + w * i // 5
        draw.line([(bx, y + h - 6), (bx, y + h - 26)], fill=color, width=4)


def chart_up(draw, x, y, w, h, color):
    pts = [(x, y + h), (x + w * 0.3, y + h * 0.65),
           (x + w * 0.55, y + h * 0.75), (x + w * 0.8, y + h * 0.3),
           (x + w, y + h * 0.08)]
    draw.line(pts, fill=color, width=6, joint="curve")
    draw.polygon([(x + w - 12, y + h * 0.08), (x + w + 2, y + h * 0.08),
                  (x + w, y + h * 0.08 - 10)], fill=color)


def skyline(draw, x, y, w, h, color):
    bars = [(0, 0.55), (0.18, 0.30), (0.38, 0.62), (0.56, 0.22),
            (0.74, 0.48), (0.88, 0.35)]
    bw = w / len(bars)
    for i, (fx, fh) in enumerate(bars):
        bx = x + i * bw + 2
        draw.rectangle([bx, y + h * fh, bx + bw - 4, y + h], fill=color)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 44  # margin
    X0, X1 = M, W - M

    # ---- Masthead ----
    f_mast = font(SERIF_BLACK, 62)
    d.text((W // 2, 34), "THE WORLD IN ONE DAY", font=f_mast, fill=INK,
           anchor="ma")
    hrule(d, X0, X1, 118, width=3)
    f_date = font(SANS_BOLD, 30)
    d.text((W // 2, 130), "Thursday, 19 November 2026", font=f_date,
           fill=INK, anchor="ma")
    hrule(d, X0, X1, 176, width=1, color=LIGHT_RULE)

    # ---- Lead story: US-Iran ----
    y = 196
    f_kick = font(SANS_BLACK, 22)
    d.text((X0, y), "MIDDLE EAST  •  CONFLICT", font=f_kick, fill=RED)
    burst(d, X1 - 34, y + 26, 30, RED)
    y += 36
    f_lead = font(SERIF_BLACK, 47)
    y = para(d, X0, y, "U.S.–Iran Strikes Widen Across the Gulf",
             f_lead, X1 - X0 - 90, 54)
    y += 8
    f_sum = font(SANS, 24)
    y = para(d, X0, y,
             "Washington hit a missile site on Iran's Qeshm Island; Tehran "
             "struck a U.S. base in Kuwait and hit Bahrain again as the "
             "fighting spreads across Gulf states.",
             f_sum, X1 - X0, 32)
    y += 14
    hrule(d, X0, X1, y, width=2)

    # ---- Grid: 4 stories, 2 x 2 ----
    stories = [
        ("DIPLOMACY  •  ASIA", BLUE,
         "Trump, Xi and Putin to Meet in Shenzhen",
         "The three leaders hold trilateral talks on the sidelines of the "
         "APEC summit.",
         lambda x, yy: circles3(d, x, yy + 2, 11, [RED, (255, 210, 63), BLUE])),
        ("TECHNOLOGY", TEAL,
         "Nvidia Halts H-Chips to China",
         "Acting chief Colette Kress says no more Hopper chips for the "
         "mainland — and pledges earlier pay rises.",
         lambda x, yy: chip(d, x + 4, yy + 2, 26, TEAL)),
        ("EUROPE  •  WAR", PURPLE,
         "Crimean Bridge Struck a Third Time",
         "The crossing is hit again in a week; traffic halts while damage "
         "is assessed.",
         lambda x, yy: bridge(d, x, yy + 6, 62, 26, PURPLE)),
        ("ECONOMY  •  U.S.", AMBER,
         "Fed Signals More Rate Hikes Ahead",
         "Minutes show nearly all officials expect further rises if "
         "inflation stays hot.",
         lambda x, yy: chart_up(d, x, yy + 10, 56, 20, AMBER)),
    ]
    gy = y + 18
    col_w = (X1 - X0 - 28) // 2
    row_h = 196
    for i, (kicker, color, head, summ, icon) in enumerate(stories):
        cx = X0 + (i % 2) * (col_w + 28)
        cy = gy + (i // 2) * (row_h + 14)
        d.text((cx, cy), kicker, font=font(SANS_BLACK, 20), fill=color)
        icon(cx + col_w - 70, cy - 4)
        yy = cy + 32
        f_h = font(SERIF_BOLD, 29)
        yy = para(d, cx, yy, head, f_h, col_w, 35)
        yy += 4
        yy = para(d, cx, yy, summ, font(SANS, 22), col_w, 29, color=(60, 60, 58))
        if i % 2 == 0:
            d.line([(cx + col_w + 14, cy), (cx + col_w + 14, cy + row_h - 8)],
                   fill=LIGHT_RULE, width=1)
    gy2 = gy + 2 * row_h + 14
    hrule(d, X0, X1, gy2, width=2)

    # ---- Bottom story: GTA VI ----
    y = gy2 + 16
    d.text((X0, y), "CULTURE  •  GAMES", font=font(SANS_BLACK, 20), fill=GREEN)
    skyline(d, X1 - 84, y - 2, 80, 44, GREEN)
    y += 32
    f_h = font(SERIF_BOLD, 30)
    d.text((X0, y), "GTA VI Begins Its Global Rollout", font=f_h, fill=INK)
    y += 40
    y = para(d, X0, y,
             "Grand Theft Auto VI launches worldwide as players enter Vice "
             "City.",
             font(SANS, 22), X1 - X0, 29, color=(60, 60, 58))
    hrule(d, X0, X1, y + 12, width=1, color=LIGHT_RULE)

    # ---- Footer ----
    f_foot = font(SANS, 18)
    d.text((W // 2, H - 44),
           "Six stories from 19 November 2026  •  As reported by wire services",
           font=f_foot, fill=GREY, anchor="ma")

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    size = os.path.getsize(out)
    print(f"wrote {out}: {img.size[0]}x{img.size[1]}, {size} bytes")


if __name__ == "__main__":
    main()
