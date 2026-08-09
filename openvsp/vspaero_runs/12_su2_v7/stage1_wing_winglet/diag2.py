import math
import gmsh

STEP = "wing_winglet.stp"
RHO, VINF, MU = 5.581e-4, 774.5, 2.877e-7
NU = MU / RHO
CREF = 5.0236
RE_MAC = RHO * VINF * CREF / MU
CF = 0.455 / (math.log10(RE_MAC)) ** 2.58
TAU_W = 0.5 * CF * RHO * VINF ** 2
U_TAU = math.sqrt(TAU_W / RHO)
Y1 = 30.0 * NU / U_TAU
GROWTH, N_LAYERS = 1.20, 6

gmsh.initialize()
gmsh.option.setString("Geometry.OCCTargetUnit", "FT")
gmsh.option.setNumber("Geometry.OCCFixDegenerated", 1)
gmsh.option.setNumber("Geometry.OCCFixSmallEdges", 1)
gmsh.option.setNumber("Geometry.OCCFixSmallFaces", 1)
gmsh.option.setNumber("Geometry.OCCSewFaces", 1)
gmsh.model.occ.importShapes(STEP)
gmsh.model.occ.synchronize()
gmsh.model.occ.removeAllDuplicates()
gmsh.model.occ.synchronize()
wing_surfs = gmsh.model.occ.getEntities(2)
print("input wing surfaces:", len(wing_surfs))
for dim, tag in wing_surfs:
    bb = gmsh.model.getBoundingBox(dim, tag)
    print(f"  surf {tag}: ybounds=({bb[1]:.5f},{bb[4]:.5f})")

d = [Y1]
for i in range(1, N_LAYERS):
    d.append(d[-1] + Y1 * GROWTH ** i)
extbl = gmsh.model.geo.extrudeBoundaryLayer(wing_surfs, [1] * N_LAYERS, d, True)
gmsh.model.geo.synchronize()

top = []
for i in range(1, len(extbl)):
    if extbl[i][0] == 3:
        top.append(extbl[i - 1])
print("\ntop surfaces:", len(top))
for dim, tag in top:
    bb = gmsh.model.getBoundingBox(dim, tag)
    print(f"  top {tag}: y=({bb[1]:.6f},{bb[4]:.6f}) x=({bb[0]:.3f},{bb[3]:.3f}) z=({bb[2]:.3f},{bb[5]:.3f})")

# check for non-manifold / naked edges directly among 'top' surfaces
bnd_indiv = gmsh.model.getBoundary(top, combined=False, oriented=False)
print(f"\nnon-combined boundary curve count: {len(bnd_indiv)}")
bnd_comb = gmsh.model.getBoundary(top, combined=True, oriented=False)
print(f"combined boundary curve count: {len(bnd_comb)}")

gmsh.finalize()
