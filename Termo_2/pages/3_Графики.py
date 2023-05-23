import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
c1=10000
c2=0.002
k1=100
k2=50
y=np.linspace(0,0.004,100)
k=np.linspace(0,0.002,10)
phi= 1/(1+np.exp(-c1*(y-c2)))
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
    plt.plot(y,x(y))
    st.line_chart(x(y))
    def f(phi):
        k=k2*phi + k1*(1-phi)
        return k
    plt.plot(k)
    st.line_chart(f(phi))

with col2:
    r"""
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