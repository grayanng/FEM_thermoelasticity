import streamlit as st
from PIL import Image
import os.path

menu = st.sidebar.radio('***',
    ('Крупная сетка 20х4 (mshr)',
     'Сетка 50х10 (mshr)',
     'Сетка (gmsh)',)
)



"""
# Результат численного моделирования

"""
if menu == "Крупная сетка 20х4 (mshr)":

    block1 = '''mesh = RectangleMesh(Point(0.0, 0.0), Point(0.02, 0.012), 20, 4)'''

    st.code(block1,language='python')
    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/mesh_mshr.png')
    image = Image.open(path_to_image)
    st.image (image)

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/temp.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/ums.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/u(x).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/u(y).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

if menu == "Сетка 50х10 (mshr)":
    block1 = '''mesh = RectangleMesh(Point(0.0, 0.0), Point(0.02, 0.012), 50, 10)'''

    st.code(block1, language='python')
    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/mesh_mshr.png')
    image = Image.open(path_to_image)
    st.image(image)

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/temp.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение температуры')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/vms.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение напряжений')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/u(x).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по x')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/u(y).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по y')

if menu == "Сетка (gmsh)":

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v3/mesh_mshr.png')
    image = Image.open(path_to_image)
    st.image(image)

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v3/temp.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение температуры')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v3/vms.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение напряжений')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v3/u(x).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по x')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v3/u(y).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по y')
