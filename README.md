# Immersive 3D Presentation Skill (v10)

An AI agent skill & plugin for generating **single-file, interactive, 3D-enhanced HTML presentations** (RTL Arabic, LTR English, and Bilingual) with Three.js contextual 3D models, Motion.dev-grade spring & cross-glide transitions, Paper-Cut theatrical infographics, Papyrus historical manuscripts, native SVG infographics, opaque 3D flip cards, and a clean HUD-free stage.

## Key Features
- **Mandatory 5-Question Intake Gate:** Always asks for topic/historical check, visual style or UI reference image, slide-specific images/visuals, audience & length, and language/presenter before generating code.
- **Motion.dev-Grade Transitions (v9+):** Simultaneous GPU-accelerated cross-glide (`expo.out` + subtle scale & motion blur), real spring-damped progress bar (`stiffness: 100, damping: 30`), layered depth parallax, `.clip-reveal` unveils, and inertia-locked wheel/trackpad navigation.
- **Dynamic Shadowed Three.js 3D Models (`data-prop` / `data-3d`):** 4–6 procedural 3D models swapping per slide and per step, realistic `PCFSoftShadowMap` + breathing contact shadows, centered floating Cover Surround on Slide 1, and automatic `data-hero="hide"` on full-width grids/infographics.
- **Modular Style Archetypes:**
  - `paper-cut` — Paper-Cut S-wave curtains, glowing infographic tree, 3D perspective timeline road, and 6 isometric pillars (`references/paper-cut.md`).
  - `muted-morph` — Minimalist matte-clay 3D shapes with continuous spatial morph transitions.
  - `papyrus` — Aged parchment historical lessons with sepia ink sketches, timelines, and interactive exercises.
  - `editorial` & `isometric-data` — Model-crafted native inline SVG infographics (zero external stock links).
- **Zero Text Overflow & Clean Stage:** HTML-first auto-wrapping diagram nodes over SVG connector lines, opaque 3D flip cards, bidirectional arrow-key stepping, and zero visible bottom HUD bar (`O`, `S`, `F`, `R`, `Esc`, `1–9`).

## Repository Structure

```text
immersive-3d-presentation-skill/
├── README.md                              # Main GitHub documentation
├── standalone/
│   └── SKILL.md                           # Single-file version for Gemini & Web Chat AI
└── immersive-3d-presentation/             # Modular Plugin for Claude / OpenCode / Gemini CLI
    ├── SKILL.md
    ├── MERGE-NOTES.md
    ├── README.md
    ├── assets/
    │   └── deck-template.html
    ├── references/
    │   ├── paper-cut.md
    │   ├── infographics-and-visuals.md
    │   ├── style-archetypes.md
    │   ├── threejs-3d.md
    │   ├── rtl-arabic.md
    │   └── huashu-design-integration.md
    └── scripts/
        ├── detect_direction.py
        └── smoke_test.py
```

## Installation

### Option A — Claude Code / OpenCode / Gemini CLI (Modular Plugin)
```bash
git clone https://github.com/mustafasalem222/immersive-3d-presentation-skill.git
cp -r immersive-3d-presentation-skill/immersive-3d-presentation ~/.claude/skills/
```

### Option B — Gemini / Web Chat AI (Single-File Standalone)
Copy or upload `standalone/SKILL.md` directly into your Gem, Custom Instructions, or Chat AI skill uploader.
