"""Stage 1 SU2 volume mesh: wing+winglet half-model, wall-function RANS, using gmsh's 3D boundary-layer extrudeBoundaryLayer() API (v3) -- v1 (STEP->OCC boolean-cut a farfield sphere) failed because OpenVSP's STEP export leaves an open shell at the wing root and OCC's boolean cut needs a closed solid; v2 (OpenVSP's own CFD Mesh tool, watertight) failed because gmsh 4.15.2's BoundaryLayer field only accepts NodesList/EdgesList, not 3D surfaces. Wall spacing targets y+~30-100, not the y+~1 cfdinstructions.md asks for, since the 7.6GB-RAM/no-MPI WSL box can't hold the ~40-45 layers y+~1 would need. Usage: python3 make_mesh.py [--coarse]"""
import argparse
import math
import os

import gmsh

HERE = os.path.dirname(os.path.abspath(__file__))
STEP = os.path.join(HERE, "wing_winglet.stp")

# ---- freestream & wall-spacing derivation (FL410, M0.80) -------------------
RHO, VINF, MU = 5.581e-4, 774.5, 2.877e-7          # slug/ft^3, ft/s, slug/(ft.s)
NU = MU / RHO
CREF, SEMISPAN = 5.0236, 23.166                     # ft
RE_MAC = RHO * VINF * CREF / MU

CF = 0.455 / (math.log10(RE_MAC)) ** 2.58           # Schlichting flat-plate
TAU_W = 0.5 * CF * RHO * VINF ** 2
U_TAU = math.sqrt(TAU_W / RHO)
YPLUS_TARGET = 30.0
Y1 = YPLUS_TARGET * NU / U_TAU                       # first prism layer height, ft
GROWTH = 1.20
N_LAYERS = 8

# winglet tip chord (0.95 ft, ~0.114 ft thick) is far smaller than the 5.0236 ft MAC the y+ spacing was sized against -- a uniform BL stack sized for the root swallows the tip's cross-section and folds over itself; this, not TE sharpness, caused the first "PLC Error: segment and facet intersect" failure (8 layers @1.2 ~6.3mm vs the original 16 layers @1.25 ~35-50mm, comparable to the tip's own ~35mm thickness)

FAR = 150.0    # ft, half-extent of the box beyond the wing's own bbox


