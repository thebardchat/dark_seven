# THE MAN — likeness-locked generation prompt (Gemini pipeline)
*For DARK SEVEN: DARK CORRIDORS. The man IS Shane — keep his likeness exact every time.*

## THE RULE — likeness lock (do this every time)
1. **Attach Shane's own reference photo** (his real face — e.g. IMG_8586, or the noir portrait `shane noir portrait.png`) to the generation. Text-only generation lets the face drift — always attach the reference.
2. In the prompt, say plainly: **"Keep this exact man's face and likeness — same beard, same features. Do NOT change his face."**
3. Three colors only: **black, white, and blood red. Blood is the ONLY color.** Everything else cold monochrome grey — no warm skin, no gold, no other hue.

## GENERATION PROMPT (fists at sides, torn suit, veins)
```
Using the EXACT man in the attached photo — keep his face, beard, and likeness
precisely; do NOT alter his features — render a full-body cinematic black-and-white
film-noir portrait of him standing defiant against a PURE BLACK background.

Cold desaturated grey skin, no warmth anywhere. He wears a badly TORN white suit —
ripped shoulder seam, torn lapel, dangling threads, blood-spattered — over a black
shirt. Both arms hang straight DOWN, fists clenched hard AT HIS SIDES (not raised),
thick forearms and hands corded with heavy bulging veins, knuckles scarred and split
and dripping vivid BLOOD RED.

Blood red is the ONLY color in the frame — everything else is black, white, and grey.
Enraged, confident Scarface expression. Hard rim light, deep chiaroscuro shadows,
film grain, dark vignette. Cinematic graphic-novel key art. Portrait orientation.
```

## COLOR-LOCK CORRECTION (paste if skin goes warm / any non-blood color appears)
```
Keep everything exactly as it is — the pose, the man's face, the torn suit, the
lighting are all perfect. Change ONLY the color. Use strictly three colors and
nothing else: pure black, clean white, and BOLD PURE BLOOD RED (vivid saturated
crimson, never brown or maroon). The skin and suit must be cold monochrome grey/
white — no warm tones, no gold, no other color. Blood is the only color in the frame.
```

## NOTES
- The fast HF model (FLUX-schnell) won't do "arms at sides" or "torn suit" and can't hold a likeness — that's why we use Gemini with the attached reference photo here.
- Ref images already made (text-only, face drifts slightly): `art/the-man-v2.webp`, `art/the-man-poster-v3.webp`, `art/fists-of-rage-v1.webp`.
- Same recipe works for any DARK SEVEN shot of the man — always attach his photo, always keep the three-color law.
