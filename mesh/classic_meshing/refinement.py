import gmsh
import sys
from math import sqrt
gmsh.initialize(sys.argv)

gmsh.model.add("geom")

# Let's create a simple rectangular geometry:
lc = 2.e-3
LX = 0.02
dy = 0.002
LY = 0.01 + dy
diY = LY / 10
diX = LY / 10
# В командную строку ДОЛЖЕН поопасть правильный путь к *.geo файлу
gmsh.open(sys.argv[1]) 

print('Model ' + gmsh.model.getCurrent() + ' (' + 
      str(gmsh.model.getDimension()) + 'D)')
bous = gmsh.model.getPhysicalGroups(2)

# Здесь мы синхронизируемся с моделью
gmsh.model.geo.synchronize()


gmsh.model.mesh.field.add("Distance", 1)
gmsh.model.mesh.field.setNumbers(1, "PointsList", [3, 4])
gmsh.model.mesh.field.setNumbers(1, "CurvesList", [7])
gmsh.model.mesh.field.setNumber(1, "Sampling", 200)
"""
Принцип работы параметра Threshold. Объекты для которых определяется дистанция
переаются через поле Distance

SizeMax -                     /------------------
                             /
                            /
                           /
SizeMin -o----------------/
         |                |    |
       Point         DistMin  DistMax
"""
gmsh.model.mesh.field.add("Threshold", 2)
gmsh.model.mesh.field.setNumber(2, "InField", 1)
gmsh.model.mesh.field.setNumber(2, "SizeMin", lc / 20.)
gmsh.model.mesh.field.setNumber(2, "SizeMax", lc / 10.)
gmsh.model.mesh.field.setNumber(2, "DistMin", 0.001)
gmsh.model.mesh.field.setNumber(2, "DistMax", 0.002)
gmsh.model.mesh.field.setNumber(2, "Sigmoid", 1)

gmsh.model.mesh.field.add("Min", 3)
gmsh.model.mesh.field.setNumbers(3, "FieldsList", [2])

gmsh.model.mesh.field.setAsBackgroundMesh(3)

min_size = sqrt(LX**2 + LY**2) / 1.e2 # Характерный размер геометрии
# Три лямбда-функции для оптимизации размеров
# Ограничение сверху через жёстко заданный размер min_size 
cback1 = lambda dim, tag, x, y, z, lc: lc if lc <  min_size else min_size 
# Контролируется исключительно geo файлом и функциями сверху
cback2 = lambda dim, tag, x, y, z, lc: lc
# Жёстко фиксирована через характерный размер области
cback3 = lambda dim, tag, x, y, z, lc: sqrt(LX**2 + LY**2) / 1.e2

gmsh.model.mesh.setSizeCallback(cback1)

# Убираем параметры генерации по умолчанию
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)


gmsh.option.setNumber("Mesh.Algorithm", 5) # Делоне-классический 
#gmsh.option.setNumber("Mesh.Algorithm", 6) # Делоне-классический 
gmsh.model.mesh.generate(2)
gmsh.write(f'{gmsh.model.getCurrent()}.msh')

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()