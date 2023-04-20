import streamlit as st
from PIL import Image
import os.path

r'''
### Параметры образца
'''

code = '''
dW = 0.02  # [m] domain width
dH = 0.012  # [m] domain height

mu1 = Constant(0.8e11)
mu2 = Constant(0.5e11)
lambda1 = Constant(1.25e11)
lambda2 = Constant(0.65e11)
k1 = Constant(200.)
k2 = Constant(100.)
beta1 = Constant(6.0e-6)
beta2 = Constant(3.0e-6)
alphaAir = Constant(50.)
TAir = Constant(20.)
THot = Constant(150.)
T0 = Constant(40.)

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

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/tem2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/vms2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/ux2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/uy2.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

if menu == "Сетка 2":
    """
    # Результат численного моделирования

    """

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/tem2.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение температуры')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/vms2.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение напряжений')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/ux2.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по x')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/uy2.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по y')

