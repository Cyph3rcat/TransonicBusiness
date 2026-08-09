"""Convert the repo's text-layer PDFs to markdown under refs/.

Text-layer PDFs only. The lecture-slide decks are image-only (their figures are
embedded bitmaps, not text) and are transcribed by hand into refs/lectureslides/
instead -- see that directory's README.

Raymer is split per chapter rather than emitted as one 1097-page file, so a
chapter can be read or grepped without loading the whole book. Printed page
numbers are preserved as `<!-- p.N -->` markers because every citation in
config.md / doubts.md refers to printed pages, not PDF indices.

Usage:  python tools/pdf_to_md.py
"""
import os
import re
import sys

import pypdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "refs")

# Raymer: PDF page index = printed page + 29 (verified against printed p.96/97
# at indices 125/126). Chapter start pages are from the book's own contents.
RAYMER = ("Daniel P. Raymer - Aircraft Design_ A Conceptual Approach "
          "(2018, American Institute of Aeronautics and Astronautics Inc.) - libgen.li.pdf")
RAYMER_OFFSET = 29
RAYMER_CHAPTERS = [
    (1, "Design - A Separate Discipline", 1),
    (2, "Overview of the Design Process", 9),
    (3, "Sizing from a Conceptual Sketch", 27),
    (4, "Airfoil and Wing-Tail Geometry Selection", 53),
    (5, "Thrust-to-Weight Ratio and Wing Loading", 115),
    (6, "Initial Sizing", 145),
    (7, "Configuration Layout and Loft", 165),
    (8, "Special Considerations in Configuration Layout", 213),
    (9, "Crew Station, Passengers, and Payload", 261),
    (10, "Propulsion and Fuel System Integration", 275),
    (11, "Landing Gear and Subsystems", 337),
    (12, "Aerodynamics", 389),
    (13, "Propulsion", 455),
    (14, "Structures and Loads", 491),
    (15, "Weights", 559),
    (16, "Stability, Control, and Handling Qualities", 585),
    (17, "Performance and Flight Mechanics", 641),
    (18, "Cost Analysis", 687),
    (19, "Sizing and Trade Studies", 709),
    (20, "Electric Aircraft", 735),
    (21, "VTOL Aircraft Design", 765),
    (22, "Extremes of Flight", 807),
    (23, "Design of Unique Aircraft Types", 843),
    (24, "Conceptual Design Examples", 881),
]

# Standalone documents: (pdf path, output name, title)
SINGLES = [
    ("19900007394.pdf", "nasa_19900007394.md", "NASA 19900007394"),
    ("Journal_of_Aircraft_Vol40_No4_P609_P615_SHM_1_NLF.pdf",
     "joa_vol40_no4_nlf.md", "Journal of Aircraft Vol.40 No.4 pp.609-615 - NLF"),
    ("MSRM-31-12-2022-C11110814.pdf", "msrm_31_12_2022.md", "MSRM-31-12-2022-C11110814"),
    ("TCDS IM E  016  issue 13_210721.pdf", "tcds_im_e_016.md",
     "EASA TCDS IM.E.016 issue 13 - Williams FJ44"),
]

# Ligatures and the soft hyphen this scan emits mid-word.
FIXES = [("ﬁ", "fi"), ("ﬂ", "fl"), ("ﬀ", "ff"),
         ("ﬃ", "ffi"), ("ﬄ", "ffl"), ("�", "-"),
         ("­", "-"), ("‘", "'"), ("’", "'"),
         ("“", '"'), ("”", '"')]


def clean(text):
    for a, b in FIXES:
        text = text.replace(a, b)
    # This scan splits words across line breaks with a trailing hyphen.
    text = re.sub(r"-\s*\n\s*", "", text)
    # Collapse the runs of spaces the OCR leaves inside words ("Air craft").
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def write_md(path, title, source, pages, reader, offset=0):
    parts = [f"# {title}\n", f"*Converted from `{source}` by `tools/pdf_to_md.py`. "
             f"Page markers are printed page numbers.*\n"]
    for idx in pages:
        printed = idx - offset if offset else idx + 1
        raw = reader.pages[idx].extract_text() or ""
        parts.append(f"\n<!-- p.{printed} -->\n\n{clean(raw)}\n")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts))
    return sum(len(p) for p in parts)


def main():
    os.makedirs(os.path.join(OUT, "raymer"), exist_ok=True)

    raymer_path = os.path.join(ROOT, RAYMER)
    if os.path.exists(raymer_path):
        reader = pypdf.PdfReader(raymer_path)
        n = len(reader.pages)
        bounds = [(c, t, p) for c, t, p in RAYMER_CHAPTERS]
        for i, (num, title, start) in enumerate(bounds):
            end = bounds[i + 1][2] if i + 1 < len(bounds) else n - RAYMER_OFFSET
            i0, i1 = start + RAYMER_OFFSET, min(end + RAYMER_OFFSET, n)
            slug = re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")
            out = os.path.join(OUT, "raymer", f"ch{num:02d}_{slug}.md")
            size = write_md(out, f"Raymer Ch.{num} - {title}", RAYMER,
                            range(i0, i1), reader, RAYMER_OFFSET)
            print(f"  raymer/ch{num:02d}_{slug}.md  printed p.{start}-{end - 1}  {size // 1024} KB")
        # Front matter carries the nomenclature list, which is worth grepping.
        write_md(os.path.join(OUT, "raymer", "ch00_front_matter.md"),
                 "Raymer - Front Matter (contents, nomenclature)", RAYMER,
                 range(0, RAYMER_OFFSET + 1), reader)
        print("  raymer/ch00_front_matter.md")

    for src, name, title in SINGLES:
        path = os.path.join(ROOT, src)
        if not os.path.exists(path):
            # The TCDS filename has an irregular run of spaces; match on prefix.
            cands = [f for f in os.listdir(ROOT)
                     if f.lower().startswith(src.split()[0].lower()) and f.endswith(".pdf")]
            if not cands:
                print(f"  SKIP (not found): {src}")
                continue
            path = os.path.join(ROOT, cands[0])
        reader = pypdf.PdfReader(path)
        size = write_md(os.path.join(OUT, name), title,
                        os.path.basename(path), range(len(reader.pages)), reader)
        print(f"  {name}  {len(reader.pages)}p  {size // 1024} KB")


if __name__ == "__main__":
    sys.exit(main())
