"""Stage 2 SU2 volume mesh: wing+winglet+fuselage+belly fairing+tail, EULER.

Why this differs from stage1's make_mesh_euler3.py: that script's shortcut
(skip classifySurfaces/createGeometry, keep OpenVSP's triangles verbatim,
sort exactly 2 raw connected components into wing/farfield) relied on the
GUI export happening to produce 2 cleanly disconnected pieces. Checked here
first (diag_stage2_topology, 2026-08-09) and it does NOT hold: CFDMesh fused
the ENTIRE aircraft (fuselage+fairing+wing+tail) and the farfield box into
ONE connected component (40,772 of 40,778 triangles), plus 3 tiny 2-triangle
degenerate slivers at the box's top face. There is no clean raw split to
exploit here.

So this goes back to the classifySurfaces()+createGeometry() approach
(dihedral-angle patch decomposition, same as the ORIGINAL make_mesh_euler2.py
before the stage1 shortcut was found) -- it doesn't need a clean raw
connectivity split because it re-derives real parametrized surface patches
from the triangle soup directly, then sorts THOSE by bounding box into
wing_wall / symmetry / farfield.

y=0 cap handling: stage1's root cause (OpenVSP mis-triangulating a flat
symmetry-plane cap, confirmed 2026-08-08/09 by finding real overlapping
facets there and by the crash disappearing once tighter export settings
happened to clean that face up on their own) generalizes here as a
first-class step: any leftover naked-edge boundary after classification gets
patched with ONE flat plane surface, exactly like stage1's proven fix,
regardless of which body (wing, vertical tail, dorsal fin) the gap belongs
to -- same technique, general to any symmetric part clipped at y=0.

Usage:  python3 make_mesh_stage2.py [--coarse]
"""
import argparse
import math
import os

import gmsh

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_STL = os.path.join(HERE, "stage2_cfdmesh_boxstrip2.stl")
FAR, FAR_TOL = 150.0, 5.0   # ft, matches export_stage2_cfdmesh.vspscript's box


def classify():
    gmsh.option.setNumber("Mesh.AngleToleranceFacetOverlap", 0.01)
    gmsh.merge(SRC_STL)
    gmsh.model.mesh.removeDuplicateNodes()
    gmsh.model.mesh.removeDuplicateElements()
    # 45, not stage1's 35: at 35 deg, one patch at the T-tail junction (where
    # the horizontal tail root meets the vertical tail tip, both swept,
    # meeting at a compound angle) classified as a single connected region
    # with an 80-segment boundary that createGeometry() could not
    # parametrize. Confirmed to be REAL 3D wetted surface, not a flat y=0 cap
    # (0 of 898 triangles fully at y=0) -- so this could not be discarded and
    # rebuilt flat like every previous fix this session. Bumping to 45 deg
    # regroups that same triangle soup into patches with cleaner boundaries;
    # tested 45/60/90, all pass, 45 chosen as the smallest change that fixes
    # it (81 surfaces vs 89 at 35 deg -- not the near-total collapse seen at
    # 90 deg's 26 surfaces).
    angle = 45
    gmsh.model.mesh.classifySurfaces(angle * math.pi / 180.0, True, True, 0.01)
    gmsh.model.mesh.createGeometry()

    surfs = gmsh.model.getEntities(2)
    wing_surfs, sym_surfs, far_surfs = [], [], []
    for dim, tag in surfs:
        bb = gmsh.model.getBoundingBox(dim, tag)
        xmin, ymin, zmin, xmax, ymax, zmax = bb
        is_sym = (ymax - ymin) < 1e-4 and ymin < 1e-3
        touches_far = (xmin < -FAR + FAR_TOL or xmax > FAR - FAR_TOL or
                       zmin < -FAR + FAR_TOL or zmax > FAR - FAR_TOL or
                       ymax > FAR - FAR_TOL)
        if is_sym:
            sym_surfs.append(tag)
        elif touches_far:
            far_surfs.append(tag)
        else:
            wing_surfs.append(tag)
    print(f"classified surfaces: wetted={len(wing_surfs)} sym={len(sym_surfs)} "
          f"far={len(far_surfs)} (total {len(surfs)})")
    if not wing_surfs or not far_surfs:
        raise RuntimeError("classification found zero wetted or farfield "
                            "surfaces -- inspect before proceeding")
    return wing_surfs, sym_surfs, far_surfs, surfs


