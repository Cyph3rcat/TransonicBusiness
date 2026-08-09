"""Strip OpenVSP's y=0 root-cap triangles out of a CFD Mesh STL.

Root cause finally located (2026-08-08): every meshing failure this session
has been an overlapping-facet pair lying exactly on the y=0 root cap --
at the root LEADING edge in the tightened export, at the root TRAILING edge
in the GUI export (30 true same-side overlaps at x=6.38-6.54, z=0.03-0.07,
where the flat cap meets the truncated blunt TE). The far-field box in the
same file has ZERO overlaps, so this is specific to how OpenVSP triangulates
the flat end cap, not a general tessellation problem.

The cap is planar by construction (y=0 exactly), so OpenVSP's triangulation
of it carries no geometric information a flat gmsh plane surface doesn't
also carry. Dropping it and letting the downstream gap-patch logic rebuild
it as a single plane is therefore lossless -- and it removes the only region
that has ever produced an overlap.

Usage: python3 strip_root_cap.py <in.stl> <out.stl> [y_tol]
"""
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
            # Only strip the cap on the WING solid; the far-field box is clean
            # and its y=0 face (if any) is a legitimate symmetry boundary.
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
