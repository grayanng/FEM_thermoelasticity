import streamlit as st
from PIL import Image
import os.path

path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'Picture_3.png')

"""
# Сетка 
На данный момент, использовалось построение сетки по умолчанию, без определения дополнительных параметров. ($$ 1D \implies 2D $$ )

"""
image = Image.open(path_to_image)
st.image (image, caption= 'Рисунок 3 - Сетка упрощенной модели ')