def build(coarse=False):
    scale = 2.0 if coarse else 1.0

    gmsh.initialize()
    gmsh.model.add("stage2_euler")
    gmsh.option.setNumber("General.Terminal", 1)

    wing_surfs, sym_surfs, far_surfs, all_surfs = classify()

    all_tags = [t for _, t in all_surfs]
    gaps = gmsh.model.getBoundary([(2, t) for t in all_tags], combined=True,
                                   oriented=True)
    print(f"leftover naked edges (should be small/empty): {len(gaps)}")

    if gaps:
        # Stage1 (make_mesh_euler3.py) treated all leftover naked edges as
        # ONE closed loop -- valid there because there was only ever one
        # gap. Stage2 has many more bodies clipped at y=0 (fuselage, belly
        # fairing, wing, vertical tail, horizontal tail), so a single
        # combined boundary can legitimately be SEVERAL separate holes, not
        # one. Confirmed by inspection (2026-08-09): 110 gap curves here
        # form 4 disjoint closed loops (85/16/6/3 curves), not one -- feeding
        # all 110 into a single addCurveLoop built an invalid, effectively
        # self-intersecting "patch" that the 3D fill then choked on
        # (repeating "Impossible to recover edge" warnings, timed out at 30
        # min with no progress -- same stuck-loop signature as stage1's
        # aborted CFD-source attempt). Fix: group by curve connectivity
        # (union-find on shared endpoint vertices) and patch each loop with
        # its own plane surface.
        by_curve_pts = {}
        for dim, tag in gaps:
            pts = gmsh.model.getBoundary([(1, abs(tag))], combined=False,
                                         oriented=False)
            by_curve_pts[tag] = [p[1] for p in pts]

        parent = {}

        def find(x):
            root = x
            while parent.get(root, root) != root:
                root = parent[root]
            while parent.get(x, x) != root:
                parent[x], x = root, parent.get(x, x)
            return root

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for tag, pts in by_curve_pts.items():
            parent.setdefault(tag, tag)
            for p in pts:
                parent.setdefault(p, p)
                union(tag, p)

        groups = {}
        for tag in by_curve_pts:
            groups.setdefault(find(tag), []).append(tag)
        print(f"grouped into {len(groups)} disjoint loop(s): "
              f"{sorted((len(v) for v in groups.values()), reverse=True)}")

        # A loop's own bounding-box "reach" (max abs coordinate over its
        # points) distinguishes an OUTER boundary (the far-field box rim,
        # reaching ~FAR) from an INNER hole (an aircraft body's footprint,
        # reaching only a few tens of ft). This matters structurally, not
        # just cosmetically: one outer loop + N inner holes bound ONE
        # annular flat region and MUST go into a single addPlaneSurface
        # call as [outer, inner1, inner2, ...] -- treating each disjoint
        # group as its own independent patch (the original approach) is
        # only correct when the holes truly don't nest, and produced a
        # broken, self-intersecting "outer" patch here that choked the 3D
        # boundary-recovery step (confirmed 2026-08-09: the box's rim and
        # an aircraft footprint hole are exactly this outer/inner case).
        def reach(tags):
            r = 0.0
            for t in tags:
                for p in by_curve_pts[t]:
                    c = gmsh.model.getValue(0, p, [])
                    r = max(r, abs(c[0]), abs(c[2]))
            return r

        ranked = sorted(groups.values(), key=reach, reverse=True)
        outer_tags = ranked[0]
        inner_groups = ranked[1:]
        print(f"  outer loop: {len(outer_tags)} curves (reach {reach(outer_tags):.1f} ft)")
        for ig, tags in enumerate(inner_groups):
            print(f"  inner hole {ig}: {len(tags)} curves (reach {reach(tags):.1f} ft)")

        outer_loop = gmsh.model.geo.addCurveLoop(outer_tags)
        inner_loops = [gmsh.model.geo.addCurveLoop(tags) for tags in inner_groups]
        patch = gmsh.model.geo.addPlaneSurface([outer_loop] + inner_loops)
        gmsh.model.geo.synchronize()
        # Force the patch to mesh as one un-subdivided face -- a subdivided
        # patch is what produced the razor-thin overlapping sliver in
        # stage1 (its own remesh landed a node a hair off the shared
        # boundary with its neighbour).
        patch_pts = gmsh.model.getBoundary([(2, patch)], recursive=True)
        gmsh.model.geo.mesh.setSize(patch_pts, 10.0)
        gmsh.model.geo.synchronize()
        print(f"patched far-field y=0 annulus with plane surface {patch}")
        all_tags.append(patch)
        sym_surfs.append(patch)

    loop = gmsh.model.geo.addSurfaceLoop(all_tags)
    vol = gmsh.model.geo.addVolume([loop])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(3, [vol], name="fluid")
    gmsh.model.addPhysicalGroup(2, wing_surfs, name="wing_wall")
    gmsh.model.addPhysicalGroup(2, sym_surfs, name="symmetry")
    gmsh.model.addPhysicalGroup(2, far_surfs, name="farfield")

    # Non-uniform sizing (per the plan agreed 2026-08-08): fine only where
    # curvature/pressure gradients are sharp (wing/tail leading edges), not
    # uniformly fine everywhere -- the fuselage is a big smooth barrel that
    # doesn't need wing-nose-grade resolution, and stage2 is already a much
    # bigger model than stage1 (memory budget: 10GB WSL limit / 11.7KB/node
    # measured on stage1 -> ~850k node ceiling).
    size_min = 0.05 * scale
    size_max = 15.0 * scale
    gmsh.option.setNumber("Mesh.MeshSizeMin", size_min)
    gmsh.option.setNumber("Mesh.MeshSizeMax", size_max)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 10 if not coarse else 6)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # plain Delaunay
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    # Mesh 2D, clean up, THEN fill 3D -- stage1 found this ordering (not one
    # monolithic generate(3) call) avoids a near-duplicate-triangle rejection
    # at shared patch boundaries.
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.removeDuplicateNodes()
    gmsh.model.mesh.removeDuplicateElements()
    gmsh.model.mesh.generate(3)

    gmsh.option.setNumber("Mesh.ScalingFactor", 0.3048)
    out = os.path.join(HERE, "coarse_stage2.su2" if coarse else "stage2_wing_fuselage_tail.su2")
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
