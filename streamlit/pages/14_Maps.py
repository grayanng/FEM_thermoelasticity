import streamlit as st
import pandas as pd
import numpy as np

r"""
# Карты
- Использование карт это очень интересная функция и особенность Streamlit
"""
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

expander = st.expander("Вывод карты в вашей презентации")
expander.write ( r"""```python
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)

""")