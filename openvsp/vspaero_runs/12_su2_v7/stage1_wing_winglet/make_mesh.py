"""Stage 1 SU2 volume mesh: wing+winglet half-model, wall-function RANS.

v3: real 3D prism boundary layer via gmsh.model.geo.extrudeBoundaryLayer(),
following gmsh's own official example (naca_boundary_layer_3d.py, shipped
with the gmsh pip package under share/doc/gmsh/examples/api/). Two earlier
attempts failed and are why this one looks the way it does:

  v1 (raw STEP -> OCC solid -> boolean-cut a farfield sphere): OpenVSP's STEP
     export is an open shell at the wing ROOT (by design -- Sym_Planar_Flag
     is off so there's no fuselage to blend into, the root cross-section is
     just... open, meant to sit flush on a symmetry plane). OCC's boolean
     cut needs a closed solid operand; healShapes(makeSolids=True) could not
     close it. Boolean cut failed every time ("BOPAlgo_AlertTooFewArguments").

  v2 (OpenVSP's own CFD Mesh tool -> classifySurfaces -> field-based
     BoundaryLayer): the CFD Mesh tool DID produce a clean watertight
     half-model triangle soup (wing + symmetry cap + farfield box, no
     boolean needed) -- that half is solid. But gmsh 4.15.2's
     mesh.field "BoundaryLayer" type only accepts NodesList/EdgesList
     (verified by probing every option name it supports) -- it is a 2D
     curve-extrusion field, not a 3D surface one, in this build. There is no
     way to hand it the wing's *surfaces*.

v3 uses gmsh's dedicated (non-Field) 3D boundary-layer API instead:
extrudeBoundaryLayer() extrudes prism layers directly off a list of
surfaces. It doesn't need a closed solid to start from (works on the STEP
import's open shell directly) and doesn't touch the Field system at all.
The official example handles exactly our topology -- a wing-like body open
only where it meets a symmetry plane -- by extruding the BL, then using the
boundary curve of the BL stack's outer ("top") surface as a hole cut into a
flat symmetry-plane face. No boolean anywhere in this script.

Wall spacing: y+~30-100 (wall-function RANS), not the y+~1 cfdinstructions.md
literally asked for -- decided 2026-08-07 against the 7.6GB-RAM/no-MPI WSL
box, which can't hold the ~40-45 layers y+~1 needs (see stage1 planning
notes). y+~30-100 needs ~16 layers instead.

Usage:  python3 make_mesh.py [--coarse]
"""
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

# Winglet tip chord is 0.95 ft (12%-thick section -> ~0.114 ft physical
# thickness there), far smaller than the 5.0236 ft MAC the y+ spacing above
# was sized against. A BL stack sized for the root chord's scale, applied
# uniformly (extrudeBoundaryLayer only takes one height list for every input
# surface), swallows most of the winglet tip's own cross-section and folds
# over itself -- this, not TE sharpness, is what actually caused the first
# "PLC Error: segment and facet intersect" failure (confirmed: 8 layers @
# growth 1.2 sums to ~6.3mm total, <20% of the tip's ~35mm thickness, vs the
# original 16 layers @ 1.25 summing to ~35-50mm -- comparable to the tip
# thickness itself).

FAR = 150.0    # ft, half-extent of the box beyond the wing's own bbox


