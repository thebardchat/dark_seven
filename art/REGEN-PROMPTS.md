# DARK SEVEN — REGEN PROMPTS (the gibberish pages)
*Re-generate the 13 pages whose captions came back garbled. Every prompt below obeys `DESIGN-LAW.md`, the character bible (`CHARACTER-DESIGN-SHEETS.md`), and the veil.*

---

## THE ONE RULE THAT FIXES GIBBERISH
Image models **cannot spell.** Every garbled page is a page where we asked the model to draw text. So we stop. **Generate the ART with blank caption plates, then letter it yourself afterward.** Every prompt below ends with the NO-TEXT lock:

```
LETTERING LOCK: Render every caption box, title bar, and speech balloon as an
EMPTY blank plate — solid black or solid white, with NO text, letters, words,
numbers, labels, or writing anywhere in the image. No signage text either.
Leave clean empty space for lettering to be added later.
```

**Workflow:** `gemini-gen.py` already auto-appends the strict color code and runs `color-fix.py`, so output is on-law. Generate → letter the empty plates from the matching script section (named per page) → done. Likeness-locked pages MUST pass the reference image as the last arg.

Handy references (pass as the trailing image arg):
- **The man (= Shane):** `shane noir portrait.png` (face), `the-man-bloodyfists-edit.webp` (rage/fists), `cover_plain.png`
- **Tapioca (real face):** `tapioca-real-face-ref.jpg`
- **The back tattoo — NEVER redraw the cross:** attach the cross photo and say "do NOT redraw the cross."

---

## GROUP A — CHARACTER / MODEL SHEETS (the "Artist Bible" pages)

### `26` — Character Model Sheet (the trio)
```
python gemini-gen.py "Comic-book character model sheet, Style C GTA-cel: bold clean black outlines, flat controlled grey fills, high contrast. Three vertical columns of full-body turnarounds against plain grey — LEFT: a broad, heavy, weathered bearded man with grey-streaked hair swept back (the detective), in a rain-worn grey coat; MIDDLE: an older dignified disabled veteran, plain at-home clothes, carrying quiet weight; RIGHT: a lean fit younger man with short dark hair pulled back and a short goatee. Small inset boxes for expression heads and hands. Everything pure black/white/grey. Empty blank label plates under each figure. LETTERING LOCK: every caption box and label is an EMPTY blank plate with NO text, letters, words, or numbers anywhere. No writing at all." out_26.png \"shane noir portrait.png\""
```
*Letter afterward from `CHARACTER-DESIGN-SHEETS.md`. Lock the RIGHT figure's face with a second pass using `tapioca-real-face-ref.jpg`.*

### `35` — The Man (the detective) sheet
```
python gemini-gen.py "Character model sheet, Style C GTA-cel, pure black/white/grey. The same broad heavy weathered bearded man throughout (grey-streaked hair swept back, hard tired eyes). Full-body turnaround front/side/back; the BACK view is critical — show the long box-cutter scar straight down the spine. Three wardrobe states side by side: grey rain-soaked coat, clean white suit over black shirt, and blood-spattered white suit. An expression row: controlled mask, enraged snarl, bleeding resolve on one knee. Oversized scarred bare fists. Blood red appears ONLY on wounds/spatter, nowhere else. Empty blank plates for all labels. LETTERING LOCK: no text, letters, words, or numbers anywhere — every caption box is an empty blank plate." out_35.png \"the-man-bloodyfists-edit.webp\""
```
*The back scar map = the wound map. For the Celtic cross on the back, do a follow-up edit pass attaching the real cross photo with "do NOT redraw the cross."*

