"""Stage 2 SU2 volume mesh: wing+winglet+fuselage+belly fairing+tail, EULER. Differs from stage1's make_mesh_euler3.py because CFDMesh fused the ENTIRE aircraft + farfield box into ONE connected component (confirmed 2026-08-09), so there's no clean raw wing/farfield split to exploit; falls back to classifySurfaces()+createGeometry() dihedral-angle patch decomposition (like the original make_mesh_euler2.py) and bbox-sorts the resulting patches into wing_wall/symmetry/farfield. Any leftover naked-edge boundary after classification gets patched with a flat plane surface, generalizing stage1's y=0-cap fix to any symmetric body clipped at y=0. Usage: python3 make_mesh_stage2.py [--coarse]"""
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
    # 45, not stage1's 35: at 35 deg the T-tail junction (HT root meets VT tip, compound sweep) classified as one connected region with an unparametrizable 80-segment boundary -- a real 3D wetted surface, not a flat cap, so it couldn't be discarded and rebuilt flat; 45 deg regroups it cleanly (81 surfaces vs 89 at 35, not the near-collapse seen at 90's 26)
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
        # stage1 treated all leftover naked edges as one closed loop (valid there, only one gap existed); stage2 has several bodies clipped at y=0, so the 110 gap curves here form 4 disjoint closed loops (85/16/6/3), not one -- feeding them all into one addCurveLoop built a self-intersecting patch that choked the 3D fill ("Impossible to recover edge", timed out); fix: group by curve connectivity (union-find on shared endpoints) and patch each loop separately
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

        # a loop's bounding-box reach (max abs coordinate) distinguishes an OUTER boundary (far-field box rim, reaching ~FAR) from an INNER hole (an aircraft body's footprint, a few tens of ft) -- one outer loop + N inner holes bound ONE annular region and must go into a single addPlaneSurface([outer, inner1, ...]) call, not separate patches (which produced a self-intersecting outer patch that choked 3D boundary recovery)
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
        # force the patch to mesh as one un-subdivided face -- a subdivided patch produced the razor-thin overlapping sliver in stage1 (its remesh landed a node off its shared boundary)
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

    # non-uniform sizing: fine only where curvature/pressure gradients are sharp (wing/tail LEs), not the smooth fuselage barrel -- memory budget is 10GB WSL / 11.7KB per node (measured on stage1) -> ~850k node ceiling
    size_min = 0.05 * scale
    size_max = 15.0 * scale
    gmsh.option.setNumber("Mesh.MeshSizeMin", size_min)
    gmsh.option.setNumber("Mesh.MeshSizeMax", size_max)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 10 if not coarse else 6)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # plain Delaunay
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    # mesh 2D, clean up, THEN fill 3D -- stage1 found this ordering avoids a near-duplicate-triangle rejection at shared patch boundaries
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
