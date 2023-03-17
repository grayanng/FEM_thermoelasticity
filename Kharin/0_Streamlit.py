import streamlit
import streamlit as st
from PIL import Image
import os.path


path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'streamlit.jpg')


r"""
# Научный проект на тему: Streamlit и его возможности

## Проект команды №2

Выполнили студенты группы ВМ-122:
- Харин Александр Николаевич
- Мулин Георгий Денисович
- Понаморенко Дмитрий Сергеевич
- Сизая Анжелика  Владимировна
"""


image = Image.open(path_to_image)
st.image (image, caption= 'Streamlit')