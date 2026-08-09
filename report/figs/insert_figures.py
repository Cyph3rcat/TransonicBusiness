"""Replace the [FIGURE ...] placeholders in prelim_design_report.html with the generated images; idempotent because it matches on placeholder paragraphs that no longer exist after the first pass."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPORT = os.path.dirname(HERE)
DOC = os.path.join(REPORT, "prelim_design_report.html")

# figure number -> (file, caption); captions are the report's own descriptions, rewritten from draughtsman instructions.
FIGURES = {
    "1.1": ("fig_1_1_market.png",
            "The competitive set in range and cruise Mach, marker area proportional "
            "to maximum takeoff weight. The gap this design targets is the empty "
            "upper-left region: Phenom-class cruise speed at HondaJet-class weight."),
    "2.1": ("fig_2_1_weight_comparison.png",
            "Maximum takeoff, empty and usable fuel weights against the competitive "
            "set. This design sits in the HondaJet weight class while carrying the "
            "same eight occupants as the CJ4 and Phenom."),
    "3.1": ("fig_3_1_nose_profile.png",
            "The two nose profiles. The rejected power law meets the barrel at a "
            "10° tangency break; the adopted sine-power law is tangent by "
            "construction and blunt at the tip, so a rotating radar dish fits."),
    "3.2": ("fig_3_2_area_distribution.png",
            "Cross-sectional area distribution measured on both lofts by the "
            "OpenVSP wave-drag tool, with the Sears–Haack ideal at the same length "
            "and volume. The un-waisted body scores better on the M1.0 metric "
            "(1.49 against 1.53 ft²) while enclosing 17% more volume, because the "
            "metric responds to the smoothness of dA/dx rather than to peak height."),
    "3.3": ("fig_3_3_cabin_layout.png",
            "Cabin arrangement in plan and side elevation, drawn on the as-lofted "
            "full_v7 body. Seat pitch, aisle width, the enclosed lavatory, both "
            "baggage bays and the pressure bulkhead stations are shown."),
    "5.0": ("fig_5_0_airfoil_gallery.png",
            "The shortlisted sections drawn to scale from their UIUC coordinate "
            "files: the conventional fallback, the CFD screen winner, the section "
            "selected on volumetric grounds, the thicker family member carried "
            "forward, and the inverse-design demonstration."),
    "5.1": ("fig_5_1_drag_rise.png",
            "Constant-lift drag rise for SC(2)-0412 from the adopted v3 SU2 sweep, "
            "with ±1σ error bars from the windowed statistics over the last 1,500 "
            "of 5,000 iterations. The two independent drag-divergence criteria "
            "agree to within 0.008 in Mach number, and that agreement is the basis "
            "for calling the result defensible."),
    "5.2": ("fig_5_2_cp_distributions.png",
            "Surface pressure at the design lift coefficient, each curve "
            "interpolated between the two bracketing angle-of-attack runs so all "
            "three Mach numbers are compared at C<sub>L</sub> = 0.248. The flat "
            "supercritical rooftop and the shock forming near 65% chord at M0.80 "
            "are both solver output, not sketched."),
    "5.3": ("fig_5_3_span_loading.png",
            "Spanwise load distribution and section lift coefficient at the cruise "
            "condition, from the VSPAERO wake integration. First stall falls at "
            "η ≈ 0.60, inboard of the ailerons, which is what taper 0.35 plus 3° "
            "of washout is bought for."),
    "5.4": ("fig_5_4_winglet_polar.png",
            "Induced drag against the square of lift coefficient, with and without "
            "the winglet, on a fixed reference span. The winglet reduces the slope "
            "by about 10%; roughly three-quarters of that is span growth a plain "
            "tip extension would also deliver."),
    "6.1": ("fig_6_1_neutral_point.png",
            "Left: neutral point against horizontal tail area over the four-point "
            "parametric, in which only S<sub>HT</sub> varies. Right: the static "
            "margin each sizing basis actually delivers. The historical "
            "volume-coefficient answers land at roughly twice the tail this "
            "aircraft needs."),
    "6.2": ("fig_6_2_pitching_moment.png",
            "Pitching moment against lift coefficient for the final configuration, "
            "with the retracted unclosed-body result overlaid. The retracted curve "
            "is not merely offset: it is non-monotone, and it reported the static "
            "margin backwards. Neither model produced an error message."),
    "7.1": ("fig_7_1_landing_gear.png",
            "Landing gear geometry. Tipback and tail-strike clearance are "
            "comfortable; the 10.3° roll angle to wing-tip strike is the flagged "
            "item of §7.3, and it is thin against the 10°–15° landing attitudes "
            "this clearance exists to protect."),
    "8.1": ("fig_8_1_cg_envelope.png",
            "Centre-of-gravity envelope built from two bracketing loading "
            "sequences rather than from four corner states. The aft limit at 34.1% "
            "MAC leaves a 5.3% static margin, below the 10% floor adopted here, "
            "which is what drives the tail growth recommended in §8.6."),
    "8.2": ("fig_8_2_group_weights.png",
            "Class-II group weight statement from Raymer's general-aviation "
            "equations, driven by this aircraft's own geometry. The total lands "
            "0.9 lb from the Chapter 2 comparable-aircraft anchor, by a route that "
            "shares no inputs with it."),
    "9.1": ("fig_9_1_drag_breakdown.png",
            "Parasite drag by component, from the buildup on the measured outer "
            "mould line. Hatched bars carry the Q = 1.30 interference factor that "
            "the over-the-wing installation forces."),
    "9.2": ("fig_9_2_drag_polar.png",
            "The cruise drag polar, with parasite and induced contributions "
            "separated, the three cruise states marked, and both candidate optima "
            "annotated."),
    "9.3": ("fig_9_3_ld_optima.png",
            "Why the two optima differ. A jet maximises range at maximum "
            "C<sub>L</sub><sup>1/2</sup>/C<sub>D</sub>, not at L/D<sub>max</sub>. "
            "Measured against the correct optimum the aircraft cruises within 2–3% "
            "of its best-range condition throughout."),
    "10.1": ("fig_10_1_climb.png",
             "Rate of climb against altitude on a realistic climb schedule, all "
             "engines and one engine inoperative. The one-engine-inoperative "
             "ceiling of 42,750 ft is the operationally meaningful number: an "
             "engine failure at FL450 requires a drift-down, one at FL410 does not."),
    "10.2": ("fig_10_2_payload_range.png",
             "Payload–range diagram with the design requirement marked, and the "
             "same aircraft at a specific fuel consumption of 0.65 overlaid to "
             "show what closing that gap would buy."),
    "10.3": ("fig_10_3_vn_diagram.png",
             "V–n diagram in equivalent airspeed. The manoeuvre case governs at "
             "n = +3.21 against a worst gust case of +2.98, a margin of only 7%."),
}

TITLE_ART = (
    "fig_0_0_three_view.png",
    "General arrangement of configuration full_v7, drawn from the geometry "
    "drivers in <code>gen_v7.py</code> — the same numbers OpenVSP lofted and "
    "VSPAERO solved."
)

FIG_CSS = """figure { margin: 1.6em 0; text-align: center; }
figure img { max-width: 100%; height: auto; border: 1px solid #ddd; }
figcaption { font-size: 0.88em; color: #444; text-align: left; margin-top: 0.6em;
             line-height: 1.45; }
figcaption b { color: #111; }
"""


def figure_html(num, fname, caption):
    label = "Figure " + num if num else "Frontispiece"
    return (f'<figure>\n<img src="figures/{fname}" alt="{label}">\n'
            f'<figcaption><b>{label}.</b> {caption}</figcaption>\n</figure>')


def main():
    with open(DOC, encoding="utf-8") as f:
        doc = f.read()

    if "figure img {" not in doc:
        doc = doc.replace("hr { border: none;", FIG_CSS + "hr { border: none;", 1)

    # Title-page artwork.
    doc = re.sub(r"<p><em>\[TITLE PAGE ARTWORK:.*?\]</em></p>",
                 figure_html("", *TITLE_ART), doc, flags=re.S)

    n = 0
    for num, (fname, cap) in FIGURES.items():
        pat = re.compile(r"<p><em>\[FIGURE " + re.escape(num) + r":.*?\]</em></p>",
                         re.S)
        doc, k = pat.subn(lambda _m, f=fname, c=cap, x=num: figure_html(x, f, c),
                          doc)
        n += k
        if k == 0 and num != "5.0":
            print(f"  ! no placeholder found for FIGURE {num}")

    # Figure 5.0 has no placeholder in the original text, so anchor it just before the nine-candidate screening table.
    anchor = ("<p>with the technology factor $$\\kappa_A = 0.87$$ for conventional "
              "sections and 0.95 for the NASA supercritical family. All coordinates "
              "were taken from the UIUC database [13].</p>")
    if anchor in doc and "fig_5_0_airfoil_gallery" not in doc:
        doc = doc.replace(anchor, anchor + "\n\n" + figure_html("5.0", *FIGURES["5.0"]))
        n += 1

    with open(DOC, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"inserted {n + 1} figures into {os.path.relpath(DOC, REPORT)}")


if __name__ == "__main__":
    main()
