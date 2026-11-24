# Paper-Cut Infographics & Theatrical Curtains (`data-motif="paper-cut"`)

Use this modular style recipe whenever the user selects **Paper-Cut Infographics** (or wants a tactile, theatrical, layered-cardstock presentation for keynotes, roadmaps, or multi-pillar frameworks).

---

## 1. Visual Tokens & Palette
- **Canvas (`--bg`):** `#e8f1ec` (calm studio sage-mist) or `#f3f6f5` (pearl cardstock).
- **Card / Paper Layers (`--surface`):** `#ffffff`, `#f2f5f4`, `#e4ebe8` stacked with directional drop shadows (`filter: drop-shadow(0 16px 28px rgba(15,35,28,0.16))`).
- **Ink (`--ink` / `--muted`):** `#172a24` deep forest charcoal / `#4f665e` muted slate-sage.
- **Accents (`--accent` / `--accent2`):** `#ef6c57` glowing coral (focal nodes & active highlights) + `#2c8c72` emerald-sage (structural caps & secondary callouts).
- **WebGL Coordination:** Set `data-hero="hide"` on pure paper-cut SVG slides so layered paper shadows and extruded typography stay razor-sharp.

---

## 2. Five Signature Paper-Cut Slide Patterns

### Pattern A — Theatrical S-Wave Curtain Opening & Closing
- **Markup:** Place two multi-layered SVG S-curve curtains (`.paper-curtain.left` and `.paper-curtain.right`, 3 offset white/silver wave paths each) above the centered title.
- **Extruded 3D Type:** Apply `.extrude-3d` (`text-shadow: 0 2px 0 rgba(0,0,0,.08), 0 5px 0 rgba(0,0,0,.07), 0 9px 0 rgba(0,0,0,.05), 0 18px 28px rgba(0,0,0,.16)`) to the main greeting/closing headline.
- **Animation:**
  - *Opening (Slide 1):* Part curtains outward (`xPercent: -100` / `+100`, `duration: 1.15s`, `ease: 'expo.out'`) to reveal the centered title.
  - *Closing (Final Slide):* Bind the final forward `.step` action to sweep the curtains closed from the corners (and reverse open when pressing the Back arrow).

### Pattern B — Glowing Infographic Tree (`[data-step-group]`)
- **Visual:** Central minimalist SVG trunk & symmetrical branches with 6 circular nodes (alternating luminous white and glowing coral `filter: drop-shadow(0 0 14px rgba(239,108,87,0.65))`).
- **Sync:** Each arrow-key step pops the next node elastically (`scale: 0 -> 1`, `duration: 0.7s`, `ease: 'elastic.out(1, 0.55)'`) while highlighting its corresponding HTML talking-point card (auto-wrapping, zero text overflow).

### Pattern C — 3D Perspective Winding Timeline Road
- **Visual:** A crisp white perspective-tapered SVG `<path>` road curving from wide foreground at the bottom to a narrow horizon point near the top, with dashed center markings.
- **Milestones:** 4–6 chronological pins/cards positioned along the curve with progressive perspective scaling (`scale: 1.0` in foreground → `0.78` near horizon), popping in sequentially from foreground to horizon on arrow keys.

### Pattern D — 6 Isometric Elevated Pillars (`.iso-pillars` + `.iso-pillar`)
- **Visual:** 4–6 clean white vertical pedestals on the sage canvas with angled emerald-tinted top caps (`border-top: 8px solid ...`) and soft grounded floor shadows.
- **Motion:** Slide upward sequentially (`y: 64 -> 0`, `opacity: 0 -> 1`, `duration: 0.65s`, `ease: 'expo.out'`) as the presenter steps forward.

### Pattern E — Tactile Paper-Cut Flip Cards / Quiz
- Reuse the standard opaque `.flip` cards and `.quiz` blocks styled with soft multi-layer cardstock shadows (`box-shadow: 0 20px 32px -18px rgba(15,35,28,0.22)`) and coral active borders.
