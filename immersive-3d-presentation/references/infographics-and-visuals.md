# Hybrid Visuals, Native SVG Infographics & Hand-Drawn Sketches

Presentations should NEVER feel monotonous or restricted to Three.js 3D alone. Mix visual media purposefully across slides so each concept gets the clearest visual medium.

## 1. Visual Media Matrix (`data-visual`)

Assign a purposeful `data-visual` mode to every slide:

| Mode | Best For | 3D Canvas Behavior |
|---|---|---|
| `3d` | Cover, section openers, spatial/physical concepts, interactive contextual ladders (`data-prop` / `data-3d`) | Prominent hero or contextual prop (`data-hero="2.8,0,0.95"`) |
| `infographic` | Processes, data comparisons, system architectures, frameworks, timelines | Gracefully fades/hides (`data-hero="hide"`) or parks tiny in corner so the SVG infographic owns the stage |
| `sketch` | Storytelling, historical lessons, brainstorming, concept analogies, kroki illustrations | Fades (`data-hero="hide"`) or pairs with subtle parchment/ambient particles |
| `hybrid` | Split slides combining a compact 3D object on one side with a crisp inline SVG diagram, chart, or callout graphic | Balanced side-by-side (`data-hero="3.3,0,0.75"`) |
| `photo` | Real-world places, historical artifacts, case studies, user-supplied photos | Fades (`data-hero="hide"`) so the framed photo and caption breathe |

---

## 2. Model-Crafted Native Infographics (Zero External Assets!)

**Rule:** NEVER link to external stock infographic URLs, Slidesgo links, or raw emoji icons. Build every infographic **natively inside the HTML** using crisp inline `<svg>` + CSS Grid + GSAP animations so it scales infinitely, matches the deck palette, and animates step-by-step on arrow keys.

### Style A — Editorial Flat-Line Infographic (Inspired by Modern Education Infographics)
Best for educational explanations, concept breakdowns, and modern clean light/cream decks:
- **Line work:** Crisp `2px` dark ink outlines (`stroke="#16181D"` or `var(--ink)`, `stroke-linecap="round"`, `stroke-linejoin="round"`).
- **Pastel semantic fills:** Mint (`#8CE0CB`), soft lavender (`#D8C6F2`), muted coral (`#E07A68`), warm butter (`#FDE6A8`) on clean white/ivory cards.
- **Callout architecture:** Rounded pill labels (`rx="999"`) connected to focal shapes via clean **90-degree orthogonal leader lines** (`<polyline>` with small terminal dots).
- **Vector scenes:** Clean geometric cards, browser/window frames, envelopes, characters/silhouettes, and icons built directly from `<rect>`, `<circle>`, `<path>`, and `<line>`.

### Style B — Isometric & Layered Data Infographic (Inspired by Modern Data Infographics)
Best for tech, analytics, AI, architectures, KPIs, and multi-layer workflows:
- **Base & depth:** Isometric diamond/prism base (`polygon` or CSS `rotateX(55deg) rotateZ(-45deg)`) with soft shadow glow.
- **Floating layered panels:** Translucent stacked cards displaying crisp code/data glyphs (`</>`, `1010`, mini sparklines, progress bars).
- **Orthogonal node wiring:** Thin `1.5px` crisp connector lines linking circular lettered/icon badges (`A`, `B`, `C`, gears, nodes) positioned around the central stack.
- **Step animation:** Reveal layers and trace connector wires sequentially with GSAP `strokeDashoffset` as the user presses the forward arrow.

### Style C — Kroki / Hand-Drawn Ink Sketch (Inspired by Papyrus & Sketchbook Lessons)
Best for historical narratives, literature, science notebooks, conceptual metaphors, and classroom analogies:
- **Organic ink strokes:** Variable-feel SVG `<path>` drawings using deep sepia (`#482400`) or charcoal ink (`#1E1E24`), `fill="none"`, `stroke-linecap="round"`, subtle cross-hatching lines (`opacity="0.45"`).
- **Draw-on animation:** Add class `.svg-draw` to key `<path>` / `<polyline>` / `<line>` elements — the engine measures `getTotalLength()` and animates `stroke-dashoffset` smoothly when the slide or `.step` activates!
- **Motif ideas:** Feather quill, stacked vintage books, compass & scroll, pyramid, ancient sailing ship, lightbulb sketch, hand-drawn arrow annotations, circled emphasis words.

---

## 3. User-Specified Images & Photo Framing

