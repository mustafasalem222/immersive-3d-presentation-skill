# Style archetypes and how to choose one

Read this in Step 0 (analyze content) and again in Step 4 (design). It holds the three Canva-derived
reference styles, two extra archetypes for content they do not cover, and the rules for matching
content to a style.

## Contents
1. What the Canva references are (and are not)
2. Choosing: content signals -> archetype
3. The five archetypes (tokens, type, layout, motion, 3D)
4. Mixing, overriding, and brand colors
5. Fidelity upgrade: when the user shares screenshots

---

## 1. What the Canva references are (and are not)

The user supplied three Canva templates as visual references:

| Reference (from the template's own title) | Archetype here |
|---|---|
| Blue and Gold Elegant Museum Art Gallery Presentation | `frames` (Gallery Elegant) |
| Baroque Art Period Presentation in Black and Yellow Painterly Style | `chiaroscuro` (Baroque Painterly) |
| Blue Illustrated Philosophy Project Presentation | `ideas` (Illustrated Philosophy) |

**Provenance, stated honestly:** Canva blocks automated access to template pages. When this skill was
written only one of the three pages returned anything (its title and meta tags); the other two were
blocked. The archetypes below are therefore built from each template's **title** (colour pair, style
keyword, subject) plus the established visual conventions of that genre. They are a faithful *direction*,
not a pixel-level analysis. Say so briefly if the user asks how closely a deck matches the Canva originals,
and offer section 5.

**Never copy Canva artwork, photos, fonts files or layouts verbatim.** Use the references as mood and
structure only. Draw everything in CSS/SVG/WebGL.

---

## 2. Choosing: content signals -> archetype

Do this silently in Step 0, then state the pick and the reason in one line when you ask the questions.

1. Extract signals from the topic, any pasted text, the audience and the setting.
2. Score each archetype: +2 for a subject keyword match, +1 for an audience/tone match, +1 for a
   setting match. Highest score wins; show the runner-up as the alternative.
3. Tie, or all scores below 2 -> use `ideas` (the most flexible) and say it is a default.
4. A brand identity from the user overrides the palette and fonts but **not** the layout, motion or 3D
   behaviour of the winning archetype.

| Archetype | Subject signals | Audience / tone signals | Setting signals |
|---|---|---|---|
| `frames` Gallery Elegant | art, museum, exhibition, gallery, heritage, culture, architecture, design, fashion, jewellery, luxury, tourism, awards, ceremony | adults, formal, refined, curated, premium | conference, opening, donor/stakeholder talk, cultural centre |
| `chiaroscuro` Baroque Painterly | art history, baroque/renaissance/any "period", history, war, empire, religion, literature, theatre, film, myth, biography, true-crime, storytelling | dramatic, serious, emotional, cinematic | lecture hall, documentary-style talk, seminar |
| `ideas` Illustrated Philosophy | philosophy, ethics, psychology, critical thinking, humanities, social studies, language, learning theory, AI ethics, "big questions", student project | students, teachers, curious general audience, discussion-based | classroom, workshop, group project, training |
| `blueprint` Technical Blueprint | science, engineering, programming, data, AI/ML, maths, networks, security, product/tech, research results | technical, analytical, professionals, university | lab meeting, tech talk, bootcamp, demo day |
| `playful` Playful Classroom | primary/middle school, early learning, kids' topics, games, nature for kids, festivals | ages 5-12, parents, energetic, friendly | school, family workshop |

Bilingual or RTL content does not change the archetype; it changes fonts, direction and the side the 3D
object sits on (see `rtl-arabic.md`).

---

## 3. The five archetypes

Each block gives: tokens (hex), fonts (Latin + Arabic), layout vocabulary, motion language, 3D motif, and
what to avoid. Colour meaning must stay fixed through the whole deck (Step 4 of SKILL.md).

### `frames`: Gallery Elegant (ref: blue and gold museum gallery)
- **Tokens:** `--bg #0b1b3a` navy, `--surface #12285a`, `--ink #f4efe3` warm ivory, `--accent #d4af37` gold
  (= the thing to remember), `--accent2 #e8d08a` pale gold (= secondary label). Gold appears only as thin
  rules, frames, numerals and one emphasised word per slide.
- **Fonts:** display = Cormorant Garamond 500/700 (Arabic: **Amiri**); body = Inter (Arabic: **Cairo**).
- **Layout:** generous margins, centered or asymmetric title with a thin gold rule, "exhibit label"
  captions (small caps title, year, one-line description), large framed image areas with a double-line
  frame (outer gold, inner pale mat), numbered rooms/sections like gallery wings.
- **Motion:** slow and ceremonial. Fade + slight rise (0.6 s), rules that draw themselves, "spotlight"
  reveal (radial gradient mask expanding). No bounces.
- **3D:** `frames` motif: a tilted carousel of gold-edged frames under a warm spot. Use CSS-3D tilt on
  image cards. Camera drifts a few degrees between slides.
- **Avoid:** heavy shadows, saturated colours, more than one gold element competing per slide.

