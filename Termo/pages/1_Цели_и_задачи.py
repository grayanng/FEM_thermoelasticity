import streamlit
import streamlit as st
from PIL import Image
import os.path

r"""
# **Актуальность**
- Процессы тепловых деформаций сущуественно влиют на прочностные характеристики детали при 3D-печати по металлу
"""
path_to_image_1= os.path.join(os.path.dirname(__file__), 'images', 'picture_2.png')
image = Image.open(path_to_image_1)
st.image (image)

r"""
- Численный алгоритм моделирования осуществляется на движущихся сетках, следовательно метод конечных элементов (МКЭ) заменяет метод конечных разностей
- Необходимо решение пользовательских уравнений. поэтому МКЭ-решатель должен быть ***с открытым исходным кодом***
"""

r"""
# **Цель работы**
- Решение совместной задачи термоупругости на вычислительной платформе ***FEniCS с открытым исходным кодом и Python интерпретатором.***
"""
path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'picture_1.png')
image = Image.open(path_to_image)
st.image (image)
