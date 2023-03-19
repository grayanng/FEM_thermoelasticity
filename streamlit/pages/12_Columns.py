import streamlit as st
import numpy as np
r"""
# Колонки
- Такой вид колонки подойдет для описания графиков.
"""
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

expander = st.expander("Как вывести колоквиум")
expander.write ( r"""```python
col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
""")

