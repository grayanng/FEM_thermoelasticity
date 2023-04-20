import streamlit as st
from PIL import Image
import os.path

path_to_image= os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images', 'MSU.png')

if st.button('Клац'):
    r"""
    # Спасибо за внимание!
    """
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        image = Image.open(path_to_image)
        st.image(image, caption='')

else:
    st.write(r"""
    # Заключение
- Реализована математическая модель одного слоя 2D образца при поверхностном нагреве материала с учетом тепловых деформаций и напряжений

    """)