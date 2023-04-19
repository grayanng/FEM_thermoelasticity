import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

c1 = 1000
c2 = 0.002

r"""
# Учет двухслойности 

"""
col1, col2 = st.columns(2)

with col1:
    r"""
    ### Графики

    """
    a = -1.
    b = 1.


    def f(x):
        return 1. / (1. + 25 * x ** 2)


    from fenics import *
    mesh = IntervalMesh(m, a, b)
    xm = mesh.coordinates()
    ym = np.zeros((m + 1), "float")

    V = FunctionSpace(mesh, sfem, p)
    n = V.dim() - 1

    fr = Expression("1/(1+25*x[0]*x[0])", degree=p + 2)
    if spr == "интерполяции":
        u = interpolate(fr, V)
    else:
        u = project(fr, V)

    N = 500
    xx = np.linspace(a, b, N)
    yy = np.linspace(a, b, N)
    ye = f(xx)

    xn = V.tabulate_dof_coordinates()
    yn = np.zeros((len(xn)), "float")

    for i in range(0, N):
        yy[i] = u(Point(xx[i]))

    fig1 = plt.figure(1)
    ss = "$m = $" + str(m) + "$, \ p = $" + str(p)
    plt.title(ss)
    plt.scatter(xn, yn)
    plt.scatter(xm, ym)
    plt.plot(xx, ye)
    plt.plot(xx, yy)

    plt.xlabel('$x$')
    plt.grid(True)

    c1, c2, = st.columns([3, 1])
    c1.pyplot(fig1)
    plt.clf()
