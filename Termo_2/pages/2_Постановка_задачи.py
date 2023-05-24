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
    
    - реализация программы на Python для решения задачи стационарной теплопроводности для двуслойного 2D образца с поверхностным нагревом
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
      #### Уравнение теплопроводности 
    $$
      \begin{aligned}
      &-\nabla  (k \nabla T) = 0\\
      \end{aligned}
    $$
    """
    r"""
    #### Граничные условия
    $$
    \begin{aligned}
    T(x,t) &= g(x) &x&\isin Г_1\cupГ_3  \\ 
    -k\dfrac {\partial T}{\partial n}(x,t)&=0  &x&\isinГ_2
    \end{aligned}
    $$
    """
    r"""
      #### Слабая форма
    $$
    \begin{aligned}
     &-\int_{\varOmega}k (\nabla \omega  \nabla T)d\varOmega = 0  
    \end{aligned}
    $$

    """
    expander = st.expander(" Используемые переменные ")
    expander.write(
        r""" $$T$$ - поле температуры  $$\\ k$$ - коэффициент теплопроводности 
        $$\\$$ $$w$$ - тестовая функция $$\\$$ $$\alpha_{air}$$ -  коэффициент конвекции $$\\$$ 
         $$T_{air}$$ - температура окружающей среды """)


if menu=='Постановка задачи упругости':
    r"""
         # Постановка задачи упругости $$\\$$
    """
    path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'pic2D.png')
    image = Image.open(path_to_image_2)
    st.image(image, caption='')

    r"""
     #### Уравнение Гука (упругости) 
    $$
    \begin{aligned}
    &div\sigma = 0\\
    &\sigma = \lambda\thetasym I + 2\mu\varepsilon^{el} \\ 
    &\varepsilon = \varepsilon^{el}+{\varepsilon^{th}}\\
    &\varepsilon = \frac{1}{2} (\nabla{u} + (\nabla u)^{T})\\
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
    $$I$$ - единичная диагональная матрица$$\\$$ $$\alpha$$ - коэффициент теплового расширения\
    $$T_{ref}$$ - температура, при которой материал имеет свой нормальный объем

    """)


    r"""
     #### Граничные условия
     $$
     U_1(x_1,x_2) = 0 \quad U_2(x_2 ) = 0
     $$
     """
    r"""
    #### Слабая форма 
    $$
      {\int_{\varOmega} \sigma\varepsilon dx} = 0
    $$
    """
    r"""
    #### Напряжение по Мизесу
    $$
    \sigma_M = \sqrt{\frac{3}{2}s:s} \\
    s = \sigma - \frac {1}{2}tr(\sigma)I
    
    $$
    
    """
    expander = st.expander(" Используемые переменные ")
    expander.write(
    r""" 
    $$s$$ - тензор девиаторного напряжения $\\$
    $$tr(\sigma)$$ - первый инвариант тензора напряжений
    """)