When the user asks for images on specific slides (in Step 1):
- **If the user uploaded an image:** Embed it directly (or reference the provided path/data URI) inside a styled `.photo-frame` matching the deck's visual grammar (e.g., aged parchment frame with subtle tape/sepia tint in `papyrus` mode; crisp 2px hard-shadow frame in `brutalist` mode; double gold frame in `frames` mode).
- **If the user wants an image on a slide but hasn't uploaded one yet:** Never insert broken URLs or fake stock links. Either:
  1. Generate a rich native SVG illustration/infographic in its place if illustrative, OR
  2. Render a clean, clearly labeled **Drop-In Photo Frame** (`<div class="photo-slot" data-photo-hint="...">`) with exact dimensions and an instant local-file click-to-load picker (`<input type="file" accept="image/*">`) so the presenter can drop their own photo in 1 click without editing HTML!

---

## 4. Papyrus Historical Lesson Visual Kit

When the topic is **historical, archaeological, literary, cultural, or heritage-focused**, proactively suggest the **`papyrus` archetype** (inspired by classic Papyrus History Lesson decks):
- **Palette:** Aged parchment `#f4ebd9`, warm papyrus tan `#c1ad8f`, elevated scroll card `#fbf6ec`, deep sepia ink `#482400`, muted sepia `#75583a`, heritage terracotta accent `#6b2d1b` / `#553333`.
- **Signature Layouts & Interactive Activities:**
  1. **Chronological Timeline (`[data-step-group]`):** Horizontal or vertical sepia-ink date markers (`3150 BC → 1453 AD`) with animated ink connectors.
  2. **Historical Data Chart (Inline SVG):** Smooth sepia-ink line/area/percentage chart with zero-based axes and animated path drawing.
  3. **Etymology / Origins Spotlight:** Large calligraphic quote or word-origin cards.
  4. **Interactive Classroom Exercises:** True/False toggle table, Matching pairs, Fill-in-the-blanks reveal, or Multiple-Choice quiz — all controllable via arrow keys AND clicks!
  5. **Hybrid 3D + Kroki Mix:** Pair subtle bronze/sepia 3D objects (ancient scroll, compass, pyramid, globe) on cover/opener slides with pure hand-drawn sepia SVG sketches and parchment photo frames on content slides.


---

## 5. Strict Zero-Text-Overflow Rules for Diagrams, Mind Maps & Cards (v8)

Hardcoded narrow SVG `<rect>` + `<text>` boxes frequently cause Arabic and long English titles to spill outside borders or clip past card edges. Follow these mandatory rules:

1. **HTML-First Nodes + SVG Connector Underlay (Preferred for ALL Text-Bearing Diagrams):**
   - For radial mind maps, dual-pillar bridges, flowcharts, and org charts containing multi-word labels (especially Arabic), **NEVER cram labels into fixed-width SVG `<rect>` boxes**.
   - Instead, place an `<svg class="diagram-lines">` (`position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none;`) strictly for lines, dashed connectors, arrows, and decorative arches, and render every text node as a real **HTML/CSS flex/grid box** (`.diag-node`) with:
     - `padding: 14px 22px; max-width: 100%; overflow-wrap: break-word; word-break: normal; text-align: center;`
     - Automatic height growth (`height: auto; min-height: ...`) so text NEVER escapes its border!
2. **If Pure SVG Text Is Used (Short 1–2 Word Labels Only):**
   - Wrap multi-word labels into `<tspan x="..." dy="1.25em">` lines.
   - Guarantee generous box width (`rectWidth >= longestLineChars * fontSize * 0.85 + 56px` for Arabic).
   - Keep all SVG shapes and text strictly inside the `viewBox` with at least `32px` internal margin on all 4 sides, and ensure the parent container fits well within the `1600×900` stage's safe margins (`72px` horizontal, `56px` vertical).

---

## 6. High-Craft Motion & Framing Techniques (v8 — Inspired by Top Motion Decks)

Mix these high-impact techniques selectively on hero, showcase, or photo slides:

### A. Geometric Hexagon Mosaic Image Reveal (Staggered Center-Outward Zoom)
- Ideal for photo-heavy showcase slides (places, history, products, case studies) instead of a flat rectangular photo box.
- Construct a cluster of 7–13 interlocking CSS hexagon tiles (`.hex-tile` using `clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)`), sharing a single aligned background photo (`background-size` & `background-position` mapped to the mosaic container) with a subtle inner shadow (`box-shadow: inset 0 0 20px rgba(0,0,0,0.45)`) against a clean solid/dark backdrop.
- Animate tiles on slide entry with GSAP staggered zoom from center (`scale: 0 -> 1`, `opacity: 0 -> 1`, `stagger: { from: 'center', amount: 0.65 }`, `ease: 'back.out(1.2)'`).