### `34` — The Old Soldier / Grandfather sheet
```
python gemini-gen.py "Character model sheet, Style C GTA-cel, pure black/white/grey. An older dignified disabled veteran seated in a worn recliner that knows his shape, mostly swallowed by the dark of a small room. One window beside him with a clean BRIGHT WHITE light beyond it (grace-white, NOT gold, NOT amber, NOT warm) — the window is the only bright thing. Expression heads: watching, weary, letting go. His face is grey; the ONLY red is a faint wash of movie-blood thrown on his face by an off-panel screen. Empty blank label plates. LETTERING LOCK: no text, letters, words, or numbers anywhere; all caption boxes are empty blank plates." out_34.png"
```
*Critical fix vs the old render: the house-light window must be pure WHITE, never amber/gold.*

### `30` & `32` — The Fractured Architect (VEILED — never a face)
```
python gemini-gen.py "Veiled-horror concept page, Style C, pure black/white/grey. NEVER show a face or a body. Depict the predator ONLY as: a single ringless open patient HAND entering from the very edge of the frame (offering, not grabbing), lit by a warm off-panel glow rendered in WHITE/GREY light ONLY (never gold, never amber, never any color). Around it, its 'presence' motifs: a false-moon lightbulb hanging where a moon should be; windows going black one at a time; a grey smothered sky. A torn caption box in one corner with a single red drip (the only red in the frame — it reads as blood). NO figure, NO silhouette of a person, NO face anywhere. Empty blank caption plates. LETTERING LOCK: no text, letters, words, or numbers anywhere; caption boxes are empty blank plates." out_30.png"
```
*This one prompt replaces BOTH `30` and `32` (they were duplicate concepts). Old breaches fixed: rust-brown gate and warm candle glow are gone — off-panel light is strictly white/grey.*

---

## GROUP B — STORY / COMIC PAGES

### `25` — The Wound Map spread (the table of contents)
```
python gemini-gen.py "Full noir comic spread, Style C GTA-cel, pure black/white/grey on a BLACK page (no cream, no parchment, no beige). CENTER: the bare muscular back of a broad bearded man, a long vivid blood-red box-cutter slash running straight down his spine — this scar is the spine of the page. Arranged around the center, six small inset panels, each a single wound-cut moment (arm, spine, shoulder blade, scalp, neck, a buried knife low in the back). Blood red ONLY on the cuts; everything else black/white/grey. Empty blank caption plates beside each inset. LETTERING LOCK: no text, letters, words, or numbers anywhere; every caption box and title bar is an empty blank plate." out_25.png \"the-man-bloodyfists-edit.webp\""
```
*Letter from `VOLUME-THREE-skeleton.md` (the wound map) or `DARK-SEVEN.md` structure block.*

### `5` — The Shield / The Save (Cut 5)
```
python gemini-gen.py "Single dramatic comic panel, Style C, pure black/white/grey. A giant weathered bare forearm and hand (scarred, bleeding vivid red from an old wound) lifting upward like a shield. Above the hand, high and small, the back-turned silhouette of a boy standing in a shaft of pure WHITE light (grace-white). A patient off-panel presence is being pushed back and denied — show it only as receding dark at the edge, NO face, NO body. Blood red only on the forearm wound. Empty blank caption plate. LETTERING LOCK: no text, letters, words, or numbers anywhere; the caption box is an empty blank plate." out_5.png"
```
*Veil: the boy is a back-turned silhouette in white light, never face-front. Letter from the Cut 5 section of `DARK-SEVEN_Cut4-to-Cut5_pencil-ready.md`.*

### `16` — PAGE H storyboard (the save, 3 panels)
```
python gemini-gen.py "A 3-panel vertical comic page, Style C GTA-cel, thin black gutters, pure black/white/grey. Panel 1: close on a victim with a razor blade held to his bared throat, a thin vivid red line beginning. Panel 2: a man airborne, flying over the hood of a sedan, arms out, torn open and pouring blood, to strike the attacker — the impossible save. Panel 3: the same beat canted 90 degrees, chaotic. Blood red ONLY on wounds. Empty blank caption boxes in each panel. LETTERING LOCK: no text, letters, words, numbers, or reference tags anywhere; every caption box is an empty blank plate." out_16.png \"tapioca-real-face-ref.jpg\""
```
*The airborne man is Tapioca — pass his real-face ref. Letter from the Cut 5 / Floor save beats.*

