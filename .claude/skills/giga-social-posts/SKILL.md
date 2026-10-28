---
name: giga-social-posts
description: Build on-brand giga! (Singapore mobile) social posts and event promo assets as 3:4 PNGs, using the giga brandbook, Gino the cat, Poppins, pink/teal palette and the house style agreed in the Tech Show 2026 campaign. Use when asked for giga! posts, event/booth promos, offer or price callouts, or "recreate this in giga style".
---

# giga! social posts

Builds 1080 x 1440 (3:4) social posts as HTML, rendered to PNG with Playwright. Everything needed is in this folder:

- `assets/` logo lockups, five Gino poses, Poppins fonts, `common.css`
- `tools/render.js` HTML to PNG; `tools/build_*.py` generators that show how each post was made
- `examples/` the seven finished Tech Show 2026 posts (PNG) plus two HTML sources

Before designing, look at 2 or 3 files in `examples/` so new work matches the established look.

## Brand rules (from the giga! brandbook)

**Colours** (pink and teal always dominate; black and white used sparingly)
- Pink `#ED1285`, teal `#94E0E4`
- Black `#000000`, white `#FFFFFF`
- Accents, used moderately: grey `#D1D3D4`, coral `#FF6F5C` (the book calls it orange). Coral is used for price numbers.

**Type**: Poppins only, for headlines and body. Headlines are usually full uppercase, ExtraBold or Black, with a white outline or a black drop shadow behind in-visual copy.

**Logo**
- Always pink wordmark "giga!" with the exclamation mark. Never recolour, reverse, distort, dot the "i", add shadow, drop the "!" or recreate the outline by hand. Use the supplied files.
- Use the "5G+ feels good" lockup whenever space allows. On pink backgrounds use `assets/logo-lockup-onpink.png`; on teal or white use `assets/logo-lockup.png`.
- Keep clear space of 3x the width of the "!" around it. Minimum width 15 mm / 41 px.

**Gino the cat** (male, use "he")
- Always use the supplied artwork. Do not redraw him: a hand-drawn version was rejected as "doesn't look anything like my Gino". Scale, crop, rotate or flip only.
- Available in `assets/`: `gino-wave`, `gino-cool` (hat and sunglasses), `gino-cart`, `gino-dance`, `gino-phone`, `gino-rocket`. The full pack has 10 poses; ask for the rest if needed.
- Eyes always look sideways, never straight ahead. Never hide his legs behind a UI element (it looks like an unnaturally long leg). Do not cover his face or sunglasses with other shapes.
- He is the character, not the focus of offer posts (see house style).

**Tone**: witty, friendly, upbeat, transparent. Short, punchy copy that lets the offer shine. Write "giga" in lowercase, even at the start of a sentence; "giga!" with the exclamation mark on first public mention (in social captions, plain "giga").

## House style (learned from review feedback)

1. **Pink-led.** Pink is the main background. Teal is the supporting colour and can lead on one or two posts for variety.
2. **Vary the layout.** Do not reuse one skeleton. Each post gets its own composition (tickets, price starburst, photo plus slanted panel, giant type, and so on). Keep the brand system the same: palette, Poppins, headline treatment, Gino poses, logo, booth block.
3. **The offer is the hero**, not Gino. Make the key offer the biggest thing on the post.
4. **Headlines**: uppercase Poppins Black, white fill with a black drop shadow on pink; pink fill with a white outline and black shadow on teal. Keep outlines thin enough that letters do not merge.
5. **Always say what and where.** Event promo posts carry a label such as "TECH SHOW 2026 PROMO", the booth number, dates and venue, and a clear call to action ("COME DOWN TO BOOTH 8428").
6. **Keep it clean.** No sunburst backgrounds, tiled-number patterns, stock bars or extra badges. One strong visual idea per post.
7. **Price callouts must look exciting**: big coral numerals, a starburst or ticket, and "U.P. $xxx" struck through next to the offer price when a usual price exists.
8. **Avoid ambiguous glyphs.** Do not use `$?.??` to hide a price ("$" and "?" look alike). Use a padlock or "price revealed at the booth".
9. **No invented venue art.** A drawn Suntec skyline was rejected as inaccurate. Use text for the venue unless the user supplies a reference.
10. Real photos, floor plans and prizes go in clearly marked dashed placeholders (`data-placeholder="..."`) until the user supplies them.

## Venue and event wording

For the Tech Show 2026 campaign the venue line is always "Suntec City Convention Centre, Level 4" (no hall numbers), with booth 8428 and 13–15 Nov. Use this exact wording on every post, including map headers.

## gigaAI (product carousels)

`assets/giga-ai-logo.svg` is the gigaAI wordmark ("Powered by AI Fiesta"). It is pink, so it disappears on a pink background: always place it on a white rounded card. `assets/gigaai/` holds screenshots of six features (Image Studio, Video Studio, Live Websites, Slides, Multi Chat, Experts & Legends). `tools/build_carousel.py` builds an 8-slide carousel: cover, one slide per feature, call to action. Keep gigaAI copy to what the supplied slides say; do not claim speeds or capabilities that are not in them.

## Workflow

1. Gather the facts: event, dates, venue, booth, offers and exact wording, T&Cs, and any usual prices. Ask for anything missing. Never invent prices, prizes or T&Cs. If wording is a stand-in, say so.
2. Write the post as an HTML file that links `assets/common.css` (fonts, colour variables, shared classes such as `.strip`, `.booth`, `.when`, `.fine`). Canvas is `<div class="post" id="post">` at 1080 x 1440.
3. Render: `node tools/render.js post.html out/post.png` (needs Playwright; Chromium is pre-installed in Claude Code cloud sessions). Always open the PNG and check for overlaps and clipped text before showing the user.
4. Show the user, then iterate on their comments. A review page built with the Artifact tool and the `comments` capability works well for gathering feedback on several posts at once.
5. Export finished PNGs, named like `giga-<event>_<nn>_<slug>.png`.

## Floor plans and maps

Redraw the organiser's plan as a clean vector in brand colours rather than pasting a screenshot. Highlight the client's booth with a solid pink block, a ring and a label, and add a zoomed inset with readable booth numbers. `tools/build_plan.py` shows the approach (hand-read coordinates, SVG output). Tell the user the redraw is hand-traced and must be checked against the official plan.

## Always flag before the user publishes

- Placeholder T&Cs wording
- Any price or "U.P." figure the user has not confirmed for this event
- Empty placeholders (booth photo, prize, floor plan)
- Visual-only elements that could imply a claim (such as a "going fast" bar)
