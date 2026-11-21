# RTL, Arabic and bilingual decks

Read this in Step 0 (detect) and Step 4/6 (design and build). The template already implements the
mechanics (logical CSS, mirrored keys/swipe/progress/arrows, mirrored 3D hero side); this file explains
the rules so new slides you write stay correct.

## Contents
1. Detecting direction (decision rules)
2. Setting up the document
3. Mirror this / do not mirror this
4. Typography for Arabic
5. Numerals
6. Bilingual decks
7. Charts and diagrams
8. 3D and RTL
9. RTL check list

---

## 1. Detecting direction

Run the bundled detector on everything the user gave you (topic, pasted content, audience notes):

```bash
python scripts/detect_direction.py "the user's text"      # or: --file content.txt
```

It counts **letters only** (digits, punctuation, URLs and code fences are ignored) and returns
`mode`, `dir`, `lang` and `rtl_ratio`:

| rtl_ratio | mode | Deck setup |
|---|---|---|
| >= 0.65 | `rtl` | `<html dir="rtl" lang="ar">` (or `fa`, `ur`, `he` as detected) |
| 0.15 to 0.65 | `bilingual` | primary direction on `<html>` (RTL if ratio >= 0.5), every text block gets `dir="auto"` |
| < 0.15 | `ltr` | `<html dir="ltr" lang="en">` |

Rules that override the number:
- **An explicit request wins.** "Make it in Arabic" -> RTL even if the prompt itself is English.
  "English slides for an Arabic-speaking audience" -> LTR.
- **Language of the request is a signal, not the answer.** A user writing to you in Arabic about
  "Machine Learning" almost certainly wants an Arabic deck with English terms in parentheses.
- If the topic is a title only (very few letters), fall back to the language of the user's message.
- Persian/Urdu are detected by letters absent from Arabic (پ چ ژ گ / ٹ ڈ ڑ ں ے). They need `lang="fa"` /
  `"ur"`; use Persian digits for `fa` unless told otherwise (section 5). For Hebrew use `lang="he"`
  and the Hebrew font in section 4.
- Say what you detected in the assumptions list: "Detected: Arabic (RTL), 97% Arabic letters."

## 2. Setting up the document

```html
<html lang="ar" dir="rtl" data-motif="ideas" data-digits="latn">
```
- `lang` selects the font tokens in the template CSS and the `Intl.NumberFormat` locale.
- Write **all** spacing with logical properties: `margin-inline-start`, `padding-inline-end`,
  `inset-inline-start`, `text-align:start`, `border-inline-start`. Never `left/right` for layout.
  The one exception is a transform origin: `[dir=rtl] .rule{transform-origin:right}`.
- Use `flex`/`grid`; they reverse automatically. A `grid-template-columns` of 3 cards puts card 1 on the
  right in RTL, which is correct.

## 3. Mirror this / do not mirror this

**Mirror:** layout order of columns and cards; progress bar fill direction; slide-transition travel
(`x: 80*SIGN`); previous/next arrows; step-by-step flows and timelines (earliest on the right); list
bullets and numbering position; keyboard (`ArrowLeft` = next in RTL); touch swipe (swipe right = next);
speaker-notes and slide-list alignment; side-by-side comparisons ("before" on the right); the side the 3D
hero sits on.

**Do not mirror:** logos and brand marks; photos and illustrations of real things; clocks and rotation
directions; play/pause/volume icons; numbers and maths expressions; code; phone numbers and URLs;
Latin-script product names; a "checkmark" icon; charts' value axis direction (values still grow upward / outward).

## 4. Typography for Arabic

| Role | Recommended (Google Fonts) | Notes |
|---|---|---|
| Display, elegant/historical | **Amiri** | calligraphic naskh, pairs with Cormorant Garamond; for `frames` and `chiaroscuro` |
| Display, modern | **Reem Kufi**, **Tajawal** 800 | geometric; `playful`, `blueprint` titles |
| Body, general | **Cairo**, **IBM Plex Sans Arabic**, **Tajawal** | pick one; keep weights 400/700 |
| Long reading text | **Noto Naskh Arabic** | high legibility at small sizes |
| Hebrew | **Heebo**, **Assistant**, **Frank Ruhl Libre** (serif) | `lang="he"` |
| Persian | **Vazirmatn** | `lang="fa"` |

Rules:
- **No letter-spacing, ever** on Arabic script (it breaks joining). The template forces
  `letter-spacing:0` under `lang^="ar"`. Also no `text-transform: uppercase` and no italics (Arabic has none).
