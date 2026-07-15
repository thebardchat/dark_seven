#!/usr/bin/env python3
r"""
DARK SEVEN — reliable Gemini image generator (uses YOUR paid API, no free servers).
Auto-applies the strict color code + color-fix so every output is canon.

USAGE:
  python gemini-gen.py "PROMPT" out.png                 # text -> image
  python gemini-gen.py "EDIT INSTRUCTION" out.png ref.png [ref2.png ...]   # edit/likeness-lock from reference(s)

Key is read from env GEMINI_API_KEY or file C:\Users\Hubby\.gemini-key (never printed).
Model: gemini-3-pro-image (Google's top tier — best likeness preservation across
new poses; falls back to 2.5-flash-image). Confirmed 2026-07-12 to nail Shane's likeness.
Every result is run through color-fix (grayscale + blood-red only, gloves/costume/eyes stripped).
"""
import os, sys
from pathlib import Path
from io import BytesIO

STRICT = (
    " STRICT COLOR CODE: the entire image is pure black, white, and grey ONLY, "
    "except vivid crimson BLOOD RED which appears ONLY on actual blood. No red "
    "objects, no red clothing, no red eyes, no gold, amber, cream, blue, teal, or "
    "any other color anywhere. If it is red, it is bleeding. Bold clean black "
    "outlines, flat cel-shaded high-contrast graphic-novel comic style. No text."
)

def load_key():
    for v in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY"):
        if os.environ.get(v):
            return os.environ[v]
    kf = Path(r"C:\Users\Hubby\.gemini-key")
    if kf.exists() and kf.read_text(encoding="utf-8").strip():
        return kf.read_text(encoding="utf-8").strip()
    print("NO KEY. Run gemini-check.py for setup instructions."); sys.exit(2)

def color_fix(inp):
    """grayscale + keep red only on small blood regions (strip gloves/capes/eyes)."""
    try:
        import numpy as np
        from PIL import Image
        from scipy import ndimage
    except Exception:
        print("(color-fix skipped: numpy/scipy/PIL missing)"); return
    im = Image.open(inp).convert("RGB"); a = __import__("numpy").asarray(im).astype("float32")
    import numpy as np
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    lum = 0.299*R + 0.587*G + 0.114*B
    red = (R > G*1.4) & (R > B*1.4) & ((R-G) > 40) & ((R-B) > 40) & (R > 70)
    lbl, n = ndimage.label(red)
    if n:
        sizes = ndimage.sum(np.ones_like(lbl), lbl, range(1, n+1))
        keep = np.zeros_like(red)
        for i, s in enumerate(sizes, start=1):
            if s < 1400:
                keep |= (lbl == i)
    else:
        keep = red
    # kill red in the top face band (eyes)
    fg = np.where((lum < 235).any(axis=1))[0]
    if len(fg):
        keep[:int(fg[0] + (fg[-1]-fg[0])*0.20), :] = False
    g = np.clip(lum, 0, 255); out = np.stack([g]*3, axis=-1); sh = np.clip(g/255., .25, 1.)
    out[keep, 0] = np.clip(70+sh[keep]*150, 0, 255)
    out[keep, 1] = np.clip(sh[keep]*32, 0, 255)
    out[keep, 2] = np.clip(sh[keep]*32, 0, 255)
    Image.fromarray(out.astype("uint8")).save(inp)
    print(f"color-fixed (blood px kept: {int(keep.sum())})")

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    prompt, out = sys.argv[1], sys.argv[2]
    refs = sys.argv[3:]
    from google import genai
    from PIL import Image
    client = genai.Client(api_key=load_key())
    contents = [prompt + STRICT]
    for r in refs:
        contents.append(Image.open(r))
    resp = None
    for _model in ("gemini-3-pro-image", "gemini-2.5-flash-image"):
        try:
            resp = client.models.generate_content(model=_model, contents=contents)
            if any(getattr(pt, "inline_data", None) and pt.inline_data.data
                   for pt in resp.candidates[0].content.parts):
                break
        except Exception:
            resp = None
    if resp is None:
        print("all models failed"); sys.exit(1)
    saved = False
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            Image.open(BytesIO(part.inline_data.data)).save(out)
            saved = True
            break
    if not saved:
        # surface any text (e.g. refusal/explanation)
        txt = "".join(getattr(p, "text", "") or "" for p in resp.candidates[0].content.parts)
        print("NO IMAGE RETURNED.", txt[:400]); sys.exit(1)
    print("saved ->", out)
    color_fix(out)

if __name__ == "__main__":
    main()
