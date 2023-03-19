import streamlit as st

r"""
# Expanders
- Очень полезная функция в Streamlit - использование комментариев в вашей презентации
"""
expander = st.expander("Здесь может быть ваш любой коментарий ")
expander.write ( r"""```Python
expander = st.expander("Здесь может быть ваш любой коментарий ")
expander.write("Текст")

""")