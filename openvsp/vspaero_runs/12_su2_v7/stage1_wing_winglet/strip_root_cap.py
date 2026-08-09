"""Strips OpenVSP's y=0 root-cap triangles from a CFD Mesh STL: every meshing failure this session was an overlapping-facet pair lying exactly on that flat cap (root LE in the tightened export, root TE in the GUI export) while the far-field box in the same file had zero overlaps -- specific to how OpenVSP triangulates the cap, not a general tessellation problem. The cap is planar by construction, so dropping it and letting the downstream gap-patch logic rebuild it as a single gmsh plane is lossless and removes the only region that has ever produced an overlap. Usage: python3 strip_root_cap.py <in.stl> <out.stl> [y_tol]"""
import sys


def main():
    src, dst = sys.argv[1], sys.argv[2]
    ytol = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-7

    with open(src) as f:
        lines = f.readlines()

    out, i = [], 0
    n_kept = n_dropped = 0
    cur_solid = None
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("solid"):
            cur_solid = s.split(None, 1)[1] if len(s.split(None, 1)) > 1 else ""
            out.append(lines[i]); i += 1; continue
        if s.startswith("facet"):
            facet = lines[i:i + 7]          # facet/outer/3x vertex/endloop/endfacet
            ys = []
            for L in facet:
                t = L.strip().split()
                if t and t[0] == "vertex":
                    ys.append(float(t[2]))
            # only strip the cap on the WING solid; the far-field box is clean and its y=0 face (if any) is a legitimate symmetry boundary
            is_cap = (len(ys) == 3 and all(abs(y) < ytol for y in ys)
                      and "FarField" not in (cur_solid or ""))
            if is_cap:
                n_dropped += 1
            else:
                out.extend(facet); n_kept += 1
            i += 7; continue
        out.append(lines[i]); i += 1

    with open(dst, "w") as f:
        f.writelines(out)
    print(f"kept {n_kept} facets, dropped {n_dropped} root-cap facets")
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
