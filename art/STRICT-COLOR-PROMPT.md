# DARK SEVEN — THE STRICT COLOR PROMPT
*Paste this onto any image generation or edit (Gemini, FLUX, Kontext, etc.) to lock the color code. The rule: black + white + grey, and the ONLY color that ever appears is blood red — and only on actual bloodshed. Nothing else is ever colored.*

---

## FULL STRICT COLOR PROMPT (paste with any image)
```
STRICT COLOR CODE — obey exactly. This image uses ONLY three inks:
pure BLACK, clean WHITE, and their greys — plus ONE single color, BLOOD RED,
and blood red appears ONLY on blood/bloodshed. Nothing else in the entire
frame is ever colored.

- Everything except blood is pure grayscale: black, white, and grey tones only.
- The ONE color is a vivid, saturated CRIMSON blood red (like fresh blood) —
  never brown, maroon, rust, chocolate, orange, or dark dried red.
- Blood red is used ONLY for blood. Never a red object, red light, red cloth,
  red sign, red rose, red skin, or red anything else. If it is red, it is bleeding.
- Absolutely NO other colors anywhere: no gold, amber, yellow, cream, beige,
  sepia, tan, brown, blue, teal, cyan, green, purple, or pink. Skin, suit,
  hair, eyes, background — all rendered in grayscale only.
- High-contrast film-noir: deep black chiaroscuro shadows, blown highlights,
  heavy black spotting. When in doubt, more black.
- If the scene is the 1996 flashback, render it in blinding BLOWN-OUT WHITE
  daylight (overexposed to near-white), NOT gold — blood still the only color.

Three inks, no fourth. Blood is the only color. Break this nowhere.
```

## SHORT APPEND-TAG (when you just need to bolt it on)
```
Black, white, and grey ONLY — the single exception is vivid crimson BLOOD RED,
and only on actual blood. No gold, amber, cream, sepia, brown, blue, or any
other color anywhere. High-contrast noir. If it's red, it's bleeding.
```

## COLOR-LOCK CORRECTION (paste if it drifts warm / adds color)
```
Keep everything exactly as it is — pose, face, composition, lighting are all
correct. Change ONLY the color. Use strictly three: pure black, clean white,
and BOLD PURE BLOOD RED (vivid saturated crimson like fresh blood). Everything
that is NOT blood must be pure grayscale — desaturate all skin, suit, hair,
and background to black/white/grey. The blood must NOT be brown, maroon, rust,
or dried; make it bright glossy crimson. Remove every other color — no gold,
amber, yellow, cream, beige, sepia, blue, teal, or green anywhere in the frame.
```

---

## WHY THESE WORDS (so it lands first try)
- Models default WARM — they sneak in gold/amber glow and brown/maroon "blood." You must **name the wrong colors to ban them** ("not brown, maroon, rust; no gold, cream, amber"). Saying "blood red" alone is not enough.
- "**If it is red, it is bleeding**" stops the model from coloring random objects red — it ties red to blood only.
- "**desaturate all skin/suit/hair/background**" is what forces true grayscale — otherwise faces stay warm.
- For '96: say **blown-out WHITE, not gold** explicitly, or it defaults to golden-hour.
- Pair with the noir-comic tool (`noir-comic-tool.py`) as a post-process to *guarantee* the code even if the model wobbles: it forces everything to grayscale and re-injects red only on true blood.

*Canon color law, DARK SEVEN: DARK CORRIDORS. Black, white, blood red. Nothing else, ever. The Devil does not win.*
