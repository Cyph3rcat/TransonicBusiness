"""Drop the degenerate far-field-box-corner triangle fan from the Stage 2 STL.

Found 2026-08-09: classifySurfaces() failed with "one edge is incident to 3
triangles" -- a genuine non-manifold defect, different in kind from stage1's
near-duplicate-overlap pattern. All 4 offending edges cluster in one tiny
spot: x in [76,80], y=0 exactly, z=152.667 -- a rounded corner of the 300 ft
far-field box, roughly 300 ft from the aircraft (which spans x:0-45,
z:-6..+12). This is a localized far-field tessellation glitch, unrelated to
the wing-root/y=0-cap lesson from stage1 -- confirmed by the fact that this
cluster sits at the OUTER box boundary, not on any aircraft body.

Deliberately scoped tight (y=0 AND far outside the aircraft's own extent) so
this cannot touch the wing root, vertical tail root, or fuselage centerline
-- all of which legitimately have y=0 vertices that must NOT be stripped.

Usage: python3 strip_farfield_glitch.py <in.stl> <out.stl>
"""
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
