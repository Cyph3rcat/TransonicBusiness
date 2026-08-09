"""Repair OpenVSP's raw CFDMesh STL with pymeshlab before handing it to gmsh.

Why this exists: the gmsh classify()+fill pipeline (make_mesh_euler2.py) hits
a facet-overlap at the wing root leading edge on the tightened (fine) mesh
settings, at the exact same node IDs regardless of gmsh-side tolerance,
density, or local-refinement changes. That pattern says the defect is a tiny
near-duplicate triangle pair baked into OpenVSP's own triangulation, not
something gmsh's generic removeDuplicateNodes() (which found ZERO duplicates
here even at Geometry.Tolerance=1e-7) is built to catch. pymeshlab has repair
filters purpose-built for exactly this class of defect (stitching, collapsing
near-coincident vertices, dropping degenerate/duplicate faces) -- this script
runs those on the STL as a standalone cleanup pass, before gmsh ever sees it.

Usage: python3 repair_stl_pymeshlab.py <in.stl> <out.stl> [merge_threshold_ft]
"""
import sys

import pymeshlab

def main():
    in_stl = sys.argv[1]
    out_stl = sys.argv[2]
    # Root LE feature scale here is ~0.025-0.08 ft (MinLen/BaseLen). The
    # crack itself is sub-micron in dihedral terms but the actual vertex gap
    # is apparently larger than 1e-7 ft (gmsh's Geometry.Tolerance=1e-7 did
    # nothing) and smaller than 1e-4 ft (that value catastrophically merged
    # 42,745 unrelated nodes across the whole model). Start at 5e-5 ft --
    # inside that bracket, well below the smallest real feature size.
    merge_thresh = float(sys.argv[3]) if len(sys.argv) > 3 else 5e-5

    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(in_stl)
    m = ms.current_mesh()
    print(f"loaded: {m.vertex_number()} verts, {m.face_number()} faces")

    ms.meshing_remove_duplicate_vertices()
    ms.meshing_remove_duplicate_faces()

    print(f"merging close vertices, threshold={merge_thresh} ft (absolute)")
    ms.meshing_merge_close_vertices(threshold=pymeshlab.PureValue(merge_thresh))

    ms.meshing_remove_duplicate_faces()
    ms.meshing_remove_t_vertices()
    ms.meshing_repair_non_manifold_edges()
    ms.meshing_repair_non_manifold_vertices()

    m = ms.current_mesh()
    print(f"after repair: {m.vertex_number()} verts, {m.face_number()} faces")

    ms.save_current_mesh(out_stl)
    print(f"wrote {out_stl}")


if __name__ == "__main__":
    main()
