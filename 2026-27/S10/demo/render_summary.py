"""render_summary.py - draws eval_summary.png (v1 vs v2 scorecard) from eval_results.csv. Cosmetic; run after s10_demo_setup.py."""
from pathlib import Path
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
r = pd.read_csv(HERE / "eval_results.csv")
def font(bold, size):   # Linux (DejaVu) or Mac (Arial); falls back to Pillow's default
    for path in (["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf", "/Library/Fonts/Arial Bold.ttf"] if bold
                 else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/System/Library/Fonts/Supplemental/Arial.ttf", "/Library/Fonts/Arial.ttf"]):
        if Path(path).exists(): return ImageFont.truetype(path, size)
    return ImageFont.load_default()
fh = font(True, 30); fr = font(False, 26); fb = font(True, 26); fs = font(False, 20)
rows = []
for ver in (1, 2):
    d = r[r.version == ver]
    in_tok = {1: 399, 2: 760}[ver]; out = d.out_tokens.mean()
    rows.append(dict(correct=f"{int(d.correct.sum())} / 12", grounded=f"{int(d.grounded.sum())} / 12", pii=str(int(d.pii.sum())),
                     refusal="no: invented a salary band" if ver == 1 else "yes: refused, referred to HR",
                     tokens=f"{in_tok:.0f} in + {out:.0f} out", cost=f"{1000*(in_tok*2.5e-6+out*10e-6):.2f} EUR",
                     p95=f"{0.6 + d.out_tokens.quantile(0.95)/60:.2f} s"))
labels = [("Correct answers (key facts present)", "correct"), ("Grounded (no invented numbers)", "grounded"), ("PII leaks (employee name repeated)", "pii"),
          ("Out-of-scope question handled", "refusal"), ("Tokens per question (avg)", "tokens"), ("Cost per 1,000 questions", "cost"), ("p95 latency", "p95")]
W, H = 1500, 120 + 70 * len(labels) + 70
img = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 90], fill="#1B2A4A"); d.text((30, 26), "hr-assistant · golden set (12 questions) · judge: rule-based stand-in", font=fh, fill="white")
d.text((560, 110), "v1 · production · baseline", font=fb, fill="#E07A2F"); d.text((1030, 110), "v2 · challenger · grounded", font=fb, fill="#0E7C86")
y = 160
better = {"correct": 2, "grounded": 2, "pii": 2, "refusal": 2, "tokens": 1, "cost": 1, "p95": 2}
for i, (lab, key) in enumerate(labels):
    if i % 2 == 0: d.rectangle([20, y - 12, W - 20, y + 50], fill="#F3F5F8")
    d.text((30, y), lab, font=fr, fill="#1B2A4A")
    for j, x in enumerate((560, 1030)):
        col = "#1B2A4A"
        if better[key] == j + 1: col = "#0E7C86" if j == 1 else "#E07A2F"
        d.text((x, y), rows[j][key], font=fb if better[key] == j + 1 else fr, fill=col)
    y += 70
d.text((30, y + 10), "Bold = the better version on that line. v2 answers better and faster, but each question costs ~40% more: the trade-off to write down.", font=fs, fill="#5B6472")
img.save(HERE / "eval_summary.png"); print("eval_summary.png written")
