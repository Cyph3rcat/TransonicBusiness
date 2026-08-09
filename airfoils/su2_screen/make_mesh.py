"""
Generate an O-grid CFD mesh (unstructured triangles + boundary-layer wedge)
around a 2D airfoil from Selig-format coordinates, export to SU2 format.

Usage: python3 make_mesh.py <coords.dat> <output_name> [hwall]
"""
import sys
import math
import gmsh
import meshio

def read_selig(path):
    pts = []
    with open(path) as f:
        lines = f.readlines()
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        x, y = float(parts[0]), float(parts[1])
        pts.append((x, y))
    return pts

def build_mesh(datfile, name, hwall=5e-6, farfield_r=25.0):
    pts = read_selig(datfile)
    closed = (abs(pts[0][0] - pts[-1][0]) < 1e-9 and abs(pts[0][1] - pts[-1][1]) < 1e-9)
    if closed:
        pts = pts[:-1]  # drop duplicate coincident last point; loop back to tag 0 instead

    gmsh.initialize()
    gmsh.model.add(name)

    # airfoil surface points
    pt_tags = []
    lc_af = 1.0  # controlled by fields, not point lc
    for (x, y) in pts:
        t = gmsh.model.geo.addPoint(x, y, 0, lc_af)
        pt_tags.append(t)

    # spline through all points; for a sharp-TE (closed) section, loop back to
    # the first point tag so the spline itself is the whole closed boundary
    loop_pts = pt_tags + [pt_tags[0]] if closed else pt_tags
    spline = gmsh.model.geo.addSpline(loop_pts)
    curves = [spline]
    if not closed:
        te_close = gmsh.model.geo.addLine(loop_pts[-1], loop_pts[0])
        curves.append(te_close)

    af_loop = gmsh.model.geo.addCurveLoop(curves)

    # farfield circle centered at (0.5, 0)
    cx, cy = 0.5, 0.0
    c0 = gmsh.model.geo.addPoint(cx, cy, 0, farfield_r)
    c_n = gmsh.model.geo.addPoint(cx, cy + farfield_r, 0, farfield_r)
    c_e = gmsh.model.geo.addPoint(cx + farfield_r, cy, 0, farfield_r)
    c_s = gmsh.model.geo.addPoint(cx, cy - farfield_r, 0, farfield_r)
    c_w = gmsh.model.geo.addPoint(cx - farfield_r, cy, 0, farfield_r)
    arc1 = gmsh.model.geo.addCircleArc(c_n, c0, c_e)
    arc2 = gmsh.model.geo.addCircleArc(c_e, c0, c_s)
    arc3 = gmsh.model.geo.addCircleArc(c_s, c0, c_w)
    arc4 = gmsh.model.geo.addCircleArc(c_w, c0, c_n)
    ff_loop = gmsh.model.geo.addCurveLoop([arc1, arc2, arc3, arc4])

    surf = gmsh.model.geo.addPlaneSurface([ff_loop, af_loop])

    gmsh.model.geo.synchronize()

    gmsh.model.addPhysicalGroup(1, curves, name="airfoil")
    gmsh.model.addPhysicalGroup(1, [arc1, arc2, arc3, arc4], name="farfield")
    gmsh.model.addPhysicalGroup(2, [surf], name="fluid")

    # --- mesh size fields ---
    dist = gmsh.model.mesh.field.add("Distance")
    gmsh.model.mesh.field.setNumbers(dist, "CurvesList", curves)
    gmsh.model.mesh.field.setNumber(dist, "Sampling", 400)

    thr = gmsh.model.mesh.field.add("Threshold")
    gmsh.model.mesh.field.setNumber(thr, "InField", dist)
    gmsh.model.mesh.field.setNumber(thr, "SizeMin", 0.003)
    gmsh.model.mesh.field.setNumber(thr, "SizeMax", farfield_r * 0.12)
    gmsh.model.mesh.field.setNumber(thr, "DistMin", 0.03)
    gmsh.model.mesh.field.setNumber(thr, "DistMax", farfield_r * 0.8)

    # boundary layer around airfoil
    bl = gmsh.model.mesh.field.add("BoundaryLayer")
    gmsh.model.mesh.field.setNumbers(bl, "CurvesList", curves)
    gmsh.model.mesh.field.setNumber(bl, "hwall_n", hwall)
    gmsh.model.mesh.field.setNumber(bl, "ratio", 1.22)
    gmsh.model.mesh.field.setNumber(bl, "thickness", 0.025)
    gmsh.model.mesh.field.setNumber(bl, "Quads", 0)
    gmsh.model.mesh.field.setAsBoundaryLayer(bl)

    gmsh.model.mesh.field.setAsBackgroundMesh(thr)
    gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
    gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
    gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
    gmsh.option.setNumber("Mesh.Algorithm", 6)  # Frontal-Delaunay, robust for hybrid BL meshes

    gmsh.model.mesh.generate(2)

    msh_path = f"{name}.msh"
    gmsh.write(msh_path)
    gmsh.finalize()

    m = meshio.read(msh_path)
    write_su2(m, f"{name}.su2")
    print(f"[{name}] points={len(pts)} closed={closed} -> {name}.su2 written")
    n_tri = sum(len(c.data) for c in m.cells if c.type == "triangle")
    print(f"[{name}] triangles: {n_tri}")


def write_su2(m, path):
    """Manual SU2 mesh writer (meshio's built-in su2 writer is broken for this
    meshio version's CellBlock API), using physical group names from gmsh."""
    # map physical-group name -> physical tag id, from gmsh field_data
    name_to_tag = {nm: tags[0] for nm, tags in m.field_data.items()}
    tag_to_name = {v: k for k, v in name_to_tag.items()}

    tri_blocks = [c for c in m.cells if c.type == "triangle"]
    line_blocks = [c for c in m.cells if c.type == "line"]

    n_tri = sum(len(c.data) for c in tri_blocks)
    pts = m.points

    with open(path, "w") as f:
        f.write("NDIME= 2\n")
        f.write(f"NELEM= {n_tri}\n")
        for c in tri_blocks:
            for tri in c.data:
                f.write(f"5 {tri[0]} {tri[1]} {tri[2]}\n")

        f.write(f"NPOIN= {len(pts)}\n")
        for i, p in enumerate(pts):
            f.write(f"{p[0]:.10f} {p[1]:.10f} {i}\n")

        # bucket line cells by physical tag -> marker name
        phys_by_block = m.cell_data.get("gmsh:physical", None)
        markers = {}
        if phys_by_block is not None:
            li = 0
            for c in m.cells:
                if c.type == "line":
                    tags = phys_by_block[li]
                    for e, t in zip(c.data, tags):
                        mname = tag_to_name.get(int(t), f"marker_{int(t)}")
                        markers.setdefault(mname, []).append(e)
                li += 1
        else:
            raise RuntimeError("no physical tags found on line elements")

        f.write(f"NMARK= {len(markers)}\n")
        for mname, edges in markers.items():
            f.write(f"MARKER_TAG= {mname}\n")
            f.write(f"MARKER_ELEMS= {len(edges)}\n")
            for e in edges:
                f.write(f"3 {e[0]} {e[1]}\n")

if __name__ == "__main__":
    datfile = sys.argv[1]
    name = sys.argv[2]
    hwall = float(sys.argv[3]) if len(sys.argv) > 3 else 5e-6
    build_mesh(datfile, name, hwall)
