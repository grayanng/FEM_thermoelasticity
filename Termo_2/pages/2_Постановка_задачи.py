import streamlit as st
from PIL import Image
import os.path
menu = st.sidebar.radio('***',
    (
    'Задачи 2-го этапа',
     'Постановка задачи теплопроводности','Постановка задачи упругости')
)
if menu=='Задачи 2-го этапа':
    r"""
    # Задачи 2-го этапа $$\\$$
    
    - реализация программы на Python для решения задачи стационарной теплопроводности для двухслойного 2D образца с поверхностным нагревом
    - генерация сеток в gmsh
    - добавление решения уравнений упругости
    - визуализация расчетов в ParaView
    
    """
if menu=='Постановка задачи теплопроводности':

    r"""
    # Постановка задачи теплопроводности $$\\$$

    """

    path_to_image_1 = os.path.join(os.path.dirname((__file__)), 'images', 'Task.png')
    image = Image.open(path_to_image_1)
    st.image(image, caption='')

    r"""
    $$
    \begin{align*}
    T(x,t) &= g(x) &x&\isin Г_1\cupГ_3  \\ 
    -k\dfrac {\partial T}{\partial n}(x,t)&=0  &x&\isinГ_2
    \end{align*}
    $$
    """
if menu=='Постановка задачи упругости':
    r"""
         # Постановка задачи упругости $$\\$$
        
     """
    path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'Task_2.png')
    image = Image.open(path_to_image_2)
    st.image(image, caption='')
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        r"""
                $$U_1 = 0 \quad U_2 = 0$$
         """
