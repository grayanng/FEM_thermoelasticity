# -----------------------------------------------------------------------------
#
#  Gmsh Python extended tutorial 1
#
#  Geometry and mesh data
#
# -----------------------------------------------------------------------------

# The Python API allows to do much more than what can be done in .geo
# files. These additional features are introduced gradually in the extended
# tutorials, starting with `x1.py'.

# In this first extended tutorial, we start by using the API to access basic
# geometrical and mesh data.

import gmsh
import sys
import math

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[1] + " file")
    exit()

gmsh.initialize()

# You can run this tutorial on any file that Gmsh can read, e.g. a mesh file in
# the MSH format: `python t1.py file.msh'

gmsh.open(sys.argv[1])
# Print the model name and dimension:s
print('Model ' + gmsh.model.getCurrent() + ' (' + 
      str(gmsh.model.getDimension()) + 'D)')
bous = gmsh.model.getPhysicalGroups(2)
gmsh.model.geo.synchronize()  # Sync with model

lc = 1.e-3

LX = 0.02
dy = 0.002
LY = 0.01 + dy
diY = LY / 10
diX = LY / 10
di = math.sqrt(diX ** 2 + diY ** 2)
gmsh.model.geo.addPoint(0.0, 0.0, 0, lc, 1)
# Distance
gmsh.model.mesh.field.add("Distance", 1)
gmsh.model.mesh.field.setNumbers(1, "PointsList", [3, 4])
gmsh.model.mesh.field.setNumber(1, "Sampling", 100)
# Threshold
gmsh.model.mesh.field.add("Threshold", 2)
gmsh.model.mesh.field.setNumber(2, "InField", 1)
gmsh.model.mesh.field.setNumber(2, "SizeMin", lc / 30.)
gmsh.model.mesh.field.setNumber(2, "SizeMax", lc)
gmsh.model.mesh.field.setNumber(2, "DistMin", di)
gmsh.model.mesh.field.setNumber(2, "DistMax", di)

gmsh.model.mesh.field.add("Min", 3)
gmsh.model.mesh.field.setNumbers(3, "FieldsList", [1, 2])
gmsh.model.mesh.field.setAsBackgroundMesh(3)

gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)

callback = lambda dim, tag, x, y, z, lc: min(lc, 0.02 * x + 0.01)
gmsh.model.mesh.setSizeCallback(callback)

gmsh.option.setNumber("Mesh.Algorithm", 5)
gmsh.model.mesh.generate(2)
gmsh.write(f'{gmsh.model.getCurrent()}.msh')

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()
for ent in bous:
    print('Surface ' + str(ent[1]))

gmsh.clear()

gmsh.finalize()
