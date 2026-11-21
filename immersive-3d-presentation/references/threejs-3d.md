# 3D in presentations: two tiers, one director

Read this in Step 5/6 when planning or editing the 3D layer. It merges the parts of the upstream
**CloudAI-X/threejs-skills** (MIT licence; targets three.js **r186**) that matter for slides with the deck's
own pattern. For anything deeper than this file, use the table in section 8.

## Contents
1. The two tiers
2. Which 3D for which content
3. How the deck's 3D layer works
4. r186 rules (what the models still get wrong)
5. Budget, performance and disposal
6. Fallbacks and failure modes
7. Adding or changing a motif
8. Going deeper: upstream skill map
9. Testing 3D headlessly

---

## 1. The two tiers

| Tier | What | Use for | Why |
|---|---|---|---|
| **A. CSS-3D UI** | `perspective`, `rotateX/Y`, `translateZ`, `preserve-3d` on DOM elements: tilt cards, flip cards, stacked depth layers, carousels | anything with readable text or that must be clickable | crisp text, accessible, RTL-safe, no GPU risk |
| **B. WebGL scene** | one `<canvas>` behind the stage with three.js: a hero object, particles, a camera that moves between slides | atmosphere and one meaningful object per section | depth and motion CSS cannot do |

Rules of thumb: **text is always HTML.** The WebGL layer never carries information the audience must read;
if the canvas disappeared, every slide must still make complete sense. 3D must also *mean* something
(section change = camera move, concept = object); decorative 3D that fights the text is cut.

## 2. Which 3D for which content

| Content | Tier A device | Tier B motif (in `deck-template.html`) |
|---|---|---|
| Art, culture, heritage, formal | framed image cards with soft tilt; stacked "gallery wall" depth | `frames` (tilted ring of gold frames) |
| History, drama, baroque, film | slow push-in zoom on a dark card; light-sweep reveal | `chiaroscuro` (sculptural knot, one warm spot, fog) |
| Philosophy, humanities, ideas | flip cards (idea -> meaning); thought bubbles | `ideas` (glass-like platonic solids) |
| Science, tech, data, systems | layered "exploded" diagram using `translateZ` | `network` (nodes and links) |
| Kids / playful | big flip cards, wobbling sticker cards | `ideas` with bright tokens, larger and slower |
| Comparison of two positions | two cards rotating in `rotateY` like a book | any motif, hero parked small at the top |
| Timeline | horizontal strip with `translateZ` depth per era (reverse order in RTL) | camera dolly along x |

Set intensity from the audience and venue: **Rich** (hero + particles + tilt), **Subtle** (particles + tilt),
**None** (Tier A only; add `class="no-gl"` to `<body>`). Weak projectors or low-end laptops -> Subtle.

## 3. How the deck's 3D layer works

`assets/deck-template.html` splits the code on purpose:

1. **Engine** = a classic `<script>` with no imports (navigation, steps, flips, counters, tilt, HUD).
   It emits `deck:slide` and keeps `window.__deckCurrent`.
2. **3D layer** = a separate `<script type="module">` that `await import('three')` inside `try/catch`.
   If the import, the GPU or WebGL fails, it adds `body.no-gl` (a CSS gradient background) and the
   deck is unaffected.
3. **One renderer, one scene, per-slide poses.** Each slide declares where the camera and the hero object
   go:
   ```html
   <section class="slide" data-cam="0.8,0.3,9" data-hero="2.8,-0.2,.9"> <!-- cam x,y,z · hero x,y,scale -->
   ```
   The director tweens the camera and the hero group with GSAP. `x` values are multiplied by `SIGN` (-1 in
   RTL), so the hero is always opposite the text column. Never create one WebGL context per slide:
   browsers cap live contexts (around 16) and each costs memory.
4. **Touchable hero.** Dragging empty slide area rotates the hero (`world.rotation`, with a little inertia and a
   clamp on tilt); a click without movement raycasts against `world.children` and, on a hit, spins it. Drag
   offsets ease back to zero on every slide change. Interactive widgets (`button`, `.flip`, `.quiz`, `.poll`,
   timers, HUD) are excluded so they never start a drag. Touch pointers are excluded too: on touch screens
   horizontal swipes navigate slides. The hook `window.__deck3d = {world, camera}` exists for the smoke test.
5. **Pointer parallax** adds a small camera offset (disabled for reduced motion). Slides never wait for 3D.
6. **Reduced motion:** no animation loop; a single frame is rendered at each slide change with
   zero-duration tweens.

Keep text clear of the hero: with the stage at 1600x900 and the camera at z=9, the safe half-width at the
hero plane is about +/-5 world units. Hero x of 2.6 to 2.8 with an object radius up to ~2 fits; check
the screenshot for clipping at the canvas edge.

