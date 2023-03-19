import streamlit as st
import pandas as pd
import numpy as np

r"""
# Карты
- Использование карт это очень интересная функция и особенность Streamlit
"""
df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [54.92172764865859, 43.22875333880689],
    columns=['lat', 'lon'])

st.map(df)

expander = st.expander("Вывод карты в вашей презентации")
expander.write ( r"""```python
df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [54.76, 43.4],
    columns=['lat', 'lon'])

st.map(df)

""")