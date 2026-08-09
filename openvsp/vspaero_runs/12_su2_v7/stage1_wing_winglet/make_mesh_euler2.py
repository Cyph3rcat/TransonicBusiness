"""Stage 1 SU2 volume mesh: wing+winglet half-model, EULER -- built from OpenVSP's own CFD Mesh tool output instead of the raw STEP export, because the raw STEP export (used by make_mesh.py/make_mesh_euler.py) carries a self-intersection warning from OCC on the very first import/heal step, independent of anything downstream; OpenVSP's CFD Mesh tool output (export_wing_cfdmesh.vspscript) is a different, confirmed-watertight triangulated surface (28305 triangles, clean 40-patch classifySurfaces decomposition) that only failed later in the RANS-only BoundaryLayer field step, so with no BL needed for Euler this script picks it back up and goes straight to an isotropic tet fill. Usage: python3 make_mesh_euler2.py [--coarse]"""
import argparse
import math
import os

import gmsh

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_MSH = os.path.join(HERE, "wing_winglet_cfdmesh.msh")
FAR, FAR_TOL = 150.0, 5.0   # ft, matches export_wing_cfdmesh.vspscript's box


def classify():
    gmsh.option.setNumber("Mesh.AngleToleranceFacetOverlap", 2.0)
    # the patch-vs-neighbour duplicate triangle at the 3D fill stage is a ~1e-6 degree dihedral -- nodes coincident to within floating-point noise that removeDuplicateNodes()'s default tolerance doesn't catch, so the general snapping tolerance is loosened instead
    gmsh.merge(SRC_MSH)
    # OpenVSP's own tessellation leaves 3 stray boundary edges out of 28305 triangles (a tiny triangulation crack, not a topology error) -- merge coincident nodes within a small tolerance to stitch it before classifying
    gmsh.model.mesh.removeDuplicateNodes()
    gmsh.model.mesh.removeDuplicateElements()
    angle = 35
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
    print(f"classified surfaces: wing={len(wing_surfs)} sym={len(sym_surfs)} "
          f"far={len(far_surfs)} (total {len(surfs)})")
    if not wing_surfs or not far_surfs:
        raise RuntimeError("classification found zero wing or farfield "
                            "surfaces -- inspect before proceeding")
    return wing_surfs, sym_surfs, far_surfs, surfs


def build(coarse=False):
    scale = 2.5 if coarse else 1.0

    gmsh.initialize()
    gmsh.model.add("wing_winglet_euler2")
    gmsh.option.setNumber("General.Terminal", 1)

    wing_surfs, sym_surfs, far_surfs, all_surfs = classify()

    all_tags = [t for _, t in all_surfs]
    gaps = gmsh.model.getBoundary([(2, t) for t in all_tags], combined=True,
                                   oriented=True)
    print(f"leftover naked edges (should be empty): {gaps}")
    for dim, tag in gaps:
        bb = gmsh.model.getBoundingBox(dim, abs(tag))
        print(f"  gap curve {tag}: bbox={bb}")
    if gaps:
        # OpenVSP's own tessellation leaves tiny cracks near y=0 (root TE with the coarse skin, root LE too with the finer one) -- patch directly with a plane surface from whatever gap curves are found, rather than treating it as a hard failure
        patch_loop = gmsh.model.geo.addCurveLoop([c[1] for c in gaps])
        patch = gmsh.model.geo.addPlaneSurface([patch_loop])
        gmsh.model.geo.synchronize()
        # force this tiny patch to mesh as a single un-subdivided surface via a huge boundary point size -- a subdivided patch independently invented a point off its shared boundary, producing a razor-thin overlapping sliver (~1e-6 degree dihedral; tightening Geometry.Tolerance to 1e-7 had zero effect)
        patch_pts = gmsh.model.getBoundary([(2, patch)], recursive=True)
        gmsh.model.geo.mesh.setSize(patch_pts, 10.0)
        gmsh.model.geo.synchronize()
        print(f"patched root-TE crack with plane surface {patch}")
        all_tags.append(patch)
        sym_surfs.append(patch)

    loop = gmsh.model.geo.addSurfaceLoop(all_tags)
    vol = gmsh.model.geo.addVolume([loop])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(3, [vol], name="fluid")
    gmsh.model.addPhysicalGroup(2, wing_surfs, name="wing_wall")
    gmsh.model.addPhysicalGroup(2, sym_surfs, name="symmetry")
    gmsh.model.addPhysicalGroup(2, far_surfs, name="farfield")

    size_wing = 0.05 * scale
    size_far = 12.0 * scale
    gmsh.option.setNumber("Mesh.MeshSizeMin", size_wing)
    gmsh.option.setNumber("Mesh.MeshSizeMax", size_far)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 12 if not coarse else 6)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # plain Delaunay -- HXT chokes on a tiny overlapping-facet pair from remeshing two adjacent classified patches near their shared boundary
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    # mesh the surface first, then clean up before filling the volume -- the patch's own 2D remesh sometimes lands a node off its shared boundary, producing a near-zero-dihedral duplicate triangle (~1.2e-6 deg) that the 3D fill rejects outright, and Mesh.AngleToleranceFacetOverlap doesn't gate this regardless of value
    gmsh.model.mesh.generate(2)
    gmsh.model.mesh.removeDuplicateNodes()
    gmsh.model.mesh.removeDuplicateElements()
    gmsh.model.mesh.generate(3)

    # SU2's tutorial-standard convention is SI (meters); the model up to here is in feet (matching OpenVSP's ft-based Sref/bref/cref) -- scale only at export so nothing upstream has to change
    gmsh.option.setNumber("Mesh.ScalingFactor", 0.3048)
    out = os.path.join(HERE, "coarse_euler2.su2" if coarse else "wing_winglet_euler2.su2")
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
