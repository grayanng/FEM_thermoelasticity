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
    
      #### Слабая форма
      $$
      \int_\varOmega k\cdotp (\bold{\nabla w \cdotp \bold{\nabla} T )d\varOmega =}  \int_\varOmega w\cdotp Q d\varOmega 
      $$

      """
    expander = st.expander(" Используемые переменные ")
    expander.write(
        r""" $$T$$- поле температуры  $$\\ k$$- коэффициент теплопроводности$$  \\ Q$$- объемный источник тепла  $$\\ \bold{q}$$- тепловой поток $$\\$$ $$w-$$тестовая функция""")

    r"""
    #### Граничные условия
    $$
    \begin{aligned}
    T(x,t) &= g(x) &x&\isin Г_1\cupГ_3  \\ 
    -k\dfrac {\partial T}{\partial n}(x,t)&=0  &x&\isinГ_2
    \end{aligned}
    $$
    """
if menu=='Постановка задачи упругости':
    r"""
         # Постановка задачи упругости $$\\$$
    """
    path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'Task_2.png')
    image = Image.open(path_to_image_2)
    st.image(image, caption='')

    r"""
     #### Уравнение Гука (упругости) 
    $$
    \begin{aligned}
    &div\sigma = 0\\
    &\sigma = \lambda\thetasym I + 2\mu\varepsilon^{el} \\ 
    &\varepsilon = \varepsilon^{el}+{\varepsilon^{th}}\\
    &\varepsilon = \frac{1}{2}\cdotp (\nabla{u} + (\nabla u)^{T})\\
    &\varepsilon^{th} = [(3\lambda + 2\mu) \alpha(T-T_{ref})]I
    &\end{aligned}
    $$
    """
    expander = st.expander(" Используемые переменные ")
    expander.write(
    r""" 
    $$\lambda$$ -первый коэффициент Ламе \
    $$\mu$$ - второй коэффициент Ламе\
    $$\varepsilon^{el}$$ - линейный тензор упругой деформации \
    $$\thetasym$$ = $$tr(\varepsilon^{el})$$ - первый инвариант линейного тензора упругой деформации (объемное расширение в линейном приближении)\
    I - единичная диагональная матрица$$\\$$ $$\alpha$$ - коэффициент теплового расширения\
    $$T_{ref}$$ - температура, при которой материал имеет свой нормальный объем

    """)

    r"""
    #### Слабая форма 
    $$
      {\int_{\varOmega} \sigma\varepsilon dx} = 0
    $$
    """
    expander = st.expander(" Используемые переменные ")
    expander.write(r""" $$T$$-усилие $$\\$$ $$v$$-тестовая функция """)
    r"""
     #### Граничные условия
     $$
     U_1 = 0 \quad U_2 = 0
     $$
     """

    r"""
    #### Напряжение по Мизесу
    $$
    \sigma_M = \sqrt{\frac{3}{2}s:s} \\
    s = \sigma - \frac {1}{2}tr(\sigma)I
    
    $$
    
    """