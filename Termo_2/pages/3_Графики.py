import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
c1=1000
c2=0.002
y=np.linspace(0,10)
r"""
# Учет двухслойности 

"""
col1, col2 = st.columns(2)

with col1:
    r"""
    ### Графики
    
    """
    def x(y):
        return 1/(1+np.exp(-c1*(y-c2)))
    plt.plot(x(y))
    plt.show


with col2:
    r"""
    ### Комментарии
    ## Сигмоида
    $$
    \phi =\frac  {1}{1+e^{-C_1(y-C_2)}}\\
    $$
    $$C_1$$ - коэффициент сглаженности перехода\
    $$C_2$$ - координата перехода
    ## Пример расчета коэффициента теплопроводности
    $$
    k = k_2\cdotp \phi + k_1 (1-\phi)\\
    $$
    $$k_1$$ - коэффициент нижнего слоя \
    $$k_2$$ - коэффициент верхнего слоя
    """