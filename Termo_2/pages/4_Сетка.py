import streamlit as st
from PIL import Image
import os.path

r"""
# Сетка 
"""

path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'Сетка_новая.png')
image = Image.open(path_to_image_2)
st.image(image, caption='Сетка 2D объекта')

expander = st.expander(" geo файл ")
expander.write(r"""```
// Параметры
LX = 0.02;
dy = 0.002;
LY = 0.01+dy;
p1 = LY/50;
p2 = LY/100;

// Создадим расчетную область
Point(1) = { 0, 0, 0, p1};
Point(2) = { 0, dy, 0, p2};
Point(3) = { 0, LY, 0, p1};
Point(4) = { LX, LY, 0, p1};
Point(5) = { LX, dy, 0, p2};
Point(6) = { LX, 0, 0, p1};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 1};
Line(7) = {2, 5};
Line Loop(8) = {7, -4, -3, -2};
Plane Surface(9) = {8};
Line Loop(10) = {6, 1, 7, 5};
Plane Surface(11) = {10};

// Отметим подобласти и границы
Physical Surface("upper", 1) = {9};
Physical Surface("lower", 2) = {11};
Physical Line("upper_boundary", 1) = {3};
Physical Line("lower_boundary", 2) = {6};
Physical Point("fix_points", 1) = {3, 4};
Physical Curve("interface", 3) = {7};
Physical Curve("conv_edges", 4) = {2, 4, 5, 1};

'''""")


expander = st.expander(" Пример реализации ")
expander.write(r"""```python
import gmsh
import sys
from tkinter import filedialog
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
```
"""
r""" 
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
"""```python
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
#gmsh.write(f'{gmsh.model.getCurrent()}.msh')
file = filedialog.asksaveasfilename()
gmsh.write(file)

# Launch the GUI to see the results:
if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

"""
        )