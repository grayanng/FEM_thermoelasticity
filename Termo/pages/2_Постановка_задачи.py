import streamlit as st
from PIL import Image
import os.path
r"""
# Постановка задачи $$\\$$

"""
path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'Picture_5.png')
image = Image.open(path_to_image_2)
st.image(image, caption='Рисунок 3 - Область задачи ')
r"""
$$
T(x,t) = g(x) \quad x\isin Г_1\cupГ_2 \quad U_1=0 \quad U_2=0 \\
-k\frac {\partial T}{\partial n}(x,t)=0 \quad x\isinГ_2
$$
"""