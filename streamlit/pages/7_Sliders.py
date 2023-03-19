import streamlit as st
from datetime import datetime

r"""
# Интерактивный ввод данных
"""
x=st.slider('Square the number',-1.0,10.0,7.55,0.2)
x**2
expander = st.expander("Посмотреть исходный код")
expander.write ( r"""```Python
x=st.slider('Square the number',-1.0,10.0,7.55,0.2)
x**2
""")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

expander = st.expander("Посмотреть исходный код")
expander.write ( r"""```Python
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
""")

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

expander = st.expander("Посмотреть исходный код")
expander.write ( r"""```Python
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
""")

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

expander = st.expander("Посмотреть исходный код")
expander.write ( r"""```Python
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

""")