## 4. r186 rules (what the models still get wrong)

These come from the upstream skills' Common Mistakes lists and were checked against the `three@0.186.0`
package while building the template.

| Do not write | Write | Reason |
|---|---|---|
| `<script src="three.min.js">` | `import map` + `import * as THREE from 'three'` | `build/three.js` and `three.min.js` were removed in r161; three loads as ES modules |
| `import ... from 'three/examples/jsm/...'` | `import ... from 'three/addons/...'` | the `three/examples/jsm/` specifier does not resolve under the standard import map |
| `new THREE.Clock()` | `const timer = new THREE.Timer(); timer.connect(document); timer.update(); timer.getDelta()` | Clock is deprecated since r183; `connect` freezes delta while the tab is hidden |
| `requestAnimationFrame(loop)` | `renderer.setAnimationLoop(loop)` | recommended by the docs; also what WebGPU and XR require |
| `renderer.outputEncoding = THREE.sRGBEncoding` | nothing (default `SRGBColorSpace`) | encoding API removed |
| `renderer.physicallyCorrectLights = true` | delete it; give Point/Spot lights candela-scale intensity | physical units are always on |
| `material.envMapIntensity` for scene lighting | `scene.environmentIntensity` | `envMapIntensity` only scales the material's own `envMap` |
| `PCFSoftShadowMap` | `PCFShadowMap` | deprecated in r182 |
| `RGBELoader` | `HDRLoader` | renamed |
| `mesh.dispose()` alone | dispose geometry, material **and its textures** | `Object3D.dispose()` frees per-object state only |
| WebGL1 assumptions | WebGL2 only | WebGL 1 support is gone |

Version pin: `three@0.186.0` from jsDelivr, **exact version, never `@latest`**
(`https://cdn.jsdelivr.net/npm/three@0.186.0/build/three.module.js`). The import map in the template is the
canonical one. For WebGPU/TSL (not used by default) four map keys are required; see the upstream
`threejs-fundamentals` skill.

Lights in r186 use physical units. In the template: a `SpotLight` of intensity 500-900 at distance ~8-10 gives a
well-exposed warm key; ambient 0.08-0.5 sets how dark the shadows are. Tune by looking at the screenshot.

If the host only permits classic global `<script>` builds (some sandboxes allow only cdnjs), the global
build of three.js itself ended before r161 and the commonly hosted one is r128, whose API differs (`Clock`
instead of `Timer`, no `CapsuleGeometry`, no `three/addons`). In that case use Tier A only, or a minimal r128
scene, and tell the user.

## 5. Budget, performance and disposal

- **Pixel ratio:** `Math.min(devicePixelRatio, 2)`; 1 when `navigator.hardwareConcurrency <= 2`.
- **Geometry:** keep under ~50k triangles in total; use `InstancedMesh` for repeated objects (>20) and one
  `Points` for particles (400 max; 150 on low-power).
- **Shadows:** off by default. If a motif needs them (`chiaroscuro`), one light and a 1024 map.
- **No per-frame allocation:** hoist `new Vector3()` out of the loop.
- **Only the active slide matters:** one loop, paused when the tab is hidden (`Timer.connect(document)`).
- **Materials:** `MeshStandardMaterial` is plenty; avoid `MeshPhysicalMaterial` transmission on slides.
- **Dispose** everything you create when the page unloads or a motif is swapped:
  ```js
  const hold=[]; const keep=o=>{hold.push(o);return o;};   // wrap every geometry/material/texture
  addEventListener('pagehide',()=>{ renderer.setAnimationLoop(null); hold.forEach(o=>o.dispose()); renderer.dispose(); });
  ```
  For a loaded glTF, traverse it and dispose each mesh's geometry, each material and each material texture.
- Measure with `renderer.info.render.calls` **after** `render()` (it resets at the start of each render).

## 6. Fallbacks and failure modes

| Failure | What happens | Where handled |
|---|---|---|
| CDN blocked / offline | dynamic import rejects -> `body.no-gl`, gradient background | template `catch` |
| WebGL unavailable | `new WebGLRenderer` throws -> same | template `catch` |
| GSAP blocked | tiny shim applies end states; deck works with jump cuts | engine |
| Reduced motion | still frame, instant transitions | engine + 3D layer |
| Fonts blocked | fallback stack | CSS |
| Low-power device | pixel ratio 1, fewer particles, no MSAA | 3D layer |

