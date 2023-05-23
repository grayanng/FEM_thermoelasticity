import gmsh
import sys
from tkinter import filedialog
import meshio as mio
from math import sqrt

gmsh.initialize(sys.argv)

gmsh.model.add("geom")

# Характерный разер сетки 
lc = 4.e-3
LX = 0.02
dy = 0.002
LY = 0.01 + dy
diY = LY / 10
diX = LY / 10
# В командную строку ДОЛЖЕН поопасть правильный путь к *.geo файлу
gmsh.open(sys.argv[1]) 

print('Model ' + gmsh.model.getCurrent() + ' (' + 
      str(gmsh.model.getDimension()) + 'D)')

# Здесь мы синхронизируемся с моделью
gmsh.model.geo.synchronize()


gmsh.model.mesh.field.add("Distance", 1)
gmsh.model.mesh.field.setNumbers(1, "PointsList", [14, 13, 11, 10])
gmsh.model.mesh.field.setNumbers(1, "SurfacesList", [28])
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

min_size = sqrt(LX**2 + LY**2) / 5.e1 # Характерный размер геометрии
# Три лямбда-функции для оптимизации размеров
# Ограничение сверху через жёстко заданный размер min_size 
cback1 = lambda dim, tag, x, y, z, lc: lc if lc <  min_size else min_size 


gmsh.model.mesh.setSizeCallback(cback1)

# Убираем параметры генерации по умолчанию
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromPoints", 0)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 0)
gmsh.option.setNumber("Mesh.MshFileVersion",2.2)

gmsh.model.mesh.generate(3)
#gmsh.write(f'{gmsh.model.getCurrent()}.msh')
file = filedialog.asksaveasfilename()
gmsh.write(file)

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()