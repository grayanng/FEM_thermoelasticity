import streamlit as st
from PIL import Image
import os.path

path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'Picture_1.png')
path_to_image_1= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'Picture_2.png')

r"""
# Геометрия задачи
Были реализованы две геометрии:\
1. для упрощенной модели (см.рис 1)
1. для базовой модели (см.2)

Для дальнейшего удобства работы с геометрией требуется на этапе работы с gmsh разметить физические границы (стенки, точки, поверхности)


"""

image = Image.open(path_to_image)
st.image (image, caption= 'Рисунок 1 - Упрощенная модель')
r"""
### Параметры
LX =  0.02;\
dy = 0.002;\
LY = 0.01 + dy;\
p1 = LY/50;\
p2 = LY/100;
### Создание расчетной области
Point(1) = {0,0,0,p1};\
Point(2) = {0,dy,0,p2};\
Point(3) = {0,LY,0,p1};\
Point(4) = {LX,LY,0,p1};\
Point(5) = {LX,dy,0,p2};\
Point(6) = {LX,0,0,p1};\
Line(1) = {1,3};\
Line(2) = {3,4};\
Line(3) = {4,6};\
Line(4) = {6,1};\
Line Loop(5) = {1,2,3,4};\
Plane Surface(6) = {5};
### Отметим подобласти и границы
Physical Point ("fix_point",7) = {3,4}; - точки\
Physical Point("fix_point", 7) = {3, 4}; - точки закрепления\
Physical Curve("fixed_walls", 8) = {1, 3}; - закреплённые стенки\
Physical Curve("moving_walls", 9) = {2, 4}; - подвижные стенки\
Physical Surface("material", 10) = {6}; - область решения
"""

image = Image.open(path_to_image_1)
st.image (image, caption= 'Рисунок 2 - Базовая модель')
r"""
### Параметры
LX = 0.02;\
dy = 0.002;\
LY = 0.01+dy;\
p1 = LY/50;\
p2 = LY/100;
### Создадим расчетную область
Point(1) = { 0, 0, 0, p1};\
Point(2) = { 0, dy, 0, p2};\
Point(3) = { 0, LY, 0, p1};\
Point(4) = { LX, LY, 0, p1};\
Point(5) = { LX, dy, 0, p2};\
Point(6) = { LX, 0, 0, p1};\
Line(1) = {1, 2};\
Line(2) = {2, 3};\
Line(3) = {3, 4};\
Line(4) = {4, 5};\
Line(5) = {5, 6};\
Line(6) = {6, 1};\
Line(7) = {2, 5};\
Line Loop(8) = {7, -4, -3, -2};\
Plane Surface(9) = {8};\
Line Loop(10) = {6, 1, 7, 5};\
Plane Surface(11) = {10};
- Физические границы идентичны упрощённым

"""