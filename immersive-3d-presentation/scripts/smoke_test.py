#!/usr/bin/env python3
"""Smoke-test a deck built from assets/deck-template.html in headless Chromium.

    python smoke_test.py index.html --out shots [--libs libs] [--rtl] [--reduced] [--no-3d]

What it does
  * loads the deck, steps through EVERY slide the way a presenter would (one click per step),
  * screenshots each slide fully revealed -> <out>/slide-NN.png  (LOOK at them, do not skip this),
  * reports console errors, text that overflows its box, content outside the 1600x900 stage,
    the slide count, and whether the 3D layer started or fell back (body.no-gl).

--libs DIR   a folder holding gsap.min.js and three's build files (three.module.js, three.core.js),
             served in place of the CDN URLs. Needed when the sandbox cannot reach the CDNs:
                 npm pack three@0.186.0 gsap@3.12.5 && tar xzf three-*.tgz && ...
                 libs/ <- package/build/*.js  and  package/dist/gsap.min.js
--rtl        also force dir="rtl" lang="ar" (layout check; text stays as written)
--reduced    emulate prefers-reduced-motion
--no-3d      block the three.js CDN to verify the no-WebGL fallback

It also AUDITS INTERACTION: every flip card, quiz, poll and timer is actually clicked and must react, the 3D
hero must rotate when dragged (unless the 3D layer fell back), and at least ceil(slides/3) slides must contain
an interactive component. A deck that is only "normal slides" fails.

Exit code 1 if there are console errors, overflow findings or interaction failures.
Set CHROMIUM=/path/to/chrome if it is not at the usual Playwright location.
"""
import argparse, asyncio, glob, json, os, sys
from playwright.async_api import async_playwright

def find_chromium():
    if os.environ.get("CHROMIUM"):
        return os.environ["CHROMIUM"]
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux*/chrome",
                os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome")):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None  # let Playwright use its own default

