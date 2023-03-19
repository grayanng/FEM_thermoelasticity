import streamlit as st
from PIL import Image
import os.path

path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'Picture_3.png')

if st.button('Клац'):

    image = Image.open(path_to_image)
    st.image (image, caption= '')

else:
    st.write(r"""
    # Заключение
    *Streamlit* обладает большими возможностями для реализации вашего проекта. 
    В данной презентации были рассмотрены самые интересные и необычные функции данной платформы. Более подробно можете ознакомится на оффициальном сайте: https://docs.streamlit.io/library/get-started.
    """)