def build(coarse=False):
    scale = 2.5 if coarse else 1.0
    # BL geometry (y1, layer count) is NOT scaled by `coarse` -- it's already
    # sized against the smallest feature on the wing (the winglet tip chord),
    # so making it coarser here would reopen the tip self-intersection this
    # sizing was chosen to avoid. `coarse` only relaxes surface/farfield
    # tessellation, below.
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

    # The STEP import already contains the wing's OWN flat root-cap patch,
    # sitting exactly at y=0 (found by inspection: one surface has a y
    # bounding box of (0,0) while every other surface spans a real y range).
    # Boundary-layer-extruding THAT cap too (my first three attempts did)
    # is nonsensical -- there's no flow normal to a symmetry-plane cap -- and
    # is what actually produced a small, thickness- and crease-independent
    # self-intersection every time, since offsetting a degenerate flat cap
    # by a surface normal is ill-conditioned. Fix: exclude it from the BL
    # extrusion and use its own (already exactly planar) boundary curve
    # directly for the symmetry-plane hole -- the wetted surfaces' naked
    # root edge, left un-extruded, still matches it exactly.
    # Same failure family as this project's earlier belly-fairing width-sliver
    # bug (doubts.md #20/#22): the airfoil's small existing TE gap (~0.55%
    # chord), interpolated down to the 0.95 ft winglet tip chord and further
    # split across the 4-station crease blend, produces genuinely
    # zero-area sliver TE-cap patches at the tip (found by inspection:
    # gmsh.model.occ.getMass reports 0.00000 ft^2 for two of the 21
    # surfaces, exactly at HXT's reported intersection point). A
    # boundary-layer offset of a zero-area surface has no defined normal --
    # exclude any surface with area < 1e-3 ft^2 from the BL extrusion, same
    # treatment as the root cap.
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

    # HXT pinpointed the intersection to (10.49, 22.10, 1.91) -- right at
    # the winglet's outermost sub-panel (chord tapers to 0.95 ft there,
    # smallest on the whole wing). The full-thickness BL stack (~1.5-5mm)
    # is comparable to that panel's own physical TE thickness -- an offset
    # surface pinching shut on itself, same mechanism as the earlier crease
    # failure, just from small local scale instead of a sharp angle.
    #
    # Tried and rejected: (a) uniform TE blunting -- matching the BL stack's
    # absolute size at this chord needs a ~5-6% chord TE gap there, which at
    # the root's 6.9 ft chord would be a 0.35+ ft blunt TE, a real shape
    # change, not a meshing tweak; (b) splitting into a thin-BL group for
    # just the tip panel -- extrudeBoundaryLayer'd separately, its side
    # walls don't reconcile with the neighbouring full-thickness group at
    # their shared seam ("Could not find extruded node" at that same point).
    #
    # Settled on: one UNIFORM, thinner stack for the whole wing, sized off
    # the tip's constraint instead of the root's. y+ at the root drops from
    # the ~30 target to ~7.5 -- inside the buffer layer rather than the
    # log-law region, a real accuracy cost for the production mesh, but
    # avoids every failure mode above and is fine for this validation pass.
    y1 = y1 / 4.0
    d = [y1]
    for i in range(1, n_layers):
        d.append(d[-1] + y1 * GROWTH ** i)
    print(f"revised uniform y1={y1:.3e} ft ({y1*304.8:.4f} mm), "
          f"total stack={d[-1]*304.8:.4f} mm")
    extbl = gmsh.model.geo.extrudeBoundaryLayer(
        wing_surfs, [1] * n_layers, d, True)
    gmsh.model.geo.synchronize()
    # extrudeBoundaryLayer returns, per input surface, a run of entities
    # ending in its dim=3 volume; the dim=2 entry right before the volume is
    # that surface's outer ("top") cap, already collected below. The OTHER
    # dim=2 entries in each run are the prism stack's vertical side walls.
    # Most of those sit at internal seams shared between adjacent wing
    # panels and must stay internal (excluding them from the outer boundary
    # is correct). But the panels touching the naked ROOT edge (y=0) also
    # get a side wall there -- and THAT one has to be included, or the
    # outer skin (offset away from y=0 by the BL thickness) leaves an
    # un-closed sliver ring against the symmetry-plane hole cut from
    # root_cap's un-offset boundary. Found via an explicit leftover-naked-
    # edge check on the full assembly (8 small gap curves, all near the
    # root) after the first version of this script only ever collected
    # "top" and dropped every side wall unconditionally.
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
    # Use the root cap's OWN boundary (guaranteed exactly planar, since it's
    # a real flat OCC face) rather than the BL top surfaces' boundary --
    # the wetted surfaces were never extruded at their naked root edge, so
    # it still lines up with this curve exactly.
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
    # HXT (10), not plain Delaunay (1) -- gmsh's own official 3D wing
    # boundary-layer example (naca_boundary_layer_3d.py) uses HXT
    # specifically; it's the more robust fill algorithm for reconciling a
    # sub-mm near-wall mesh against a 10s-of-ft farfield in one pass.
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