**Fully offline venues:** copy `three.module.js`, `three.core.js` (both in `three@0.186.0/build/`) and
`gsap.min.js` into a `libs/` folder next to `index.html`, point the import map at `./libs/...` and the GSAP
`<script>` at `./libs/gsap.min.js`, and deliver the folder as a zip. (`three.module.js` imports
`three.core.js` by relative path, so both files must travel together.) A single self-contained file cannot
inline three as a module, so for a one-file deliverable tell the user the 3D layer needs internet and the
deck falls back gracefully without it.

## 7. Adding or changing a motif

A motif is a function in `MOTIFS` that adds objects to `world` (the hero group) or `scene`, registers
disposables with `keep(...)`, and **returns `t => { ...animate by time... }`**. Guidelines:
- One idea per motif; 1-3 draw-call families.
- Colour only from the CSS tokens (`accent`, `accent2`, `bg`), so archetype and brand colour changes carry
  over automatically.
- Keep it centred on the origin and about 4 world units wide, so `data-hero` placement stays predictable.
- Ideas worth adding when content calls for them: a **globe** (sphere of points + arcs) for geography/trade;
  **extruded bars** (instanced boxes growing from y=0) for data stories; a **helix/spiral path** the camera
  follows for timelines; a **book/page stack** for literature; **terrain** (displaced plane, wireframe) for
  environmental topics. Use upstream `threejs-geometry` for instancing and `threejs-shaders` for custom
  materials before inventing your own.
- Interaction (hover a node, click an object) -> raycast only against an explicit list with `layers`
  (see `threejs-interaction`); keep a Tier A control as the primary path.

## 8. Going deeper: upstream skill map

If the upstream skills are installed (Claude Code: `~/.claude/skills/threejs-*`; install with
`npx skills add cloudai-x/threejs-skills`), read the matching one before writing non-trivial 3D. They are
not required for the deck template.

| Need | Upstream skill |
|---|---|
| scene, camera, renderer, resize, loops | `threejs-fundamentals` |
| shapes, instancing, merged geometry, points, lines | `threejs-geometry` |
| PBR, blending, node materials | `threejs-materials` |
| light types, units, shadows, HDR environments | `threejs-lighting` |
| textures, colour spaces, render targets | `threejs-textures` |
| keyframes, AnimationMixer, skeletal/morph | `threejs-animation` |
| glTF (Draco, meshopt, KTX2), progress, disposal | `threejs-loaders`, `threejs-asset-pipeline` |
| custom shaders, TSL | `threejs-shaders` |
| bloom, DOF, screen effects | `threejs-postprocessing` |
| raycasting, controls, selection | `threejs-interaction` |
| frame cost, draw calls, memory | `threejs-performance` |
| React component form | `threejs-react-three-fiber` |

## 9. Testing 3D headlessly

`scripts/smoke_test.py` launches Chromium with software GL (`--use-angle=swiftshader
--enable-unsafe-swiftshader`), so WebGL scenes render in a sandbox without a GPU. Frames are slow but correct
for layout checks. Always open at least the first, a middle and the last screenshot: a blank-looking canvas
usually means the hero is off-screen (check `data-hero` x and scale) or the import failed (check
`no_gl_fallback` in the JSON report). Reading pixels back from a `alpha:true` WebGL canvas with
`drawImage` returns blank after compositing; judge by screenshot, not by pixel probes.


## 10. Topic-Expressive 3D Models & Slide-Synchronized Motion

Whenever the presentation topic has recognizable real-world objects, **build a custom procedural 3D model** for the `world` group instead of falling back to generic platonic solids:
- Combine clean Three.js primitives (`BoxGeometry`, `CylinderGeometry`, `TorusGeometry`, `CapsuleGeometry`, `ConeGeometry`, `ExtrudeGeometry`) into a cohesive hero sculpture + orbiting thematic props (e.g., a 3D game controller + `✕ ○ △ □` symbols for gamification; a DNA helix for biology; a rising 3D chart/coins for finance; an open book/cap for education).
- Give every `<section class="slide">` distinct `data-cam="x,y,z"`, `data-hero="x,y,scale"`, and `data-rot="rx,ry,rz"` attributes so the 3D model glides, scales, and rotates noticeably whenever the slide moves.
- The director also injects a directional spin impulse on `deck:slide` and a subtle micro-nudge on `deck:step`, linking the 3D scene directly to slide navigation.
- On light/cream backgrounds, increase `AmbientLight` + `DirectionalLight` contrast and use rich solid/matte-metallic colors from the deck palette so the 3D model stands out crisply.


## 11. Dynamic Contextual 3D Prop Switching (`data-prop`)

