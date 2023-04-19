import streamlit
import streamlit as st
from PIL import Image
import os.path

menu = st.sidebar.radio('***',
    (
    'Цель работы','Этапы работы',
     'Задачи этапа 1',)
)

if menu == 'Цель работы':
    r"""
    # **Цель работы**
    - Решение совместной задачи термоупругости на вычислительной платформе ***FEniCS с открытым исходным кодом и Python интерпретатором***
    """
    path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'Picture_1.jpg')
    image = Image.open(path_to_image)
    st.image (image)

if menu == 'Этапы работы':
    r"""
    # Этапы работы
    1. Упрощенная модель
    - Решение задачи термоупругости для однослойного образца в 2D
    2. Базовая модель
    - Решение задачи термоупругости для двуслойного образца в 2D
    3. Усложненная модель
    - Решение задачи термоупругости для двуслойного образца в 3D
    """

if menu == 'Задачи этапа 1':
    """
    # Задачи этапа 1

    1. Решение задачи стационарной теплопроводности однослойного двумерного образца на языке Python с применением модуля Fenics
    1. Генерация сеток в gmsh
    1. Добавление решения уравнения упругости
    1. Визуализация расчетов в ParaView


    """