### `chiaroscuro`: Baroque Painterly (ref: black and yellow painterly baroque)
- **Tokens:** `--bg #0a0806` near-black, `--surface #1a1510`, `--ink #f2e8d0` parchment,
  `--accent #f2b705` yellow (= the focal point, like the lit figure in a painting),
  `--accent2 #c0762b` burnt ochre (= secondary tone).
- **Fonts:** display = Cormorant Garamond bold, large and tight (Arabic: **Amiri** bold);
  body = Inter or Lora (Arabic: **Cairo** or Noto Naskh Arabic).
- **Layout:** one dominant subject per slide emerging from darkness, very large type, asymmetry (text
  hugging one edge, subject on the other), diagonal compositions, a painterly grain overlay (SVG
  `feTurbulence`, already in the template), captions like museum wall text.
- **Motion:** dramatic and slow: light *arriving* (opacity + brightness ramp), slow push-in zoom (0.94 -> 1),
  text revealed by a moving light edge. 0.8-1 s ease-out, never snappy.
- **3D:** `chiaroscuro` motif: one sculptural form, one warm spot, deep shadow, fog. The single strong
  light is the whole point; do not add fill lights.
- **Avoid:** bright backgrounds, many colours, evenly lit scenes, playful easing.

### `ideas`: Illustrated Philosophy (ref: blue illustrated philosophy project)
- **Tokens:** `--bg #0e2a5c` deep blue, `--surface #16408a`, `--ink #f6f3ea` cream,
  `--accent #ffd166` warm yellow (= the question / key idea), `--accent2 #7fd6ff` sky blue (= the concept
  being examined).
- **Fonts:** display = Cormorant Garamond (Arabic: **Amiri**); body = Inter (Arabic: **Cairo**).
  Optional hand-drawn feel from SVG underlines and arrows, not from a script font.
- **Layout:** concept maps, thought/speech bubbles, "question of the day" big-statement slides, side-by-side
  positions (for / against), timelines of thinkers, flip cards for "idea -> meaning". Hand-drawn SVG
  doodles: stars, spirals, arrows, underlines (draw them yourself; stroke-dashoffset animation).
- **Motion:** playful but purposeful: arrows and underlines draw in, cards flip, thought bubbles pop with
  a small overshoot (`back.out(1.4)`), concepts connect with growing lines.
- **3D:** `ideas` motif: floating glass-like platonic solids (the "forms") orbiting a point; CSS flip cards.
- **Avoid:** photographic clutter, stock clip-art, long paragraphs. One question per slide.

### `blueprint`: Technical Blueprint (no Canva reference; added for science/tech content)
- **Tokens** (already in the template under `data-motif="network"`): `--bg #07131f`, `--surface #0f2336`, `--ink #e8f1f8`, `--accent #4cc9f0` cyan
  (= the signal / result), `--accent2 #b8f2e6` mint (= the baseline / comparison).
- **Fonts:** display + body = IBM Plex Sans (Arabic: **IBM Plex Sans Arabic**); code = IBM Plex Mono.
- **Layout:** thin grid lines in the background, labelled diagrams, big-number slides, aligned data
  tables, annotated charts. Numbers use tabular figures.
- **Motion:** precise and linear-ish (`power2.out`, 0.4 s): lines trace, bars grow from zero, nodes light up in
  sequence to explain a flow. Motion always explains.
- **3D:** `network` motif (shipped in the template): nodes and links slowly rotating; set `data-motif="network"`.
  Light up nodes in sequence (GSAP on a uniform or material colour) when a slide explains a flow.
- **Avoid:** decorative 3D that does not map to the content, glow overload.

### `playful`: Playful Classroom (no Canva reference; added for young audiences)
- **Tokens:** `--bg #1d2b64`, `--surface #2f45a3`, `--ink #fffaf0`, `--accent #ff7a59` coral (= the answer),
  `--accent2 #6be3b5` mint (= the helper idea). Bright but on a dark base so the 3D layer and contrast still work.
- **Fonts:** display = Baloo 2 or Fredoka (Arabic: **Cairo** 700 or **Tajawal** 800); body = Nunito
  (Arabic: Cairo). Larger sizes (body >= 32 px).
- **Layout:** big rounded cards, one idea and one picture-like SVG per slide, counting/sorting games,
  stickers (SVG), progress as steps along a path.
- **Motion:** bouncy (`elastic.out(1,.6)` sparingly), 0.5 s, plenty of click-to-reveal.
- **3D:** `ideas` motif with bright tokens, bigger, slower solids; large CSS flip cards.
- **Avoid:** small text, fast flashing, more than 2 entrance styles per slide.

---

## 4. Mixing, overriding, and brand colours

- **Brand given:** replace `--bg --surface --ink --accent --accent2` and the fonts; keep the archetype's
  layout vocabulary, motion language and 3D motif. Check contrast (WCAG AA) after substitution.
- **Mixed content** (e.g. an art-history lesson for teenagers): pick the archetype of the *subject*
  (`chiaroscuro`), then borrow one device from the *audience* archetype (`ideas` flip cards). Never blend
  two palettes.
