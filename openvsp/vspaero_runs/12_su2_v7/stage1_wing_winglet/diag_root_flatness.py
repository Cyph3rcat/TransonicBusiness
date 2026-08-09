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

d = [Y1]
for i in range(1, N_LAYERS):
    d.append(d[-1] + Y1 * GROWTH ** i)
extbl = gmsh.model.geo.extrudeBoundaryLayer(wing_surfs, [1] * N_LAYERS, d, True)
gmsh.model.geo.synchronize()

top = []
for i in range(1, len(extbl)):
    if extbl[i][0] == 3:
        top.append(extbl[i - 1])
print("top surfaces:", top)

bnd = gmsh.model.getBoundary(top, combined=True, oriented=True)
print("boundary curves:", bnd)
pts = gmsh.model.getBoundary(bnd, combined=False, oriented=False, recursive=True)
ys = []
for dim, tag in pts:
    x, y, z = gmsh.model.getValue(0, tag, [])
    ys.append(y)
    print(f"pt {tag}: ({x:.6f}, {y:.6f}, {z:.6f})")
print(f"\nY range of boundary points: {min(ys):.6e} .. {max(ys):.6e}")
print(f"max |Y|: {max(abs(v) for v in ys):.6e} ft = {max(abs(v) for v in ys)*304.8:.4f} mm")

gmsh.finalize()
