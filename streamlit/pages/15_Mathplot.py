import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
r"""
# Использование графиков MathPlot
- Тоже интересная функция, которая поможет продемонстрировать результаты вашей работы в полной мере.
"""
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

expander = st.expander(" Как вывести график ")
expander.write ( r"""```python
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
""")