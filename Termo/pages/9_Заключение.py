import streamlit as st
from PIL import Image
import os.path

path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'Picture_3.jpg')

if st.button('Клац'):

    image = Image.open(path_to_image)
    st.image (image, caption= '')

else:
    st.write(r"""
    # Заключение
    
    """)