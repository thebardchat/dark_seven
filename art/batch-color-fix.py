#!/usr/bin/env python3
"""
DARK SEVEN — BATCH color-code fixer.
Scans a folder; for each image detects ILLEGAL color (any saturated pixel that
isn't blood-red, plus large red objects like gloves). Files with violations are
backed up to _pre-fix-backup/ then overwritten with a code-compliant version
(pure grayscale + blood-red only, red-eyes/gloves stripped). Already-clean
images are skipped untouched.
Usage: python batch-color-fix.py "<folder>"
"""
import sys, os
from pathlib import Path
import numpy as np
from PIL import Image
from scipy import ndimage

EXT = {".png", ".webp", ".jpg", ".jpeg"}

def analyze_and_fix(path):
    try:
        im = Image.open(path).convert("RGB")
    except Exception as e:
        return ("skip-error", str(e))
    a = np.asarray(im).astype(np.float32)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    mx = np.maximum(np.maximum(R, G), B); mn = np.minimum(np.minimum(R, G), B)
    sat = (mx - mn)                                    # 0..255 chroma
    reddish = (R > G) & (R > B) & ((R - G) > 25) & ((R - B) > 25)
    colored = sat > 28                                 # meaningfully colored pixel
    illegal_color = colored & (~reddish)               # blue/green/gold/warm-skin

    # blood = red regions, but drop LARGE red objects (gloves/capes)
    red = reddish & (sat > 30) & (R > 70)
    lbl, n = ndimage.label(red)
    keep = np.zeros_like(red)
    if n:
        sizes = ndimage.sum(np.ones_like(lbl), lbl, range(1, n + 1))
        for i, s in enumerate(sizes, start=1):
            if s < 1400:
                keep |= (lbl == i)
    big_red = red & (~keep)                             # gloves/capes = illegal

    # illegal in the face band (kill red eyes)
    lum = 0.299*R + 0.587*G + 0.114*B
    fg = np.where((lum < 235).any(axis=1))[0]
    face_red = np.zeros_like(red)
    if len(fg):
        band = int(fg[0] + (fg[-1]-fg[0]) * 0.20)
        face_red[:band, :] = keep[:band, :]

    violation_px = int(illegal_color.sum() + big_red.sum() + face_red.sum())
    total = R.size
    if violation_px < max(400, total * 0.0008):        # essentially clean
        return ("clean", violation_px)

    # ---- FIX: grayscale everything, re-inject only real blood ----
    keep2 = keep.copy()
    keep2[big_red] = False
    if len(fg):
        keep2[:band, :] = False                         # no red in face band
    g = np.clip(lum, 0, 255); out = np.stack([g]*3, axis=-1); sh = np.clip(g/255., .25, 1.)
    out[keep2, 0] = np.clip(70 + sh[keep2]*150, 0, 255)
    out[keep2, 1] = np.clip(sh[keep2]*32, 0, 255)
    out[keep2, 2] = np.clip(sh[keep2]*32, 0, 255)
    return ("fix", Image.fromarray(out.astype(np.uint8)), violation_px)

def main():
    folder = Path(sys.argv[1])
    backup = folder / "_pre-fix-backup"
    fixed = clean = errors = 0
    for p in sorted(folder.iterdir()):
        if p.suffix.lower() not in EXT or p.parent.name == "_pre-fix-backup":
            continue
        res = analyze_and_fix(p)
        if res[0] == "clean":
            clean += 1
            print(f"  CLEAN  {p.name}  ({res[1]}px)")
        elif res[0] == "fix":
            backup.mkdir(exist_ok=True)
            # save original (as png to preserve) then overwrite
            try:
                Image.open(p).save(backup / (p.stem + p.suffix))
            except Exception:
                pass
            res[1].save(p) if p.suffix.lower() != ".webp" else res[1].save(p, "WEBP", quality=90)
            fixed += 1
            print(f"  FIXED  {p.name}  (stripped {res[2]}px illegal color)")
        else:
            errors += 1
            print(f"  ERR    {p.name}  {res[1]}")
    print(f"\n== {folder.name}: fixed {fixed}, already-clean {clean}, errors {errors} ==")

if __name__ == "__main__":
    main()