- **Size up ~10%** vs the Latin equivalent: Arabic glyphs look smaller at the same px. Body 30 px -> 33 px;
  and line-height 1.5 -> 1.7 so marks (tashkeel) never collide.
- **Embedded Latin terms:** wrap in `<bdi>` or give the element `dir="ltr"`, so punctuation around them
  does not jump sides: `<bdi>Machine Learning</bdi>`. A trailing period attached to an English phrase in an
  RTL line will render on the wrong side without this.
- **Punctuation:** Arabic comma `،`, semicolon `؛`, question mark `؟`; quotation marks `« »` or `" "`.
- **Always give a fallback stack** (`"Cairo","Segoe UI",Tahoma,sans-serif`): if Google Fonts is blocked the
  deck must still be readable. Test with fonts blocked (the smoke test does).
- Keep diacritics (tashkeel) only where they teach (Qur'an, language lessons); otherwise omit.

## 5. Numerals

Decide once per deck and set `data-digits` on `<html>`; every counter and slide number uses it through
`Intl.NumberFormat(lang + '-u-nu-' + digits)`.
- `latn` (0-9): default for Arabic business/tech content and most of the Gulf and North Africa classrooms.
- `arab` (٠-٩): when the user asks for it, for religious/literary content, or school material that uses it.
- `arabext` (۰-۹): Persian/Urdu.
Ask in Step 1 only if the audience's convention is unclear. Never mix both systems in one deck.
Percent sign: `36%` in Latin digits reads fine in Arabic text; in Arabic-Indic digits use `٣٦٪`.

## 6. Bilingual decks

- Keep **one primary direction** for the deck shell (progress, controls, transitions).
- Two-column parallel text: each column gets its own `lang` and `dir`; put the primary language in the
  inline-start column.
- Mixed lines: `dir="auto"` on each paragraph, `<bdi>` around inline foreign terms.
- Titles in both languages: Arabic title large, English subtitle smaller beneath; do not put both in one line.
- Slide count and timing are unchanged; bilingual text needs shorter sentences: keep the 30-word limit per
  language.

## 7. Charts and diagrams

- Chart.js in an RTL deck: `options.scales.x.reverse = true` (categories run right to left),
  `options.scales.y.position = 'right'`, and `rtl: true` with `textDirection: 'rtl'` inside
  `plugins.legend` and `plugins.tooltip`. Set `Chart.defaults.font.family` to the Arabic body font.
  Verify in the smoke test screenshot; if a Chart.js option behaves differently in the pinned version,
  trust the screenshot over this note.
- Bars still start at zero and the value axis still grows upward.
- Draw diagrams as SVG with `direction` aware layout: build the flow left-to-right in data, then apply
  `transform="scale(-1,1)"` to the *arrangement group only* and re-flip each text node (or place text in
  HTML overlays) so letters never mirror.
- Never mirror text. If something looks like reversed letters, a transform is applied to a text node.

## 8. 3D and RTL

- The deck's HTML text and the WebGL canvas are separate layers. **All readable text stays in HTML/CSS.**
  Three.js `TextGeometry` (typeface JSON fonts) does not shape Arabic: letters come out isolated and in
  the wrong order. Other text-in-WebGL libraries vary in Arabic support and each needs its own test, so the
  default is HTML. A `CanvasTexture` is acceptable for a short label drawn with
  `ctx.direction='rtl'; ctx.font='700 64px Cairo'`, and only after the font has loaded
  (`await document.fonts.load('700 64px Cairo')`).
- Mirror the *composition*, not the objects: `data-hero` x and `data-cam` x are multiplied by `SIGN`
  in the template, so the hero sits opposite the text column in either direction.
- Orbit and spin direction are not mirrored. Scroll/slide travel is.
- CSS-3D cards: flipping is `rotateY(180deg)` either way; the back face is pre-rotated so its text reads
  correctly in RTL (verified).

## 9. RTL check list

- [ ] `lang` and `dir` on `<html>`; `data-digits` set; fonts and fallback stack set.
- [ ] No physical `left/right` in layout CSS; no `letter-spacing` on Arabic; line-height >= 1.6.
- [ ] Controls, progress, arrows, swipe and keys mirrored (open the smoke test screenshots with `--rtl`).
- [ ] Every Latin term inside Arabic text is isolated (`<bdi>`); no stray punctuation at the wrong end.
- [ ] Numbers consistent (one numeral system); counters use the formatter.
- [ ] Hero 3D object opposite the text; no readable text inside WebGL.
- [ ] Charts mirrored as in section 7; bars from zero; source line present.
- [ ] Ran `scripts/smoke_test.py index.html --rtl` and viewed the screenshots.
