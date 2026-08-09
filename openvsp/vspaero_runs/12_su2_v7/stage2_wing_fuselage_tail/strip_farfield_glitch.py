"""Drops the degenerate far-field-box-corner triangle fan from the Stage 2 STL: classifySurfaces() failed with "one edge is incident to 3 triangles", a genuine non-manifold defect (unlike stage1's near-duplicate-overlap pattern) localized to 4 edges at x in [76,80], y=0, z=152.667 -- a rounded corner of the 300 ft far-field box, ~300 ft from the aircraft (x:0-45, z:-6..+12), so unrelated to stage1's wing-root/y=0-cap lesson. Scoped tight (y=0 AND far outside the aircraft's extent) so it can't touch the wing root, VT root, or fuselage centerline, which legitimately have y=0 vertices. Usage: python3 strip_farfield_glitch.py <in.stl> <out.stl>"""
import sys

YTOL = 1e-6
FAR_GATE = 140.0   # aircraft's own extent is well inside +-45 ft


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f:
        lines = f.readlines()

    out, i, kept, dropped = [], 0, 0, 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("facet"):
            facet = lines[i:i + 7]
            verts = []
            for L in facet:
                t = L.strip().split()
                if t and t[0] == "vertex":
                    verts.append((float(t[1]), float(t[2]), float(t[3])))
            is_glitch = (len(verts) == 3 and
                        all(abs(y) < YTOL for _, y, _ in verts) and
                        all(max(abs(x), abs(z)) > FAR_GATE for x, _, z in verts))
            if is_glitch:
                dropped += 1
            else:
                out.extend(facet)
                kept += 1
            i += 7
            continue
        out.append(lines[i])
        i += 1

    with open(dst, "w") as f:
        f.writelines(out)
    print(f"kept {kept} facets, dropped {dropped} far-field-glitch facets")


if __name__ == "__main__":
    main()
