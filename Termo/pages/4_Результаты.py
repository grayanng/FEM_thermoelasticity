import streamlit as st
from PIL import Image
import os.path

menu = st.sidebar.radio('***',
    ('Сетка 20х4',
     'Сетка 50х10',
     'Сетка 50х50',
     'Сетка (gmsh)',)
)



"""
# Результат численного моделирования

"""
if menu == "Сетка 20х4":

    block1 = '''mesh = RectangleMesh(Point(0.0, 0.0), Point(0.02, 0.012), 20, 4, 'left/right')'''

    st.code(block1,language='python')
    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/mesh_mshr.png')
    image = Image.open(path_to_image)
    st.image (image)

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/temp.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение температуры')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/vms.png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение напряжений')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/u(x).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по x')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/u(y).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений по y')

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v1/u(m).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений')

if menu == "Сетка 50х10":
    block1 = '''mesh = RectangleMesh(Point(0.0, 0.0), Point(0.02, 0.012), 50, 10, 'left/right')'''

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

    path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v2/u(m).png')
    image = Image.open(path_to_image)
    st.image (image, caption='Распределение перемещений')

if menu == "Сетка 50х50":
    block1 = '''mesh = RectangleMesh(Point(0.0, 0.0), Point(0.02, 0.012), 50, 50, 'left/right')'''

    st.code(block1, language='python')
    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/mesh_mshr.png')
    image = Image.open(path_to_image)
    st.image(image)

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/temp.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение температуры')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/vms.png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение напряжений')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/u(x).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по x')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/u(y).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений по y')

    path_to_image = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', './v4/u(m).png')
    image = Image.open(path_to_image)
    st.image(image, caption='Распределение перемещений')

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
