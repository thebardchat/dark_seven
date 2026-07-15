#!/usr/bin/env python3
"""
DARK SEVEN — Gemini API LIVE CHECKER.
Confirms your paid Gemini API key works and lists the image models available.
FREE to run (just lists models; generates nothing). Reads the key from, in order:
  1. env var  GEMINI_API_KEY  (or GOOGLE_API_KEY)
  2. file      C:\\Users\\Hubby\\.gemini-key   (one line: the key)
The key is NEVER printed.
"""
import os, sys
from pathlib import Path

def load_key():
    for v in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY"):
        if os.environ.get(v):
            return os.environ[v], f"env:{v}"
    kf = Path(r"C:\Users\Hubby\.gemini-key")
    if kf.exists():
        k = kf.read_text(encoding="utf-8").strip()
        if k:
            return k, "file:~/.gemini-key"
    return None, None

def main():
    key, src = load_key()
    if not key:
        print("NO KEY FOUND.")
        print("Set it one of two ways (the key is never shown to Claude):")
        print("  A) PowerShell:  setx GEMINI_API_KEY \"your-key-here\"   (then reopen shell)")
        print(r"  B) Save the key as one line in:  C:\Users\Hubby\.gemini-key")
        sys.exit(2)
    print(f"key source: {src}  (len {len(key)}, value hidden)")
    try:
        from google import genai
        client = genai.Client(api_key=key)
        models = list(client.models.list())
        img = [m.name for m in models if "image" in m.name.lower() or "imagen" in m.name.lower()]
        print(f"API LIVE [OK]   {len(models)} models reachable.")
        print("Image-capable models:")
        for n in img[:20]:
            print("   -", n)
        if not img:
            print("   (none matched 'image/imagen' — full list still reachable, API is up)")
    except Exception as e:
        print("API ERROR:", type(e).__name__, str(e)[:300])
        sys.exit(1)

if __name__ == "__main__":
    main()
