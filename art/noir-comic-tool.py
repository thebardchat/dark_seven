#!/usr/bin/env python3
"""
DARK SEVEN noir-comic converter.
Turns any submitted photo into a Noir Dark Comic character, LOCKED to the
color code: black + white + grey, and the ONLY color that survives is BLOOD RED.
Three style presets: A=Ink Noir (Spawn), B=Rotoscope (Scanner Darkly), C=GTA Cel.
Usage: python noir-comic-tool.py <input> <preset A|B|C> <output>
"""
import sys, numpy as np
from PIL import Image, ImageFilter, ImageOps

BLOOD = (200, 18, 26)  # vivid blood red

def load_rgb_on_black(path):
    im = Image.open(path).convert("RGBA")
    bg = Image.new("RGBA", im.size, (0, 0, 0, 255))
    bg.alpha_composite(im)
    return bg.convert("RGB")

def blood_mask(arr):
    # Only TRUE blood: strongly red-dominant AND saturated, so warm skin is excluded.
    R, G, B = arr[..., 0], arr[..., 1], arr[..., 2]
    return (R > G * 1.55) & (R > B * 1.55) & ((R - G) > 55) & ((R - B) > 55) & (R > 90)

def luminance(arr):
    return (0.299*arr[...,0] + 0.587*arr[...,1] + 0.114*arr[...,2])

def posterize(L, levels):
    step = 255.0 / (levels - 1)
    return np.round(L / step) * step

def edge_ink(L_img, thresh):
    e = L_img.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.MaxFilter(3))
    e = np.asarray(e).astype(np.float32)
    return e > thresh  # True where an ink line should be black

def convert(path, preset, out):
    im = load_rgb_on_black(path)
    arr = np.asarray(im).astype(np.float32)
    bmask = blood_mask(arr)
    L = luminance(arr)
    Limg = Image.fromarray(L.astype(np.uint8))

    if preset == "A":       # INK NOIR (Spawn): crushed blacks, blown whites, heavy ink
        L2 = np.clip((L - 90) * 2.4 + 90, 0, 255)
        L2 = posterize(L2, 3)
        edges = edge_ink(Limg, 45)
    elif preset == "B":     # ROTOSCOPE (Scanner Darkly): flat cel bands, thin traced edges
        sm = Limg.filter(ImageFilter.MedianFilter(5))
        L2 = posterize(np.asarray(sm).astype(np.float32), 5)
        edges = edge_ink(sm, 30)
    else:                    # C = GTA CEL: bold outlines, poster tones, lifted blacks
        sm = Limg.filter(ImageFilter.MedianFilter(7))
        L2 = np.clip(posterize(np.asarray(sm).astype(np.float32), 4) + 18, 0, 255)
        edges = edge_ink(sm, 32)

    outarr = np.stack([L2, L2, L2], axis=-1)
    outarr[edges] = (0, 0, 0)  # ink the edges black
    # re-inject BLOOD as the only color, shaped by local luminance
    bl = np.clip(L, 0, 255) / 255.0
    outarr[bmask, 0] = np.clip(90 + bl[bmask]*150, 0, 255)
    outarr[bmask, 1] = np.clip(bl[bmask]*38, 0, 255)
    outarr[bmask, 2] = np.clip(bl[bmask]*38, 0, 255)
    Image.fromarray(outarr.astype(np.uint8)).save(out)
    print("wrote", out, preset)

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2], sys.argv[3])