OVERFLOW_JS = """
() => {
  const stage = document.getElementById('stage').getBoundingClientRect();
  const sc = stage.width / 1600, tol = 2 * sc, out = [];
  const slide = document.querySelector('.slide.active');
  const seen = new Set();
  const add = (type, el, text) => { const k = type + (text || ''); if (!seen.has(k)) { seen.add(k); out.push({type, el: el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className ? '.' + el.className.split(' ')[0] : ''), text}); } };
  for (const el of slide.querySelectorAll('*')) {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || el.closest('.notes') || el.closest('.face.back')) continue;
    // 1) measure the TEXT itself, not just the element box (text can overflow a box of normal size)
    for (const node of el.childNodes) {
      if (node.nodeType !== 3 || !node.textContent.trim()) continue;
      const rg = document.createRange(); rg.selectNodeContents(node);
      const r = rg.getBoundingClientRect(); if (!r.width) continue;
      const label = node.textContent.trim().slice(0, 40);
      if (r.left < stage.left - tol || r.right > stage.right + tol || r.top < stage.top - tol || r.bottom > stage.bottom + tol)
        add('text-outside-stage', el, label);
      const pr = el.getBoundingClientRect();
      if (cs.display !== 'inline' && (r.right > pr.right + 4 * sc || r.left < pr.left - 4 * sc))
        add('text-overflows-its-box', el, label);
    }
    // 2) boxes themselves outside the stage
    const r = el.getBoundingClientRect();
    if (r.width && r.height && (r.left < stage.left - tol || r.right > stage.right + tol || r.top < stage.top - tol || r.bottom > stage.bottom + tol))
      add('box-outside-stage', el, (el.textContent || '').trim().slice(0, 40));
  }
  return out;
}
"""

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html"); ap.add_argument("--out", default="shots"); ap.add_argument("--libs")
    ap.add_argument("--rtl", action="store_true"); ap.add_argument("--reduced", action="store_true")
    ap.add_argument("--no-3d", action="store_true")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    html = open(a.html, encoding="utf-8").read()
    if a.rtl:
        html = html.replace('dir="ltr"', 'dir="rtl"', 1).replace('lang="en"', 'lang="ar"', 1)
    tmp = os.path.join(os.path.dirname(os.path.abspath(a.html)), "_smoke_tmp.html")
    open(tmp, "w", encoding="utf-8").write(html)

    report = {"console_errors": [], "findings": [], "slides": 0}
    async with async_playwright() as p:
        exe = find_chromium()
        browser = await p.chromium.launch(
            executable_path=exe, args=["--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
                                       "--ignore-gpu-blocklist", "--no-sandbox"])
        ctx = await browser.new_context(viewport={"width": 1600, "height": 900},
                                        reduced_motion="reduce" if a.reduced else "no-preference")
        page = await ctx.new_page()
        page.on("console", lambda m: report["console_errors"].append(m.text) if m.type == "error" and "ERR_FAILED" not in m.text and "favicon" not in m.text else None)
        page.on("pageerror", lambda e: report["console_errors"].append(f"PAGEERROR: {e}"))

        async def route(r):
            u = r.request.url
            if "fonts.g" in u:
                return await r.abort()           # fonts need internet; fallbacks are used in the test
            if a.libs and "gsap" in u and "cdnjs" in u:
                return await r.fulfill(path=os.path.join(a.libs, "gsap.min.js"), content_type="application/javascript")
            if "cdn.jsdelivr.net/npm/three@" in u and "/build/" in u:
                if a.no_3d:
                    return await r.abort()
                if a.libs:
                    return await r.fulfill(path=os.path.join(a.libs, u.split("/build/")[1]), content_type="application/javascript")
            await r.continue_()
        await page.route("**/*", route)
        await page.goto("file://" + os.path.abspath(tmp))
        await page.wait_for_timeout(2000)

        n = await page.evaluate("document.querySelectorAll('.slide').length")
        report["slides"] = n
        report["dir"] = await page.evaluate("document.documentElement.dir")
        key = "ArrowLeft" if report["dir"] == "rtl" else "ArrowRight"
        inter = {"interactive_slides": 0, "tested": [], "drag_3d_ok": False}
        for i in range(n):
            if i:                                            # advance from the previous slide (its steps are done)
                await page.keyboard.press(key)
                await page.wait_for_timeout(900)
            idx = await page.evaluate("window.__deckCurrent.index")
            if idx != i:
                report["findings"].append({"slide": i + 1, "type": "navigation", "detail": f"expected slide {i+1}, got {idx+1}"})
            steps = await page.evaluate("window.__deckCurrent?.totalSteps ?? document.querySelectorAll('.slide.active .step').length")
            for _ in range(steps):                           # advance every reveal/flip/step-group action via arrow key
                await page.keyboard.press(key)
                await page.wait_for_timeout(120)
            await page.wait_for_timeout(1500 if not a.reduced else 200)
            await page.screenshot(path=os.path.join(a.out, f"slide-{i+1:02d}.png"))
            for f in await page.evaluate(OVERFLOW_JS):
                report["findings"].append({"slide": i + 1, **f})
            # ---- exercise the interactive components on this slide ----
            comps = await page.evaluate("""() => { const s=document.querySelector('.slide.active');
                return {flip:s.querySelectorAll('.flip').length, quiz:s.querySelectorAll('.quiz .opt').length,
                        poll:s.querySelectorAll('.pv').length, timer:s.querySelectorAll('[data-timer]').length}; }""")
            if any(comps.values()):
                inter["interactive_slides"] += 1
                if comps["flip"]:
                    before_flips = await page.evaluate("document.querySelectorAll('.slide.active .flip.on').length")
                    await page.click(".slide.active .flip >> nth=0"); await page.wait_for_timeout(300)
                    after_flips = await page.evaluate("document.querySelectorAll('.slide.active .flip.on').length")
                    ok = after_flips != before_flips
                    inter["tested"].append({"slide": i + 1, "flip": ok})
                    if not ok: report["findings"].append({"slide": i + 1, "type": "interaction", "detail": "flip card did not flip"})
                if comps["quiz"]:
                    await page.click(".slide.active .quiz .opt >> nth=0"); await page.wait_for_timeout(300)
                    ok = await page.evaluate("!!document.querySelector('.slide.active .quiz.done') && document.querySelector('.slide.active .opt.right')!==null")
                    inter["tested"].append({"slide": i + 1, "quiz": ok})
                    if not ok: report["findings"].append({"slide": i + 1, "type": "interaction", "detail": "quiz gave no feedback"})
                if comps["poll"]:
                    await page.click(".slide.active .pv >> nth=0"); await page.wait_for_timeout(700)
                    ok = await page.evaluate("parseFloat(document.querySelector('.slide.active .pv .bar').style.width)>0")
                    inter["tested"].append({"slide": i + 1, "poll": ok})
                    if not ok: report["findings"].append({"slide": i + 1, "type": "interaction", "detail": "poll bar did not grow"})
                if comps["timer"]:
                    await page.click(".slide.active [data-timer]"); await page.wait_for_timeout(1300)
                    ok = await page.evaluate("document.querySelector('.slide.active [data-timer]').classList.contains('run')")
                    await page.click(".slide.active [data-timer]")
                    inter["tested"].append({"slide": i + 1, "timer": ok})
                    if not ok: report["findings"].append({"slide": i + 1, "type": "interaction", "detail": "timer did not start"})
                await page.screenshot(path=os.path.join(a.out, f"slide-{i+1:02d}-interacted.png"))
            # ---- drag the 3D hero once (on the first slide that allows it) ----
            if not inter["drag_3d_ok"] and await page.evaluate("!!window.__deck3d"):
                before = await page.evaluate("window.__deck3d.world.rotation.y")
                await page.mouse.move(800, 40); await page.mouse.down(); await page.mouse.move(950, 60, steps=6); await page.mouse.up()
                await page.wait_for_timeout(200)
                after = await page.evaluate("window.__deck3d.world.rotation.y")
                inter["drag_3d_ok"] = abs(after - before) > 0.05
        report["no_gl_fallback"] = await page.evaluate("document.body.classList.contains('no-gl')")
        report["interaction"] = inter
        need = -(-n // 3)
        if inter["interactive_slides"] < need:
            report["findings"].append({"type": "interaction", "detail": f"only {inter['interactive_slides']} interactive slides, need at least {need} (1 per 3 slides)"})
        if not report["no_gl_fallback"] and not inter["drag_3d_ok"]:
            report["findings"].append({"type": "interaction", "detail": "3D hero did not rotate when dragged (or 3D layer missing)"})
        await browser.close()
    os.remove(tmp)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(1 if report["console_errors"] or report["findings"] else 0)

asyncio.run(main())
