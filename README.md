<div align="center">

# 🎬 Immersive 3D & Hybrid Presentation Skill (`v8`)

**Build single-file, projector-ready, interactive HTML presentations powered by real-shadow Three.js 3D models, GSAP Morph motion, model-generated SVG infographics, live hand-drawn sketches, and native Arabic RTL / English LTR support.**

![Version](https://img.shields.io/badge/version-8.0-06B6D4?style=for-the-badge)
![Three.js](https://img.shields.io/badge/Three.js-Real%20Shadows-111115?style=for-the-badge&logo=three.js)
![GSAP](https://img.shields.io/badge/GSAP-Morph%20Motion-88CE02?style=for-the-badge)
![RTL & LTR](https://img.shields.io/badge/i18n-Arabic%20RTL%20%7C%20English%20LTR-F59E0B?style=for-the-badge)
![Compatible](https://img.shields.io/badge/AI%20Ready-Claude%20%7C%20Gemini%20%7C%20CLI-7C6EA6?style=for-the-badge)

</div>

---

> ### 🇪🇬 ملخص سريع بالعربية
> مهارة متكاملة لتحويل أي موضوع أو ملف (PDF / PPTX / ملاحظات) إلى **عرض تقديمي تفاعلي في ملف HTML واحد** يجمع بين **المجسمات ثلاثية الأبعاد بظلال واقعية (Three.js)**، و**رسومات الإنفوجرافيك المولّدة بالكود بدون خروج نص خارج الإطارات**، و**الرسومات الكروكية الحيّة بالقلم**، مع **دعم كامل للغة العربية (RTL)**، وتنقّل وتحريك ثنائي الاتجاه بالأسهم، وغلاف سينمائي مركزي موحّد، وبدون أي شريط أزرار يشتّت الجمهور.

---

## ✨ Key Features

### 1. 🛑 Strict 5-Question Pre-Flight Intake Gate
Before writing a single line of code—even if you upload a PDF or PPTX immediately—the AI **stops and asks 5 targeted questions**:
1. **Topic & Historical Mode Detection:** Automatically suggests the **Papyrus Historical Manuscript** theme if the topic is historical or chronological.
2. **UI Reference Image or Archetype:** Accepts any screenshot/reference image to extract its exact palette, typography, and layout motifs—or lets you pick a built-in archetype.
3. **Per-Slide Custom Images & Visual Modes:** Asks if you want to embed specific photos or assign a custom visual style (hand sketch, infographic, timeline, or 3D) to individual slides.
4. **Audience & Slide Count:** Calibrates tone, density, and pacing for seminars, lectures, or executive decks.
5. **Language, Presenter & Build Mode:** Confirms RTL/LTR direction, presenter name (or anonymous), and immediate build vs. outline first.

### 2. 🎯 Mandatory Centered Anticipation Cover (Slide 1)
Across **every** visual archetype, Slide 1 follows a unified cinematic composition:
* **Protected Centered Safe-Zone:** Eyebrow, Display Title, accent divider, and subtitle centered dead-middle.
* **Perimeter 3D & 2D Anticipation:** 3–4 floating Three.js 3D models with soft shadows gently bob up and down in staggered sinusoidal motion around the outer perimeter (never crossing behind the title), creating an *"event is about to begin"* atmosphere.

### 3. 🧊 Real-Shadow Dynamic Three.js 3D Engine (`data-3d`)
* **Context-Aware Per-Slide & Per-Step Props:** Procedural topic-specific 3D models swap seamlessly via `data-3d="propName"` not only between slides, but also as you step through individual list items (e.g., 3D bar charts → 3D flowcharts → 3D storyboards → 3D balance scales).
* **True Studio Shadows:** Every 3D prop casts soft shadows (`PCFSoftShadowMap` + `ShadowMaterial` floor plane) paired with a radial **breathing contact shadow disc** that scales inversely as the object floats.
* **Zero Awkward Peeking:** 3D models only render on the Cover perimeter or inside a dedicated 44% open visual lane. On full-width card grids, infographics, sketches, and photo slides, the WebGL layer fades out cleanly (`is-hidden` / `data-hero="hide"`).
* **Balanced Morph Flourishes:** Tasteful 360° spins or cinematic tilt-lifts trigger only on milestone slides (`data-flourish="true"`) with a `1.8s` cooldown—smooth and classy, never distracting.

### 4. 🎨 Hybrid Visual Engine (Beyond 3D)
Mixes four native visual mediums cleanly inside a single HTML file—with **zero broken external image URLs**:
* **3D Studio Models:** Procedural Three.js scenes with real lighting and shadows.
* **Model-Generated Inline SVG + HTML Infographics:** Editorial flat-line diagrams, isometric glowing data platforms, bridge/ecosystem charts, and animated bars.
* **Live Hand-Drawn Kroki / Ink Sketches:** Organic bezier SVG paths (`.draw-path`) drawn live via GSAP `strokeDashoffset` on slide entry and reversed cleanly on back.
* **Framed User Photos:** Clean `.photo-frame` and `.photo-slot` containers for slides where real photography shines.

### 5. 🛡️ Zero Text Overflow & Opaque 3D Flip Cards
* **HTML-Over-SVG Diagram Pattern:** Connectors, arches, and illustrations live in `<svg>`, while all text-bearing diagram boxes use auto-sizing HTML/Flex containers (or `<foreignObject>`) plus a runtime `fitSvgLabels()` guard—making Arabic text spilling outside boxes impossible.
* **Opaque 3D Flip Cards:** When a card flips (`.flip.on`), the front face completely hides (`opacity: 0; visibility: hidden; pointer-events: none`) and the back face renders on a **100% solid opaque surface**—zero front-face bleed.
* **Zero Slide Overlap:** Inactive slides are hard-hidden (`display: none`) and all GSAP tweens are killed before transitioning.

### 6. ↔️ Bidirectional Arrow-Key Animation & HUD-Free Stage
* **Clean Presentation Canvas:** Zero bottom settings bar, Prev/Next buttons, or clutter—only a thin `4px` top progress bar.
* **Unified Action Queue (`next()` / `prev()`):** Every reveal (`.step`), interactive ladder/tab (`[data-step-group]`), 3D flip card (`.flip`), live sketch (`.draw-path`), quiz reveal (`.quiz`), and 3D prop swap (`data-3d`) steps forward and reverses cleanly with arrow keys (while still supporting mouse clicks).

### 7. 🌐 Native Arabic RTL & Typography Excellence
* Strict `letter-spacing: 0 !important` for connected Arabic cursive scripts.
* Proper `<bdi>` isolation for inline English terms and numbers.
* `list-style: none` enforced to prevent native browser numbering (`1. 2.`) from duplicating custom Arabic badges (`١ ٢`).
* Projector-ready typography (`Cairo` + `Amiri` via Google Fonts) on a responsive fixed `1600×900` stage.

---

## 🎭 Built-In Visual Archetypes

| Archetype | Theme Attribute | Aesthetic & Best Use Case |
| :--- | :--- | :--- |
| **Muted 3D Morph Editorial** | `data-theme="muted-morph"` | Soft `#EFEFEF` studio canvas, frosted glass cards, velvety matte clay 3D shapes with soft shadows, and continuous PowerPoint-Morph-style glides. Ideal for modern seminars & marketing decks. |
| **Papyrus Historical Manuscript** | `data-theme="papyrus"` | Aged parchment (`#F3E9D2`), deep sepia ink (`#482400`), `Amiri` + `Cairo` fonts, live ink sketches (quill, pyramid, ship, compass), and timelines. Automatically suggested for historical topics. |
| **Clean Editorial Infographic** | `data-theme="editorial"` | Crisp light canvas with high-contrast flat-line educational illustrations and structured data diagrams. |
| **Dark Studio / Neo-Brutalist** | `data-theme="dark-studio"` | Deep charcoal/navy (`#07070A` / `#08121E`), luminous cyan/mint & lavender/gold accents, sharp borders, and dramatic rim-lit 3D props. |
| **Custom Reference Image** | *Extracted on the fly* | Upload any UI screenshot during intake and the skill extracts its exact palette, surfaces, accents, and corner motifs. |

---

## ⌨️ Keyboard & Touch Controls

| Action | Arabic (`dir="rtl"`) | English (`dir="ltr"`) |
| :--- | :--- | :--- |
| **Next step / slide** | `ArrowLeft` · `Space` · `PageDown` · Swipe Right | `ArrowRight` · `Space` · `PageDown` · Swipe Left |
| **Previous step / slide** | `ArrowRight` · `PageUp` · Swipe Left | `ArrowLeft` · `PageUp` · Swipe Right |
| **Slide Overview Grid** | `O` | `O` |
| **Speaker Notes Drawer** | `S` | `S` |
| **Toggle Fullscreen** | `F` | `F` |
| **Replay Current Slide** | `R` | `R` |
| **Select Quiz Option** | `1` – `4` | `1` – `4` |
| **Close Overlay** | `Esc` | `Esc` |

---

## 📂 Repository Structure

```text
immersive-3d-presentation/
├── README.md                              # Project documentation (this file)
├── SKILL.md                               # Core AI skill instructions & 5-question intake gate
├── MERGE-NOTES.md                         # Version history & design architecture notes
├── assets/
│   └── deck-template.html                 # Master v8 single-file hybrid engine template
├── references/
│   ├── threejs-3d.md                      # Real shadows, perimeter cover ring & dynamic data-3d guide
│   ├── infographics-and-visuals.md        # Zero-overflow HTML-over-SVG, isometric & kroki sketch patterns
│   ├── style-archetypes.md                # Muted Morph, Papyrus, Editorial, Dark & UI extraction specs
│   ├── rtl-arabic.md                      # Arabic RTL mirroring, Cairo/Amiri & zero letter-spacing rules
│   └── huashu-design-integration.md       # Layout rhythm, visual hierarchy & slide density guidelines
└── scripts/
    ├── detect_direction.py                # Auto-detects RTL/LTR direction from source text/files
    └── smoke_test.py                      # Automated Playwright QA checker for generated decks
```

---

## 🚀 Installation & Usage

### Option A: Claude Code / Skill Plugins / CLI Agents (Full Package)
Clone or copy the entire `immersive-3d-presentation/` folder into your skills directory:

```bash
git clone https://github.com/<your-username>/immersive-3d-presentation.git
cp -r immersive-3d-presentation ~/.claude/skills/
```
*(For platforms that import `.skill` archives, zip the `immersive-3d-presentation/` folder and rename `.zip` to `.skill`.)*

### Option B: Gemini Gems / Web Chat AI / Custom GPTs (Single-File Mode)
Web chat interfaces typically accept a single instruction file rather than a multi-folder plugin:
1. Open the standalone self-contained **`SKILL.md`**.
2. Paste its contents into your **Gemini Gem Instructions**, **Claude Project Instructions**, or **Custom GPT Instructions** (or upload `SKILL.md` directly in chat).
3. Start a prompt with your topic or attach a PDF—the AI will automatically trigger the 5 intake questions first.

### Option C: Local QA Verification (Optional)
Run the included helper scripts to verify slide direction and catch layout/console issues:

```bash
python scripts/detect_direction.py path/to/notes.txt
python scripts/smoke_test.py path/to/generated-presentation.html
```

---

## 📝 Changelog (v8 Highlights)
* Added **Mandatory Centered Anticipation Cover** with slow-bobbing perimeter 3D models for all themes.
* Upgraded Three.js renderer with **real soft shadows (`PCFSoftShadowMap`)**, shadow-catching floor planes, and **breathing contact shadows**.
* Enforced **zero 3D peeking** behind full-width cards, infographics, sketches, and photos (`data-hero="hide"` / `#gl.is-hidden`).
* Introduced **HTML-over-SVG Zero-Overflow Diagrams** + runtime `fitSvgLabels()` guard.
* Added **`Muted 3D Morph`** editorial archetype (`#EFEFEF`, clay 3D shapes, frosted glass, Morph glides) alongside **`Papyrus Historical Manuscript`** (`#F3E9D2`, sepia ink sketches).
* Hardened the **5-Question Pre-Flight Intake Gate** across both Claude and Gemini.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE). Feel free to fork, customize archetypes, and share your presentations!# immersive-3d-slides
# immersive-3d-slides
# immersive-3d-presentation-skill
# immersive-3d-presentation-skill
