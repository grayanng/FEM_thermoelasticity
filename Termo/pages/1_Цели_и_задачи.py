import streamlit
import streamlit as st
from PIL import Image
import os.path

r"""
# **Цель работы**
- Решение совместной задачи термоупругости на вычислительной платформе ***FEniCS с открытым исходным кодом и Python интерпретатором.***
"""
path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'picture_1.png')
image = Image.open(path_to_image)
st.image (image)
