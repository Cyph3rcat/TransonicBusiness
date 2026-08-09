"""Builds one markdown file per lecture-slide deck, pairing the title/footer-only text layer (bitmap decks yield nothing else) with a link to render_slides.py's page image; slides in TRANSCRIPTIONS get hand-verified text inlined, everything else is flagged as unverified.

Usage:  python tools/render_slides.py --all && python tools/slides_to_md.py
"""
import os
import re
import glob

import pypdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "lectureslides")
OUT = os.path.join(ROOT, "refs", "lectureslides")

# Hand-transcribed from the rendered images. Keyed by (deck slug, slide number).
TRANSCRIPTIONS = {
    ("week6_3", 6): "**Figure 5.38 — The effect of the sweep angle on the normal Mach number.** "
                    "Swept wing at sweep Λ to the fuselage centreline; freestream Mach M resolves "
                    "to a normal component `M·cos(Λ)` across the wing. Streamwise chord `C` becomes "
                    "`C/cos(Λ)` measured normal to the quarter-chord line. Stagnation streamline "
                    "shown with lateral curvature.",
    ("week6_3", 7): "μ = sin⁻¹(1/M)   (Mach angle)\n\n"
                    "Λ = 1.2 · (90 − μ)   (supersonic sweep rule of thumb)",
    ("week6_3", 8): "1. **Low subsonic aircraft.** If max speed is below Mach 0.3, no sweep is "
                    "recommended — its disadvantages negate the improvement. 5 deg of sweep might "
                    "cut drag ~2% but raise manufacturing cost ~15%. A straight wing is recommended.\n"
                    "2. **High subsonic and supersonic aircraft.** Initial value from Eq. (5.32) as a "
                    "function of cruise speed. The final value is settled after aerodynamics, "
                    "performance, stability, control, structures, cost and manufacturability "
                    "analysis. A tapered wing must have some sweep anyway.\n"
                    "3. **High subsonic:** sweep enough that the normal component of the Mach number "
                    "is under the critical Mach number of the airfoil.",
    ("week6_3", 10): "**Sadraey Table 5.12 — Dihedral (or anhedral) angles for several aircraft.** "
                     "Selected rows: Cessna 750 Citation X, business jet, low wing — **3 deg**; "
                     "Falcon 900B, business jet transport, low wing — 0 deg 30 min; "
                     "MD-11 jet transport low wing — 6; Boeing 767 low wing — 4 deg 15 min; "
                     "Boeing 747 low wing — 7; Airbus 310 low wing — 11 deg 8 min; "
                     "Pilatus PC-9 low wing — 7 outboard; F-16 mid-wing — 0; "
                     "BAE Sea Harrier high wing — −12; C-130 high wing — 2 deg 30 min.",
    ("week6_3", 11): "**Raymer Table 4.2 — Dihedral Guidelines** (deg), by wing position:\n\n"
                     "| | Low | Mid | High |\n|---|---|---|---|\n"
                     "| Unswept (civil) | 5 to 7 | 2 to 4 | 0 to 2 |\n"
                     "| Subsonic swept wing | **3 to 7** | −2 to 2 | −5 to −2 |\n"
                     "| Supersonic swept wing | 0 to 5 | −5 to 0 | −5 to 0 |\n\n"
                     "Quoted note: for a wing with a flat centre section and dihedral only on the "
                     "outer panels, a first approximation is the dihedral that puts the tips as high "
                     "as they would be with dihedral starting at the root.",
    ("week6_3", 12): "C_Di = C_L² / (π · e · AR)\n\n"
                     "Oswald efficiency factor e = 1.0 for a wing with an ideal elliptical lift "
                     "distribution. \"Play with these parameters to minimize drag.\"",
    ("week6_3", 15): "13. A shorter wing costs less to build than a long wing — for cost, low AR is "
                     "desired.\n14. As AR increases, aileron reversal becomes more likely since the "
                     "wing is more flexible — for this reason low AR is desired.\n"
                     "15. In general, a rectangular high-AR wing is gust sensitive.",
    ("week6_3", 16): "Two major goals for employing twist in wing design:\n"
                     "1. Avoiding tip stall before root stall.\n"
                     "2. Modification of the lift distribution to an elliptical one.\n\n"
                     "One unwanted output of twist:\n3. Reduction in lift.\n\n"
                     "**Figure 5.48** — negative (wash-out) twist unloads the outboard wing, pulling "
                     "the span load down near the tip relative to the untwisted case.",
    ("week6_2", 3): "1. Determine the average aircraft weight in cruising flight:\n"
                    "   W_avg = ½ (W_i + W_f)   (5.9)\n"
                    "2. Calculate the aircraft ideal cruise lift coefficient. In cruise, weight "
                    "equals lift, so:\n   C_Lc = 2·W_ave / (ρ·V_c²·S)   (5.10)",
    ("week6_2", 5): "4. Calculate the wing airfoil ideal lift coefficient (C_li). The wing is a "
                    "three-dimensional body while an airfoil is a two-dimensional section. For a "
                    "constant chord, unswept, no-dihedral, infinite-span wing the wing lift "
                    "coefficient would equal the airfoil's. In reality span is limited and the wing "
                    "is usually swept and tapered, so the wing lift coefficient is slightly less "
                    "than the airfoil lift coefficient.",
    ("week6_2", 9): "**Figure 5.53 — Typical effects of a high-lift device on wing airfoil section "
                    "features.** Three panels, solid = without flap deflection, dashed = with flap "
                    "deflection: (left) C_l vs α — flap raises C_lmax and shifts the curve left, "
                    "lowering α_s; (middle) C_m vs α — flap makes C_m more negative; "
                    "(right) C_d vs C_l — flap raises C_dmin and shifts the drag bucket to higher C_l.",
    ("week6_2", 11): "**Airfoil selection chart** — maximum lift coefficient (c_lmax) vs ideal lift "
                     "coefficient (C_li) for the NACA 4-, 5-, 6- and 7-series sections. All data at "
                     "Re = 6×10⁶, no flap deflection. Used to pick a section against the C_li and "
                     "c_lmax targets computed in the preceding steps.",
    ("week7_3", 5): "23. Select vertical tail configuration (conventional, twin vertical tail, "
                    "vertical tail at swept wing tip, V-tail) (Section 6.8.2.1).\n"
                    "24. Select the vertical tail volume coefficient, V̄_v (Table 6.4):\n\n"
                    "    **V̄_v = l_v · S_v / (b · S)**   (6.72)\n\n"
                    "where l_v is the distance between the vertical tail aerodynamic centre (ac_v) "
                    "and the **wing/fuselage aerodynamic centre**, S_v is the vertical tail planform "
                    "area, b is the wing span and S the wing reference area. The vertical tail "
                    "aerodynamic centre is at the quarter chord of the vertical tail MAC.",
    ("week7_3", 6): "**Sadraey Table 6.4 — horizontal (V̄_H) and vertical (V̄_v) tail volume "
                    "coefficients:**\n\n"
                    "| No. | Aircraft | V̄_H | V̄_v |\n|---|---|---|---|\n"
                    "| 1 | Glider and motor glider | 0.6 | 0.03 |\n"
                    "| 2 | Home-built | 0.5 | 0.04 |\n"
                    "| 3 | GA single prop-driven engine | 0.7 | 0.04 |\n"
                    "| 4 | GA twin prop-driven engine | 0.8 | 0.07 |\n"
                    "| 5 | GA with canard | 0.6 | 0.05 |\n"
                    "| 6 | Agricultural | 0.5 | 0.04 |\n"
                    "| 7 | Twin turboprop | 0.9 | 0.08 |\n"
                    "| 8 | Jet trainer | 0.7 | 0.06 |\n"
                    "| 9 | Fighter aircraft | 0.4 | 0.07 |\n"
                    "| 10 | Fighter (with canard) | 0.1 | 0.06 |\n"
                    "| 11 | Bomber/military transport | 1 | 0.08 |\n"
                    "| 12 | **Jet transport** | **1.1** | **0.09** |\n\n"
                    "Note: there is no light-business-jet row; jet transport is the nearest class.",
    ("week7_3", 8): "Vertical tail airfoil section:\n"
                    "- Should be symmetric\n"
                    "- Should be thinner than the wing airfoil to reduce compressibility effects\n"
                    "- High lift-curve slope for good static directional stability",
    ("week7_3", 10): "The main purposes of the taper ratio are (i) to reduce the bending stress on "
                     "the vertical tail root and (ii) to allow the vertical tail to have a sweep angle.",
    ("week7_3", 11): "33. Calculate vertical tail span (b_v), root chord (C_Vroot), tip chord "
                     "(C_Vtip) and MAC_v by solving four equations simultaneously:\n\n"
                     "    AR_v = b_v / C̄_v = b_v² / S_v            (6.77)\n"
                     "    λ_v  = C_Vtip / C_Vroot                  (6.78)\n"
                     "    C̄_v  = (2/3) · C_Vroot · (1 + λ_v + λ_v²)/(1 + λ_v)   (6.79)\n"
                     "    S_v  = b_v · C̄_v                         (6.80)\n\n"
                     "Required inputs: vertical tail planform area, aspect ratio and taper ratio.",
    ("week7_3", 12): "34. Check static directional stability.",
}


