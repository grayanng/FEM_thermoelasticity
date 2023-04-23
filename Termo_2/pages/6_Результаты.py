import streamlit as st
from PIL import Image
import os.path

r'''
### Параметры образца
'''

code = '''
dW = 0.02  # [m] domain width
dH = 0.012  # [m] domain height

# Lamé's first parameter
lambda1 = Constant(1.25e11) 
lambda2 = Constant(0.65e11)

# Lamé's second parameter
mu1 = Constant(0.8e11) 
mu2 = Constant(0.5e11)

# [W/(m*K)] thermal conductivity
k1 = Constant(200.) 
k2 = Constant(100.)

# [1/K] thermal expansion coefficient
beta1 = Constant(6.0e-6) 
beta2 = Constant(3.0e-6)

alphaAir = Constant(50.) # convection coefficient
TAir = Constant(20.) # [K] ambient temperature
THot = Constant(150.) # [K] temperature of heating
T0 = Constant(40.) # [K] initial temperature

'''
st.code(code, language='python')

menu = st.sidebar.radio('***',
    ('Сетка 1',
     'Сетка 2')
)







if menu == "Сетка 1":

    """
    # Результат численного моделирования
    
    """

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/tem3.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/vms2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/ux3.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/uy3.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

if menu == "Сетка 2":
    """
    # Результат численного моделирования

    """

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/tem3.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение температуры')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/vms2.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение напряжений')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/ux3.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по x')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/uy3.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по y')

