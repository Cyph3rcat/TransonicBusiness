"""Stage 1 SU2 volume mesh, EULER -- v3, built on the actual root cause.

WHAT WAS ACTUALLY WRONG (found 2026-08-08, after ~7 failed approaches)
----------------------------------------------------------------------
Every meshing failure this session was an overlapping-facet pair lying
exactly on the y=0 root cap:

  * tightened script export -> crack/overlap at the root LEADING edge, y=0
  * GUI export (half-mesh off) -> 30 true same-side overlapping pairs at the
    root TRAILING edge, x=6.38-6.54 (root chord 6.909, blunt TE cut at
    x/c=0.95 -> 6.563), z=0.03-0.07, y=0
  * the far-field box in the very same file -> ZERO overlaps

Same face both times, and only that face. So it is not mesh resolution, not
gmsh, and not a repairable input defect in the general sense -- it is
specifically how OpenVSP triangulates the flat end cap. This was confirmed by
elimination: spanwise density (SectTess_U/InCluster), chordwise density
(Tess_W -- which turned out not to reach CFDMesh at all), local refinement
(AddCFDSource line source -- made it far worse, ~99k invalid elements),
Geometry.Tolerance sweeps, and a full pymeshlab repair pass (merged 2 verts,
dropped 8 faces, changed nothing) ALL left the failure bit-identical.

THE FIX
-------
The root cap is planar by construction -- it lies exactly at y=0. OpenVSP's
triangulation of it therefore encodes no geometry that a single flat gmsh
plane surface does not also encode. So: strip every y=0 facet, then rebuild
that whole plane as ONE plane surface (outer loop = far-field box's y=0
outline, inner loop = the wing's root airfoil outline, i.e. a plane with a
wing-shaped hole). Geometrically lossless, and it deletes the only region
that has ever produced an overlap.

Second, equally important change: this script does NOT remesh the wing
surface. v2 ran classifySurfaces()+createGeometry() and let gmsh re-triangulate
everything, which was both unnecessary (OpenVSP's skin already respects the
geometry) and a source of its own trouble. Here createTopology() keeps
OpenVSP's triangles verbatim and only the new symmetry plane is meshed.

Tagging also gets simpler and exact: instead of bbox-sorting ~50 classified
patches into wing/sym/far, there are exactly three surfaces by construction.

Usage:  python3 make_mesh_euler3.py [--coarse]
"""
import argparse
import os
import sys

import gmsh

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_STL = os.path.join(HERE, "wing_winglet_cfdmesh.stl")
STRIPPED = os.path.join(HERE, "cfdmesh_nocap.stl")
FAR = 150.0   # ft, half-extent of the box set in export_wing_cfdmesh.vspscript

sys.path.insert(0, HERE)


def strip_cap(src, dst, ytol=1e-7):
    """Drop every facet whose three vertices all sit at y=0."""
    with open(src) as f:
        lines = f.readlines()
    out, i, kept, dropped = [], 0, 0, 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith("facet"):
            facet = lines[i:i + 7]
            ys = [float(L.strip().split()[2]) for L in facet
                  if L.strip().startswith("vertex")]
            if len(ys) == 3 and all(abs(y) < ytol for y in ys):
                dropped += 1
            else:
                out.extend(facet); kept += 1
            i += 7
            continue
        out.append(lines[i]); i += 1
    with open(dst, "w") as f:
        f.writelines(out)
    print(f"stripped y=0 cap: kept {kept} facets, dropped {dropped}")