def build(coarse=False):
    scale = 2.5 if coarse else 1.0
    # BL geometry (y1, layer count) is NOT scaled by `coarse` -- it's sized against the winglet tip chord already, so coarsening it would reopen the tip self-intersection; `coarse` only relaxes surface/farfield tessellation
    n_layers = N_LAYERS - (2 if coarse else 0)
    y1 = Y1

    gmsh.initialize()
    gmsh.model.add("wing_winglet")
    gmsh.option.setNumber("General.Terminal", 1)
    gmsh.option.setString("Geometry.OCCTargetUnit", "FT")   # STEP is mm; model is ft
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
    if ymin > 0.01:
        raise RuntimeError(f"wing root not at y=0 (ymin={ymin}) -- the "
                            "symmetry-plane hole logic below assumes it is")

    # STEP import includes the wing's own flat y=0 root-cap patch; BL-extruding it is nonsensical (no flow normal to a symmetry cap) and was what produced small crease-independent self-intersections every time, so it's excluded here and its own planar boundary curve is used directly for the symmetry-plane hole (the wetted surfaces' naked root edge, left un-extruded, still matches it exactly). Same failure family as the belly-fairing sliver bug (doubts.md #20/#22): interpolating the airfoil's ~0.55% chord TE gap down to the 0.95 ft winglet tip produces genuine zero-area sliver TE-cap surfaces (area<1e-3 ft^2, confirmed via gmsh.model.occ.getMass), which get the same BL-extrusion exclusion since a zero-area surface has no defined normal
    root_cap, wing_surfs, degenerate = None, [], []
    for dim, tag in all_surfs:
        bb = gmsh.model.getBoundingBox(dim, tag)
        area = gmsh.model.occ.getMass(dim, tag)
        if abs(bb[1]) < 1e-6 and abs(bb[4]) < 1e-6:
            root_cap = (dim, tag)
        elif area < 1e-3:
            degenerate.append((dim, tag))
        else:
            wing_surfs.append((dim, tag))
    if root_cap is None:
        raise RuntimeError("no flat y=0 root-cap surface found among the "
                            "STEP import -- inspect before proceeding")
    print(f"root cap: {root_cap}, degenerate slivers excluded: {degenerate}, "
          f"wetted BL surfaces: {len(wing_surfs)}")

    print(f"\n--- mesh recipe ---")
    print(f"Re_MAC={RE_MAC:.3e}  Cf={CF:.5f}  u_tau={U_TAU:.2f} ft/s")
    print(f"y1 (y+={YPLUS_TARGET:.0f}) = {y1:.3e} ft = {y1*304.8:.4f} mm")
    print(f"n_layers={n_layers}  growth={GROWTH}")

    # HXT pinpointed the intersection at (10.49, 22.10, 1.91), the winglet's outermost sub-panel (chord tapers to 0.95 ft there), where the full-thickness BL stack (~1.5-5mm) is comparable to the panel's own TE thickness. Tried and rejected: uniform TE blunting (needs a 0.35+ ft blunt TE at the root's 6.9 ft chord, a real shape change) and a separate thin-BL group for just the tip panel (side walls didn't reconcile with the full-thickness group at the shared seam). Settled on one uniform thinner stack sized off the tip instead of the root -- root y+ drops from the ~30 target to ~7.5 (inside the buffer layer, a real accuracy cost) but avoids every failure mode above and is fine for this validation pass.
    y1 = y1 / 4.0
    d = [y1]
    for i in range(1, n_layers):
        d.append(d[-1] + y1 * GROWTH ** i)
    print(f"revised uniform y1={y1:.3e} ft ({y1*304.8:.4f} mm), "
          f"total stack={d[-1]*304.8:.4f} mm")
    extbl = gmsh.model.geo.extrudeBoundaryLayer(
        wing_surfs, [1] * n_layers, d, True)
    gmsh.model.geo.synchronize()
    # extrudeBoundaryLayer returns each input surface's prism-stack entities ending in its dim=3 volume; the dim=2 entry just before it is the outer "top" cap (collected below), the rest are internal side walls at shared seams -- except the side walls at the naked y=0 root edge, which must also be kept or the offset outer skin leaves an unclosed sliver ring against the symmetry-plane hole (found via 8 leftover gap curves near the root when the first version only ever kept "top")
    top, root_sides = [], []
    for i in range(1, len(extbl)):
        if extbl[i][0] == 3:
            top.append(extbl[i - 1])
        elif extbl[i][0] == 2:
            try:
                bb = gmsh.model.getBoundingBox(*extbl[i])
            except Exception:
                continue
            if bb[1] <= 1e-6 <= bb[4]:
                root_sides.append(extbl[i])
    print(f"BL 'top' surfaces: {len(top)}, root-closing side walls: {len(root_sides)}")
    top = top + root_sides

    # ---- symmetry-plane face (y=0) with a hole where the wing root sits --
    # use the root cap's own boundary (guaranteed planar) rather than the BL top surfaces' boundary -- the wetted surfaces were never extruded at their naked root edge, so it still lines up exactly
    bnd = gmsh.model.getBoundary([root_cap], combined=True, oriented=True)
    hole_loop = gmsh.model.geo.addCurveLoop([c[1] for c in bnd])

    x0, x1 = xmin - FAR, xmax + FAR
    z0, z1 = zmin - FAR, zmax + FAR
    y1f = ymax + FAR   # far extent in the +y (outboard) direction

    def pt(x, y, z):
        return gmsh.model.geo.addPoint(x, y, z)

    # y=0 (symmetry) face corners
    p1, p2, p3, p4 = pt(x0, 0, z0), pt(x1, 0, z0), pt(x1, 0, z1), pt(x0, 0, z1)
    # y=y1f (outer) face corners
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
    all_faces = [t[1] for t in top] + box_faces
    gmsh.model.geo.synchronize()
    gaps = gmsh.model.getBoundary([(2, t) for t in all_faces], combined=True,
                                   oriented=False)
    print(f"leftover naked edges in the full assembly (should be empty): "
          f"{gaps}")
    for dim, tag in gaps:
        bb = gmsh.model.getBoundingBox(dim, tag)
        print(f"  gap curve {tag}: bbox={bb}")
    sl = gmsh.model.geo.addSurfaceLoop(all_faces)
    vol = gmsh.model.geo.addVolume([sl])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(3, [vol], name="fluid")
    gmsh.model.addPhysicalGroup(2, [t[1] for t in top], name="wing_wall")
    gmsh.model.addPhysicalGroup(2, [sym_face], name="symmetry")
    gmsh.model.addPhysicalGroup(2, box_faces[1:], name="farfield")

    size_far = 10.0 * scale
    gmsh.model.geo.mesh.setSize([(0, p) for p in (p1, p2, p3, p4, p5, p6, p7, p8)],
                                 size_far)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    # HXT (10), not plain Delaunay (1) -- gmsh's own naca_boundary_layer_3d.py example uses HXT, the more robust fill for reconciling a sub-mm near-wall mesh against a 10s-of-ft farfield in one pass
    gmsh.option.setNumber("Mesh.Algorithm3D", 10)
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    gmsh.model.mesh.generate(3)

    out = os.path.join(HERE, "coarse.su2" if coarse else "wing_winglet.su2")
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