Instead of showing the exact same 3D model on every slide, build a **`PROPS` registry** (`registerProp(name, buildFn)`) containing:
- `hero`: the main topic sculpture (cover, closing, general slides).
- 3–6 contextual sub-models for specific slides or individual `.step-item` items (e.g., `chart` for bar/pie charts, `diagram` for flowcharts/trees, `storyboard` for sequential frames, `audio` for microphone/waves, `vr` for VR headset, `book` for text/reading).

Attach `data-prop="chart"` directly to `<section class="slide">` or `<li class="step-item" data-prop="chart">`. When the user navigates with Left/Right arrows, `setProp()` smoothly scales out the old model and springs in the new contextual model in ~0.45s without dizzying constant rotation.


## 12. Hybrid Visual Coordination (`data-hero="hide"` & `data-visual`)

Not every slide needs a WebGL object front and center. For slides showcasing **native inline SVG infographics** (editorial flat-line or isometric data diagrams), **hand-drawn kroki/ink sketches**, or **user-requested photographs**:
- Set `data-hero="hide"` (or `data-visual="infographic"` / `"sketch"` / `"photo"`) on `<section class="slide">`.
- The 3D director smoothly fades/scales the 3D canvas (`opacity: 0`) while that slide is active so the 2D infographic, sketch, or photo has 100% visual clarity with zero visual clutter — then smoothly brings the 3D model back when transitioning to a `3d` or `hybrid` slide.
- When using `data-motif="papyrus"`, render warm bronze/parchment-toned 3D props (e.g., rolled papyrus scroll, antique compass/globe, stepped pyramid) under warm key lighting so the 3D seamlessly blends with sepia ink sketches.


## 13. Realistic Studio Shadows, Cover Surround & Strict Safe-Zone Policy (v8)

### A. Real Shadows + Breathing Contact Shadow Disc (Mandatory)
3D models floating with zero shadow look pasted-on and flat. Every Three.js scene MUST include:
1. **WebGL Soft Shadow Map:**
   - `renderer.shadowMap.enabled = true;`
   - `renderer.shadowMap.type = THREE.PCFSoftShadowMap;`
   - Primary `DirectionalLight` with `castShadow = true`, `shadow.mapSize.set(1024, 1024)`, tight frustum (`±6`), and `shadow.bias = -0.0005`.
   - Set `castShadow = true` and `receiveShadow = true` on all procedural meshes (`traverse(o => { if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; } })`).
   - Add an invisible shadow-catcher floor plane (`THREE.ShadowMaterial({ opacity: isLightBg ? 0.16 : 0.32 })`) beneath the hero (`y = -1.95`, `receiveShadow = true`).
2. **Dynamic Breathing Contact Shadow Disc:**
   - Create a procedural radial-gradient canvas texture (soft dark oval fading smoothly to transparent) on a horizontal plane directly underneath each floating 3D object/group.
   - As the 3D object gently floats up and down (`bobY = Math.sin(t * 0.7) * 0.16`), scale the shadow disc inversely (`1 - bobY * 0.35`) and modulate its opacity (`baseOpacity - bobY * 0.12`) so the shadow subtly tightens when the object dips and softens as it rises.

### B. Cinematic Centered Cover Surround (`data-cover-surround="true"`)
Slide 1 MUST be a centered cover layout:
- Title, subtitle, and accent rule sit dead-center on the 1600×900 stage.
- **Balanced 3D Cover Surround:** On Slide 1, position 2–4 gentle topic-relevant 3D models symmetrically around the outer perimeter (left and right flanks, safely outside the centered text box) slowly rising and falling at staggered phases (`Math.sin(t * 0.65 + phase) * 0.22`) — creating calm anticipation as if the event is just about to begin, each casting a soft breathing shadow below it.
- On transition from Slide 1 → Slide 2, smoothly glide/morph the cover surround out and bring in the active slide's contextual 3D prop (or hide cleanly if Slide 2 is a full-width layout).

### C. Strict 3D Placement Policy (NO Random Corner Peeking!)
- **NEVER** park a 3D model behind cards, tables, or top-left/top-right UI borders where it partially peeks out awkwardly behind a card.
- Show 3D models **ONLY** in dedicated, unobstructed open visual zones:
  - Slide 1 Cover: symmetrical perimeter surround around the centered title.
  - Split / Stepper / Statement slides: unobstructed open half opposite the text column (`col` max-width `780px` on inline-start; 3D centered cleanly in the open inline-end half).
- On **full-width multi-card grids** (3-column flip cards, 4-card matrices, full-width diagrams/mind-maps, dense tables, pure 2D infographics/sketches, or full-bleed photos), ALWAYS set **`data-hero="hide"`** so `#gl` fades cleanly to `opacity: 0`.
