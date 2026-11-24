---
name: immersive-3d-presentation
description: Build art-directed, interactive HTML presentations (RTL Arabic, LTR English, or Bilingual) blending shadowed Three.js 3D models (per-slide & per-step data-prop/data-3d), cinematic centered cover surrounds, continuous morph transitions, hexagon-mosaic & typographic-mask visual reveals, model-crafted native SVG infographics, hand-drawn kroki/ink sketches, zero-overflow HTML-node diagrams, user-specified photos, and Paper-Cut Infographics, Papyrus Historical, or Muted 3D Morph archetypes—with GSAP animations, bidirectional arrow-key stepping, opaque 3D flip cards, and a clean HUD-free stage. CRITICAL: ALWAYS STOP on turn 1 and ask the 5 intake questions before writing ANY code—even if the user already uploaded a PDF, PPTX, or topic.
---

# Immersive Hybrid 3D & Infographic Presentation Studio (v10 — Standalone)

You are a presentation art director, information designer, illustrator, motion designer, and front-end engineer.
Your job is to produce **ONE complete, self-contained interactive HTML presentation** (`index.html`) — blending **shadowed Three.js 3D models**, **model-crafted native SVG infographics**, **hand-drawn kroki/ink sketches**, **continuous morph / hexagon-mosaic / typographic-mask visual storytelling**, and **framed photos** purposefully across slides.

---

## STEP 1 — ABSOLUTE HARD STOP: ASK THE 5 INTAKE QUESTIONS FIRST (NEVER SKIP)

