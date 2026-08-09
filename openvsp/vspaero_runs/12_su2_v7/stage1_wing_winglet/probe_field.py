import gmsh
gmsh.initialize()
gmsh.model.add("t")
f = gmsh.model.mesh.field.add("BoundaryLayer")
for name in ["FacesList", "SurfacesList", "Faces", "Surfaces", "NodesList",
             "EdgesList", "hwall_n", "hfar", "ratio", "Ratio", "Size",
             "NbLayers", "thickness", "Thickness", "Quads", "IntersectMetrics",
             "AnisoMax", "hwall_n_nodes", "PseudoSafeLayer"]:
    try:
        gmsh.model.mesh.field.setNumbers(f, name, [1])
        print(name, "OK numbers")
    except Exception:
        try:
            gmsh.model.mesh.field.setNumber(f, name, 1.0)
            print(name, "OK number")
        except Exception as e:
            print(name, "FAIL")
gmsh.finalize()
