Merged package: original user-provided immersive-presentation files retained; main SKILL.md rewritten to integrate selected Huashu Design workflows. No Huashu source code/assets were copied. See references/huashu-design-integration.md for scope and attribution.


## v2 Updates
- Removed the visible bottom HUD/settings control bar for a clean full-screen stage (keyboard & swipe navigation retained).
- Upgraded navigation to bidirectional arrow-key animation control (RTL: Left advances animations/steps/flips/ladders, Right reverses them step-by-step before going to the previous slide).
- Fixed CSS 3D flip-card back face clarity: solid opaque back face + hidden front face on flip so front-face background/text never bleeds through.
- Added an explicit Step 1 prompt asking if the user wants to provide a UI reference image/screenshot to match colors, background, imagery, and layout style.

## v3 Updates
- Mandated topic-expressive procedural 3D models (e.g. game controller + ✕ ○ △ □ for gamification, subject-specific props for every topic) instead of generic abstract shapes.
- Added slide-synchronized 3D choreography (`data-cam`, `data-hero`, `data-rot`, directional slide-transition spin impulse, and `deck:step` micro-reactions) so 3D models visibly move and reframe whenever slides move.
- Hardened slide transitions in `deck-template.html` to immediately hide inactive slides and prevent any visual slide overlap.

## v4 Updates (High-Compliance Context Rewrite + Restrained 3D Flourish)
- Compressed and restructured `SKILL.md` from ~27 KB to ~8 KB with an unmistakable STEP 1 HARD STOP (mandatory onboarding questions before coding) and a 7-point Non-Negotiable Build Contract so any AI agent reliably builds the full Three.js 3D models, opaque 3D flip cards, bidirectional arrow engine, UI reference matching, and clean no-HUD stage instead of defaulting to a plain slideshow.
- Upgraded `assets/deck-template.html` 3D director with a **restrained stylish flourish** on arrow-key slide transitions (alternating crisp 360° orbital spin + scale pop and cinematic bank-and-lift every 2nd slide or `data-flourish="true"` with a 1.8s cooldown, while staying calm during internal bullet steps).

## v5 Updates (Airtight Step 1 Gate + Dynamic Contextual 3D Props)
- Hardened `STEP 1 — ABSOLUTE HARD STOP` in both YAML frontmatter `description` and top of `SKILL.md` so Claude and other AI agents ALWAYS stop and ask the 4 onboarding questions first even when a PDF/source is uploaded.
- Added Dynamic Contextual 3D Prop Switching (`registerProp` + `data-prop="..."` on both `<section class="slide">` and individual `.step-item` elements) so the 3D scene swaps smoothly to match each specific slide or active step (e.g., 3D bar chart when discussing charts, 3D flowchart nodes when discussing diagrams, 3D storyboard frames when discussing sequential visuals).
- Fixed `.ladder` CSS (`list-style: none; padding: 0;`) to prevent duplicate browser numbering alongside Arabic step badges.

## v6 Updates (Complete Synchronized Plugin Package)
- Synchronized `README.md`, `references/style-archetypes.md`, `references/threejs-3d.md`, `SKILL.md`, and `assets/deck-template.html` into a unified plugin bundle.
- Added a working Contextual 3D Stepper demo slide (`data-prop="chart" | "diagram" | "storyboard"`) directly inside `assets/deck-template.html` so agents immediately follow the per-step 3D prop switching pattern.

## v7 Updates (Hybrid Visuals, Native SVG Infographics, Slide-Specific Media & Papyrus Historical Archetype)
- Expanded Step 1 Hard-Stop Intake Gate to 5 questions: explicitly asks about **slide-specific images**, **slide-specific custom visual styles** (kroki sketch, infographic, chart, photo, 3D), and **whether the topic is historical** (proactively offering the Papyrus & Parchment Historical Lesson style).
- Added `references/infographics-and-visuals.md` defining **model-crafted inline SVG infographics** (Editorial Flat-Line + Isometric Layered Data), **hand-drawn kroki/ink sketches** (`.svg-draw`), and **framed photo / drop-in image slots** — removing any limitation to 3D-only slides.
- Added the full **`papyrus` Historical Parchment & Ink-Sketch archetype** (derived from `Papyrus History Lesson XL`: `#f4ebd9` parchment, `#482400` deep sepia ink, `#c1ad8f` papyrus tan, paper grain, sepia sketches, timelines, historical data charts, and interactive exercises) to `references/style-archetypes.md` and `assets/deck-template.html`.
- Added automatic `data-hero="hide"` WebGL handoff in `assets/deck-template.html` so 2D infographics, sketches, and photos own the stage cleanly without colliding with Three.js.

## v8 Updates (Zero-Overflow Diagrams, 3D Studio Shadows, Centered Floating Cover, Strict 3D Safe-Zones & Motion Techniques)
- **Zero Text Overflow:** Replaced narrow SVG `<rect>+<text>` diagram patterns with HTML-first auto-wrapping `.diag-node` boxes over `<svg class="diagram-lines">` underlays + strict `1600×900` safe margins.
- **Strict 3D Safe-Zones:** Eliminated awkward 3D corner peeking behind full-width flip-card/grid slides by enforcing `data-hero="hide"` on full-width grids and limiting 3D models strictly to unobstructed zones.
- **Real 3D Shadows:** Added `PCFSoftShadowMap` directional shadows, invisible `ShadowMaterial` floor catchers, and dynamic breathing radial contact shadow discs beneath every floating 3D object.
- **Cinematic Centered Cover (Slide 1):** Standardized Slide 1 across all themes as a dead-center cover surrounded by 2D motifs and slow-floating shadowed 3D surround models (`data-cover-surround="true"`).
- **Motion & Archetype Expansion:** Integrated **Hexagon Mosaic staggered zoom reveals** (`.hex-mosaic`), **Editorial Typography Masks** (`.type-mask-hero`), and the **`muted-morph`** minimalist 3D continuous-morph archetype (`#efefef` / `#000000` / `#5d447b`).

## v9 Updates (Motion.dev-Grade Spring Physics & Silky Cross-Glide Parallax Transitions)
- Upgraded slide transitions in `assets/deck-template.html` and `SKILL.md` to match Motion.dev (`motion.dev/docs/react-scroll-animations`) smoothness:
  - Simultaneous GPU-accelerated cross-glide (`expo.out`, subtle scale + soft motion blur handoff) with stale-slide cleanup for zero overlap even on rapid key presses.
  - Real spring-physics top progress bar (`stiffness: 100, damping: 30, restDelta: 0.001`).
  - Multi-layer depth parallax on slide entry (background motifs slower than primary text and foreground cards).
  - Center-outward `.clip-reveal` (`inset(0% 50% 0% 50%) -> inset(0% 0% 0% 0%)`) for showcase images and cards.
  - Inertia-locked wheel/trackpad navigation (`650ms` cooldown) alongside bidirectional arrow keys and touch swipe.

## v10 Updates (Paper-Cut Infographics & Theatrical Curtains Archetype)
- Added the **`paper-cut`** archetype (`data-motif="paper-cut"`) to `SKILL.md`, `references/style-archetypes.md`, `references/infographics-and-visuals.md`, and `assets/deck-template.html`:
  - Multi-layered S-wave paper-cut curtains (`.paper-curtain`) with realistic cast shadows that part on opening and close on the final step.
  - Extruded 3D display typography (`.extrude-3d`), glowing coral/white infographic tree nodes (`elastic.out`), 3D perspective winding timeline road, and 6 isometric elevated pillars (`.iso-pillars` / `.iso-pillar`).
