import streamlit
import streamlit as st
from PIL import Image
import os.path


path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'streamlit.jpg')


r"""
# Образовательный проект на тему: Streamlit и его возможности

## Проект команды №3

Выполнили студенты группы ВМ-122:
- Харин Александр Николаевич
- Муллин Георгий Денисович
- Пономаренко Дмитрий Сергеевич
- Сизая Анжелика  Владимировна
"""


image = Image.open(path_to_image)
st.image (image, caption= 'Streamlit')

expander = st.expander("Вывод картинки в Streamlit")
expander.write ( r"""```python
path_to_image= os.path.join(os.path.dirname(__file__), 'images', 'streamlit.jpg')
image = Image.open(path_to_image)
st.image (image, caption= 'Streamlit')
""")