def slug_of(stem):
    return stem.lower().replace(" ", "").replace("(", "_").replace(")", "")


def main():
    os.makedirs(OUT, exist_ok=True)
    index = ["# Lecture slides (AAE5203) — converted\n",
             "The decks are PowerPoint exports with bitmap content. Text extraction "
             "(pypdf / markitdown / pdfminer) recovers only titles and footers, so each deck below "
             "pairs the text layer with a full-page render of every slide.\n",
             "**Transcribed** slides have had their image read and written out in full. "
             "Slides marked *not transcribed* have a render but no verified text — open the image "
             "rather than assuming the content.\n",
             "Source PDFs stay in `lectureslides/`; renders are in `refs/lectureslides/img/`.\n",
             "| Deck | Topic | Slides | Transcribed |", "|---|---|---|---|"]

    for pdf in sorted(glob.glob(os.path.join(SRC, "*.pdf"))):
        stem = os.path.splitext(os.path.basename(pdf))[0]
        slug = slug_of(stem)
        reader = pypdf.PdfReader(pdf)
        n = len(reader.pages)
        title = (reader.pages[0].extract_text() or stem).strip().split("\n")
        topic = " ".join(t.strip() for t in title[:2] if t.strip())[:60] or stem

        lines = [f"# {stem} — {topic}\n",
                 f"*Converted from `lectureslides/{os.path.basename(pdf)}`. "
                 f"{n} slides. Content is bitmap; renders in `img/`.*\n"]
        ntrans = 0
        for i in range(n):
            raw = (reader.pages[i].extract_text() or "").strip()
            # Drop the date/slide-number footer PowerPoint stamps on every slide.
            raw = re.sub(r"\b\d{1,2}/\d{1,2}/\d{4}\b", "", raw)
            raw = "\n".join(l.strip() for l in raw.split("\n") if l.strip())
            img = f"img/{slug}_s{i + 1:02d}.png"
            lines.append(f"\n## Slide {i + 1}\n")
            lines.append(f"![{stem} slide {i + 1}]({img})\n")
            if raw:
                lines.append("Text layer:\n")
                lines.append("```\n" + raw + "\n```\n")
            key = (slug, i + 1)
            if key in TRANSCRIPTIONS:
                ntrans += 1
                lines.append("Transcribed content:\n")
                lines.append(TRANSCRIPTIONS[key] + "\n")
            elif not raw:
                lines.append("*Image only — not transcribed.*\n")
        out = os.path.join(OUT, f"{slug}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        index.append(f"| [{stem}]({slug}.md) | {topic} | {n} | {ntrans} |")
        print(f"  {slug}.md  {n} slides, {ntrans} transcribed")

    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(index) + "\n")
    print("  README.md")


if __name__ == "__main__":
    main()
