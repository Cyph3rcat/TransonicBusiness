"""Renders lecture-slide PDF pages to PNG so image-only decks can be transcribed; whole pages are rendered rather than extracting embedded images, which would fragment a slide into template art plus disconnected figures.

Usage:
    python tools/render_slides.py "Week 7 (3)"      # one deck
    python tools/render_slides.py --all             # every deck in lectureslides/
"""
import os
import sys
import glob

import pypdfium2 as pdfium

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "lectureslides")
OUT = os.path.join(ROOT, "refs", "lectureslides", "img")
SCALE = 2.2  # ~158 DPI: readable equations without huge files


def render(pdf_path):
    stem = os.path.splitext(os.path.basename(pdf_path))[0]
    slug = stem.lower().replace(" ", "").replace("(", "_").replace(")", "")
    doc = pdfium.PdfDocument(pdf_path)
    os.makedirs(OUT, exist_ok=True)
    written = []
    for i in range(len(doc)):
        img = doc[i].render(scale=SCALE).to_pil()
        path = os.path.join(OUT, f"{slug}_s{i + 1:02d}.png")
        img.save(path)
        written.append(path)
    doc.close()
    print(f"{stem}: {len(written)} slides -> refs/lectureslides/img/{slug}_sNN.png")
    return written


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    if args[0] == "--all":
        targets = sorted(glob.glob(os.path.join(SRC, "*.pdf")))
    else:
        targets = []
        for a in args:
            hits = glob.glob(os.path.join(SRC, f"{a}*.pdf"))
            if not hits:
                print(f"no deck matching {a!r}")
                return 1
            targets += hits
    for t in targets:
        render(t)
    return 0


if __name__ == "__main__":
    sys.exit(main())
