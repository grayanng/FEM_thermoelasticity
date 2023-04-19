import streamlit as st
from PIL import Image
import os.path

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    path_to_image_2 = os.path.join(os.path.dirname((__file__)), 'images', 'MSU.png')
    image = Image.open(path_to_image_2)
    st.image(image, caption='',output_format=('auto'))
r"""
# Научный проект на тему
### Решение совместной задачи термоупругости 2D образца, подверженному  стационарному нагерву, с использованием FEniCS 

## Проект команды №3

Выполнили студенты группы ВМ-122
- Харин Александр Николаевич
- Муллин Георгий Денисович
- Пономаренко Дмитрий Сергеевич
- Сизая Анжелика  Владимировна
"""