### `17` — PAGE F, inverted (the flip / Cut 4)
```
python gemini-gen.py "A comic page designed to be read UPSIDE DOWN (the book physically inverts here), Style C, pure black/white/grey. A man hanging inverted with a slit throat bleeding vivid red upward; behind him an inverted gothic cathedral interior; small under-the-car POV insets; a single falling blood drop. The whole composition rotated 180 degrees. Blood red only on the throat wound and drop. Empty blank caption plates (they will be lettered upside down later). LETTERING LOCK: no text, letters, words, or numbers anywhere; caption boxes are empty blank plates." out_17.png"
```

### `19` — Inverted fall toward the cathedral (Cut 4)
```
python gemini-gen.py "A dramatic inverted comic panel, Style C, pure black/white/grey (NO gold, NO amber, NO warm light anywhere — this is the fix). A man falling head-first toward the spire of a vast gothic cathedral seen from above; at the peak, tiny and back-turned, a boy stands in a shaft of pure WHITE light. Everything monochrome; no blood needed. Empty blank caption plates. LETTERING LOCK: no text, letters, words, or numbers anywhere; caption boxes are empty blank plates." out_19.png"
```
*Veil: boy is a tiny back-turned silhouette. Fix vs old render: kill all amber/gold — cathedral in grey, light strictly white.*

### `20` — PAGE C-4, the scalp (mirrored)
```
python gemini-gen.py "A comic page, Style C GTA-cel, pure black/white/grey. A bloodied man's head wrenched violently back by a fistful of hair, a razor opening his scalp crown-to-nape with vivid red. The composition mirrored/doubled as a disorienting inverted reflection. Blood red only on the scalp/head wounds. Empty blank caption boxes. LETTERING LOCK: no text, letters, words, or numbers anywhere; every caption box is an empty blank plate." out_20.png \"the-man-bloodyfists-edit.webp\""
```

### `21` — PAGE C-2, the scalp (4 panels)
```
python gemini-gen.py "A 4-panel comic page, Style C GTA-cel, thin black gutters, pure black/white/grey. Panel 1: a hand gripping a man's hair from behind. Panel 2: a razor drawn across the scalp, vivid red opening. Panel 3: the throat split, blood spray. Panel 4: the man's shocked, enraged face. Blood red ONLY on the wounds. Empty blank caption boxes and SFX plates. LETTERING LOCK: no text, letters, words, numbers, or SFX lettering anywhere; every box is an empty blank plate." out_21.png \"the-man-bloodyfists-edit.webp\""
```

### `23` — The 9-panel Style-C spread (overview)
```
python gemini-gen.py "A 9-panel comic grid (3x3), Style C GTA-cel, thin black gutters, pure black/white/grey (NO amber, NO gold anywhere — the fix). The beats in order: a descent into dark; a choking veil; a patient off-panel HAND holding a tire iron at the frame edge (NO face, NO body); the turn — a man rising; a shield-up stance, bleeding; a boy as a tiny back-turned silhouette dwarfed by a cathedral; a blown-white '96 highway origin. Blood red ONLY on wounds. Empty blank caption boxes throughout. LETTERING LOCK: no text, letters, words, numbers, or SFX anywhere; every caption box is an empty blank plate." out_23.png \"the-man-bloodyfists-edit.webp\""
```
*Veil holds twice here: the phantom is hand-only; Keystone is a back-turned silhouette. Fix vs old: no warm glow behind the hand.*

---

## AFTER YOU GENERATE
1. Eyeball each for stray gibberish (there should be none — plates are blank) and for any warm-color leak the auto color-fix missed.
2. Letter the empty plates from the matching script file (named per page above).
3. Drop the finals into `art/`; keep these `out_*.png` names or rename to the page's canonical name.
4. Re-run the color check if you want: `python batch-color-fix.py art` (backs up any violators first).

*Blood is the only color. The veil is law. The likeness is Shane. The Devil does not win.*
