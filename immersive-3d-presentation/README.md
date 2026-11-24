# Immersive Hybrid 3D & Infographic Presentation Studio (v10)

A complete skill & plugin package for building art-directed, interactive HTML presentations (RTL Arabic, LTR English, and Bilingual) combining:
- **Cinematic Centered Cover Slide (Slide 1):** Dead-center title framed by thematic 2D motifs and slow-floating shadowed 3D surround models bobbing gently as if the event is about to begin.
- **Realistic 3D Studio & Breathing Contact Shadows:** WebGL `PCFSoftShadowMap` shadows + dynamic radial contact shadow discs that soften and contract as 3D models float.
- **Strict 3D Safe-Zone Policy:** 3D models appear ONLY in dedicated unobstructed zones and cleanly hide (`data-hero="hide"`) on full-width card grids, mind maps, infographics, sketches, and photos — zero awkward peeking behind cards.
- **Zero-Overflow HTML-Node Diagrams:** Auto-wrapping HTML/CSS nodes over an SVG connector underlay so Arabic and English text NEVER spills outside rounded boxes or clips past card edges.
- **Dynamic Per-Slide & Per-Step 3D Props (`data-prop` / `data-3d`):** 4–6 custom procedural Three.js models swapping smoothly as you navigate slides and ladder/stepper items.
- **Paper-Cut Infographics & Theatrical Curtains (`paper-cut`):** Multi-layered S-wave paper curtains with drop shadows, glowing infographic tree nodes, 3D perspective winding timeline road, and 6 isometric elevated pillars.
- **High-Craft Visual Techniques:** Continuous Morph transitions (`muted-morph` archetype), Hexagon Mosaic staggered image reveals (`.hex-mosaic`), Editorial Typography Masks (`.type-mask-hero`), Model-Crafted Native SVG Infographics, Hand-Drawn Kroki Sketches (`.svg-draw`), and Papyrus Historical Manuscript mode (`papyrus`).
- **Motion.dev-Grade Silky Transitions:** Simultaneous GPU cross-glide (`expo.out` + subtle blur/scale handoff), layered depth parallax, spring-damped progress bar (`stiffness: 100, damping: 30`), `.clip-reveal` image unveils, and inertia-locked wheel/trackpad stepping.
- **Clean HUD-Free Stage & Bidirectional Arrow Stepping:** Zero bottom control bar, opaque 3D flip cards, and full forward/reverse arrow-key control.

## Install (Claude Code / OpenCode / Gemini CLI)

```bash
mkdir -p ~/.claude/skills
unzip immersive-3d-presentation-v10.zip -d ~/.claude/skills/
```

- Includes `references/paper-cut.md` as a modular style recipe.
