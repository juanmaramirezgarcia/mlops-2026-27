"""
render_assets.py  -  turns console_output.txt and alert_message.md into the two PNGs used on the Video 1
slides (console_output.png, alert_message.png). Cosmetic only; run after run_alert_checks.py.
"""
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ------------------------------------------------------------------ 1. the console
lines = (HERE / "console_output.txt").read_text().rstrip("\n").split("\n")
f = ImageFont.truetype(MONO, 22)
W = 1900; lh = 32
img = Image.new("RGB", (W, lh * len(lines) + 50), "#1B2A4A")
d = ImageDraw.Draw(img)
for i, ln in enumerate(lines):
    col = "#E6ECF5"
    if ln.strip().startswith("PASS"): col = "#7FD1C8"
    if ln.strip().startswith("FIRE"): col = "#F4A26B"
    if "[incident]" in ln: col = "#FF8A7A"
    d.text((28, 22 + i * lh), ln, font=f, fill=col)
img.save(HERE / "console_output.png")

# ------------------------------------------------------------------ 2. the Slack-style card
import textwrap
raw = (HERE / "alert_message.md").read_text().rstrip("\n").split("\n")
md = []
for ln in raw:   # wrap the headline lines so nothing runs off the card
    if ln.startswith((":warning:", ":rotating_light:")):
        icon, rest = ln.split(" ", 1)
        parts = textwrap.wrap(rest, 66 if icon == ":rotating_light:" else 76)
        md.append(f"{icon} {parts[0]}"); md += ["      " + p for p in parts[1:]]
    else:
        md.append(ln)
fb = ImageFont.truetype(SANS_B, 24); fr = ImageFont.truetype(SANS, 22); fs = ImageFont.truetype(SANS, 19)
W = 1200
img = Image.new("RGB", (W, 60 + 34 * len(md) + 40), "white")
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 56], fill="#4A154B"); d.text((24, 14), "#churn-model-alerts", font=fb, fill="white")
d.rectangle([20, 72, 26, img.height - 20], fill="#E07A2F")
d.text((44, 74), "monitoring-bot  APP  11:46", font=fs, fill="#616061")
y = 108
for ln in md:
    txt = ln.replace("*", "")
    if ln.startswith(":warning:"):
        txt = txt.replace(":warning:", "").strip(); d.text((44, y), "⚠", font=fb, fill="#E07A2F"); d.text((76, y), txt, font=fb, fill="#1D1C1D")
    elif ln.startswith(":rotating_light:"):
        txt = txt.replace(":rotating_light:", "").strip()
        d.rounded_rectangle([44, y + 2, 156, y + 30], radius=6, fill="#B42318"); d.text((52, y + 4), "INCIDENT", font=fs, fill="white")
        d.text((170, y), txt, font=fb, fill="#1D1C1D")
    elif ln.startswith("      "):   # continuation of a wrapped headline
        d.text((76, y), txt.strip(), font=fb, fill="#1D1C1D")
    elif ln.startswith("    "):
        d.text((76, y), txt.strip(), font=fr, fill="#1D1C1D")
    else:
        d.text((44, y), txt, font=fb if ln.startswith("*") else fr, fill="#1D1C1D")
    y += 34
img.save(HERE / "alert_message.png")
print("console_output.png", "alert_message.png", "written")
