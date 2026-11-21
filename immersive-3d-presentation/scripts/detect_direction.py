#!/usr/bin/env python3
"""Detect the writing direction and language of presentation content.

Usage:
    python detect_direction.py "text ..."          # text as an argument
    python detect_direction.py --file content.txt  # or from a file
    echo "text" | python detect_direction.py       # or from stdin

Prints one JSON object, e.g.
    {"dir": "rtl", "lang": "ar", "mode": "rtl", "rtl_ratio": 0.93, ...}

mode is one of:
    "rtl"       -> set <html dir="rtl" lang="ar|fa|ur|he">
    "ltr"       -> set <html dir="ltr" lang="en|...">
    "bilingual" -> keep the primary direction on <html> and mark every text
                   block with dir="auto" so each paragraph resolves itself

Only letters are counted. Digits, punctuation, emoji, code and URLs are
direction-neutral and would skew the ratio, so they are ignored.
"""
import json
import re
import sys
import unicodedata

# script name -> (default lang code, inclusive code point ranges)
RTL_SCRIPTS = {
    "arabic": ("ar", [(0x0600, 0x06FF), (0x0750, 0x077F), (0x08A0, 0x08FF),
                      (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)]),
    "hebrew": ("he", [(0x0590, 0x05FF), (0xFB1D, 0xFB4F)]),
    "syriac": ("syr", [(0x0700, 0x074F)]),
    "thaana": ("dv", [(0x0780, 0x07BF)]),
}
# Letters used in Persian / Urdu but not in plain Arabic
PERSIAN_ONLY = set("پچژگ")          # pe, che, zhe, gaf
URDU_ONLY = set("ٹڈڑںھےۓ")          # tteh, ddal, rreh, noon ghunna, heh doachashmee, yeh barree
CODE_FENCE = re.compile(r"```.*?```", re.S)
URL = re.compile(r"https?://\S+")


def classify(ch):
    cp = ord(ch)
    for name, (_, ranges) in RTL_SCRIPTS.items():
        if any(a <= cp <= b for a, b in ranges):
            return name
    return "ltr"


def analyse(text):
    text = CODE_FENCE.sub(" ", text)
    text = URL.sub(" ", text)
    counts = {}
    for ch in text:
        if not unicodedata.category(ch).startswith("L"):
            continue
        key = classify(ch)
        counts[key] = counts.get(key, 0) + 1

    ltr = counts.pop("ltr", 0)
    rtl = sum(counts.values())
    total = ltr + rtl
    if total == 0:
        return {"dir": "ltr", "lang": "en", "mode": "ltr", "rtl_ratio": 0.0,
                "letters": 0, "note": "no letters found; defaulting to ltr/en"}

    ratio = rtl / total
    dominant = max(counts, key=counts.get) if counts else None
    lang = RTL_SCRIPTS[dominant][0] if dominant else "en"
    if dominant == "arabic":
        if any(c in PERSIAN_ONLY for c in text):
            lang = "fa"
        elif any(c in URDU_ONLY for c in text):
            lang = "ur"

    # >=65% RTL letters -> RTL deck; 15-65% -> bilingual; <15% -> LTR deck
    if ratio >= 0.65:
        mode, direction = "rtl", "rtl"
    elif ratio >= 0.15:
        mode = "bilingual"
        direction = "rtl" if ratio >= 0.5 else "ltr"
        if ratio < 0.5:
            lang = "en"
    else:
        mode, direction, lang = "ltr", "ltr", "en"

    return {
        "dir": direction,
        "lang": lang,
        "mode": mode,
        "rtl_ratio": round(ratio, 3),
        "letters": total,
        "scripts": {**counts, "latin_or_other": ltr},
    }


def main():
    args = sys.argv[1:]
    if args and args[0] == "--file":
        with open(args[1], encoding="utf-8") as f:
            text = f.read()
    elif args:
        text = " ".join(args)
    else:
        text = sys.stdin.read()
    print(json.dumps(analyse(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
