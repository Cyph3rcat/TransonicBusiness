"""Stage 1 SU2 volume mesh: wing+winglet half-model, EULER (inviscid).

Pivoted from RANS/wall-function 2026-08-08 after 7 distinct, real failures
in gmsh's 3D boundary-layer extrusion on this geometry (unit mismatch, an
unsafe BL-thickness-vs-tip-chord ratio, a sharp winglet crease, a wrongly
BL-extruded root cap, degenerate zero-area TE slivers at the tip, a
mismatched split-BL seam, and finally a persistent small un-closed gap at
the root that was never fully root-caused). Every one of those was about
the ANISOTROPIC OFFSET SURFACE a boundary layer needs -- Euler needs no
boundary layer at all, just a closed watertight surface and an isotropic
tet fill, which sidesteps the entire failure family:
  - no y+/wall spacing, no prism layers, no offset-surface self-intersection
  - the degenerate TE slivers and the root cap are still handled explicitly
    below (they're real STEP-export quirks, not RANS-specific), but with no
    extrusion step there's no possibility of an offset-vs-original mismatch
  - much smaller cell count is fine (no viscous sublayer to resolve), so
    this is also far cheaper to solve, consistent with the earlier decision
    to drop y+~1 for hardware reasons -- Euler sidesteps that whole
    constraint rather than compromising around it

Usage:  python3 make_mesh_euler.py [--coarse]
"""
import argparse
import math
import os

import gmsh

HERE = os.path.dirname(os.path.abspath(__file__))
STEP = os.path.join(HERE, "wing_winglet.stp")

FAR = 150.0    # ft, half-extent of the box beyond the wing's own bbox


