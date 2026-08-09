import gmsh

gmsh.initialize()
gmsh.option.setString("Geometry.OCCTargetUnit", "FT")
gmsh.option.setNumber("Geometry.OCCFixDegenerated", 1)
gmsh.option.setNumber("Geometry.OCCFixSmallEdges", 1)
gmsh.option.setNumber("Geometry.OCCFixSmallFaces", 1)
gmsh.option.setNumber("Geometry.OCCSewFaces", 1)
gmsh.model.occ.importShapes("wing_winglet.stp")
gmsh.model.occ.synchronize()
gmsh.model.occ.removeAllDuplicates()
gmsh.model.occ.synchronize()

surfs = gmsh.model.occ.getEntities(2)
print(f"{len(surfs)} surfaces")
for dim, tag in surfs:
    area = gmsh.model.occ.getMass(dim, tag)
    bb = gmsh.model.getBoundingBox(dim, tag)
    dx, dy, dz = bb[3] - bb[0], bb[4] - bb[1], bb[5] - bb[2]
    print(f"surf {tag:3d}: area={area:9.5f} ft^2  bbox extents dx={dx:.4f} "
          f"dy={dy:.4f} dz={dz:.4f}  near(10.49,22.10,1.91)="
          f"{bb[0]<=10.6<=bb[3] and bb[1]<=22.2<=bb[4] and bb[2]<=2.0<=bb[5]}")

gmsh.finalize()
