import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

c1=100000
c2=0.002
k1=100
k2=50
y=np.linspace(0,0.004,100)
k=np.linspace(0,0.002,10)
phi= 1/(1+np.exp(-c1*(y-c2)))
r"""
# Учет двуслойности 

"""
col1, col2 = st.columns(2)

with col1:

    def x(y):
        return 1/(1+np.exp(-c1*(y-c2)))
    #plt.plot(y,x(y))
    fig, ax = plt.subplots()
    ax.plot(y, x(y))
    #st.line_chart(x(y))
    st.pyplot(fig, clear_figure=True)

    def f(phi):
        k=k2*phi + k1*(1-phi)
        return k
    # plt.plot(f(phi))
    # st.line_chart(f(phi))
    fig, ax = plt.subplots()

    x = np.linspace(0, 0.02, 100)
    y1 = np.ones(100) * 0.012
    y2 = np.ones(100) * 0.002
    y0 = np.zeros(100)
    # fig/1.
    ax.plot(x, y1, label='Значения k(y)')
    ax.set_xlim(0, 0.02)
    ax.set_ylim(0, 0.012)
    ax.vlines(0.01, 0.002, 0.012)
    ax.vlines(0.015, 0, 0.002)
    ax.hlines(0.002, 0.01, 0.015)
    ax.fill_between(x, y2, y1, color='gray', alpha=0.5)
    ax.fill_between(x, y0, y1, color='gray', alpha=0.2)
    ax.set_xlabel(f'x')
    ax.set_ylabel(f'y')
    ax.legend()
    st.pyplot(fig, clear_figure=True)
with col2:
    r"""
    ## Сигмоида
    $$
    \varphi =\frac  {1}{1+e^{-C_1(y-C_2)}}\\
    $$
    $$C_1$$ - коэффициент сглаженности перехода\
    $$C_2$$ - координата перехода
    ## Пример расчета коэффициента теплопроводности
    $$
    k = k_2\cdotp \varphi + k_1 (1-\varphi)\\
    $$
    $$k_1$$ - коэффициент нижнего слоя \
    $$k_2$$ - коэффициент верхнего слоя
    """