"""Leave-one-out component buildup: how much does each component contribute
to CMy (and CL/CD) at a single operating point?

Method: run the full configuration, then run it again with exactly one
component pulled out of the VSPAERO analysis set (still built, just excluded
from GeomSet/ThinGeomSet, so it contributes zero force/moment). The
difference

    delta_Cmy(component) = Cmy_full - Cmy_without(component)

is that component's net pitching-moment contribution AT this configuration --
interference with the rest of the airframe is included, not assumed away,
because it's a real difference of two real solves, not a superposition.

Run at alpha = 3.7 deg (~cruise CL for this model), single point, both
GeomSet=0 (all bodies+lifting in one pass isn't how VSPAERO splits it, so this
still uses the fuselage/wing set convention from gen_v6.TEMPLATE).

Two configurations compared:
  v5-equivalent -- v6's (closed-tail) fuselage carrying v5's DOCUMENTED tail
                   areas (S_HT=51.68, S_VT=59.0). This isolates the tail-area
                   change from the fuselage-closure fix and the open-tail bug
                   (doubts.md #26) -- comparing against the actual v5.vsp3
                   would conflate a data-corrupting defect with the sizing
                   change being evaluated.
  v6            -- final resized tails (S_HT=34.0, S_VT=45.0).

Usage:  python component_moment.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_v6

CASES = {
    "v5eq": dict(s_ht=51.68, s_vt=59.00, xcg=19.90),
    "v6":   dict(s_ht=34.00, s_vt=45.00, xcg=19.749),
}


def read_point(path):
    hdr, row = None, None
    for line in open(path):
        s = line.strip()
        if not s or s.startswith(("Surface", "Surf-")):
            continue
        if s.startswith("Beta "):
            hdr = s.split()
            continue
        row = [float(x) for x in s.split()]
    c = {n: i for i, n in enumerate(hdr)}
    return row[c["CLtot"]], row[c["CDtot"]], row[c["CMytot"]]


def main():
    results = {}
    for tag, cfg in CASES.items():
        print(f"=== {tag}: S_HT={cfg['s_ht']}, S_VT={cfg['s_vt']} ===")
        base_name = f"mom_{tag}_full"
        d = gen_v6.make(base_name, cfg["s_ht"], cfg["s_vt"], 15.9, cfg["xcg"], "point")
        gen_v6.run(d)
        cl0, cd0, cm0 = read_point(os.path.join(d, f"{base_name}.polar"))
        print(f"  full config: CL={cl0:.4f} CD={cd0:.5f} CMy={cm0:+.5f}")
        results[tag] = dict(full=(cl0, cd0, cm0), components={})

        for comp in gen_v6.COMPONENTS:
            name = f"mom_{tag}_no{comp}"
            d = gen_v6.make(name, cfg["s_ht"], cfg["s_vt"], 15.9, cfg["xcg"],
                            "point", exclude=comp)
            gen_v6.run(d)
            cl, cd, cm = read_point(os.path.join(d, f"{name}.polar"))
            dcl, dcd, dcm = cl0 - cl, cd0 - cd, cm0 - cm
            results[tag]["components"][comp] = dict(dCL=dcl, dCD=dcd, dCMy=dcm)
            print(f"  w/o {comp:12s}: CL={cl:8.4f} CD={cd:8.5f} CMy={cm:+8.5f}"
                  f"   -> contributes dCL={dcl:+.4f} dCD={dcd:+.5f} dCMy={dcm:+.5f}")

    import json
    with open(os.path.join(gen_v6.HERE, "component_moment_results.json"), "w") as fh:
        json.dump(results, fh, indent=2)
    print("\nwrote component_moment_results.json")


if __name__ == "__main__":
    main()
