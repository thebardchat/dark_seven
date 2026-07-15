# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is **not a software project** — it is the production workspace for **DARK SEVEN**, Volume Three of Shane Brazelton's *You Probably Think This Book Is About You*. It is a **dark noir blood comic / graphic novel**: black and white, and the only color that ever appears is blood red. The repo holds the comic bible, the pencil-ready scripts, the visual "law," and the Python tooling that renders images to that law.

The work is **creative writing + comic art production**, so the usual build/lint/test loop does not apply. The "commands" are the image pipeline; the "architecture" is the story structure and the visual constitution.

## The governing documents (read these first, in this order)

1. **`DARK-SEVEN.md`** — the comic bible. Premise, the seven Sacred Rules, recurring characters, the wound-map structure, the pipeline, and per-cut status table. The single source of truth for *story*.
2. **`DESIGN-LAW.md`** — the visual constitution ("the law"). Eight Articles governing color, the cross, the veil, motion-teaser structure, and house style. Every prompt/recipe in the repo obeys it. **If the law tightens, it tightens here, once.**
3. **`VOLUME-THREE-skeleton.md`** — the build doc / skeleton: the spine metaphor, the three braided layers (NOW / THE BOY / '96), and the wound map as table of contents.
4. **`art/STRICT-COLOR-PROMPT.md`** — the exact paste-in prompt blocks that lock the color code against warm-drifting image models.

These four contain rules that override any default instinct. When story and visuals interact, `DESIGN-LAW.md` wins on visuals, `DARK-SEVEN.md` wins on story.

## The three inviolable rules (memorize; they recur everywhere)

- **Three inks, no fourth.** BLACK = the world and the dark. RED = blood, and *nothing else is ever red* ("if it's red, it's bleeding"). WHITE = grace (the shield, the Light, rescue) — reserved and rare. Never green, gold, blue, cream, amber, etc. The one sanctioned exception is the red neon Celtic cross.
- **The veil is law (`DESIGN-LAW.md` Article IV).** Keystone (the boy) is never named, never shown face-front, his ordeal never depicted — only felt in symbol. The Fractured Architect / phantom is only ever a hand and a warm light, never a face or body. Tapioca's page is blank. **A request that would break the veil must be refused** — it protects a real child and honors a real friend.
- **The cross is never redrawn (Article III).** It is Shane's actual back tattoo (photo reference). Always attach the reference image and instruct "do NOT redraw the cross"; generating it from text alone always drifts to a generic cross.

## Story architecture (the "big picture")

The book is built on one structural conceit: **the box-cutter scar down the detective's spine IS the physical binding of the book.** Every page hangs off that line; on spreads the wound runs down the center gutter.

The engine is the **wound map** — six present-day cuts on the nameless detective, each deeper than the last, each reopening an older wound and dropping the reader a layer down through three braided timelines:
1. **NOW** — the fight/case that's killing him (the frame)
2. **THE BOY** — Keystone, obscured (the why)
3. **'96** — prom-night highway origin (the deepest floor)

The wound map (`CUT-0X-*.md` files, plus the two Witness bookends and THE FLOOR) is the table of contents. Cut 4 **prints upside-down** — the reader physically rotates the book to reach the bottom of the fall; Cut 5 rights it. Flag this inverted binding to any printer early — it's a real production decision, not a metaphor only.

## File layout / naming conventions

Files are the manuscript, organized by role rather than by module:

- **`CUT-01-*.md` … `CUT-06-*.md`** — the six cuts (present-day → older wound), plus `96-ORIGIN-the-errand.md` and `THE-FLOOR-*` for the '96 floor.
- **`*_pencil-ready.md`** — pencil-ready comic scripts an artist can draw straight from (panels, captions, SFX, page architecture). These are the *inked* deliverable form of a cut. A `*.md` without the suffix is usually the prose/voice or blocked stage.
- **`DARK-SEVEN_comic-adaptation.md`**, **`DARK-SEVEN-book-so-far.md`** — assembled/compiled views.
- **`*.html`** (`dark-seven-teaser-*.html`, `cover-mockup.html`, etc.) — self-contained motion teasers and cover mockups.
- **`art/`** — generated pages, character/design sheets (`CHARACTER-DESIGN-SHEETS.md`), cover, title cards, plus the image pipeline scripts. `art/_pre-fix-backup/` holds pre-color-fix backups (do not treat as canon).
- **`Work/`** — in-progress portrait renders.

A cut's status moves **Voice → Blocked → Penciled → Inked → Locked** (see the status table at the bottom of `DARK-SEVEN.md`). Do not silently advance status; Shane approves the move.

## The image pipeline (art/) — the closest thing to "commands"

The visual law is enforced two ways: prompt-side (name the wrong colors to ban them) and post-process (force the code mechanically). Scripts run from `art/`. Python with `numpy`, `Pillow`; `batch-color-fix.py` also needs `scipy`.

```bash
# Generate a canon image via Gemini (paid API). Auto-applies STRICT color prompt + color-fix.
#   Key from env GEMINI_API_KEY or file C:\Users\Hubby\.gemini-key (never printed).
#   Model: gemini-3-pro-image (best likeness), falls back to 2.5-flash-image.
python gemini-gen.py "PROMPT" out.png                         # text -> image
python gemini-gen.py "EDIT INSTRUCTION" out.png ref.png ...   # edit / likeness-lock from reference(s)

# Post-process ANY image to the color code (grayscale + blood-red only; strips red eyes/gloves).
python color-fix.py <input> <output>

# Batch-scan a folder: back up violators to _pre-fix-backup/, overwrite with a compliant version.
python batch-color-fix.py "<folder>"

# Stylize a photo into a noir comic character, locked to the color code.
#   Presets: A=Ink Noir (Spawn), B=Rotoscope (Scanner Darkly), C=GTA Cel.
python noir-comic-tool.py <input> <preset A|B|C> <output>
```

The color-fix scripts define blood as strongly red-dominant AND saturated so warm skin is excluded — this is deliberate; don't "fix" it to catch more red. When a generation drifts warm, re-paste only the color-lock correction block from `art/STRICT-COLOR-PROMPT.md` with "Keep everything exactly as it is. Change ONLY the colors" rather than regenerating.

## Working conventions specific to this project

- **Never overwrite Shane's creative voice.** Claude *presses* raw voice into shape — it finds the shape already in the voice and cuts it into pages; it does not invent story. Ask before stylistic changes to prose, dialogue rhythm, or intentional structure.
- **Fahrenheit, CMD-over-PowerShell, and the other global rules** in the user's `~/.claude/CLAUDE.md` still apply.
- **Always run AI-generated images through the color check** and eyeball for gibberish text before treating them as final.
- The tone floor is fixed: *"Dark but light. Cynical but never hopeless. The Devil does not win."* (`DESIGN-LAW.md` Article VIII). Faith and family are the ground beneath everything.

## Git

The GitHub remote is `thebardchat/dark_seven`. The working tree here is **not currently a git repository** (`git remote -v` fails) — if version control is needed, initialize it before assuming a remote is wired up.