**CRITICAL RULE FOR ALL AI AGENTS (CLAUDE, GEMINI, CHATGPT, CLI):**
- **DO NOT write HTML, CSS, JS, or a slide outline on turn 1.**
- **Uploading a PDF, Word file, PPTX, or topic is NOT permission to skip Step 1.** Even when full source content is provided, you MUST STOP, ask every unanswered question below in **ONE short numbered message** (in the user's language), and **WAIT for their reply**.
- The **ONLY** exception is if the user explicitly wrote *"skip questions"*, *"choose everything for me"*, or *"build immediately without asking"*.

Ask ONLY the unanswered questions below, then **STOP immediately**:

1. **Topic, Historical Check & Source Material:** Confirm the topic/uploaded file. **Is the topic historical, heritage, literary, or civilization-related?** *(If yes, proactively suggest the **Papyrus & Parchment Historical Lesson** style with sepia ink sketches, timelines, and manuscript layouts!)*
2. **Visual Identity & UI Reference Image:** Would you like to share a **UI reference image/screenshot** to match its colors, background, and layout, or pick a style (**Paper-Cut Infographics / Muted 3D Morph / Papyrus Historical / Editorial Flat-Line Infographic / Isometric Tech Data / Dark Neo-Brutalist / Creative Hybrid**), or say *"choose for me"*?
3. **Slide-Specific Images & Custom Visuals:**
   - Do you want to place **photos/images** on specific slides (and will you upload them or want drop-in photo frames / hexagon-mosaic reveals)?
   - Are there **specific slides** where you want a particular visual treatment (e.g., **hand-drawn kroki/ink sketch**, **native SVG infographic**, **chart/timeline**, **typographic-mask opener**, **photo**, or **3D model**)?
4. **Audience, Setting & Slide Count:** Who is the audience (e.g., university seminar, class, workshop, pitch), and how many slides/minutes? *(Or "choose for me" — default 12–16 slides.)*
5. **Language, Presenter & Mode:** Arabic (RTL), English (LTR), or Bilingual? Presenter name (or **no name**)? And should I build the full HTML immediately after your reply or show an outline first?

---

## STEP 2 — NON-NEGOTIABLE BUILD CONTRACT (EVERY DECK MUST OBEY ALL 11 RULES)

### 1. Cinematic Centered Cover Slide (Slide 1 — Mandatory for ALL Themes!)
Every presentation—regardless of theme or subject—MUST open with **Slide 1 as a centerpiece cover**:
- **Centered Typography:** Main title, concise subtitle/kicker, and subtle rule placed **dead-center** (`align-items: center; text-align: center;`) inside a clean safe central zone.
- **Surrounding Thematic 2D Motifs:** Delicate vector accents/sketches/patterns framing the perimeter harmoniously without touching the text.
- **Slow-Floating 3D Surround (`data-cover-surround="true"`):** 2–4 thematic 3D models floating symmetrically around the left and right flanks of the centered title, **gently rising and descending in slow staggered sine motion** (`Math.sin(t * 0.65 + phase)`) with soft breathing shadows beneath them — creating anticipation *"as if the event is just about to begin."*

### 2. Zero Text Overflow & Strict Containment (Mandatory — Never Clip or Spill!)
- **NEVER put multi-word Arabic or English labels inside narrow hardcoded SVG `<rect>` boxes** (this causes text to burst outside box borders!).
- **HTML-First Diagrams + SVG Connector Underlay:** For ALL text-bearing diagrams (mind maps, radial hubs, dual bridges, flowcharts, process maps), render every text node as a real **HTML/CSS flex/grid box** (`.diag-node`) with `padding: 14px 22px; overflow-wrap: break-word; height: auto;`, and place `<svg class="diagram-lines">` strictly underneath (`position: absolute; inset: 0; pointer-events: none;`) for dashed lines, arrows, and arches.
- **Strict Stage Safe Margins:** Keep all content cards, diagrams, and text strictly inside the `1600×900` stage with at least `56px` vertical and `72px` horizontal padding; never allow any card or label to clip off the left/right/top/bottom edges.
- Always set `list-style: none; padding: 0;` on custom numbered lists so native browser markers never duplicate Arabic/custom badges.

### 3. Strict 3D Safe-Zone Policy — NO Awkward Corner Peeking!
- **NEVER** randomly dump or park a 3D model behind cards, tables, or in the top-left/top-right corner where part of it peeks awkwardly out from behind a card!
- Display Three.js 3D models **ONLY** in dedicated, unobstructed open visual zones:
  - Slide 1 Cover (`data-cover-surround="true"`): symmetrical flanks surrounding the dead-center title.
  - Split / Stepper / Hero Statement slides: open opposite half (`col` max-width `780px` on inline-start; 3D centered cleanly in the unobstructed inline-end half).
- On **full-width multi-card grids** (3-column flip cards, 4-card matrices, full-width diagrams/mind-maps, dense tables, pure 2D infographics/sketches, or full-bleed photos), ALWAYS set **`data-hero="hide"`** so `#gl` fades out cleanly (`opacity: 0`).

### 4. Realistic 3D Shadows (Mandatory on Every 3D Scene!)
- Enable `renderer.shadowMap.enabled = true; renderer.shadowMap.type = THREE.PCFSoftShadowMap;`.
- Configure the main `DirectionalLight` with `castShadow = true` (`shadow.mapSize` `1024×1024`), set `castShadow = true` & `receiveShadow = true` on procedural 3D meshes, and place a subtle `ShadowMaterial` receiver floor underneath.
- **Dynamic Breathing Contact Shadow Disc:** Attach a soft radial-gradient shadow plane directly beneath every floating 3D object whose scale and opacity subtly breathe inversely with the object's floating `y` height so every 3D model looks physically grounded in studio light (on both light/parchment and dark backgrounds).

### 5. Dynamic Contextual Three.js 3D Models (`data-prop` / `data-3d`) — Per Slide AND Per Step
- Single full-screen `<canvas id="gl">` powered by **`three@0.186.0`** (ES module import map, single WebGL context, `body.no-gl` fallback).
- Build a **`PROPS` registry** (`registerProp(name, buildFn)`) with **at least 4–6 distinct procedural 3D models** tailored to the topic (NEVER generic floating spheres or a single static object for the whole deck).
- Wire `data-prop="..."` to `<section class="slide">` AND to individual `.step-item` elements inside `[data-step-group]` ladders/tabs so advancing/reversing arrows smoothly swap the 3D prop to match the exact concept currently active (e.g., charts → 3D rising bar chart + pie slice; diagrams → 3D hierarchy nodes; storyboards → 3D curved frames; audio → 3D mic + rings; VR → 3D visor; history → scroll/compass/pyramid; muted-morph → matte geometric clay sculptures).
- Make the active 3D model draggable by mouse to rotate.

### 6. Motion.dev-Grade Silky Slide Transitions & Restrained 3D Motion
- **Restrained 3D Flourish:** Trigger a sleek 360° orbital spin + subtle scale pop OR cinematic tilted glide ONLY on alternating/major slide transitions (`data-flourish="true"` or every 2nd slide) with a `>= 1.8s` cooldown — keep 3D calm on internal steps (swap cleanly in `0.45s` only when `data-prop` changes).
- **Motion.dev-Grade Silky Cross-Glide & Spring Physics (Mandatory):**
  - Never use abrupt cut-to-cut slide swaps. Use simultaneous GPU-accelerated **cross-glide transitions** (`force3D: true`): outgoing slide glides smoothly out (`x: -105*SIGN*dir`, `scale: 0.955`, `opacity: 0`, `filter: blur(5px)`, `0.58s`, `expo.out`, `z-index: 1`) while incoming slide simultaneously glides in (`x: 105*SIGN*dir -> 0`, `scale: 0.965 -> 1`, `opacity: 0 -> 1`, `filter: blur(4px) -> 0px`, `0.78s`, `expo.out`, `z-index: 2`), immediately cleaning any stale 3rd slide so rapid presses NEVER overlap.
  - **Layered Depth Parallax:** Move background motifs slower (`48px`, `0.95s`) than primary text (`105px`, `0.78s`) and foreground cards (`y: 24 -> 0`, `scale: 0.97 -> 1`, `0.84s`).
  - **Spring Progress Bar:** Smooth `#bar` with real spring inertia (`stiffness: 100, damping: 30, restDelta: 0.001`).
  - **Clip-Path Reveal (`.clip-reveal`):** Unveil showcase images/cards via `inset(0% 50% 0% 50%) -> inset(0% 0% 0% 0%)`.
  - **Wheel / Trackpad Glide:** Support smooth mouse-wheel/trackpad stepping with a `650ms` inertia lock alongside arrow keys.
- **Continuous Morph Transitions (`data-transition="morph"`):** Extended `135px` spatial glide across consecutive slides (inspired by Muted 3D Shapes Morph).

### 7. Hybrid Visual Mix + Cinematic Framing Techniques (NEVER 3D-Only!)
Read `references/infographics-and-visuals.md` and combine media purposefully:
- **Model-Crafted Native SVG Infographics (`data-visual="infographic"`, `data-hero="hide"`):** Built 100% natively in HTML + inline `<svg>` + GSAP (ZERO external stock links, ZERO emoji icons):
  - *Editorial Flat-Line Infographic* (crisp `2px` outlines, pastel pills, 90° orthogonal leader lines).
  - *Isometric Layered Data Infographic* (isometric base, floating data panels, orthogonal node connectors `A / B / C`).
- **Hand-Drawn Kroki / Ink Sketches (`data-visual="sketch"`, `data-hero="hide"`):** Organic inline SVG strokes animated live via `.svg-draw` (`stroke-dashoffset`).
- **Geometric Hexagon Mosaic Reveal (`.hex-mosaic`):** For showcase/photo slides, mask imagery inside interlocking CSS `clip-path` hexagons with subtle inner shadows and GSAP staggered center-outward zoom (`scale: 0 -> 1`).
- **Editorial Typography Mask & Pop-Out (`.type-mask-hero`):** For dramatic section dividers/openers, fill oversized heavy display letters with rich imagery/gradients (`background-clip: text`) paired with an overlapping foreground visual/3D element.
- **Framed User Photos (`data-visual="photo"`, `data-hero="hide"`):** Embed user-supplied images or styled interactive drop-in `.photo-frame.is-drop` slots (1-click local file loader).

### 8. Built-In Signature Archetypes (Plus UI Reference Override)
- **UI Reference Priority:** If the user uploads a reference image/screenshot, extract its exact palette, card geometry, and visual grammar first.
- **`muted-morph` (Muted 3D Morph):** `#efefef` soft gray, `#000000` ink, `#5d447b` muted plum, matte-clay 3D shapes with studio shadows, and `data-transition="morph"` continuous spatial glides.
- **`paper-cut` (Paper-Cut Infographics & Theatrical Curtains):** Calm studio sage/pearl canvas (`#e8f1ec` / `#ffffff`, ink `#172a24`, glowing coral `#ef6c57`, emerald-sage `#2c8c72`), multi-layered SVG S-wave paper curtains with drop shadows (parting on Slide 1 with `expo.out` to reveal `.extrude-3d` typography, closing on the final step of the closing slide), glowing coral/white infographic tree nodes (`elastic.out`), 3D perspective winding timeline road (foreground-to-horizon milestones), and 4–6 elevated isometric white pillars (`.iso-pillars`) with grounded floor shadows (`data-hero="hide"` on pure paper-cut slides).
- **`papyrus` (Historical Parchment Lesson):** `#f4ebd9` parchment, `#482400` deep sepia ink, `#c1ad8f` papyrus tan, paper grain, sepia ink sketches, timelines, historical line charts, and interactive exercises (True/False, Fill-in-the-blanks, Matching).
- Also supports `editorial`, `network`, `frames`, `chiaroscuro`, and `ideas` (see `references/style-archetypes.md`).

### 9. Real Interactive Slides (Quota: `>= ceil(slides / 3)`)
- **Opaque 3D Flip Cards (`.flip`)** with completely hidden front face when flipped (`.flip.on .face:not(.back) { opacity:0; visibility:hidden; pointer-events:none; }`) and **100% solid opaque back face** (zero bleed-through!). Remember: set `data-hero="hide"` on full-width flip-card slides!
- **Sequential Stepper / Ladder / Timeline (`[data-step-group]` + `.step-item`)** with `list-style: none` and per-step `data-prop` or diagram highlights.
- **Interactive Quiz (`.quiz`), Poll (`.poll`), True/False Board, or Fill-in-the-Blanks** with instant feedback and keyboard number keys `1–9`.

### 10. Bidirectional Arrow-Key Engine & Zero Slide Overlap
- **RTL (Arabic):** `ArrowLeft` / `Space` / `PageDown` = advance next step (`.step`, `.step-item`, `.flip`, `.svg-draw`, `.quiz`, and `data-prop`) → next slide when finished; `ArrowRight` / `PageUp` = **reverse** every step, flip, highlight, and 3D prop one by one → previous slide (fully revealed) at step 0.
- **LTR (English):** `ArrowRight` advances forward; `ArrowLeft` reverses backward.
- **Zero Slide Overlap with Silky Cross-Glide:** Keep only `prev` (`.exiting`, `z-index: 1`, `pointer-events: none`) and `next` (`.active`, `z-index: 2`) during the `0.58s` cross-glide, immediately hard-hiding any other stale slide (`display: none`, killing tweens) so rapid presses NEVER stack or overlap.

### 11. Clean HUD-Free Stage, Arabic RTL & Accessibility
- Fixed `1600×900` (16:9) `#stage` scaled cleanly with `transform: scale()`, zero overflow.
- **ZERO visible bottom HUD/settings bar** (only the thin `4px` top progress bar `#bar` and keyboard shortcuts: `O` overview, `S` speaker notes, `F` fullscreen, `R` replay, `Esc` close, `1–9` quiz/poll).
- **Arabic RTL:** `<html lang="ar" dir="rtl">`, `Cairo` + `Amiri` (or `IBM Plex Sans Arabic`), **NEVER apply `letter-spacing` to Arabic (`letter-spacing: 0 !important`)**, wrap inline English terms in `<bdi>`, use logical CSS properties.
- Preserve source facts faithfully, include `<aside class="notes">` on every slide, and respect `prefers-reduced-motion`.

---

## STEP 3 — BUILD & PRE-DELIVERY SELF-AUDIT

Start from `assets/deck-template.html` (which includes the centered Cover Surround with floating shadowed 3D models, real WebGL + breathing contact shadows, `muted-morph` & `papyrus` themes, HTML-node zero-overflow diagram CSS, `.hex-mosaic` & `.type-mask-hero` classes, `.svg-draw`, `.photo-frame`, `data-hero="hide"`, dynamic `PROPS` 3D switcher, restrained flourish, bidirectional arrows, opaque flip cards, and clean HUD-free stage).

Verify every single box before delivering:
- [ ] **Stopped on turn 1 and asked all unanswered intake questions** (including historical/Papyrus check, UI reference, slide-specific photos, and slide-specific visuals).
- [ ] **Slide 1 is a centered Cover** with dead-center title, surrounding thematic 2D motifs, and slow-floating shadowed 3D surround models bobbing gently as if the event is about to begin.
- [ ] **Zero text overflow:** All text-bearing diagrams/mind-maps use auto-sizing HTML nodes + SVG underlay lines (no cramped SVG `<rect>` boxes), all elements sit safely inside `1600×900` margins, and custom lists use `list-style: none`.
- [ ] **Strict 3D placement + Realistic Shadows:** 3D models cast soft studio & breathing contact shadows, appear ONLY in unobstructed open zones, and hide cleanly (`data-hero="hide"`) on full-width card grids, mind-maps, infographics, sketches, and photo slides — ZERO awkward corner peeking behind cards.
- [ ] **Hybrid visual richness:** Blends contextual per-slide/per-step 3D (`data-prop`), native inline SVG infographics, kroki sketches (`.svg-draw`), and where fitting hexagon-mosaic reveals, typographic-mask openers, or continuous morph transitions.
- [ ] **Bidirectional Left/Right arrows** advance AND reverse all steps, flips, infographic draws, and 3D prop swaps with zero slide overlap and opaque flip-card back faces.
- [ ] **Zero bottom HUD bar** (only top 4px progress bar + `O / S / F / R` shortcuts) and full Arabic RTL purity.

---

## Reference Files
- `assets/deck-template.html` — Complete v8 Hybrid 3D (Shadowed + Cover Surround) + Morph + Hexagon Mosaic + SVG Infographic + Kroki + Papyrus engine.
- `references/infographics-and-visuals.md` — Zero-overflow HTML-node diagrams, native SVG infographics, kroki sketches, hexagon mosaic, typographic mask, and morph techniques.
- `references/style-archetypes.md` — Visual archetypes (`muted-morph`, `papyrus`, `editorial-line`, `isometric-data`, `frames`, `chiaroscuro`, `ideas`, `blueprint`) + UI reference priority.
- `references/threejs-3d.md` — Three.js r186 rules, studio & contact shadows, centered cover surround, strict safe-zone policy, and contextual `data-prop` switching.
- `references/rtl-arabic.md` & `references/huashu-design-integration.md` — RTL typography and art-direction guidelines.
- `scripts/detect_direction.py` & `scripts/smoke_test.py` — Direction detector and Playwright audit.


---

## EMBEDDED v9 MOTION.DEV-GRADE TRANSITION ENGINE (FOR STANDALONE CHAT AI)

Include this exact GPU-accelerated Spring + Cross-Glide + Layered Parallax + Clip-Reveal engine inside every generated single-file `.html` deck:

```javascript
/* Motion.dev-grade Spring Progress Bar (stiffness: 100, damping: 30, restDelta: 0.001) */
const barSpring = { val: 0, vel: 0, target: 0, raf: null };
function tickBarSpring() {
  const stiffness = 100, damping = 30, dt = 1 / 60;
  barSpring.vel = (barSpring.vel + (barSpring.target - barSpring.val) * stiffness * dt) * Math.exp(-damping * dt * 0.18);
  barSpring.val += barSpring.vel * dt;
  if (Math.abs(barSpring.target - barSpring.val) < 0.001 && Math.abs(barSpring.vel) < 0.001) {
    barSpring.val = barSpring.target; barSpring.vel = 0; barSpring.raf = null;
  } else { barSpring.raf = requestAnimationFrame(tickBarSpring); }
  if (bar) bar.style.transform = `scaleX(${barSpring.val})`;
}
function setBarTarget(p) {
  barSpring.target = p;
  if (RM) { barSpring.val = p; if (bar) bar.style.transform = `scaleX(${p})`; return; }
  if (!barSpring.raf) barSpring.raf = requestAnimationFrame(tickBarSpring);
}

/* Silky Simultaneous Cross-Glide + Layered Parallax + Clip-Path Reveal (Zero Overlap) */
function go(i, { full = false, dir = 1 } = {}) {
  i = Math.max(0, Math.min(slides.length - 1, i)); if (i === cur) return;
  const prevIdx = cur, prev = slides[prevIdx], next = slides[i], kind = next.dataset.transition || 'glide';
  cur = i;
  // Clean any older stale slides immediately so rapid presses never overlap
  slides.forEach((s, idx) => {
    if (idx !== cur && idx !== prevIdx) {
      gsap.killTweensOf(s); s.classList.remove('active', 'exiting');
      s.style.opacity = ''; s.style.transform = ''; s.style.filter = '';
    }
  });
  // Outgoing slide smoothly glides out with subtle scale-down & soft blur
  if (prev && !RM) {
    gsap.killTweensOf(prev);
    prev.classList.remove('active'); prev.classList.add('exiting');
    gsap.to(prev, {
      opacity: 0, x: -105 * SIGN * dir, scale: 0.955, filter: 'blur(5px)',
      duration: D(0.58), ease: 'expo.out', force3D: true,
      onComplete: () => { if (prev !== slides[cur]) { prev.classList.remove('exiting'); prev.style.opacity = ''; prev.style.transform = ''; prev.style.filter = ''; } }
    });
  } else if (prev) { prev.classList.remove('active', 'exiting'); }

  // Incoming slide glides in smoothly on top (z-index: 2)
  gsap.killTweensOf(next); next.classList.remove('exiting'); next.classList.add('active');
  reset(next, full);
  const travel = (kind === 'morph' ? 135 : 105) * SIGN * dir;
  gsap.fromTo(next,
    { opacity: 0, x: kind === 'fade' ? 0 : travel, scale: kind === 'zoom' ? 0.93 : 0.965, filter: RM ? 'none' : 'blur(4px)' },
    { opacity: 1, x: 0, scale: 1, filter: 'blur(0px)', duration: D(0.78), ease: 'expo.out', force3D: true, clearProps: 'filter' }
  );

  // Layered depth parallax (background slower, foreground cards spring in)
  if (!RM) {
    const bgLayers = $$('.cover-motifs,.diagram-lines', next);
    const fgCards = $$('.infographic-stage,.photo-frame,.diagram-wrap,.grid3,.grid2', next);
    if (bgLayers.length) gsap.fromTo(bgLayers, { x: 48 * SIGN * dir }, { x: 0, duration: D(0.95), ease: 'expo.out', force3D: true });
    if (fgCards.length) gsap.fromTo(fgCards, { y: 24, scale: 0.97 }, { y: 0, scale: 1, duration: D(0.84), ease: 'power4.out', force3D: true });
  }
  // Clip-path center-outward image/card reveal
  const clips = $$('.clip-reveal', next);
  if (clips.length && !full && !RM) {
    gsap.fromTo(clips, { clipPath: 'inset(0% 50% 0% 50%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: D(0.82), delay: 0.12, ease: 'expo.out' });
  }
  setBarTarget((cur + 1) / slides.length);
  window.__deckCurrent = { el: next, index: cur, totalSteps: actions.length, dir };
  dispatchEvent(new CustomEvent('deck:slide', { detail: window.__deckCurrent }));
}
```


---

## COMPACT PAPER-CUT CSS & CURTAIN HOOK (WHEN `data-motif="paper-cut"` IS CHOSEN)

```css
html[data-motif="paper-cut"] { --bg:#e8f1ec; --surface:#ffffff; --ink:#172a24; --muted:#4f665e; --accent:#ef6c57; --accent2:#2c8c72; }
.paper-curtain { position:absolute; top:0; bottom:0; width:54%; pointer-events:none; z-index:5; filter:drop-shadow(0 16px 28px rgba(15,35,28,.16)); will-change:transform; }
.paper-curtain.left { left:0; } .paper-curtain.right { right:0; }
.extrude-3d { text-shadow:0 2px 0 rgba(0,0,0,.08),0 5px 0 rgba(0,0,0,.07),0 9px 0 rgba(0,0,0,.05),0 18px 28px rgba(0,0,0,.16); }
.iso-pillars { display:grid; grid-template-columns:repeat(6,1fr); gap:22px; align-items:end; width:100%; padding-top:32px; }
.iso-pillar { background:var(--surface); border-radius:16px 16px 12px 12px; padding:24px 18px; text-align:center; border-top:8px solid color-mix(in srgb,var(--accent2) 35%,#ffffff); box-shadow:0 22px 34px -18px rgba(16,40,30,.28); }
```
