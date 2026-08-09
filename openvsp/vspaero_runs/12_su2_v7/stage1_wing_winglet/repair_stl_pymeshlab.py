"""Repairs OpenVSP's raw CFDMesh STL with pymeshlab before gmsh sees it: the gmsh classify()+fill pipeline (make_mesh_euler2.py) hits a facet-overlap at the wing root LE at the same node IDs regardless of gmsh-side tolerance/density/refinement, meaning the defect is a tiny near-duplicate triangle baked into OpenVSP's own triangulation (gmsh's removeDuplicateNodes found ZERO duplicates even at Geometry.Tolerance=1e-7); pymeshlab's repair filters (stitching, near-coincident vertex collapse, degenerate/duplicate face removal) are purpose-built for exactly this. Usage: python3 repair_stl_pymeshlab.py <in.stl> <out.stl> [merge_threshold_ft]"""
import sys

import pymeshlab

def main():
    in_stl = sys.argv[1]
    out_stl = sys.argv[2]
    # root LE feature scale is ~0.025-0.08 ft; the vertex gap is bracketed larger than 1e-7 ft (gmsh's Geometry.Tolerance=1e-7 did nothing) and smaller than 1e-4 ft (that catastrophically merged 42,745 unrelated nodes) -- 5e-5 ft sits inside that bracket, well below the smallest real feature
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
