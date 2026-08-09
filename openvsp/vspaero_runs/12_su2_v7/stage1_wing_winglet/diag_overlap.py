import math
import gmsh

gmsh.initialize()
gmsh.merge("wing_winglet_cfdmesh.msh")
gmsh.model.mesh.removeDuplicateNodes()
gmsh.model.mesh.removeDuplicateElements()
gmsh.model.mesh.classifySurfaces(35 * math.pi / 180.0, True, True, 0.01)
gmsh.model.mesh.createGeometry()

for tag in (1, 24):
    bb = gmsh.model.getBoundingBox(2, tag)
    elems = gmsh.model.mesh.getElements(2, tag)
    ntri = len(elems[1][0]) if elems[1] else 0
    print(f"surface {tag}: bbox={bb}, n_triangles={ntri}")

gmsh.finalize()
