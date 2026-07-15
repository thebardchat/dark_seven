#!/usr/bin/env python3
"""
DARK SEVEN color-lock fix. Desaturate an image to pure grayscale and re-inject
BLOOD RED only where there is real blood — killing illegal color (blue face,
warm skin, red eyes). Preserves linework/tones; only touches color.
Usage: python color-fix.py <input> <output>
"""
import sys, numpy as np
from PIL import Image

BLOOD = (185, 20, 26)

def run(inp, outp):
    im = Image.open(inp).convert("RGB")
    arr = np.asarray(im).astype(np.float32)
    R, G, B = arr[...,0], arr[...,1], arr[...,2]
    H, W = R.shape

    # blood = strongly red-dominant AND saturated AND not tiny-bright (eyes)
    blood = (R > G*1.45) & (R > B*1.45) & ((R-G) > 45) & ((R-B) > 45) & (R > 80)
    # kill red EYES: suppress blood in the top face band (upper 22% of the figure)
    # find the figure's vertical extent (non-near-white rows)
    lum = 0.299*R + 0.587*G + 0.114*B
    fg_rows = np.where((lum < 235).any(axis=1))[0]
    if len(fg_rows):
        top, bot = fg_rows[0], fg_rows[-1]
        face_cut = int(top + (bot-top)*0.22)
        blood[:face_cut, :] = False  # no red allowed in the head/face band

    # grayscale base (kills blue, warm skin, everything)
    gray = np.clip(lum, 0, 255)
    out = np.stack([gray, gray, gray], axis=-1)

    # re-inject blood, shaped by local darkness so it reads as wet
    shade = np.clip(gray/255.0, 0.25, 1.0)
    out[blood, 0] = np.clip(70 + shade[blood]*150, 0, 255)
    out[blood, 1] = np.clip(shade[blood]*32, 0, 255)
    out[blood, 2] = np.clip(shade[blood]*32, 0, 255)

    Image.fromarray(out.astype(np.uint8)).save(outp)
    print("fixed ->", outp, "| blood px:", int(blood.sum()))

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
