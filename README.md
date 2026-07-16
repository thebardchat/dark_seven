<div align="center">

# DARK SEVEN
## Installment I — DARK CORRIDORS

### *You Probably Think This Book Is About You* · Volume Three · The Culmination
**A dark noir blood comic. Black and white, and the only color is blood.**

[![Live Site](https://img.shields.io/badge/LIVE-thebardchat.github.io/dark__seven-c8161d?style=for-the-badge)](https://thebardchat.github.io/dark_seven/)
[![Book One](https://img.shields.io/badge/BOOK%20ONE-Amazon-ff9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD)
[![Built With](https://img.shields.io/badge/Co--built%20with-Claude-orange?style=for-the-badge)](https://claude.ai/code)

*It was always about you. It was never only about you.*
**The Devil does not win.**

</div>

---

## The series

**DARK SEVEN is a seven-title series** — seven descents into a different corridor of the same mind. This is **Installment I: DARK CORRIDORS.** The color law, the veil, and the cross carry across all seven; the corridor changes. The other six are coming.

## The trilogy — one record, three sides

| Vol. | Title | Form | Where |
|------|-------|------|-------|
| **I** | *…This Book Is About You* | Noir vignette book — the movie | [Amazon](https://www.amazon.com/Probably-Think-This-Book-About/dp/B0GT25R5FD) |
| **II** | *…This Song Is About You Too* | Noir song cycle — the album | [Amazon](https://a.co/d/0fZzwiAd) · [Site](https://thebardchat.github.io/you-probably-think-this-song-is-about-you-too/) |
| **III** | **DARK SEVEN: DARK CORRIDORS** | Noir blood comic — the culmination *(you are here)* | [Site](https://thebardchat.github.io/dark_seven/) |

---

## What this is

Volume Three of Shane Brazelton's *You Probably Think This Book Is About You*. Where the movie and the album become a **comic** — a dark noir blood comic.

Volume One watched the world. Volume Two listened to it. Volume Three **bleeds.** Six cuts on a nameless detective, each deeper than the last, each one a door into an older wound — all of them hung off the one scar down his spine, which is the binding of the book itself. Two things happen at once, neither named on the surface: a case that's really about the thing that came for his son, and a highway thirty years gone that never stopped bleeding.

**🌐 Read the site:** **https://thebardchat.github.io/dark_seven/**

## The three inviolable rules

1. **Three inks, no fourth.** BLACK is the world and the dark. RED is blood — *and nothing else is ever red* ("if it's red, it's bleeding"). WHITE is grace — the shield, the Light, rescue — reserved and rare. The one sanctioned exception is the red neon Celtic cross.
2. **The veil is law.** Keystone (the boy) is never named, never shown face-front, his ordeal never depicted — only felt in symbol. The Fractured Architect (the phantom) is only ever a hand and a warm light. It protects a real child and honors a real friend.
3. **The cross is never redrawn.** It's Shane's actual back tattoo, worn over the '96 spine scar — grace laid over the wound.

Full spec: [`DESIGN-LAW.md`](DESIGN-LAW.md) — the visual constitution, eight articles.

## The structure — the wound map

The box-cutter scar down the detective's spine **is** the physical binding of the book. Six present-day cuts drop the reader through three braided timelines — **NOW** (the case), **THE BOY** (Keystone, veiled), and **'96** (the highway origin).

```
THE FIRST WITNESS — the old soldier watches it first (frame)
CUT 1 — The Arm              first blood; teaches the reader to brace
CUT 2 — Down the Spine       the binding; the veil goes up
CUT 3 — The Shoulder Blade   the warm cut; deeper into the boy
CUT 4 — The Scalp            the deepest dive; THE FLIP (book prints inverted)
CUT 5 — The Neck / Shield    the save; the turn; WHITE enters
CUT 6 — The Knife That Stays the reveal; the floor drops all the way
THE FLOOR — '96, the origin, told straight (blown white, blood only)
THE LAST WITNESS — the old soldier lets it go (closing bookend)
```

## Repo layout

| Path | What it is |
|------|-----------|
| [`DARK-SEVEN.md`](DARK-SEVEN.md) | The comic bible — premise, sacred rules, characters, structure, status |
| [`DESIGN-LAW.md`](DESIGN-LAW.md) | The visual constitution (the color/veil/cross law) — one source of truth |
| [`VOLUME-THREE-skeleton.md`](VOLUME-THREE-skeleton.md) | Build doc — the spine, the engine, the wound map |
| `CUT-0X-*.md`, `96-ORIGIN-*`, `THE-FLOOR-*` | The wound-map sections |
| `*_pencil-ready.md` | Pencil-ready comic scripts an artist can draw straight from |
| `DARK-SEVEN_comic-adaptation.md` | Assembled adaptation |
| `index.html` | The live site (hero teaser video, wound map, cast, closing) |
| `art/` | Pages, character sheets, cover, title cards, and the image pipeline |
| `art/CHARACTER-DESIGN-SHEETS.md` | Artist reference bible — lock these, draw to them |
| `art/REGEN-PROMPTS.md` | Ready-to-run prompts that regenerate pages on-law, gibberish-free |
| `*.html` teasers | Motion teasers (the Celtic-cross loop) |
| `CLAUDE.md` | Guidance for AI sessions working in this repo |

## The art pipeline

The visual law is enforced two ways — prompt-side (name the wrong colors to ban them) and post-process (force the code mechanically). Scripts run from `art/` (Python + `numpy`, `Pillow`, `scipy`):

```bash
# Generate a canon image via Gemini (auto-applies the strict color code + color-fix)
python gemini-gen.py "PROMPT" out.png [ref.png ...]

# Force any image to the color code (grayscale + blood-red only; strips red eyes)
python color-fix.py <in> <out>

# Batch-scan a folder: back up violators, overwrite with compliant versions
python batch-color-fix.py "<folder>"

# Stylize a photo into a noir comic character (A=Ink Noir, B=Rotoscope, C=GTA Cel)
python noir-comic-tool.py <in> <A|B|C> <out>
```

**The one rule that fixes gibberish:** image models can't spell — so pages are generated with **blank caption plates** and lettered afterward from the script. See [`art/REGEN-PROMPTS.md`](art/REGEN-PROMPTS.md).

## Credit

Written by **Shane Brazelton**. Co-built with **Claude** (Anthropic).
The one that fuses everything. Black and white and red all over.

<div align="center">

*Faith · Family · Sobriety · Local AI · The Left-Behind User*
**The blood covers the cross. The blood drains. The cross comes back. The Devil does not win.**

</div>