def build(coarse=False):
    scale = 2.5 if coarse else 1.0

    gmsh.initialize()
    gmsh.model.add("wing_winglet_euler")
    gmsh.option.setNumber("General.Terminal", 1)
    gmsh.option.setString("Geometry.OCCTargetUnit", "FT")
    gmsh.option.setNumber("Geometry.OCCFixDegenerated", 1)
    gmsh.option.setNumber("Geometry.OCCFixSmallEdges", 1)
    gmsh.option.setNumber("Geometry.OCCFixSmallFaces", 1)
    gmsh.option.setNumber("Geometry.OCCSewFaces", 1)

    gmsh.model.occ.importShapes(STEP)
    gmsh.model.occ.synchronize()
    gmsh.model.occ.removeAllDuplicates()
    gmsh.model.occ.synchronize()

    all_surfs = gmsh.model.occ.getEntities(2)
    print(f"wing surfaces from STEP: {len(all_surfs)}")
    bbox = gmsh.model.getBoundingBox(-1, -1)
    print(f"wing bbox: {bbox}")
    xmin, ymin, zmin, xmax, ymax, zmax = bbox

    # Same root-cap / degenerate-sliver identification as the RANS attempt
    # (see make_mesh.py history) -- the root cap sits exactly at y=0, and
    # two TE-cap slivers at the small-chord winglet tip are genuinely
    # zero-area. No BL means there's no offset step to go wrong here, but
    # the slivers can still choke tet meshing directly, so still drop them.
    root_cap, wing_surfs, degenerate = None, [], []
    for dim, tag in all_surfs:
        bb = gmsh.model.getBoundingBox(dim, tag)
        area = gmsh.model.occ.getMass(dim, tag)
        if abs(bb[1]) < 1e-6 and abs(bb[4]) < 1e-6:
            root_cap = (dim, tag)
        elif area < 1e-2:
            degenerate.append((dim, tag))
        else:
            wing_surfs.append((dim, tag))
    print(f"root cap: {root_cap}, degenerate slivers excluded: {degenerate}, "
          f"wetted wall surfaces: {len(wing_surfs)}")

    # ---- symmetry-plane face (y=0) with a hole where the wing root sits --
    # No BL offset this time, so the wetted surfaces' naked root edge sits
    # EXACTLY at y=0, matching root_cap's boundary with no gap (the RANS
    # attempt's persistent unclosed-root-gap was specifically an offset
    # mismatch, which doesn't exist here).
    bnd = gmsh.model.getBoundary([root_cap], combined=True, oriented=True)
    hole_loop = gmsh.model.geo.addCurveLoop([c[1] for c in bnd])

    x0, x1 = xmin - FAR, xmax + FAR
    z0, z1 = zmin - FAR, zmax + FAR
    y1f = ymax + FAR

    def pt(x, y, z):
        return gmsh.model.geo.addPoint(x, y, z)

    p1, p2, p3, p4 = pt(x0, 0, z0), pt(x1, 0, z0), pt(x1, 0, z1), pt(x0, 0, z1)
    p5, p6, p7, p8 = pt(x0, y1f, z0), pt(x1, y1f, z0), pt(x1, y1f, z1), pt(x0, y1f, z1)

    l12, l23, l34, l41 = (gmsh.model.geo.addLine(p1, p2), gmsh.model.geo.addLine(p2, p3),
                           gmsh.model.geo.addLine(p3, p4), gmsh.model.geo.addLine(p4, p1))
    l56, l67, l78, l85 = (gmsh.model.geo.addLine(p5, p6), gmsh.model.geo.addLine(p6, p7),
                           gmsh.model.geo.addLine(p7, p8), gmsh.model.geo.addLine(p8, p5))
    l15, l26, l37, l48 = (gmsh.model.geo.addLine(p1, p5), gmsh.model.geo.addLine(p2, p6),
                           gmsh.model.geo.addLine(p3, p7), gmsh.model.geo.addLine(p4, p8))

    sym_outer = gmsh.model.geo.addCurveLoop([l12, l23, l34, l41])
    sym_face = gmsh.model.geo.addPlaneSurface([sym_outer, hole_loop])
    far_face = gmsh.model.geo.addPlaneSurface([gmsh.model.geo.addCurveLoop([l56, l67, l78, l85])])
    s_bot = gmsh.model.geo.addPlaneSurface([gmsh.model.geo.addCurveLoop([l12, l26, -l56, -l15])])
    s_top = gmsh.model.geo.addPlaneSurface([gmsh.model.geo.addCurveLoop([l34, l48, -l78, -l37])])
    s_in = gmsh.model.geo.addPlaneSurface([gmsh.model.geo.addCurveLoop([l41, l15, -l85, -l48])])
    s_out = gmsh.model.geo.addPlaneSurface([gmsh.model.geo.addCurveLoop([l23, l37, -l67, -l26])])
    box_faces = [sym_face, far_face, s_bot, s_top, s_in, s_out]
    gmsh.model.geo.synchronize()

    # wing_surfs are still OCC entities; box faces are geo-kernel. Both live
    # in the same model after synchronize() and can go in one surface loop.
    all_faces = [t[1] for t in wing_surfs] + box_faces
    gaps = gmsh.model.getBoundary([(2, t) for t in all_faces], combined=True,
                                   oriented=False)
    print(f"leftover naked edges (should be empty): {gaps}")
    if gaps:
        raise RuntimeError("assembly not watertight -- inspect gaps before "
                            "meshing blind")

    sl = gmsh.model.geo.addSurfaceLoop(all_faces)
    vol = gmsh.model.geo.addVolume([sl])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(3, [vol], name="fluid")
    gmsh.model.addPhysicalGroup(2, [t[1] for t in wing_surfs], name="wing_wall")
    gmsh.model.addPhysicalGroup(2, [sym_face], name="symmetry")
    gmsh.model.addPhysicalGroup(2, box_faces[1:], name="farfield")

    # Isotropic sizing only -- no y+ concern for Euler. 1-2% of local chord
    # near the wing is standard for capturing curvature/shock resolution;
    # coarse relaxes this and the farfield size for a quick pipeline check.
    size_wing = 0.05 * scale
    size_far = 12.0 * scale
    gmsh.option.setNumber("Mesh.MeshSizeMin", size_wing)
    gmsh.option.setNumber("Mesh.MeshSizeMax", size_far)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 12 if not coarse else 6)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 10)   # HXT
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    gmsh.model.mesh.generate(3)

    out = os.path.join(HERE, "coarse_euler.su2" if coarse else "wing_winglet_euler.su2")
    gmsh.write(out)
    nnodes = gmsh.model.mesh.getNodes()[0]
    print(f"\nwrote {out}")
    print(f"node count: {len(nnodes)}")

    gmsh.finalize()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--coarse", action="store_true")
    a = ap.parse_args()
    build(coarse=a.coarse)
