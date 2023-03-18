'''
Created on 17 мар. 2023 г.

@author: georgepc
Этот файл - пример того, как можно поместить GMSH сетку в FEniCS

Геометрия сделана таким образом, что файл с границами лежит отдельно от ячеек сетки
'''

from fenics import *

mesh = Mesh("composite.xml")
pr = MeshFunction("size_t", mesh, "composite_physical_region.xml")
fr = MeshFunction("size_t", mesh, "composite_facet_region.xml")
print("subdom created")