### B. Editorial Typography Mask & Foreground Subject Pop-Out
- Ideal for dramatic chapter openers or bold statement slides.
- Stack giant heavy display letters/words (`font-weight: 900; line-height: 0.88`) filled with a rich image or gradient via CSS `background-clip: text; -webkit-background-clip: text; color: transparent;`.
- Optionally overlap a crisp foreground subject (cutout image, SVG focal illustration, or floating 3D object with soft shadow) slightly in front of the oversized letters while accompanying text slides in cleanly from the side.

### C. Continuous Spatial Morph Transitions (`data-transition="morph"`)
- Inspired by minimalist 3D Morph decks (`Muted 3D Shapes Morph`):
- Carry persistent visual anchors (section label, subtle accent bar, or muted 3D geometric props) smoothly between consecutive slides: elements glide/scale cleanly from off-canvas staging positions (`x: ±140px`, `scale: 0.86 -> 1`, `duration: 0.75s`, `ease: 'power3.inOut'`) so slides feel like one continuous infinite canvas rather than disconnected cuts.


### D. Motion.dev-Grade Spring Physics & Silky Cross-Glide Transitions (v9)
Inspired by Motion (`motion.dev/docs/react-scroll-animations`):
- **Spring-Damped Progress Bar:** Drive the top progress bar `#bar` with real spring physics (`stiffness: 100, damping: 30, restDelta: 0.001`) so it glides with velvety inertia rather than a stiff linear transition.
- **Simultaneous Cross-Glide (Zero Hard Cuts, Zero Overlap):**
  - Outgoing slide (`prev.classList.add('exiting')`, `z-index: 1; pointer-events: none;`) glides smoothly out (`x: -105 * SIGN * dir`, `scale: 0.955`, `opacity: 0`, `filter: blur(5px)`, `0.58s`, `expo.out`) and cleans up on completion, while any older stale slides are immediately hard-hidden so rapid arrow presses never stack.
  - Incoming slide (`next.classList.add('active')`, `z-index: 2`) simultaneously glides in (`x: 105 * SIGN * dir -> 0`, `scale: 0.965 -> 1`, `opacity: 0 -> 1`, `filter: blur(4px) -> 0px`, `0.78s`, `expo.out`, `force3D: true`).
- **Layered Depth Parallax:** Background motifs move slower (`48px`, `0.95s`) than primary text (`105px`, `0.78s`) and foreground cards (`y: 24 -> 0`, `scale: 0.97 -> 1`, `0.84s`), creating physical depth on every slide transition.
- **Clip-Path Image Reveal (`.clip-reveal`):** Unveil showcase photos/cards smoothly from center outward (`inset(0% 50% 0% 50%) -> inset(0% 0% 0% 0%)`, `0.82s`, `expo.out`).
- **Inertia-Locked Wheel/Trackpad Glide:** Support smooth trackpad/wheel stepping alongside arrow keys with a `650ms` inertia lock.


### E. Paper-Cut Infographics, Curtains & Perspective Road (v10)
For theatrical, tactile, paper-craft presentations (`data-motif="paper-cut"`):
- **Layered Paper Depth:** Stack 2–3 SVG wave or panel layers with slightly offset shades (`#ffffff`, `#f2f5f4`, `#e4ebe8`) and soft directional `filter: drop-shadow(...)` so every edge reads like physical cut cardstock.
- **Paper-Cut Curtain Reveal (`.curtain-left`, `.curtain-right`):** On Slide 1, animate curtains outward (`xPercent: -100` / `+100`, `duration: 1.15s`, `ease: 'expo.out'`) to reveal extruded 3D text (`text-shadow` multi-layer extrusion). On the closing slide, bind the final `.step` action to sweep the curtains closed (and reverse open on Back arrow).
- **Glowing Tree Nodes (`.tree-node`):** Animate radial glow + elastic pop (`scale: 0 -> 1`, `ease: 'elastic.out(1, 0.55)'`) synchronized with each `.step-item`.
- **3D Winding Timeline Road:** Draw a perspective-tapered SVG `<path>` road (wide at bottom foreground, narrow toward upper horizon) and place milestone markers with progressive scale (`1.0` near foreground → `0.78` near horizon) revealing step-by-step.
- **Isometric Pillars (`.iso-pillar`):** Build 4–6 angled-cap pedestals with grounded oval shadows sliding upward (`y: 60 -> 0`, `opacity: 0 -> 1`) on arrow-key steps.