- **Light/print-friendly request:** the template is dark-first. Set light tokens, set `--accent` for
  contrast on white, and either remove the WebGL canvas (use `body.no-gl`) or lower particle opacity.

## 5. Fidelity upgrade: when the user shares screenshots

If the user uploads screenshots or exports of the Canva templates (or any reference), they outrank section 3:
sample the dominant colours, identify the heading/body typefaces (match to the closest free Google Font),
note the grid and the decorative devices, then write the tokens and layout vocabulary into the deck. Keep
the archetype's 3D motif and RTL behaviour. State what you matched and what you approximated.


## 6. UI Reference Screenshot Priority
When the user uploads a UI reference image or screenshot in Step 1, it **overrides** the default archetypes above:
- Extract the exact palette (`--bg`, `--surface`, `--ink`, `--muted`, `--accent`, `--accent2`) from the reference image.
- Match the visual grammar (card radius, border style, shadow depth, corner motifs, light vs. dark theme) while keeping full projector legibility and RTL mirroring when Arabic.
- Tune Three.js lights and material roughness/contrast so the contextual 3D models look crisp against the extracted background.


---

## 7. Historical & Native Infographic Archetypes (v7)

### `papyrus`: Papyrus & Ink-Sketch Historical Lesson (ref: Papyrus History Lesson XL)
- **Trigger / Suggestion Rule:** Whenever the topic involves **history, civilizations, heritage, archaeology, religion, literature, biographies, timelines, or classic lessons**, proactively ask the user in Step 1 if the topic is historical and suggest this **Papyrus & Parchment** archetype.
- **Tokens:** `--bg #f4ebd9` aged parchment, `--surface #fbf6ec` warm scroll ivory, `--ink #482400` deep sepia ink, `--muted #75583a` faded ink, `--accent #6b2d1b` heritage terracotta/sepia-red (= focal callouts & key dates), `--accent2 #c1ad8f` aged papyrus tan (= borders, rules, timeline tracks).
- **Fonts:** Display = **Amiri** / **Aref Ruqaa** (Arabic) or **Redressed** / **Cormorant Garamond** (Latin); Body = **Cairo** / **Noto Naskh Arabic** (Arabic) or **Livvic** / **Lora** (Latin).
- **Texture & Framing:** Subtle SVG `feTurbulence` paper grain overlay + delicate sepia double-rule dividers and corner scroll flourishes.
- **Visual Mix:** Hand-drawn sepia ink-sketch SVGs (`.svg-draw` animated strokes: quill, ancient books, ships, compass, pyramid, maps), sepia line-chart infographics, vintage tinted `.photo-frame` slots, interactive historical exercises (True/False, Fill-in-the-blanks, Matching, Timeline), paired selectively with warm bronze/sepia Three.js 3D props (scroll, globe, compass, pyramid).

### `editorial-line`: Clean Education Infographics (Flat-Line + Pastel Callouts)
- **Best for:** Structured academic lessons, study guides, instructional frameworks, clear conceptual comparisons.
- **Tokens:** `--bg #fcfcfd`, `--surface #ffffff`, `--ink #14171f`, `--muted #5c6473`, `--accent #6fd4bc` mint, `--accent2 #c9b6f0` lavender, `--accent3 #e07a68` soft coral.
- **Visual signature:** Crisp `2px` dark ink outlines on inline SVG illustrations, orthogonal leader-line callouts with pill badges, clean geometric vector scenes mixed selectively with light-mode Three.js 3D props.

### `isometric-data`: Layered Tech & Data Infographics
- **Best for:** Computer science, data analytics, AI, architecture, systems engineering, business metrics.
- **Tokens:** `--bg #f8faff` (light) or `#090d1a` (dark), `--accent #5dd3c4` aqua-mint, `--accent2 #6c63ff` indigo-violet.
- **Visual signature:** Isometric 3D/SVG platforms with floating layered translucent panels (`</>`, `1010`, live charts), crisp orthogonal wireframes connecting circular lettered/icon nodes (`A`, `B`, `C`), mixed with interactive Three.js 3D data/system sculptures.


### `muted-morph`: Muted Minimalist 3D Morph (ref: Muted 3D Shapes Morph Marketing Slides)
- **Best for:** Modern marketing pitches, portfolios, startup/project showcases, design reviews, executive clean decks.
- **Tokens:** `--bg #efefef` soft gallery gray, `--surface #ffffff` crisp white card, `--ink #000000` pure black display type, `--muted #5f5970` muted slate-plum, `--accent #5d447b` deep muted plum (= key callouts & progress), `--accent2 #c8bfd6` soft muted lavender (= subtle shape fills & borders).
- **Fonts:** Clean geometric sans (`Cairo` / `Tajawal` for Arabic; `Plus Jakarta Sans` / `DM Sans` / `Inter` for Latin) with generous whitespace and bold lowercase/clean display headings.
- **3D & Motion Signature:** Matte clay/satin minimalist 3D shapes (toruses, capsules, spheres, beveled prisms in muted plum, lavender, warm stone, sage) casting real soft studio shadows onto the `#efefef` stage, gliding continuously across slides via `data-transition="morph"` spatial continuity.