def build(coarse=False):
    scale = 2.5 if coarse else 1.0

    strip_cap(SRC_STL, STRIPPED)

    gmsh.initialize()
    gmsh.model.add("wing_winglet_euler3")
    gmsh.option.setNumber("General.Terminal", 1)
    # This is the threshold BELOW which two facets sharing an edge are called
    # overlapping -- so a LARGER value is stricter, not looser. v2 had it at
    # 2.0, i.e. ~20x stricter than gmsh's own 0.1 default, which is the wrong
    # direction and quietly made every marginal fold fatal.
    #
    # At the refined export settings the y=0 cap is clean (0 overlaps, down
    # from 30) but one thin fold survives out on the wing at ~14% span,
    # measured at 0.0759 degrees -- a genuine sliver, not a zero-thickness
    # duplicate, and it only trips the check because it lands just under the
    # 0.1 default. 0.01 keeps true degenerates (0.0 dihedral) fatal while
    # letting this one through.
    gmsh.option.setNumber("Mesh.AngleToleranceFacetOverlap", 0.01)

    gmsh.merge(STRIPPED)
    # Keep OpenVSP's triangulation verbatim -- no classifySurfaces/createGeometry,
    # so nothing gets re-triangulated and no new overlaps can be invented.
    gmsh.model.mesh.createTopology()

    surfs = gmsh.model.getEntities(2)
    if len(surfs) != 2:
        raise RuntimeError(f"expected 2 surfaces (wing, farfield), got {len(surfs)}")

    # Sort by extent: the far-field box reaches the domain edges, the wing does not.
    wing_tag = far_tag = None
    for dim, tag in surfs:
        bb = gmsh.model.getBoundingBox(dim, tag)
        if bb[3] > FAR * 0.5 or bb[0] < -FAR * 0.5:
            far_tag = tag
        else:
            wing_tag = tag
    if wing_tag is None or far_tag is None:
        raise RuntimeError("could not tell the wing and far-field apart by extent")
    print(f"wing surface={wing_tag}  farfield surface={far_tag}")

    # Rebuild the y=0 plane: box outline outside, wing root outline as a hole.
    wing_b = gmsh.model.getBoundary([(2, wing_tag)], combined=True, oriented=True)
    far_b = gmsh.model.getBoundary([(2, far_tag)], combined=True, oriented=True)
    if not wing_b or not far_b:
        raise RuntimeError("expected one open boundary loop on each surface "
                           f"(wing={len(wing_b)}, far={len(far_b)})")
    outer = gmsh.model.geo.addCurveLoop([c[1] for c in far_b])
    inner = gmsh.model.geo.addCurveLoop([c[1] for c in wing_b])
    sym_tag = gmsh.model.geo.addPlaneSurface([outer, inner])
    gmsh.model.geo.synchronize()
    print(f"rebuilt symmetry plane as surface {sym_tag}")

    loop = gmsh.model.geo.addSurfaceLoop([wing_tag, far_tag, sym_tag])
    vol = gmsh.model.geo.addVolume([loop])
    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(3, [vol], name="fluid")
    gmsh.model.addPhysicalGroup(2, [wing_tag], name="wing_wall")
    gmsh.model.addPhysicalGroup(2, [sym_tag], name="symmetry")
    gmsh.model.addPhysicalGroup(2, [far_tag], name="farfield")

    # Only the symmetry plane and the volume interior get meshed here -- the
    # wing and box skins keep OpenVSP's own triangles.
    gmsh.option.setNumber("Mesh.MeshSizeMin", 0.05 * scale)
    gmsh.option.setNumber("Mesh.MeshSizeMax", 12.0 * scale)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # plain Delaunay
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    gmsh.model.mesh.generate(3)

    # Whole model is in feet; SU2 convention here is metres (matches the
    # Sref/bref/cref in gen_configs.py). Scale at write time only.
    gmsh.option.setNumber("Mesh.ScalingFactor", 0.3048)
    out = os.path.join(HERE, "coarse_euler3.su2" if coarse else "wing_winglet_euler3.su2")
    gmsh.write(out)
    print(f"\nwrote {out}")
    print(f"node count: {len(gmsh.model.mesh.getNodes()[0])}")

    gmsh.finalize()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--coarse", action="store_true")
    build(coarse=ap.parse_args().coarse)
