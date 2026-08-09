"""Leave-one-out component buildup: delta_Cmy(component) = Cmy_full - Cmy_without(component), a real difference of two solves (interference included, not assumed away) at alpha=3.7 deg (~cruise CL). Compares v5-equivalent (v6's closed-tail fuselage + v5's documented tail areas, avoiding the v5.vsp3 open-tail bug in doubts.md #26) against the final resized v6 tails."""
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
