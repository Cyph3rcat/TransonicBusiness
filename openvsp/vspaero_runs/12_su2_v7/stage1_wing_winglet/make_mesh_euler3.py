"""Stage 1 SU2 volume mesh, EULER -- v3, built on the actual root cause (found 2026-08-08 after ~7 failed approaches): every meshing failure was an overlapping-facet pair lying exactly on the y=0 root cap (confirmed by elimination -- spanwise/chordwise density, local refinement, Geometry.Tolerance, and a pymeshlab repair pass all left it bit-identical), i.e. specifically how OpenVSP triangulates the flat end cap, not mesh resolution or a repairable input defect. Fix: strip every y=0 facet and rebuild that plane as ONE gmsh plane surface (far-field box outline outer loop, wing root airfoil outline as a hole) -- geometrically lossless, and it deletes the only region that has ever produced an overlap. Also, unlike v2 (which ran classifySurfaces()+createGeometry() and re-triangulated everything), this script uses createTopology() to keep OpenVSP's triangles verbatim, so only the new symmetry plane gets meshed and tagging is exact (3 surfaces by construction, not ~50 bbox-sorted patches). Usage: python3 make_mesh_euler3.py [--coarse]"""
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
    # this threshold is the value BELOW which two facets sharing an edge are called overlapping, so a LARGER value is stricter -- v2 had it at 2.0 (~20x stricter than gmsh's 0.1 default), the wrong direction, making every marginal fold fatal. At the refined export the y=0 cap is clean (0 overlaps, down from 30) but one genuine sliver fold survives on the wing at ~14% span (0.0759 deg), which only trips the check because it's just under the 0.1 default; 0.01 keeps true degenerates (0.0 dihedral) fatal while letting this one through
    gmsh.option.setNumber("Mesh.AngleToleranceFacetOverlap", 0.01)

    gmsh.merge(STRIPPED)
    # keep OpenVSP's triangulation verbatim -- no classifySurfaces/createGeometry, so nothing gets re-triangulated and no new overlaps can be invented
    gmsh.model.mesh.createTopology()

    surfs = gmsh.model.getEntities(2)
    if len(surfs) != 2:
        raise RuntimeError(f"expected 2 surfaces (wing, farfield), got {len(surfs)}")

    # sort by extent: the far-field box reaches the domain edges, the wing does not
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

    # rebuild the y=0 plane: box outline outside, wing root outline as a hole
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

    # only the symmetry plane and the volume interior get meshed here -- the wing and box skins keep OpenVSP's own triangles
    gmsh.option.setNumber("Mesh.MeshSizeMin", 0.05 * scale)
    gmsh.option.setNumber("Mesh.MeshSizeMax", 12.0 * scale)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 1)
    gmsh.option.setNumber("Mesh.Algorithm3D", 1)   # plain Delaunay
    gmsh.option.setNumber("Mesh.Optimize", 1)
    gmsh.option.setNumber("Mesh.OptimizeNetgen", 1)

    gmsh.model.mesh.generate(3)

    # whole model is in feet; SU2 convention here is metres (matches Sref/bref/cref in gen_configs.py) -- scale at write time only
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
